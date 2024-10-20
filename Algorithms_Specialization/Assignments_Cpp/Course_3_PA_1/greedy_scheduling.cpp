#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <chrono>
#include <vector>
using namespace std;
vector<pair<int, int>> read_input(const std::string file_name);
unsigned long run_sch_algo_1(vector<pair<int, int>> &);
unsigned long run_sch_algo_2(vector<pair<int, int>> &);

int main()
{
    auto entries = read_input("scheduling.txt");
    auto result_algo1 = run_sch_algo_1(entries);
    cout << "result_algo1 = " << result_algo1 << endl;
    auto result_algo2 = run_sch_algo_2(entries);
    cout << "result_algo2 = " << result_algo2 << endl;
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

vector<pair<int, int>> read_input(const std::string file_name)
{
    vector<pair<int, int>> entries;
    ifstream inputFile(file_name);

    int num_jobs, weight, length;
    inputFile >> num_jobs;
    while (inputFile >> weight >> length)
    {
        entries.push_back(make_pair(weight, length));
    }
    return entries;
}

unsigned long run_sch_algo_1(vector<pair<int, int>> &inputs)
{
    vector<pair<int, pair<int, int>>> entries;
    for (auto &elem : inputs)
    {
        auto diff = elem.first - elem.second;
        entries.push_back(make_pair(diff, elem));
    }

    auto comp = [](pair<int, pair<int, int>> a, pair<int, pair<int, int>> b)
    {
        if (a.first == b.first)
        {
            return a.second.first > b.second.first;
        }
        return a.first > b.first;
    };

    sort(entries.begin(), entries.end(), comp);

    unsigned long sum = 0;
    unsigned long completion_time = 0;
    for (auto &entry : entries)
    {
        completion_time += entry.second.second;
        sum += (entry.second.first * completion_time);
    }

    return sum;
}

unsigned long run_sch_algo_2(vector<pair<int, int>> &inputs)
{
    vector<pair<float, pair<int, int>>> entries;
    for (auto &elem : inputs)
    {
        auto ratio = static_cast<float>(elem.first) / static_cast<float>(elem.second);
        entries.push_back(make_pair(ratio, elem));
    }

    auto comp = [](pair<float, pair<int, int>> a, pair<float, pair<int, int>> b)
    {
        return a.first > b.first;
    };

    sort(entries.begin(), entries.end(), comp);

    unsigned long sum = 0;
    unsigned long completion_time = 0;
    for (auto &entry : entries)
    {
        completion_time += entry.second.second;
        sum += (entry.second.first * completion_time);
    }

    return sum;
}