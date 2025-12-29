#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
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
    int res = 0;
    while (getline(file, line)) {
        vector<int> nums;
        stringstream ss(line);
        string s;
        bool past = false;
        int exponent = -1;
        while(getline(ss, s, ' ')) {
            trim(s);
            if (s.empty()) continue ;
            if (!past && isdigit((unsigned char) s.back())) {
                nums.push_back(stoi(s));
            }
            if (past) {
                if (find(nums.begin(), nums.end(), stoi(s)) != nums.end()) {
                    cout << s << endl;
                    exponent += 1;
                }
            }
            if (s == "|") past = true;
        }
        if (exponent == -1) continue;
        res += pow(2, exponent);
    }
    cout << res << endl;

    return 0;
}
