#pragma once

#include <algorithm>
template <typename T>
auto dumbSort(T *first, T *last) -> void {
    for (auto it = first; it != last; it++) {
        for (auto jt = first; jt != last; jt++) {
            if (*it < *jt) {
                std::iter_swap(it, jt);
            }
        }
    }
}
