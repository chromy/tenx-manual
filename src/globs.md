# Globs

Many Tenx commands and configuration options take glob patterns as arguments.
The syntax for these patterns are as follows[^1]:

* `?` matches any single character. 
* `*` matches zero or more characters. 
* `**` recursively matches directories but are only legal in three situations.
  First, if the glob starts with <code>\*\*&#x2F;</code>, then it matches
  all directories. For example, <code>\*\*&#x2F;foo</code> matches `foo`
  and `bar/foo` but not `foo/bar`. Secondly, if the glob ends with
  <code>&#x2F;\*\*</code>, then it matches all sub-entries. For example,
  <code>foo&#x2F;\*\*</code> matches `foo/a` and `foo/a/b`, but not `foo`.
  Thirdly, if the glob contains <code>&#x2F;\*\*&#x2F;</code> anywhere within
  the pattern, then it matches zero or more directories. Using `**` anywhere
  else is illegal (N.B. the glob `**` is allowed and means "match everything").
* `{a,b}` matches `a` or `b` where `a` and `b` are arbitrary glob patterns.
  (N.B. Nesting `{...}` is not allowed.)
* `[ab]` matches `a` or `b` where `a` and `b` are characters. Use
  `[!ab]` to match any character except for `a` and `b`.
* Metacharacters such as `*` and `?` can be escaped with character class
  notation. e.g., `[*]` matches `*`.

In some places, negative globs are allowed. These are globs that start with
`!`, and they exclude files that match the pattern. For example, `!**/*.rs`
would exclude all Rust files from a set of files.

  [^1]: From docs for the [globset](https://docs.rs/globset/latest/globset/) crate.
