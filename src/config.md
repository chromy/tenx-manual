# Configuration

Tenx uses RON ([Rusty Object Notation](https://github.com/ron-rs/ron)) for its
config files. Configuraton comes from three sources, in order of precedence:

- **Project** configuration in `.tenx.ron`
- **Global** configuration at `~/.config/tenx/tenx.ron`[^xdg]
- Defaults created by tenx on startup

The location of the project configuration file also determines the project root
(unless over-ridden). The first thing you should do when setting up Tnex is to
create a `.tenx.ron` file in the root of your project.

```bash
cd ./my/project
touch .tenx.ron
```

You can view the full current configuration with:

```bash
tenx config
```

And you can view the configuration defaults with:

```bash
tenx config --defaults
```

These commands output the configuration in RON format, so this is also a good
way to get an overview of the configuration format.


## Quick Example

 Here's a minimal example from the Tenx project itself:

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

[^xdg]: This may actually be different based on your [XDG
    configuration](https://specifications.freedesktop.org/basedir-spec/latest/). 
