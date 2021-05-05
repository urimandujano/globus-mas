``globus-mas``
==============

A Globus-oriented CLI to facilitate everyday tasks

**Usage**:

.. code:: console

   $ globus-mas [OPTIONS] COMMAND [ARGS]...

**Options**:

-  ``-V, --version``: Print CLI version number and exit
-  ``--install-completion``: Install completion for the current shell.
-  ``--show-completion``: Show completion for the current shell, to copy
   it or customize the installation.
-  ``--help``: Show this message and exit.

**Commands**:

-  ``clients``: Work with Globus Clients
-  ``groups``: Work with Globus Groups
-  ``scopes``: Work with Globus Scopes
-  ``tokens``: Work with Globus Tokens

``globus-mas clients``
----------------------

**Usage**:

.. code:: console

   $ globus-mas clients [OPTIONS] COMMAND [ARGS]...

**Options**:

-  ``--help``: Show this message and exit.

**Commands**:

-  ``create-credential``: Create a new credential for by the…
-  ``delete-credential``: Delete a credential from the authenticated…
-  ``list``: List clients the authenticated entity is an…
-  ``list-credentials``: List all credentials owned by the…

``globus-mas clients create-credential``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new credential for by the authenticated identity.

**Usage**:

.. code:: console

   $ globus-mas clients create-credential [OPTIONS] CLIENT_ID CLIENT_SECRET

**Arguments**:

-  ``CLIENT_ID``: The authenticating client’s id. If unset, this value
   will be pulled from an environment variable. [env var:
   AUTH_CLIENT_ID;required]
-  ``CLIENT_SECRET``: The corresponding client id’s secret. If unset,
   this value will be pulled from an environment variable. [env var:
   AUTH_CLIENT_SECRET;required]

**Options**:

-  ``--credential-name TEXT``: A name for the new credential. [required]
-  ``--help``: Show this message and exit.

``globus-mas clients delete-credential``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Delete a credential from the authenticated identity.

**Usage**:

.. code:: console

   $ globus-mas clients delete-credential [OPTIONS] CLIENT_ID CLIENT_SECRET

**Arguments**:

-  ``CLIENT_ID``: The authenticating client’s id. If unset, this value
   will be pulled from an environment variable. [env var:
   AUTH_CLIENT_ID;required]
-  ``CLIENT_SECRET``: The corresponding client id’s secret. If unset,
   this value will be pulled from an environment variable. [env var:
   AUTH_CLIENT_SECRET;required]

**Options**:

-  ``--credential-id UUID``: The ID for the credential to delete.
   [required]
-  ``--help``: Show this message and exit.

``globus-mas clients list``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

List clients the authenticated entity is an owner of.

**Usage**:

.. code:: console

   $ globus-mas clients list [OPTIONS] CLIENT_ID CLIENT_SECRET

**Arguments**:

-  ``CLIENT_ID``: The authenticating client’s id. If unset, this value
   will be pulled from an environment variable. [env var:
   AUTH_CLIENT_ID;required]
-  ``CLIENT_SECRET``: The corresponding client id’s secret. If unset,
   this value will be pulled from an environment variable. [env var:
   AUTH_CLIENT_SECRET;required]

**Options**:

-  ``--client UUID``: A particular client to return data for.
-  ``--help``: Show this message and exit.

``globus-mas clients list-credentials``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List all credentials owned by the authenticated identity.

**Usage**:

.. code:: console

   $ globus-mas clients list-credentials [OPTIONS] CLIENT_ID CLIENT_SECRET

**Arguments**:

-  ``CLIENT_ID``: The authenticating client’s id. If unset, this value
   will be pulled from an environment variable. [env var:
   AUTH_CLIENT_ID;required]
-  ``CLIENT_SECRET``: The corresponding client id’s secret. If unset,
   this value will be pulled from an environment variable. [env var:
   AUTH_CLIENT_SECRET;required]

**Options**:

-  ``--help``: Show this message and exit.

``globus-mas groups``
---------------------

