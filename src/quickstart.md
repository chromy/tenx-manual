# Quickstart

Let's look at an example of using Tenx to implement a small function in Rust.
Say we have a stub Rust project with the follwing in "./src/lib.rs":

```rust
{{#include examples/quickstart_before_lib.rs}} 
```

First, we want to ask the model to implement the Fibonacci function. We'll
create a new session, add a `./src/lib.rs` to it, and then issue a code
request. In this case, we're using `quick`, which rolls all of this up into a
single command:

```bash
tenx quick
```

This is a shorthand for the following sequence:

```bash
tenx new
tenx add src/lib.rs
tenx code
```

When we issue the `quick` command, an editor is opened for us to input our
prompt. When we save and quit, the model will get to work.

After the model has made it's initial edit, we want to continue the session to
make a tweak. The model will get the complete history of our work so far, so
will have the context to make a meaningful change. We use the `code` command to
request that the model produce code within the current session:

```bash
tenx code
```

Let's see what this looks like in action:

![caption](examples/quickstart_vid.gif)

After the model has made its changes, this is the resulting code. Success!


```rust
{{#include examples/quickstart_after_lib.rs}}
```
