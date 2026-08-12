# C

Public headers go in `include/`, implementation in `src/`, tests in `tests/`. Build with CMake:

```sh
cmake -S . -B build
cmake --build build
ctest --test-dir build
```

Format with `.clang-format` (`clang-format -i src/*.c include/*.h`).