**Usage**:

.. code:: console

   $ globus-mas groups [OPTIONS] COMMAND [ARGS]...

**Options**:

-  ``--help``: Show this message and exit.

**Commands**:

-  ``add``: Add one or more users to a group.
-  ``info``: Display information on a specific group.
-  ``list``: List the groups the caller is in.
-  ``new``: Create a new group.
-  ``preferences``
-  ``update-preferences``

``globus-mas groups add``
~~~~~~~~~~~~~~~~~~~~~~~~~

Add one or more users to a group.

**Usage**:

.. code:: console

   $ globus-mas groups add [OPTIONS] GROUP_ID

**Arguments**:

-  ``GROUP_ID``: [required]

**Options**:

-  ``--user TEXT``: A user to add to the group. [repeatable] [required]
-  ``--help``: Show this message and exit.

``globus-mas groups info``
~~~~~~~~~~~~~~~~~~~~~~~~~~

Display information on a specific group.

**Usage**:

.. code:: console

   $ globus-mas groups info [OPTIONS] GROUP_ID

**Arguments**:

-  ``GROUP_ID``: [required]

**Options**:

-  ``--help``: Show this message and exit.

``globus-mas groups list``
~~~~~~~~~~~~~~~~~~~~~~~~~~

List the groups the caller is in.

**Usage**:

.. code:: console

   $ globus-mas groups list [OPTIONS]

**Options**:

-  ``--help``: Show this message and exit.

``globus-mas groups new``
~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new group. The caller’s identity will be the group’s
administrator.

**Usage**:

.. code:: console

   $ globus-mas groups new [OPTIONS] GROUP_NAME

**Arguments**:

-  ``GROUP_NAME``: [required]

**Options**:

-  ``--help``: Show this message and exit.

``globus-mas groups preferences``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Usage**:

.. code:: console

   $ globus-mas groups preferences [OPTIONS]

**Options**:

-  ``--help``: Show this message and exit.

``globus-mas groups update-preferences``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Usage**:

.. code:: console

   $ globus-mas groups update-preferences [OPTIONS] IDENTITIES...

**Arguments**:

-  ``IDENTITIES...``: An identity to allow adding to groups.
   [repeatable] [required]

**Options**:

-  ``--help``: Show this message and exit.

``globus-mas scopes``
---------------------

**Usage**:

.. code:: console

   $ globus-mas scopes [OPTIONS] COMMAND [ARGS]...

**Options**:

-  ``--help``: Show this message and exit.

**Commands**:

-  ``create``: Create a new scope associated with a client.
-  ``delete``: Delete a scope.
-  ``list``: List the scopes associated with a client.
-  ``search``: Search for a scope by UUID or scope string.
-  ``update``: Update an existing scope.

``globus-mas scopes create``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new scope associated with a client.

**Usage**:

.. code:: console

   $ globus-mas scopes create [OPTIONS] CLIENT_ID CLIENT_SECRET

**Arguments**:

-  ``CLIENT_ID``: The client id to which the created scope will belong.
   If unset, this value will be pulled from an environment variable.
   [env var: AUTH_CLIENT_ID;required]
-  ``CLIENT_SECRET``: The corresponding client id’s secret. If unset,
   this value will be pulled from an environment variable. [env var:
   AUTH_CLIENT_SECRET;required]

**Options**:

-  ``--scope-name TEXT``: A name for the new scope [required]
-  ``--scope-description TEXT``: A description for the new scope
   [required]
-  ``--scope-suffix TEXT``: The suffix which gets appended to the
   created scope_string [required]
-  ``--dependent-scope UUID``: A scope upon which the new scope should
   depend. [repeatable]
-  ``--help``: Show this message and exit.

``globus-mas scopes delete``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Delete a scope.

**Usage**:

.. code:: console

   $ globus-mas scopes delete [OPTIONS] CLIENT_ID CLIENT_SECRET

**Arguments**:

