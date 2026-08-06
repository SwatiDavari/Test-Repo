cmake_minimum_required(VERSION 3.16)
project(example_cpp_project CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(example STATIC src/example.cpp)
target_include_directories(example PUBLIC include)

enable_testing()
add_subdirectory(tests)
