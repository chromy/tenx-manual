# Project

Configures the project - that is, the location of our file tree, and which
files are included for editing.

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>globs</code></td>
    <td>List of inclusion and exclusion glob patterns. Exclusion paterns start
    with a <b>!</b>. By default, all files in the root are included, unless
    excluded in a .gitignore, .ignore or git exclude file.</td>
</tr>
<tr>
    <td><code>root</code></td>
    <td>Project root directory</td>
</tr>
</table>

# Example

```ron
(
    project: (
        globs: [
            "!target/**",
            "**/*.rs",
        ],
        root: "./",
    )
)
```
