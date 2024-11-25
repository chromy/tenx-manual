# Dialect

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