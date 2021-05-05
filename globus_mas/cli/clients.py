import typing as t
import uuid

import typer
from globus_sdk import GlobusAPIError

from globus_mas.authentication import get_basic_authorizer
from globus_mas.cli.helpers import format_and_print
from globus_mas.clients_client import ClientsClient

app = typer.Typer(short_help="Work with Globus Clients")


@app.command()
def list(
    client_id: uuid.UUID = typer.Argument(
        ...,
        help="The authenticating client's id. If unset, "
        "this value will be pulled from an environment variable.",
        envvar="AUTH_CLIENT_ID",
    ),
    client_secret: str = typer.Argument(
        ...,
        help=(
            "The corresponding client id's secret. If unset, this value will "
            "be pulled from an environment variable."
        ),
        envvar="AUTH_CLIENT_SECRET",
    ),
    client: t.Optional[uuid.UUID] = typer.Option(
        None, help="A particular client to return data for."
    ),
):
    """
    List clients the authenticated entity is an owner of.
    """
    authorizer = get_basic_authorizer(
        client_id=str(client_id), client_secret=client_secret
    )
    cc = ClientsClient.new(authorizer=authorizer)
    try:
        if client:
            response = cc.get_client(str(client))
        else:
            response = cc.get_clients()
    except GlobusAPIError as err:
        response = err
    format_and_print(response)


@app.command()
def list_credentials(
    client_id: uuid.UUID = typer.Argument(
        ...,
        help="The authenticating client's id. If unset, "
        "this value will be pulled from an environment variable.",
        envvar="AUTH_CLIENT_ID",
    ),
    client_secret: str = typer.Argument(
        ...,
        help=(
            "The corresponding client id's secret. If unset, this value will "
            "be pulled from an environment variable."
        ),
        envvar="AUTH_CLIENT_SECRET",
    ),
):
    """
    List all credentials owned by the authenticated identity.
    """
    authorizer = get_basic_authorizer(
        client_id=str(client_id), client_secret=client_secret
    )
    cc = ClientsClient.new(authorizer=authorizer)
    try:
        response = cc.get_client_credentials(str(client_id))
    except GlobusAPIError as err:
        response = err
    format_and_print(response)


@app.command()
def create_credential(
    client_id: uuid.UUID = typer.Argument(
        ...,
        help="The authenticating client's id. If unset, "
        "this value will be pulled from an environment variable.",
        envvar="AUTH_CLIENT_ID",
    ),
    client_secret: str = typer.Argument(
        ...,
        help=(
            "The corresponding client id's secret. If unset, this value will "
            "be pulled from an environment variable."
        ),
        envvar="AUTH_CLIENT_SECRET",
    ),
    credential_name: str = typer.Option(..., help="A name for the new credential."),
):
    """
    Create a new credential for by the authenticated identity.
    """
    authorizer = get_basic_authorizer(
        client_id=str(client_id), client_secret=client_secret
    )
    cc = ClientsClient.new(authorizer=authorizer)
    try:
        response = cc.create_client_credential(str(client_id), credential_name)
    except GlobusAPIError as err:
        response = err
    format_and_print(response)


@app.command()
def delete_credential(
    client_id: uuid.UUID = typer.Argument(
        ...,
        help="The authenticating client's id. If unset, "
        "this value will be pulled from an environment variable.",
        envvar="AUTH_CLIENT_ID",
    ),
    client_secret: str = typer.Argument(
        ...,
        help=(
            "The corresponding client id's secret. If unset, this value will "
            "be pulled from an environment variable."
        ),
        envvar="AUTH_CLIENT_SECRET",
    ),
    credential_id: uuid.UUID = typer.Option(
        ..., help="The ID for the credential to delete."
    ),
):
    """
    Delete a credential from the authenticated identity.
    """
    authorizer = get_basic_authorizer(
        client_id=str(client_id), client_secret=client_secret
    )
    cc = ClientsClient.new(authorizer=authorizer)
    try:
        response = cc.delete_client_credential(str(client_id), str(credential_id))
    except GlobusAPIError as err:
        response = err
    format_and_print(response)
