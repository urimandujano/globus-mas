import datetime
from functools import lru_cache
from time import sleep

from globus_mas.authentication import get_confidential_app_auth_client

GLOBUS_AUTH_CLIENT_ID = "d3a66776-759f-4316-ba55-21725fe37323"
GLOBUS_AUTH_CLIENT_SECRET = "v8EmT1B7d3ARz9XJscHrQijtWolYrFV53WlPBTmbnUA="
GLOBUS_AUTH_TOKEN = "Ag8qp1Me5gkwJpb1PDYG9z3dDQepmja0k0MzYbkJQwde2jnw6yC8C2P7DvbjXgK67gVjVByqoY0zJyt7pywlVFgpXG"

ac = get_confidential_app_auth_client(
    client_id=GLOBUS_AUTH_CLIENT_ID, client_secret=GLOBUS_AUTH_CLIENT_SECRET
)


@lru_cache
def get_dependent_tokens(token: str, auth_cache_id: str):
    print("MAKING A DEPENDENT TOKEN GRANT")
    response = ac.oauth2_get_dependent_tokens(token, {"access_type": "offline"})
    print(response.data)
    return response.data


def introspect_token(token: str):
    print("INTROSPECTING TOKEN")
    response = ac.oauth2_token_introspect(token, include="identity_set")
    print(response.data)
    return response.data


def main():
    while True:
        print(f"Now {datetime.datetime.utcnow()}")
        resp = introspect_token(GLOBUS_AUTH_TOKEN)
        auth_cache_id = resp["dependent_tokens_cache_id"]

        get_dependent_tokens(GLOBUS_AUTH_TOKEN, auth_cache_id)
        print("-" * 30)
        sleep(60)


main()
