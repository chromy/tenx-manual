# Project

Configures the project - that is, which files are included for editing.

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>include</code></td>
    <td>List of inclusion rules. Each rule can be either <code>git</code> to
    include all git-tracked files, or <code>glob(pattern)</code> for glob
    patterns</td>
</tr>
<tr>
    <td><code>exclude</code></td>
    <td>List of glob patterns for files to exclude</td>
</tr>
<tr>
    <td><code>root</code></td>
    <td>Project root directory path</td>
</tr>
</table>

# Example

```ron
(
    project: (
        include: [
            git,
            glob("scripts/*.py"),
        ],
        exclude: ["*.md", "target/"],
        root: "./",
    )
)
```
