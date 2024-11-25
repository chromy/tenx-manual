# Configuration

Configuraton comes from three sources, in order of precedence:

- **Project** configuration in `.tenx.ron`
- **Global** configuration at `~/.config/tenx/tenx.ron`[^xdg], which over-ride the defaults
- Defaults created by tenx on startup

The location of the project configuration file also determines the project root
(unless over-ridden).

You can view the current configuration with:

```bash
tenx config
```

And you can view the default configuration with:

```bash
tenx config --defaults
```


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


### Checks

Controls pre and post checks for code modifications.

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>custom</code></td>
    <td>Custom check configurations. Entries with the same name as a builtin will override the builtin</td>
</tr>
<tr>
    <td><code>builtin</code></td>
    <td>Built-in check configurations</td>
</tr>
<tr>
    <td><code>disable</code></td>
    <td>List of checks to disable</td>
</tr>
<tr>
    <td><code>enable</code></td>
    <td>List of checks to enable</td>
</tr>
<tr>
    <td><code>no_pre</code></td>
    <td>Skip all pre-checks</td>
</tr>
<tr>
    <td><code>only</code></td>
    <td>Optional single check name to run</td>
</tr>
</table>

Check configurations have the following fields:

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>name</code></td>
    <td>Name of the check for display and error reporting</td>
</tr>
<tr>
    <td><code>command</code></td>
    <td>Shell command to execute, run with sh -c</td>
</tr>
<tr>
    <td><code>globs</code></td>
    <td>List of glob patterns to match against files for determining relevance</td>
</tr>
<tr>
    <td><code>default_off</code></td>
    <td>Whether this check defaults to off in the configuration</td>
</tr>
<tr>
    <td><code>fail_on_stderr</code></td>
    <td>Whether to treat any stderr output as a failure, regardless of exit code</td>
</tr>
<tr>
    <td><code>mode</code></td>
    <td>When this check should run - one of <code>pre</code>, <code>post</code>, or <code>both</code></td>
</tr>
</table>

Example of configuring a custom check:

```ron
(
    checks: (
        custom: [
            (
                name: "mypy",
                command: "mypy --strict",
                globs: ["*.py"],
                default_off: false,
                fail_on_stderr: true,
                mode: both,
            ),
        ],
        enable: ["cargo-clippy"],
    ),
)
```

### Context

Controls what context is provided to the AI model.

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>ruskel</code></td>
    <td>List of Rust files to parse for skeleton context using ruskel</td>
</tr>
<tr>
    <td><code>path</code></td>
    <td>List of files to include as full context</td>
</tr>
<tr>
    <td><code>project_map</code></td>
    <td>Whether to include the project file structure</td>
</tr>
<tr>
    <td><code>text</code></td>
    <td>List of named text snippets to include as context</td>
</tr>
</table>

Example:
```ron
(
    context: (
        ruskel: ["tokio", "libtenx"],
        path: ["README.md", "Cargo.toml"],
        project_map: true,
        text: [
            (
                name: "style_guide",
                content: "Code style guidelines...",
            ),
        ],
    ),
)
```


### Dialect

Settings related to the dialect we are using to communicate to models. For the moment, we have only one dialect, so this section is pretty simple.

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>edit</code></td>
    <td>Allow the model to request to edit files in the project map</td>
</tr>
</table>

Example:
```ron
(
    dialect: (
        edit: true,
    ),
)
```



### Tags

Controls the **tags** dialect. This is a *DEVELOPER ONLY* section for now, and
allows you to enable functionality that is currently broken. 

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>smart</code></td>
    <td>Enable smart tag handling (experimental)</td>
</tr>
<tr>
    <td><code>replace</code></td>
    <td>Enable replacement tags</td>
</tr>
<tr>
    <td><code>udiff</code></td>
    <td>Enable unified diff format (experimental)</td>
</tr>
</table>

Example:
```ron
(
    tags: (
        smart: false,
        replace: true,
        udiff: false,
    ),
)
```



[^xdg]: This may actually be different based on your [XDG
    configuration](https://specifications.freedesktop.org/basedir-spec/latest/). 
