#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <chrono>
#include <deque>
#include "graph.h"
#include "heap.h"

using namespace std;

deque<int> read_inputs(string file_name)
{
    ifstream inputFile;
    inputFile.open(file_name, ifstream::in);
    if (!inputFile.is_open())
    {
        cerr << "Failed to open input file" << std::endl;
    }

    string line;
    deque<int> inputs;
    while (getline(inputFile, line, '\n'))
    {
        inputs.push_back(stoi(line));
    }

    return inputs;
}

int compute_median(deque<int> &input)
{
    // Define 2 heaps, 1st one a max heap to store
    // smaller half of numbers seen thus far and
    // 2nd one a min heap to store larger half of
    // numbers seen thus far.
    Heap<int> min_h, max_h;
    int size = input.size();
    int median = input.front();

    // Handle edge case, that is, computing median
    // for 2 element case.
    // TBD: check if we can absorb this into main
    // while loop for handling larger num elems.
    if (input.at(0) > input.at(1))
    {
        min_h.insert(input.at(0), input.at(0));
        max_h.insert(-input.at(1), input.at(1));
        median += input.at(1);
    }
    else
    {
        min_h.insert(input.at(1), input.at(1));
        min_h.insert(-input.at(0), input.at(0));
        median += input.at(0);
    }
    // Remove elements for which we have computed
    // running median and inserted to heap(s).
    size -= 2;
    input.pop_front();
    input.pop_front();

    // continue computing running median for remaining
    // elements
    while (size-- > 0)
    {
        // element larger than smallest element in heap
        // with larger half of elements => it needs to
        // be inserted in min heap.
        if (input.front() >= min_h.find_min().first)
        {
            min_h.insert(input.front(), input.front());
            input.pop_front();
        }
        // element smaller than largest element in heap
        // with smaller half of elements => it needs to
        // be inserted in max heap.
        else if (input.front() < -max_h.find_min().first)
        {
            max_h.insert(-input.front(), input.front());
            input.pop_front();
        }
        else
        {
            max_h.insert(-input.front(), input.front());
            input.pop_front();
        }

        // rebalance heaps to maintain the invariant
        if (min_h.size() - max_h.size() > 1)
        {
            // extract smallest element from heap with
            // larger elements and insert it into heap
            // with smaller elements
            auto a = min_h.get_min();
            max_h.insert(-a.first, a.first);
        }
        else if (max_h.size() - min_h.size() > 1)
        {
            // extract largest element from heap with
            // smaller elements and insert it into heap
            // with larger elements
            auto a = max_h.get_min();
            min_h.insert(-a.first, -a.first);
        }

        // Extract median element and add to running sum
        if (max_h.size() >= min_h.size())
        {
            median -= max_h.find_min().first;
        }
        else
        {
            median += min_h.find_min().first;
        }
    }

    return median % 10000;
}

int main()
{
    auto inputs = read_inputs("median.txt");
    auto result = compute_median(inputs);
    std::cout << "median: " << result;
}
