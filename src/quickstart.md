# Quick start

## Step 1: Configure a model

Tenx automatically configures default models based on API keys in the
environment. Refer to the [model config docs](config-models.md) to see which
models are configured for which key, and also how you can manually configure
models if needed. For our example, let's assume we're using Claude Sonnet from
Anthropic:

```bash
export ANTHROPIC_API_KEY="my-api-key"
```

Now, we can inspect the models that tenx has configured to make sure everything
is correct:

<img src="examples/quickstart_models.svg"/>


## Step 2: tenx quick

Now we have a model configured, let's write some code. Say we have a Rust
project with the following in `./src/lib.rs`:

```rust
{{#include examples/quickstart_before.rs}} 
```

First, we ask the model to implement the `fibonacci` function, using the
`quick` command:

![caption](examples/quickstart_quick.gif)

The `quick` command is a shortcut which:

- Creates a new [session](./session.md) (`tenx new`)
- Adds `./src/lib.rs` to the session (`tenx add src/lib.rs`)    
- Issues a request to cut code (`tenx code`)

The implicit **code** request causes tenx to open an editor to get the our
prompt - when we save and quit, tenx gets to work. 

The first thing that happens is that tenx runs the pre checks to ensure the
project is in a consistent state.

<img src="examples/quickstart_check.svg"/>


First, we run the configured checks for our language (Rust in this case), to
ensure that the project is in a consistent state. Then, we send the prompt to
the model, and wait for the response. After we've applied the model's changes,
we run the checks again to ensure that the changes are valid.


## Step 3: tenx code

After our intial edit, we want to continue the session to make a tweak. First,
let's look at what the session currently contains:

<img src="examples/quickstart_session.svg"/>

using the `code` command. The model will get the complete history of our work
so far, so will have the context to make a meaningful change. 

```bash
tenx code
```

![caption](examples/quickstart_code.gif)

Again, we run our checks both before and after the model's changes.

```rust
{{#include examples/quickstart_after.rs}} 
```


