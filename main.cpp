#include <cxxabi.h>

#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <string_view>
#include <typeinfo>
#include <vector>

#include "atemmel/dumb.hpp"

struct Datasets {
    std::vector<std::string> stringDataset;
    std::vector<int64_t> integerDataset;
};

auto eprint(std::string_view msg) -> void {
    std::cerr << msg << '\n';
};

auto eprint(std::string_view msg, std::string_view rest...) -> void {
    std::cerr << msg;
    eprint(rest);
};

auto ensure(bool condition, std::string_view msg...) -> void {
    if (!condition) {
        eprint(msg);
        std::exit(1);
    }
}

auto readStrings() -> std::vector<std::string> {
    auto strings = std::vector<std::string>();
    auto file    = std::ifstream("datasets/string-dataset.txt");
    std::string line;
    while (std::getline(file, line)) {
        strings.push_back(line);
    }
    return strings;
}

auto readInts() -> std::vector<int64_t> {
    auto ints = std::vector<int64_t>();
    auto file = std::ifstream("datasets/integer-dataset.txt");
    std::string line;
    while (std::getline(file, line)) {
        ints.push_back(std::stoi(line));
    }
    return ints;
}

template <typename T>
auto prettyTypeid() -> std::string {
    int status;
    char* demangled = abi::__cxa_demangle(typeid(T).name(), 0, 0, &status);
    std::string str = demangled;
    free(demangled);
    return str;
}

template <typename SortImpl, typename Dataset>
auto benchmarkImpl(SortImpl sort, Dataset dataset, std::string_view datasetName)
    -> void {
    auto isSorted = [](const auto& v) -> bool {
        return std::is_sorted(v.begin(), v.end());
    };

    auto now   = []() { return std::chrono::high_resolution_clock::now(); };
    auto delta = [](auto before, auto after) -> double {
        return std::chrono::duration<double, std::milli>(after - before)
            .count();
    };

    {
        std::cout << datasetName << ": ";
        std::cout.flush();

        auto before = now();
        sort(&*dataset.begin(), &*dataset.end());
        auto after = now();

        ensure(isSorted(dataset), prettyTypeid<SortImpl>(),
               " did not manage to sort ", datasetName);
        auto dt = delta(before, after);
        std::cout << dt << "ms\n";
    }
}

template <typename SortImpl>
auto benchmark(SortImpl sort, const Datasets& datasets) -> void {
    std::cerr << "Benchmarking " << prettyTypeid<SortImpl>() << ":\n";
    benchmarkImpl(sort, datasets.stringDataset, "string-dataset");
    benchmarkImpl(sort, datasets.integerDataset, "integer-dataset");
}

auto main() -> int {
    const auto datasets = Datasets{
        .stringDataset  = readStrings(),
        .integerDataset = readInts(),
    };

    benchmark(atemmel::DumbSort{}, datasets);
}
