import typing as t

from globus_sdk import GlobusHTTPResponse
from globus_sdk.authorizers import GlobusAuthorizer
from globus_sdk.base import BaseClient

from globus_mas.config import CURRENT_GROUPS_URL

_GroupsClient = t.TypeVar("_GroupsClient", bound="GroupsClient")


GROUPS_SCOPE = "urn:globus:auth:scope:groups.api.globus.org:all"


class GroupsClient(BaseClient):
    @classmethod
    def new(
        cls: t.Type[_GroupsClient],
        authorizer: GlobusAuthorizer,
        environment: str = "default",
    ) -> _GroupsClient:
        return cls(
            "groups",
            base_url=CURRENT_GROUPS_URL,
            http_timeout=10,
            authorizer=authorizer,
            environment=environment,
            app_name="Globus Mas SDK - GroupsClient",
        )

    def list_groups(self) -> GlobusHTTPResponse:
        return self.get("/v2/groups/my_groups")

    def group_info(self, group_id: str) -> GlobusHTTPResponse:
        return self.get(f"/v2/groups/{group_id}")

    def new_group(self, group_name: str) -> GlobusHTTPResponse:
        return self.post("/v2/groups", json_body={"name": group_name})

    def add_to_group(self, group_id: str, *new_members: str) -> GlobusHTTPResponse:
        payload: t.Dict[str, t.List] = {"add": []}
        for m in new_members:
            payload["add"].append({"identity_id": m})
        return self.post(f"/v2/groups/{group_id}", json_body=payload)

    def get_preferences(self) -> GlobusHTTPResponse:
        return self.get(f"/preferences")

    def update_preferences(self, *identities: str) -> GlobusHTTPResponse:
        payload = {i: {"allow_add": True} for i in identities}
        return self.put(f"/preferences", json_body=payload)
