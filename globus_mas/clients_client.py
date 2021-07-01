import typing as t

from globus_sdk import GlobusHTTPResponse
from globus_sdk.authorizers import GlobusAuthorizer
from globus_sdk.base import BaseClient

from globus_mas.config import CURRENT_AUTH_URL

_ClientsClient = t.TypeVar("_ClientsClient", bound="ClientsClient")


GROUPS_SCOPE = "urn:globus:auth:scope:groups.api.globus.org:all"


class ClientsClient(BaseClient):
    @classmethod
    def new(
        cls: t.Type[_ClientsClient],
        authorizer: GlobusAuthorizer,
        environment: str = "default",
    ) -> _ClientsClient:
        return cls(
            "groups",
            base_url=CURRENT_AUTH_URL,
            http_timeout=10,
            authorizer=authorizer,
            environment=environment,
            app_name="Globus Mas SDK - ClientsClient",
        )

    def get_clients(self) -> GlobusHTTPResponse:
        return self.get("/v2/api/clients/")

    def get_client(self, client_id: str) -> GlobusHTTPResponse:
        return self.get(f"/v2/api/clients/{client_id}")

    def get_client_credentials(self, client_id: str) -> GlobusHTTPResponse:
        return self.get(f"/v2/api/clients/{client_id}/credentials")

    def create_client_credential(
        self, client_id: str, credential_name: str
    ) -> GlobusHTTPResponse:
        payload = {"credential": {"name": credential_name}}
        return self.post(f"/v2/api/clients/{client_id}/credentials", json_body=payload)

    def delete_client_credential(
        self, client_id: str, credential_id: str
    ) -> GlobusHTTPResponse:
        return self.delete(f"/v2/api/clients/{client_id}/credentials/{credential_id}")
