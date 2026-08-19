cmake_minimum_required(VERSION 3.16)
project(example_c_project C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

add_library(example STATIC src/example.c)
target_include_directories(example PUBLIC include)

if(CMAKE_C_COMPILER_ID MATCHES "GNU|Clang")
  option(ENABLE_COVERAGE "Build with gcov/llvm-cov instrumentation" OFF)
  if(ENABLE_COVERAGE)
    target_compile_options(example PRIVATE --coverage -O0 -g)
    target_link_options(example PRIVATE --coverage)
  endif()
endif()

enable_testing()
add_subdirectory(tests)
