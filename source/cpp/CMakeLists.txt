cmake_minimum_required(VERSION 3.16)
project(example_cpp_project CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(example STATIC src/example.cpp)
target_include_directories(example PUBLIC include)

if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
  option(ENABLE_COVERAGE "Build with gcov/llvm-cov instrumentation" OFF)
  if(ENABLE_COVERAGE)
    target_compile_options(example PRIVATE --coverage -O0 -g)
    target_link_options(example PRIVATE --coverage)
  endif()
endif()

enable_testing()
add_subdirectory(tests)
