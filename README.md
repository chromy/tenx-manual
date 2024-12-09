
# Manual for the tenx project

[View Rendered Manual](https://cortesi.github.io/tenx-manual/)


# Dependencies

## [vhs](https://github.com/charmbracelet/vhs)

At the moment, we require the branch with the `Wait` implementation, but I
expect this to be in the main branch soon.

```bash
go install github.com/charmbracelet/vhs@latest
```

## [ansisvg](https://github.com/wader/ansisvg)

```bash
go install github.com/wader/ansisvg@latest
```

# Running

```bash
mdbook serve
```

- Run `./generate.py`, to re-render all examples 
- Push to deploy
