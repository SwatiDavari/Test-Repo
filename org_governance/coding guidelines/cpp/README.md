# C++

Same layout as `c/`: public headers in `include/`, implementation in `src/`, tests in `tests/`. Targets C++17.

```sh
cmake -S . -B build
cmake --build build
ctest --test-dir build
```

Pull in third-party deps with vcpkg or Conan rather than vendoring.
