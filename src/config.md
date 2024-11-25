# Configuration

Configuraton comes from three sources, in order of precedence:

- **Project** configuration in `.tenx.ron`
- **Global** configuration at `~/.config/tenx/tenx.ron`[^xdg], which over-ride the defaults
- Defaults created by tenx on startup

The location of the project configuration file also determines the project root
(unless over-ridden).

## Quick Example

Tenx uses RON ([Rusty Object Notation](https://github.com/ron-rs/ron)) for its
config files. Here's a minimal example from the Tenx project itself:

```ron
(
    retry_limit: 18,
    context: (
        ruskel: ["libtenx"]
    ),
    checks: (
        enable: ["cargo-clippy"]
    )
)
```

This bumps the retry limit, adds a [ruskel](https://github.com/cortesi/ruskel)
skeleton of libtenx (Tenx's own library) as context, and enables the
cargo-clippy check, which is not enabled by default.

## Config File Format

### Global values

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>session_store_dir</code></td>
    <td>
        Directory for storing session data. By default, this is in
        <code>~/.config/tenx</code>. Users will rarely have to change this.
    </td>
</tr>
<tr>
    <td><code>retry_limit</code></td>
    <td>Number of retries</td>
</tr>
</table>

Example:
```ron
(
    session_store_dir: "~/.local/share/tenx",
    retry_limit: 5,
)
```


### Project

Configures the project - that is, which files are included for editing.

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>include</code></td>
    <td>Either <code>git</code> to use git-tracked files, or <code>glob([patterns])</code> for custom patterns</td>
</tr>
<tr>
    <td><code>exclude</code></td>
    <td>List of glob patterns for files to exclude</td>
</tr>
<tr>
    <td><code>root</code></td>
    <td>Either <code>discover</code> for automatic detection or <code>path("path")</code> for explicit path</td>
</tr>
</table>

Example:
```ron
(
    project (
        include: git,
        exclude: ["*.md", "target/"],
        root: discover,
    )
)
```


### Models

Controls model selection and behavior.

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>builtin</code></td>
    <td>Built-in model configurations</td>
</tr>
<tr>
    <td><code>custom</code></td>
    <td>Custom model configurations. Entries with the same name as a builtin will override the builtin</td>
</tr>
<tr>
    <td><code>default</code></td>
    <td>The default model name</td>
</tr>
<tr>
    <td><code>no_stream</code></td>
    <td>Disable streaming for all models</td>
</tr>
</table>

Models configurations come in two varieities - **claude**, which is specific to
the Anthropic API, and **openai**, which can be used for any model compatible
with the OpenAI API.

The possible fields for **claude** models are:

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>name</code></td>
    <td>The name used to refer to this model</td>
</tr>
<tr>
    <td><code>api_model</code></td>
    <td>The API model identifier</td>
</tr>
<tr>
    <td><code>key</code></td>
    <td>The API key</td>
</tr>
<tr>
    <td><code>key_env</code></td>
    <td>Environment variable to load the API key from if key is empty</td>
</tr>
</table>

The possible fields for **openai** models are:

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>name</code></td>
    <td>The name of the model</td>
</tr>
<tr>
    <td><code>api_model</code></td>
    <td>The API model identifier</td>
</tr>
<tr>
    <td><code>key</code></td>
    <td>The API key</td>
</tr>
<tr>
    <td><code>key_env</code></td>
    <td>The environment variable to load the API key from</td>
</tr>
<tr>
    <td><code>api_base</code></td>
    <td>The base URL for the API</td>
</tr>
<tr>
    <td><code>can_stream</code></td>
    <td>Whether the model can stream responses</td>
</tr>
<tr>
    <td><code>no_system_prompt</code></td>
    <td>Whether the model supports a separate system prompt</td>
</tr>
</table>

Example of configuring a custom model using Ollama:

```ron
(
    models: (
        custom: [
            open_ai(
                name: "codellama",
                api_model: "codellama",
                key: "",  // Ollama doesn't need an API key
                key_env: "",
                api_base: "http://localhost:11434/v1",
                can_stream: true,
                no_system_prompt: false,
            ),
        ],
        default: "codellama",
    ),
)
```


### Check Configuration

Configures pre and post checks for code modifications:

- `custom`: Map of custom check configurations, each with:
  - `command`: The command to run
  - `globs`: List of file patterns to check
  - `mode`: When to run (`Pre`, `Post`, or `Both`)
  - `fail_on_stderr`: Whether stderr output indicates failure
- `disable`: List of checks to disable
- `enable`: List of checks to enable
- `no_pre`: Skip all pre-checks
- `only`: Optional single check to run

### Context 

Controls what context is provided to the AI:

- `ruskel`: List of Rust files to parse for skeleton context
- `path`: List of files to include as full context
- `project_map`: Whether to include the project file structure

### Tags Configuration

Controls how code modifications are handled:

- `smart`: Enable smart tag handling
- `replace`: Enable replacement tags
- `udiff`: Enable unified diff format

### Operations Configuration

Controls available operations:

- `edit`: Enable file editing operations

Each configuration section can be specified independently in either the global
or project configuration files. Project configurations take precedence over
global ones.


[^xdg]: This may actually be different based on your [XDG
    configuration](https://specifications.freedesktop.org/basedir-spec/latest/). 