# Quickstart

Let's look at an example of using Tenx to implement a small function in Rust.
Say we have a stub Rust project with the follwing in "./src/lib.rs":

```rust
{{#include examples/quickstart_before_lib.rs}} 
```

We'll now use the **tenx quick** command to create a session, add a file to it,
and then issue a code request.

![caption](examples/quickstart_vid.gif)


```rust
{{#include examples/quickstart_after_lib.rs}}
```
