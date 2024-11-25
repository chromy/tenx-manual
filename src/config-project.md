# Project

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

# Example

```ron
(
    project (
        include: git,
        exclude: ["*.md", "target/"],
        root: discover,
    )
)
```
