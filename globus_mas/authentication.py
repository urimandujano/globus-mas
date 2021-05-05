import platform
import typing as t

import typer
from globus_sdk.auth.client_types import ConfidentialAppAuthClient, NativeAppAuthClient
from globus_sdk.auth.token_response import OAuthTokenResponse
from globus_sdk.authorizers import BasicAuthorizer, RefreshTokenAuthorizer

from globus_mas.config import CLIENT_ID
from globus_mas.storage import TokenCache


def login(scopes: t.List[str]) -> OAuthTokenResponse:
    label = f"Globus Mas CLI on {platform.node()}"
    native_client = NativeAppAuthClient(CLIENT_ID)
    native_client.oauth2_start_flow(
        requested_scopes=scopes, refresh_tokens=True, prefill_named_grant=label
    )
    linkprompt = (
        "Please log into Globus here:\n"
        "----------------------------\n"
        f"{native_client.oauth2_get_authorize_url()}\n"
        "----------------------------\n"
    )
    typer.echo(linkprompt)
    auth_code = typer.prompt("Enter the resulting Authorization Code here").strip()
    return native_client.oauth2_exchange_code_for_tokens(auth_code)


def authorizers_by_scope(scopes: t.List[str]):
    with TokenCache() as cache:
        if cache.load_failure:
            typer.secho("Removed unusable cache entries.", fg=typer.colors.RED)

        all_in_cache = all(scope in cache for scope in scopes)
        if not all_in_cache:
            tokens = login(scopes)
            cache.update(tokens)

    authzs_by_scope = {}
    for scope in scopes:
        oauth_token_response = cache[scope]
        if oauth_token_response is None:
            continue
        authorizer = RefreshTokenAuthorizer(
            auth_client=NativeAppAuthClient(CLIENT_ID),
            refresh_token=oauth_token_response.refresh_token,
            access_token=oauth_token_response.access_token,
            expires_at=oauth_token_response.expires_at_seconds,
        )
        authzs_by_scope[scope] = authorizer
    return authzs_by_scope


def authorizer_for_scope(scope: str) -> t.Optional[RefreshTokenAuthorizer]:
    return authorizers_by_scope([scope]).get(scope)


def get_basic_authorizer(client_id: str, client_secret: str) -> BasicAuthorizer:
    return BasicAuthorizer(client_id, client_secret)


def get_confidential_app_auth_client(
    client_id: str, client_secret: str
) -> ConfidentialAppAuthClient:
    return ConfidentialAppAuthClient(client_id, client_secret)
