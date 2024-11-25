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

Controls which files are included in the project context:

- `include`: Either `Git` to use git-tracked files, or `Glob([patterns])` for custom patterns
- `exclude`: List of glob patterns for files to exclude
- `root`: Either `Discover` for automatic detection or `Path("path")` for explicit path


### Models 

Controls model selection and behavior:

- `custom`: A map of custom model configurations. Each model has:
  - `api_model`: The actual model name to use with the API
  - `key_env`: Environment variable containing the API key
  - `api_base`: Optional API endpoint URL
  - `can_stream`: Whether the model supports streaming
  - `no_system_prompt`: Whether to skip system prompts
- `default`: The default model to use
- `no_stream`: Globally disable streaming

Example of a custom model:
```ron
(
    custom: {
        "gpt-4-turbo": (
            api_model: "gpt-4-1106-preview",
            key_env: "OPENAI_API_KEY",
            can_stream: true,
        ),
    },
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
