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

[^xdg]: This may actually be different based on your [XDG
    configuration](https://specifications.freedesktop.org/basedir-spec/latest/). 