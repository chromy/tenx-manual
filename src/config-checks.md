# Checks

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

# Example

Example of configuring a custom check.

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
