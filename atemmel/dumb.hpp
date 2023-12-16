#pragma once

#include <algorithm>

template <typename T>
auto dumbSort(T *first, T *last) -> void {
    std::sort(first, last);
}

struct DumbSort {
    template <typename T>
    auto operator()(T *first, T *last) -> void {
        dumbSort(first, last);
    }
};
