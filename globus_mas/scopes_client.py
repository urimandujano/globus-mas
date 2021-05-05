import typing as t

from globus_sdk import GlobusHTTPResponse
from globus_sdk.authorizers import BasicAuthorizer
from globus_sdk.base import BaseClient

_ScopesClient = t.TypeVar("_ScopesClient", bound="ScopesClient")


class ScopesClient(BaseClient):
    @classmethod
    def new(
        cls: t.Type[_ScopesClient],
        authorizer: BasicAuthorizer,
        environment: str = "default",
    ) -> _ScopesClient:
        return cls(
            "scopes",
            base_url="https://auth.globus.org/",
            http_timeout=10,
            authorizer=authorizer,
            environment=environment,
        )

    def get_scopes_by_id(self, *scopes: str) -> GlobusHTTPResponse:
        return self.get("/v2/api/scopes", params={"ids": ",".join(scopes)})

    def get_scopes_by_string(self, *scopes: str) -> GlobusHTTPResponse:
        return self.get("/v2/api/scopes", params={"scope_strings": ",".join(scopes)})

    def create_scope(
        self,
        client_id: str,
        *,
        scope_name: str,
        scope_description: str,
        scope_suffix: str,
        dependent_scopes: t.List[str],
    ) -> GlobusHTTPResponse:
        payload = {
            "scope": {
                "name": scope_name,
                "description": scope_description,
                "scope_suffix": scope_suffix,
                "dependent_scopes": [{"scope": ds} for ds in dependent_scopes],
            }
        }
        return self.post(f"/v2/api/clients/{client_id}/scopes", json_body=payload)

    def update_scope(
        self,
        scope_id,
        *,
        scope_name: t.Optional[str] = None,
        scope_description: t.Optional[str] = None,
        dependent_scopes: t.Optional[t.List[str]] = None,
    ) -> GlobusHTTPResponse:
        payload: t.Dict = {"scope": {}}
        if scope_name:
            payload["scope"]["name"] = scope_name
        if scope_description:
            payload["scope"]["description"] = scope_description
        if dependent_scopes:
            payload["scope"]["dependent_scopes"] = [
                {"scope": ds} for ds in dependent_scopes
            ]
        return self.put(f"/v2/api/scopes/{scope_id}", json_body=payload)

    def delete_scope(self, scope_id) -> GlobusHTTPResponse:
        return self.delete(f"/v2/api/scopes/{scope_id}")

    def list_scopes(self) -> GlobusHTTPResponse:
        return self.get("/v2/api/scopes")
