#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <chrono>
#include "graph.h"
#include "heap.h"

int main(){
    Graph<int> graph;
    graph.create_graph("djikstra.txt");
    graph.print_graph();
    auto start = std::chrono::high_resolution_clock::now();
    if (1){
        graph.Djikstra_fast(1);
    }
    else {
        graph.Djikstra(1);
    }
    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
    std::cout << duration.count() << std::endl;
}

// overloaded operator to output vectors
template <typename T>
std::ostream& operator<<(std::ostream& os, std::vector<T>& v) 
{ 
    os << "[";
    for (int i = 0; i < v.size(); ++i) { 
        os << v.at(i); 
        if (i != v.size() - 1) 
            os << ", "; 
    }
    os << "]\n";
    return os; 
}

// overloaded operator to output heap
template <typename T>
std::ostream& operator<<(std::ostream& os, std::vector<std::pair<T,T>>& v) 
{ 
    os << "[";
    for (int i = 0; i < v.size(); ++i) { 
        os << "[" << v.at(i).first << " , " << v.at(i).second << "]"; 
        if (i != v.size() - 1) 
            os << ", "; 
    }
    os << "]\n";
    return os; 
}

template <typename T>
void Graph<T>::create_graph(const std::string file_name){
    std::ifstream inputFile;
    // Set exceptions to be thrown on failure
    inputFile.exceptions(std::ifstream::failbit | std::ifstream::badbit);
    try
    {
        inputFile.open(file_name, std::ifstream::in);
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
        std::cerr << "Failure to open input file \n";
    }
    
    std::string line;
    while (std::getline(inputFile, line, '\n')) {
        std::stringstream ss(line);
        std::string word;
        std::vector<std::string> vertices;
        while (std::getline(ss, word, '\t')) { // Extract word from the stream.
            vertices.push_back(word);
        }
        int node = stoi(vertices.at(0)); // TBD: This should be string to type "T" conversion
        vertices.erase(vertices.cbegin());
        for(auto& i: vertices){
            std::stringstream ss(i);
            std::vector<std::string> words;
            std::string word;
            while (std::getline(ss, word, ','))
                words.push_back(word);  
            vertex_mapping[node].push_back(std::make_pair(stoi(words[0]), stoi(words[1]))); // TBD: conversions should be string to type "T"
        }
    }
    inputFile.close(); 
}

template <typename T>
void Graph<T>::print_graph(){
    for (auto& i:vertex_mapping){
        std::cout << i.first << " => ";
        for (auto& j:i.second){
          std::cout <<  j.first << "[" << j.second << "]" << " ";
        }
        std::cout << std::endl;
    }
}

template <typename T>
void Graph<T>::Djikstra(const T& source){
    constexpr int MAX_DIST = INT32_MAX;
    int g_size = vertex_mapping.size();
    std::vector<int> visited_nodes(g_size+1, 0);
    std::vector<std::vector<int>> shortest_path(g_size+1);
    std::vector<int> shortest_distance(g_size+1, MAX_DIST);
    shortest_distance.at(source) = 0;
    visited_nodes.at(source) = 1;
    shortest_path.at(source).push_back(source);

    do {
        int dist = MAX_DIST, index, index_src;
        for(int i=1; i<=g_size; i++){
            if(visited_nodes.at(i) == 1){  // check if source is in visited cluster
                for(auto& j:vertex_mapping[i]){  // loop through all edges connected to this node
                    if(visited_nodes.at(j.first) == 0){  // check if dst is in not visited cluster 
                        if(shortest_distance.at(i) + j.second < dist){
                            dist = shortest_distance.at(i) + j.second;
                            index = j.first;
                            index_src = i;
                        }
                    }
                }
            }
        } // at the end of this loop we should have added 1 more node to visited cluster
        shortest_distance.at(index) = dist;
        visited_nodes.at(index) = 1;
        shortest_path.at(index).insert(shortest_path.at(index).end(), shortest_path.at(index_src).begin(), shortest_path.at(index_src).end());
        shortest_path.at(index).push_back(index);
    } // exit only when all nodes have been visited
    while(!std::all_of(visited_nodes.begin()+1, visited_nodes.end(), [&](int i) {return i == visited_nodes.at(source);}));

    std::vector<int> a = {7,37,59,82,99,115,133,165,188,197};
    for(auto& i:a) //Answers {2599 2610 2947 2052 2367 2399 2029 2442 2505 3068}
        std::cout << shortest_distance.at(i) << " " << shortest_path.at(i) << std::endl;
}

template <typename T>
void Graph<T>::Djikstra_fast(const T& source){
    constexpr int MAX_DIST = INT32_MAX;
    int g_size = vertex_mapping.size();
    Heap<int> heap;
    std::vector<int> visited_nodes(g_size+1, 0);
    std::vector<int> shortest_distance(g_size+1, MAX_DIST);
    shortest_distance.at(source) = 0;
    // Insert {dist, vertex} pairs to create heap
    // TBD: convert to heapify to reduce time from O(log n) to O(n)
    for(auto i=1; i<visited_nodes.size() ; i++){
        heap.insert(shortest_distance.at(i), i);
    }

    // Continue until all the vertices in graph have been visited
    while(!std::all_of(visited_nodes.begin()+1, visited_nodes.end(), [&](int i) {return i == 1;})){
        // Extract next vertex at shortest distance from visited vertices cluster
        auto w = heap.get_min();
        visited_nodes.at(w.second) = 1;
        shortest_distance.at(w.second) = w.first;

        for(auto& i:vertex_mapping[w.second]){ // Update shortest dist. for all vertices connected to last vertex added to cluster
            if (visited_nodes.at(i.first) == 0){
                auto p = heap.delete_(i.first);
                auto dist = std::min(i.second + shortest_distance.at(w.second), p.first);
                heap.insert(dist, p.second);
            }
        }
    }

    std::vector<int> a = {7,37,59,82,99,115,133,165,188,197};
    std::cout << shortest_distance << std::endl;
    for(auto& i:a) //Answers {2599 2610 2947 2052 2367 2399 2029 2442 2505 3068}
        std::cout << shortest_distance.at(i) << std::endl;
}