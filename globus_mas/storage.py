import typing as t
from pathlib import Path

import yaml
from globus_sdk import NativeAppAuthClient, RefreshTokenAuthorizer
from globus_sdk.auth.token_response import OAuthTokenResponse
from pydantic import BaseModel, ValidationError

from globus_mas.config import CACHE_FILE, CLIENT_ID


class StorageItem(BaseModel):
    access_token: str
    refresh_token: str
    expires_at_seconds: int
    token_type: str
    scope: str
    resource_server: str


class TokenCache(object):
    load_failure = False

    def __enter__(self) -> "TokenCache":
        if not hasattr(self, "cache"):
            self.cache = self.load()
        return self

    def __exit__(self, type, value, traceback):
        self.save()

    def __contains__(self, scope: str):
        return scope in self.cache

    def __getitem__(self, key: str) -> t.Optional[StorageItem]:
        return self.cache.get(key, None)

    def load(self):
        try:
            with open(CACHE_FILE, "r") as cache_file:
                raw_cache = yaml.safe_load(cache_file) or {}
        except FileNotFoundError:
            raw_cache = {}
        except yaml.YAMLError:
            raw_cache = {}
            self.load_failure = True

        cache: t.Dict[str, StorageItem] = {}
        for scope in raw_cache:
            try:
                item = StorageItem.parse_obj(raw_cache[scope])
            except ValidationError:
                self.load_failure = True
                continue
            cache[scope] = self._refreshed_item(item)
        return cache

    def save(self):
        cache = {scope: item.dict() for scope, item in self.cache.items()}
        with open(CACHE_FILE, "w") as cache_file:
            yaml.safe_dump(cache, cache_file, indent=2)

    def _refreshed_item(self, item: StorageItem) -> StorageItem:
        authorizer = RefreshTokenAuthorizer(
            auth_client=NativeAppAuthClient(CLIENT_ID),
            refresh_token=item.refresh_token,
            access_token=item.access_token,
            expires_at=item.expires_at_seconds,
        )

        # Refresh tokens if neccesary
        authorizer.check_expiration_time()
        return item.copy(
            update={
                "access_token": authorizer.access_token,
                "refresh_token": authorizer.refresh_token,
                "expires_at_seconds": authorizer.expires_at,
            }
        )

    def update(self, token_response: OAuthTokenResponse):
        updates = {}
        by_scopes = token_response.by_scopes
        for scope in by_scopes:
            updates[scope] = StorageItem.parse_obj(by_scopes[scope])
        self.cache.update(updates)
