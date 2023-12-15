#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <string_view>
#include <vector>

#include "atemmel/dumb.hpp"

auto ensure(bool condition, std::string_view msg) -> void {
    if (!condition) {
        std::cout << msg << '\n';
        std::exit(1);
    }
}

auto main() -> int {
    std::vector<int> x = {
        1, 5, 3, 7, 2,
    };

    auto sortCheck = [&]() -> bool {
        return std::is_sorted(x.begin(), x.end());
    };

    dumbSort(&*x.begin(), &*x.end());
    ensure(sortCheck(), "dumbSort did not sort as expected");
}
