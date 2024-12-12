# The Session

All model interactions happen within the context of a **session**. A session as
a single coherent conversation, which would typically result in one commit. A
consists of the following:

- The set of files we're currently editing. This is a subset of all the files
  included in the [project](./project.md).
- The non-editable [context](./context.md) that we're providing to the model.
- A list of steps, each of which is a request to the model and a response,
  along with any associated information like the patch parsed from the model
  response.
- Information needed to undo any step.

There are a few ways to create a session - explicitly with `tenx new`, which
creates a new empty session, and implicitly with commands like `tenx quick` and
`tenx fix`, both of which take a list of file globs, create a session with
those files. Consult the help for each command for more information.

You can also view the current session with the `tenx session` command:

<img src="examples/tenx_session.svg"/>

The example above introduces another crucial concept - contexts. Tenx has added
a **project map** as context to the session. Read more about contexts in the
[context section](./context.md).


The project map is just a list of
all the files in the project, without their contents. This drives the model's
ability to ask to view or edit files not yet included in the session, if
needed.


## Retry


## Reset


## Code
