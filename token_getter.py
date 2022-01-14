import os

from globus_sdk import NativeAppAuthClient

os.environ["GLOBUS_SDK_ENVIRONMENT"] = "sandbox"
CLIENT_ID = "b8409290-c9ee-4a2b-9f4f-c61c2acbc267"
SCOPE = "urn:globus:auth:scope:groups.api.globus.org:all"

native_client = NativeAppAuthClient(CLIENT_ID)
native_client.oauth2_start_flow(
    requested_scopes=[SCOPE], refresh_tokens=False, prefill_named_grant="W/E"
)
linkprompt = (
    "Please log into Globus here:\n"
    "----------------------------\n"
    f"{native_client.oauth2_get_authorize_url()}\n"
    "----------------------------\n"
)

print(linkprompt)
auth_code = input("Enter the resulting Authorization Code here: ").strip()
oauth_resp = native_client.oauth2_exchange_code_for_tokens(auth_code)
print(oauth_resp.by_scopes[SCOPE])
