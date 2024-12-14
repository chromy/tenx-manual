# Context

Controls what context is included in model interactions by default.

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>ruskel</code></td>
    <td>List of Rust module outlines to include</td>
</tr>
<tr>
    <td><code>path</code></td>
    <td>List of project files to include</td>
</tr>
<tr>
    <td><code>project_map</code></td>
    <td>Whether to include a project file map</td>
</tr>
<tr>
    <td><code>text</code></td>
    <td>List of named text blocks to include</td>
</tr>
<tr>
    <td><code>url</code></td>
    <td>List of URLs to include</td>
</tr>
</table>

Text blocks have the following fields:

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>name</code></td>
    <td>Name of the text block</td>
</tr>
<tr>
    <td><code>content</code></td>
    <td>Content of the text block</td>
</tr>
</table>

# Example

```ron
(
    context: (
        ruskel: ["src/lib.rs", "src/main.rs"],
        path: ["Cargo.toml", "README.md"],
        project_map: true,
        text: [
            (
                name: "style_guide",
                content: "- Use 4 spaces for indentation\n- Max line length 80 chars",
            ),
        ],
        url: ["https://example.com/api-docs"],
    ),
)
```
