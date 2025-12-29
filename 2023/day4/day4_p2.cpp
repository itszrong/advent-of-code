#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <numeric>
#include <boost/algorithm/string.hpp>
using namespace boost::algorithm;
using namespace std;

int main() {
    ifstream file("day4/data.txt");
    if (!file.is_open()) {
        cerr << "Error opening file" << endl;
        return 1;
    }

    string line;
    vector<int> res;
    while (getline(file, line)) {
        res.push_back(1);
    }
    file.clear();
    file.seekg(0, ios::beg);
    int i = 0;
    while (getline(file, line)) {
        vector<int> nums;
        stringstream ss(line);
        string s;
        bool past = false;
        int wins = 0;
        while(getline(ss, s, ' ')) {
            trim(s);
            if (s.empty()) continue ;
            if (!past && isdigit((unsigned char) s.back())) {
                nums.push_back(stoi(s));
            }
            if (past) {
                if (find(nums.begin(), nums.end(), stoi(s)) != nums.end()) {
                    wins += 1;
                }
            }
            if (s == "|") past = true;
        }
        for (int j = i+1; j-i <= wins; j++) {
            res[j] += res[i];
        }
        i++;
    }
    for (auto i : res) {
        cout << i << " ";
    }
    cout << endl;

    int sum = accumulate(res.begin(), res.end(), 0);
    cout << sum << endl;

    return 0;
}