-  ``CLIENT_ID``: The client id from which to delete the scope. If
   unset, this value will be pulled from an environment variable. [env
   var: AUTH_CLIENT_ID;required]
-  ``CLIENT_SECRET``: The corresponding client id’s secret. If unset,
   this value will be pulled from an environment variable. [env var:
   AUTH_CLIENT_SECRET;required]

**Options**:

-  ``--scope-id UUID``: The scope UUID. [required]
-  ``--help``: Show this message and exit.

``globus-mas scopes list``
~~~~~~~~~~~~~~~~~~~~~~~~~~

List the scopes associated with a client.

**Usage**:

.. code:: console

   $ globus-mas scopes list [OPTIONS] CLIENT_ID CLIENT_SECRET

**Arguments**:

-  ``CLIENT_ID``: The client id whose scopes to list. If unset, this
   value will be pulled from an environment variable. [env var:
   AUTH_CLIENT_ID;required]
-  ``CLIENT_SECRET``: The corresponding client id’s secret. If unset,
   this value will be pulled from an environment variable. [env var:
   AUTH_CLIENT_SECRET;required]

**Options**:

-  ``--help``: Show this message and exit.

``globus-mas scopes search``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Search for a scope by UUID or scope string. A scope can be searched for
if the client_id is is the direct owner of the scope, or if the
client_id owns the client that owns the scope, or if the scope is
publicly advertised (“advertised”: true).

**Usage**:

.. code:: console

   $ globus-mas scopes search [OPTIONS] CLIENT_ID CLIENT_SECRET

**Arguments**:

-  ``CLIENT_ID``: The client id to which the created scope will belong.
   If unset, this value will be pulled from an environment variable.
   [env var: AUTH_CLIENT_ID;required]
-  ``CLIENT_SECRET``: The corresponding client id’s secret. If unset,
   this value will be pulled from an environment variable. [env var:
   AUTH_CLIENT_SECRET;required]

**Options**:

-  ``--scope TEXT``: The scope string value to lookup. [repeatable]
   [required]
-  ``--as-uuids``: Set this flag if search scopes are provided as UUIDs.
   Otherise, the scopes must be scope strings. [default: False]
-  ``--help``: Show this message and exit.

``globus-mas scopes update``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Update an existing scope. scope_suffixes cannot be updated.

**Usage**:

.. code:: console

   $ globus-mas scopes update [OPTIONS] CLIENT_ID CLIENT_SECRET

**Arguments**:

-  ``CLIENT_ID``: The client id to which the updated scope belongs. If
   unset, this value will be pulled from an environment variable. [env
   var: AUTH_CLIENT_ID;required]
-  ``CLIENT_SECRET``: The corresponding client id’s secret. If unset,
   this value will be pulled from an environment variable. [env var:
   AUTH_CLIENT_SECRET;required]

**Options**:

-  ``--scope-id UUID``: The scope UUID. [required]
-  ``--scope-name TEXT``: A name for the new scope
-  ``--scope-description TEXT``: A description for the new scope
-  ``--dependent-scope UUID``: A scope upon which the new scope should
   depend. [repeatable]
-  ``--help``: Show this message and exit.

``globus-mas tokens``
---------------------

Most of these operations require the use of tokens and secrets. It’s
highly recommended not to paste these credentials since command line
input may be logged and aggregated. Rather, export these values into the
environment in which these commands are run.

**Usage**:

.. code:: console

   $ globus-mas tokens [OPTIONS] COMMAND [ARGS]...

**Options**:

-  ``--help``: Show this message and exit.

**Commands**:

-  ``client-credentials``: Get Access Tokens which directly represent…
-  ``introspect``: Introspect a provided token.
-  ``revoke``: Revoke an Access or Refresh token such that…
-  ``token-for-scope``: Initiate a login to generate a token valid…
-  ``view-dependant-tokens``: Display the dependant tokens for a given…

``globus-mas tokens client-credentials``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get Access Tokens which directly represent the resource server (client
id) and allow it to act on its own.

**Usage**:

