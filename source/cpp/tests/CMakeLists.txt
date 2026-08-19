# Plain assert-based unit test wired into CTest.
# Swap for GoogleTest/Catch2 later if richer assertions/fixtures are needed.

add_executable(test_example test_example.cpp)
target_link_libraries(test_example PRIVATE example)
add_test(NAME test_example COMMAND test_example)
