#include <unordered_map>
#include <vector>
#include <utility>
#include <string>

template <typename T>
class Heap {
   std::vector<std::pair<T, T>> heap;
   std::unordered_map<T, T> vidx_2_hidx;

   public:
   void insert(const T& dist, const T& vidx);
   std::pair<T, T> get_min();
   std::pair<T, T> delete_(const T& vidx);
};

template <typename T>
void Heap<T>::insert(const T& dist, const T& vidx){
    heap.push_back(std::make_pair(dist, vidx));
    vidx_2_hidx[vidx] = heap.size()-1;
    auto c_idx = heap.size()-1;
    auto p_idx = c_idx >> 1;
    while(heap.at(c_idx).first < heap.at(p_idx).first){
      std::swap(vidx_2_hidx[heap.at(c_idx).second], vidx_2_hidx[heap.at(p_idx).second]);
      std::swap(heap.at(c_idx), heap.at(p_idx));
      c_idx = p_idx;
      p_idx = c_idx >> 1;
    }
}

template <typename T>
std::pair<T, T> Heap<T>::get_min(){
    // Swap first element that we want to extract with last element in heap.
    std::swap(vidx_2_hidx[heap.at(0).second], vidx_2_hidx[heap.at(heap.size()-1).second]);
    std::swap(heap.at(0), heap.at(heap.size()-1));
    // Record content of last element before deleting it
    auto ret_val = heap.at(heap.size()-1);
    // Since element is being deleted from heap, we do not need to maintain its index in hash table
    vidx_2_hidx.erase(heap.at(heap.size()-1).second);
    heap.pop_back();
    if(heap.empty()){ // heap had only 1 element, early return possible
        return ret_val;
    }
    auto p_idx = 0;
    auto c1_idx = std::min(p_idx << 1, static_cast<int>(heap.size()-1));
    auto c2_idx = std::min((p_idx << 1) + 1, static_cast<int>(heap.size()-1));
    while(heap.at(p_idx).first > std::min(heap.at(c1_idx).first, heap.at(c2_idx).first)){
        auto smaller = (heap.at(c1_idx).first < heap.at(c2_idx).first)? c1_idx : c2_idx;
        std::swap(vidx_2_hidx[heap.at(smaller).second], vidx_2_hidx[heap.at(p_idx).second]);
        std::swap(heap.at(smaller), heap.at(p_idx));
        p_idx = smaller;
        c1_idx = std::min(p_idx << 1, static_cast<int>(heap.size()-1));
        c2_idx = std::min((p_idx << 1) + 1, static_cast<int>(heap.size()-1));
    }
    return ret_val;
}

template <typename T>
std::pair<T, T> Heap<T>::delete_(const T& vidx){
    // convert vertex index to heap index for this vertex
    auto hidx_2_delete = vidx_2_hidx[vidx];
    // save key and then replace with large negative value so that we can percolate it to min position
    auto key = heap.at(hidx_2_delete).first;
    heap.at(hidx_2_delete).first = INT32_MIN;
    // percolate element to be deleted to min position
    auto c_idx = hidx_2_delete;
    auto p_idx = c_idx >> 1;
    while(heap.at(c_idx).first < heap.at(p_idx).first){
      std::swap(vidx_2_hidx[heap.at(c_idx).second], vidx_2_hidx[heap.at(p_idx).second]);
      std::swap(heap.at(c_idx), heap.at(p_idx));
      c_idx = p_idx;
      p_idx = c_idx >> 1;
    }
    // extract element to be deleted
    auto ret_val = get_min();
    // rewrite with correct key value before returning
    ret_val.first = key;
    return ret_val;
}