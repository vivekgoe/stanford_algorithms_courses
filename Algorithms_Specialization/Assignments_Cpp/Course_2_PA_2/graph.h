#include <unordered_map>
#include <vector>
#include <utility>
#include <string>

template <typename T>
class Graph {
   std::unordered_map<T, std::vector<std::pair<T, T>>> vertex_mapping;

   public:
   void create_graph(const std::string file_name);
   void print_graph();
   void Djikstra(const T& source);
   void Djikstra_fast(const T& source);
};