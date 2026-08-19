#include <cassert>
#include "example.hpp"

int main() {
    assert(example::add(2, 3) == 5);
    assert(example::add(-1, 1) == 0);
    assert(example::add(0, 0) == 0);
    return 0;
}
