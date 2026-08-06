cmake_minimum_required(VERSION 3.16)
project(example_c_project C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

add_library(example STATIC src/example.c)
target_include_directories(example PUBLIC include)

enable_testing()
add_subdirectory(tests)