.. code:: console

   $ globus-mas tokens client-credentials [OPTIONS] CLIENT_ID CLIENT_SECRET

**Arguments**:

-  ``CLIENT_ID``: The id for the resource server for which the token was
   issued. If unset, this value will be pulled from an environment
   variable. [env var: AUTH_CLIENT_ID;required]
-  ``CLIENT_SECRET``: The corresponding resource server’s secret. If
   unset, this value will be pulled from an environment variable. [env
   var: AUTH_CLIENT_SECRET;required]

**Options**:

-  ``--scope TEXT``: Return an access token for this scope. If not
   provided, tokens for default scopes will be returned. [repeatable]
-  ``--help``: Show this message and exit.

``globus-mas tokens introspect``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Introspect a provided token. The token must have been issued for the
resource server (client id) provided. If the token is invalid or not
intended for use with the resource server, Globus Auth will return an
error.

**Usage**:

.. code:: console

   $ globus-mas tokens introspect [OPTIONS] CLIENT_ID CLIENT_SECRET TOKEN

**Arguments**:

-  ``CLIENT_ID``: The id for the resource server for which the token was
   issued. If unset, this will be pulled from an environment variable.
   [env var: AUTH_CLIENT_ID;required]
-  ``CLIENT_SECRET``: The corresponding resource server’s secret. If
   unset, this will be pulled from an environment variable. [env var:
   AUTH_CLIENT_SECRET;required]
-  ``TOKEN``: A particular token to introspect. If unset, this will be
   pulled from an environment variable. [env var: AUTH_TOKEN;required]

**Options**:

-  ``--full-details``: Include identity and session information in
   output. [default: False]
-  ``--help``: Show this message and exit.

``globus-mas tokens revoke``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Revoke an Access or Refresh token such that they can no longer be used.
The token must have been issued for the resource server (client id)
provided. If the token is invalid or not intended for use with the
resource server, Globus Auth will return an error.

**Usage**:

.. code:: console

   $ globus-mas tokens revoke [OPTIONS] CLIENT_ID CLIENT_SECRET TOKEN

**Arguments**:

-  ``CLIENT_ID``: The id for the resource server for which the token was
   issued. If unset, this value will be pulled from an environment
   variable. [env var: AUTH_CLIENT_ID;required]
-  ``CLIENT_SECRET``: The corresponding resource server’s secret. If
   unset, this value will be pulled from an environment variable. [env
   var: AUTH_CLIENT_SECRET;required]
-  ``TOKEN``: The token to invalidate. If unset, this will be pulled
   from an environment variable. [env var: AUTH_TOKEN;required]

**Options**:

-  ``--help``: Show this message and exit.

``globus-mas tokens token-for-scope``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initiate a login to generate a token valid for the listed scope.

**Usage**:

.. code:: console

   $ globus-mas tokens token-for-scope [OPTIONS] SCOPE

**Arguments**:

-  ``SCOPE``: The scope to retrieve a token for. [required]

**Options**:

-  ``--help``: Show this message and exit.

``globus-mas tokens view-dependant-tokens``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Display the dependant tokens for a given token. The token must have been
issued for the resource server (client id) provided. If the token is
invalid or not intended for use with the resource server, Globus Auth
will return an error.

**Usage**:

.. code:: console

   $ globus-mas tokens view-dependant-tokens [OPTIONS] CLIENT_ID CLIENT_SECRET TOKEN

**Arguments**:

-  ``CLIENT_ID``: The id for the resource server for which the token was
   issued. If unset, this value will be pulled from an environment
   variable. [env var: AUTH_CLIENT_ID;required]
-  ``CLIENT_SECRET``: The corresponding resource server’s secret. If
   unset, this value will be pulled from an environment variable. [env
   var: AUTH_CLIENT_SECRET;required]
-  ``TOKEN``: A particular token to return data on. If unset, this will
   be pulled from an environment variable. [env var:
   AUTH_TOKEN;required]

**Options**:

-  ``--help``: Show this message and exit.
