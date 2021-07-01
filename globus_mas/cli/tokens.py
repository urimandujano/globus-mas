import typing as t
import uuid

import typer
from globus_sdk import GlobusAPIError

from globus_mas.authentication import (
    authorizer_for_scope,
    get_confidential_app_auth_client,
)
from globus_mas.cli.helpers import format_and_print, verbosity_option

app = typer.Typer(
    short_help="Work with Globus Tokens",
    help="Most of these operations require the use of tokens and secrets. It's highly "
    "recommended not to paste these credentials since command line input may be logged "
    "and aggregated. Rather, export these values into the environment in which these "
    "commands are run.",
)


@app.command()
def token_for_scope(
    scope: str = typer.Argument(
        ...,
        help="The scope to retrieve a token for.",
    ),
    verbose: bool = verbosity_option,
):
    """
    Initiate a login to generate a token valid for the listed scope.
    """
    authorizer = authorizer_for_scope(scope)
    if authorizer:
        tokens = {
            "access_token": authorizer.access_token,
            "refresh_token": authorizer.refresh_token,
        }
        format_and_print(tokens, verbose=verbose)
    else:
        typer.secho("Unable to retrieve tokens!", fg=typer.colors.RED)


@app.command()
def introspect(
    client_id: uuid.UUID = typer.Argument(
        ...,
        help="The id for the resource server for which the token was issued. If unset,  "
        "this will be pulled from an environment variable.",
        envvar="AUTH_CLIENT_ID",
    ),
    client_secret: str = typer.Argument(
        ...,
        help="The corresponding resource server's secret. If unset, this will be "
        "pulled from an environment variable.",
        envvar="AUTH_CLIENT_SECRET",
    ),
    token: str = typer.Argument(
        ...,
        help="A particular token to introspect. If unset, this will be pulled from "
        "an environment variable.",
        envvar="AUTH_TOKEN",
    ),
    full_details: bool = typer.Option(
        False,
        "--full-details/",
        help="Include identity and session information in output.",
    ),
    verbose: bool = verbosity_option,
):
    """
    Introspect a provided token. The token must have been issued for the
    resource server (client id) provided. If the token is invalid or not
    intended for use with the resource server, Globus Auth will return an error.
    """
    ac = get_confidential_app_auth_client(
        client_id=str(client_id), client_secret=client_secret
    )

    if full_details:
        include = "identity_set,session_info,identity_set_detail"
    else:
        include = "identity_set"
    try:
        response = ac.oauth2_token_introspect(token, include=include)
    except GlobusAPIError as err:
        response = err
    format_and_print(response, verbose=verbose)


@app.command()
def view_dependant_tokens(
    client_id: uuid.UUID = typer.Argument(
        ...,
        help="The id for the resource server for which the token was issued. If unset, "
        "this value will be pulled from an environment variable.",
        envvar="AUTH_CLIENT_ID",
    ),
    client_secret: str = typer.Argument(
        ...,
        help=(
            "The corresponding resource server's secret. If unset, this value will "
            "be pulled from an environment variable."
        ),
        envvar="AUTH_CLIENT_SECRET",
    ),
    token: str = typer.Argument(
        ...,
        help="A particular token to return data on. If unset, this will be pulled from "
        "an environment variable.",
        envvar="AUTH_TOKEN",
    ),
    verbose: bool = verbosity_option,
):
    """
    Display the dependant tokens for a given token. The token must have been
    issued for the resource server (client id) provided. If the token is invalid
    or not intended for use with the resource server, Globus Auth will return an
    error.
    """
    ac = get_confidential_app_auth_client(
        client_id=str(client_id), client_secret=client_secret
    )
    try:
        response = ac.oauth2_get_dependent_tokens(token, {"access_type": "offline"})
    except GlobusAPIError as err:
        response = err
    format_and_print(response, verbose=verbose)


@app.command()
def client_credentials(
    client_id: uuid.UUID = typer.Argument(
        ...,
        help="The id for the resource server for which the token was issued. If unset, "
        "this value will be pulled from an environment variable.",
        envvar="AUTH_CLIENT_ID",
    ),
    client_secret: str = typer.Argument(
        ...,
        help="The corresponding resource server's secret. If unset, this value will "
        "be pulled from an environment variable.",
        envvar="AUTH_CLIENT_SECRET",
    ),
    scopes: t.Optional[t.List[str]] = typer.Option(
        None,
        "--scope",
        help="Return an access token for this scope. If not provided, tokens for default "
        "scopes will be returned. [repeatable]",
    ),
    verbose: bool = verbosity_option,
):
    """
    Get Access Tokens which directly represent the resource server (client id)
    and allow it to act on its own.
    """
    ac = get_confidential_app_auth_client(
        client_id=str(client_id), client_secret=client_secret
    )

    if scopes:
        scopes_string = " ".join(scopes)
    else:
        scopes_string = ""
    try:
        response = ac.oauth2_client_credentials_tokens(scopes_string)
    except GlobusAPIError as err:
        response = err
    format_and_print(response, verbose=verbose)


@app.command()
def revoke(
    client_id: uuid.UUID = typer.Argument(
        ...,
        help="The id for the resource server for which the token was issued. If unset, "
        "this value will be pulled from an environment variable.",
        envvar="AUTH_CLIENT_ID",
    ),
    client_secret: str = typer.Argument(
        ...,
        help="The corresponding resource server's secret. If unset, this value will "
        "be pulled from an environment variable.",
        envvar="AUTH_CLIENT_SECRET",
    ),
    token: str = typer.Argument(
        ...,
        help="The token to invalidate. If unset, this will be pulled from an "
        "environment variable.",
        envvar="AUTH_TOKEN",
    ),
    verbose: bool = verbosity_option,
):
    """
    Revoke an Access or Refresh token such that they can no longer be used. The
    token must have been issued for the resource server (client id) provided. If
    the token is invalid or not intended for use with the resource server,
    Globus Auth will return an error.
    """
    ac = get_confidential_app_auth_client(
        client_id=str(client_id), client_secret=client_secret
    )
    try:
        response = ac.oauth2_revoke_token(token)
    except GlobusAPIError as err:
        response = err
    format_and_print(response, verbose=verbose)
