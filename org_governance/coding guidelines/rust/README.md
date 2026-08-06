# Rust

Cargo workspace; one crate per component under `crates/`. Add new crates with `cargo new crates/<name> --lib` and list them in the workspace `Cargo.toml`.

```sh
cargo fmt --check
cargo clippy --workspace
cargo test --workspace
```
