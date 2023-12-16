#pragma once

#include <algorithm>

namespace atemmel {

template <typename T>
static auto dumbSort(T *first, T *last) -> void {
    std::sort(first, last);
}

struct DumbSort {
    template <typename T>
    auto operator()(T *first, T *last) -> void {
        dumbSort(first, last);
    }
};

}  // namespace atemmel
