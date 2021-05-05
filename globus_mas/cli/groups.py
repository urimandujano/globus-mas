import typing as t
import uuid

import typer

from globus_mas.authentication import authorizer_for_scope
from globus_mas.cli.callbacks import uniqueify
from globus_mas.cli.helpers import format_and_print
from globus_mas.groups_client import GROUPS_SCOPE, GroupsClient

app = typer.Typer(short_help="Work with Globus Groups")


@app.command()
def list():
    """
    List the groups the caller is in.
    """
    authorizer = authorizer_for_scope(GROUPS_SCOPE)
    gc = GroupsClient.new(authorizer=authorizer)
    response = gc.list_groups()
    format_and_print(response)


@app.command()
def info(group_id: uuid.UUID):
    """
    Display information on a specific group.
    """
    authorizer = authorizer_for_scope(GROUPS_SCOPE)
    gc = GroupsClient.new(authorizer=authorizer)
    response = gc.group_info(str(group_id))
    format_and_print(response)


@app.command()
def new(group_name: str):
    """
    Create a new group. The caller's identity will be the group's administrator.
    """
    authorizer = authorizer_for_scope(GROUPS_SCOPE)
    gc = GroupsClient.new(authorizer=authorizer)
    response = gc.new_group(group_name)
    format_and_print(response)


@app.command()
def add(
    group_id: uuid.UUID,
    users: t.List[str] = typer.Option(
        ...,
        "--user",
        help="A user to add to the group. [repeatable]",
        callback=uniqueify,
    ),
):
    """
    Add one or more users to a group.
    """
    authorizer = authorizer_for_scope(GROUPS_SCOPE)
    gc = GroupsClient.new(authorizer=authorizer)
    response = gc.add_to_group(str(group_id), *users)
    format_and_print(response)


@app.command()
def preferences():
    authorizer = authorizer_for_scope(GROUPS_SCOPE)
    gc = GroupsClient.new(authorizer=authorizer)
    response = gc.get_preferences()
    format_and_print(response)


@app.command()
def update_preferences(
    identities: t.List[str] = typer.Argument(
        ...,
        help="An identity to allow adding to groups. [repeatable]",
        callback=uniqueify,
    ),
):
    authorizer = authorizer_for_scope(GROUPS_SCOPE)
    gc = GroupsClient.new(authorizer=authorizer)
    response = gc.update_preferences(*identities)
    format_and_print(response)
