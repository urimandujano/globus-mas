import os
import typing as t
from pathlib import Path

CLIENT_ID = "c0ff9c71-6a2f-4242-bf68-baf572c09079"
CACHE_FILE = Path.home() / ".globus-mas.yml"

AUTH_API_ENVIRONMENTS: t.Dict[str, str] = {
    "default": "https://auth.globus.org",
    "production": "https://auth.globus.org",
    "preview": "",
    "sandbox": "https://auth.sandbox.globuscs.info",
    "test": "https://auth.test.globuscs.info",
    "integration": "https://auth.integration.globuscs.info",
    "staging": "https://auth.staging.globuscs.info",
}

GROUPS_API_ENVIRONMENTS: t.Dict[str, str] = {
    "default": "https://groups.api.globus.org",
    "production": "https://groups.api.globus.org",
    "preview": "",
    "sandbox": "https://groups.api.sandbox.globuscs.info",
    "test": "https://groups.api.test.globuscs.info",
    "integration": "https://groups.api.integration.globuscs.info",
    "staging": "https://groups.api.staging.globuscs.info",
}

GLOBUS_SDK_ENV = os.getenv("GLOBUS_SDK_ENVIRONMENT", "production")
CURRENT_AUTH_URL = AUTH_API_ENVIRONMENTS[GLOBUS_SDK_ENV]
CURRENT_GROUPS_URL = GROUPS_API_ENVIRONMENTS[GLOBUS_SDK_ENV]
