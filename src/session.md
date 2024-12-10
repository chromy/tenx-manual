# The Session

The session is a core concept in Tenx - it consists of the following:

- The set of files we're currently editing. This is a subset of all the files
  included in the project.
- The non-editable context that we're providing to the model.
- A list of steps, each of which is a request to the model and a response,
  along with any associated information like the patch parsed from the model
  response.

## Creating a session

There are two ways to create a session - explicitly with `tenx new`, which
creates a new empty session, and implicitly with `tenx quick`, which takes a
list of file globs as argument, creates a session with those files, and then
prompts the user for a request to cut code.


## Context
