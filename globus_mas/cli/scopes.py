import typing as t
import uuid

import typer
from globus_sdk import GlobusAPIError

from globus_mas.authentication import get_basic_authorizer
from globus_mas.cli.callbacks import scope_suffix_validator
from globus_mas.cli.helpers import format_and_print
from globus_mas.scopes_client import ScopesClient

app = typer.Typer(short_help="Work with Globus Scopes")


@app.command()
def create(
    client_id: uuid.UUID = typer.Argument(
        ...,
        help="The client id to which the created scope will belong. If unset, "
        "this value will be pulled from an environment variable.",
        envvar="AUTH_CLIENT_ID",
    ),
    client_secret: str = typer.Argument(
        ...,
        help="The corresponding client id's secret. If unset, this value will be pulled "
        "from an environment variable.",
        envvar="AUTH_CLIENT_SECRET",
    ),
    scope_name: str = typer.Option(..., help="A name for the new scope"),
    scope_description: str = typer.Option(..., help="A description for the new scope"),
    scope_suffix: str = typer.Option(
        ...,
        help="The suffix which gets appended to the created scope_string",
        callback=scope_suffix_validator,
    ),
    dependent_scopes: t.List[uuid.UUID] = typer.Option(
        None,
        "--dependent-scope",
        help="A scope upon which the new scope should depend. [repeatable]",
    ),
):
    """
    Create a new scope associated with a client.
    """
    authorizer = get_basic_authorizer(
        client_id=str(client_id), client_secret=client_secret
    )
    sc = ScopesClient.new(authorizer=authorizer)
    try:
        response = sc.create_scope(
            str(client_id),
            scope_name=scope_name,
            scope_description=scope_description,
            scope_suffix=scope_suffix,
            dependent_scopes=[str(ds) for ds in dependent_scopes],
        )
    except GlobusAPIError as err:
        response = err
    format_and_print(response)


@app.command()
def update(
    client_id: uuid.UUID = typer.Argument(
        ...,
        help="The client id to which the updated scope belongs. If unset, "
        "this value will be pulled from an environment variable.",
        envvar="AUTH_CLIENT_ID",
    ),
    client_secret: str = typer.Argument(
        ...,
        help="The corresponding client id's secret. If unset, this value will be pulled "
        "from an environment variable.",
        envvar="AUTH_CLIENT_SECRET",
    ),
    scope_id: uuid.UUID = typer.Option(..., help="The scope UUID."),
    scope_name: t.Optional[str] = typer.Option(None, help="A name for the new scope"),
    scope_description: t.Optional[str] = typer.Option(
        None, help="A description for the new scope"
    ),
    dependent_scopes: t.Optional[t.List[uuid.UUID]] = typer.Option(
        None,
        "--dependent-scope",
        help="A scope upon which the new scope should depend. [repeatable]",
    ),
):
    """
    Update an existing scope. scope_suffixes cannot be updated.
    """
    authorizer = get_basic_authorizer(
        client_id=str(client_id), client_secret=client_secret
    )
    sc = ScopesClient.new(authorizer=authorizer)
    try:
        response = sc.update_scope(
            str(scope_id),
            scope_name=scope_name,
            scope_description=scope_description,
            dependent_scopes=[str(ds) for ds in dependent_scopes]
            if dependent_scopes
            else None,
        )
    except GlobusAPIError as err:
        response = err
    format_and_print(response)


@app.command()
def delete(
    client_id: uuid.UUID = typer.Argument(
        ...,
        help="The client id from which to delete the scope. If unset, this value will "
        "be pulled from an environment variable.",
        envvar="AUTH_CLIENT_ID",
    ),
    client_secret: str = typer.Argument(
        ...,
        help="The corresponding client id's secret. If unset, this value will be pulled "
        "from an environment variable.",
        envvar="AUTH_CLIENT_SECRET",
    ),
    scope_id: uuid.UUID = typer.Option(..., help="The scope UUID."),
):
    """
    Delete a scope.
    """
    authorizer = get_basic_authorizer(
        client_id=str(client_id), client_secret=client_secret
    )
    sc = ScopesClient.new(authorizer=authorizer)
    try:
        response = sc.delete_scope(scope_id)
    except GlobusAPIError as err:
        response = err
    format_and_print(response)


@app.command()
def list(
    client_id: uuid.UUID = typer.Argument(
        ...,
        help="The client id whose scopes to list. If unset,  this value will be pulled "
        "from an environment variable.",
        envvar="AUTH_CLIENT_ID",
    ),
    client_secret: str = typer.Argument(
        ...,
        help="The corresponding client id's secret. If unset, this value will be pulled "
        "from an environment variable.",
        envvar="AUTH_CLIENT_SECRET",
    ),
):
    """
    List the scopes associated with a client.
    """
    authorizer = get_basic_authorizer(
        client_id=str(client_id), client_secret=client_secret
    )
    sc = ScopesClient.new(authorizer=authorizer)
    try:
        response = sc.list_scopes()
    except GlobusAPIError as err:
        response = err
    format_and_print(response)


@app.command()
def search(
    client_id: uuid.UUID = typer.Argument(
        ...,
        help="The client id to which the created scope will belong. If unset, "
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
    scopes: t.List[str] = typer.Option(
        ...,
        "--scope",
        help="The scope string value to lookup. [repeatable]",
    ),
    as_uuids: bool = typer.Option(
        False,
        "--as-uuids/",
        help="Set this flag if search scopes are provided as UUIDs. Otherise, the "
        "scopes must be scope strings.",
    ),
):
    """
    Search for a scope by UUID or scope string. A scope can be searched for if
    the client_id is is the direct owner of the scope, or if the client_id owns
    the client that owns the scope, or if the scope is publicly advertised
    ("advertised": true).
    """
    authorizer = get_basic_authorizer(
        client_id=str(client_id), client_secret=client_secret
    )
    sc = ScopesClient.new(authorizer=authorizer)
    try:
        if as_uuids:
            response = sc.get_scopes_by_id(*scopes)
        else:
            response = sc.get_scopes_by_string(*scopes)
    except GlobusAPIError as err:
        response = err
    format_and_print(response)
