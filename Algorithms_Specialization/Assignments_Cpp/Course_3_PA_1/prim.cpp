#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <chrono>
#include "graph.h"
#include "heap.h"

int main()
{
    Graph<int> graph;
    graph.create_graph("prim.txt");
    graph.print_graph();
    auto ans = graph.Prim(1);
    std::cout << "answer = " << ans << std::endl;
}

template <typename T>
void Graph<T>::create_graph(const std::string file_name)
{
    std::ifstream inputFile;
    // Set exceptions to be thrown on failure
    inputFile.exceptions(std::ifstream::badbit);
    try
    {
        inputFile.open(file_name, std::ifstream::in);
    }
    catch (const std::exception &e)
    {
        std::cerr << e.what() << '\n';
        std::cerr << "Failure to open input file \n";
    }

    std::string line;
    std::getline(inputFile, line, '\n');
    while (std::getline(inputFile, line, '\n'))
    {
        std::stringstream ss(line);
        std::string word;
        std::vector<std::string> vals;
        while (std::getline(ss, word, ' '))
        { // Extract word from the stream.
            vals.push_back(word);
        }
        vertex_mapping[stoi(vals.at(0))].push_back(std::make_pair(stoi(vals.at(1)), stoi(vals.at(2)))); // TBD: conversions should be string to type "T"
        vertex_mapping[stoi(vals.at(1))].push_back(std::make_pair(stoi(vals.at(0)), stoi(vals.at(2)))); // TBD: conversions should be string to type "T"
    }
    inputFile.close();
}

template <typename T>
void Graph<T>::print_graph()
{
    for (auto &i : vertex_mapping)
    {
        std::cout << i.first << " => ";
        for (auto &j : i.second)
        {
            std::cout << j.first << "[" << j.second << "]" << " ";
        }
        std::cout << std::endl;
    }
}

// overloaded operator to output vectors
template <typename T>
std::ostream &operator<<(std::ostream &os, std::vector<T> &v)
{
    os << "[";
    for (int i = 0; i < v.size(); ++i)
    {
        os << v.at(i);
        if (i != v.size() - 1)
            os << ", ";
    }
    os << "]\n";
    return os;
}

// overloaded operator to output heap
template <typename T>
std::ostream &operator<<(std::ostream &os, std::vector<std::pair<T, T>> &v)
{
    os << "[";
    for (int i = 0; i < v.size(); ++i)
    {
        os << "[" << v.at(i).first << " , " << v.at(i).second << "]";
        if (i != v.size() - 1)
            os << ", ";
    }
    os << "]\n";
    return os;
}

template <typename T>
int Graph<T>::Prim(const T &source)
{
    constexpr int MAX_DIST = INT32_MAX;
    int g_size = vertex_mapping.size();
    Heap<int> heap;
    std::vector<int> visited_nodes(g_size + 1, 0);
    visited_nodes[source] = 1;
    // Insert {dist, vertex} pairs to create heap
    for (auto i = 1; i < visited_nodes.size(); i++)
    {
        int flag = 0;
        for (auto j : vertex_mapping[source])
        {
            if (i == j.first)
            {
                flag = 1;
                heap.insert(j.second, i);
                break;
            }
        }
        if (!flag && (i != source))
        {
            heap.insert(MAX_DIST, i);
        }
    }

    // Continue until all the vertices in graph have been visited
    int sum = 0;
    while (!std::all_of(visited_nodes.begin() + 1, visited_nodes.end(), [&](int i)
                        { return i == 1; }))
    {
        // Extract next vertex at shortest distance from visited vertices cluster
        auto w = heap.get_min();
        sum += w.first;
        visited_nodes.at(w.second) = 1;

        for (auto &i : vertex_mapping[w.second])
        { // Update shortest dist. for all vertices connected to last vertex added to cluster
            if (visited_nodes.at(i.first) == 0)
            {
                auto p = heap.delete_(i.first);
                auto dist = std::min(i.second, p.first);
                heap.insert(dist, p.second);
            }
        }
    }
    return sum;
}