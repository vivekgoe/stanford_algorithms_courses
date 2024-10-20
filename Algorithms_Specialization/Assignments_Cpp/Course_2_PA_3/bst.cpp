#include "bst.h"
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>

vector<int> read_inputs(string file_name)
{
    ifstream inputFile;
    inputFile.open(file_name, ifstream::in);
    if (!inputFile.is_open())
    {
        cerr << "Failed to open input file" << std::endl;
    }

    string line;
    vector<int> inputs;
    while (getline(inputFile, line, '\n'))
    {
        inputs.push_back(stoi(line));
    }

    return inputs;
}

int main()
{
    //vector<int> inputs = {1, 2, 10, 6, 4, 15};
    auto inputs = read_inputs("median.txt");
    Bst<int> bst;
    int median_sum = 0, count = 1;
    for (const auto &i : inputs)
    {
        bst.insert(i, i);
        int median;
        if (count % 2)
        {
            // for odd element median is (k+1)/2 element
            median = bst.select((count + 1) / 2, bst.get_tree_root());
        }
        else
        {
            // for even element median is k/2 element
            median = bst.select(count / 2, bst.get_tree_root());
        }
        count++;
        median_sum += median;
    }
    //bst.delete_node(1, bst.get_tree_root());
    //bst.delete_node(10, bst.get_tree_root());
    //bst.delete_node(6, bst.get_tree_root());
    //cout << bst;
    //cout << "tree height: " << bst.get_tree_height() << endl;
    //cout << "tree size: " << bst.get_tree_elements() << endl;
    cout << "answer: " << median_sum % 10000 << endl;
}