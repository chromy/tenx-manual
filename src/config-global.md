# Global Values

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

# Example

```ron
(
    session_store_dir: "~/.local/share/tenx",
    retry_limit: 5,
)
```
