#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main() {
    ifstream file("day1/data.txt");
    if (!file.is_open()) {
        cerr << "Error opening file" << endl;
        return 1;
    }

    
    string line;
    map<string, char> map = {
        {"one", '1'},
        {"two", '2'},
        {"three", '3'},
        {"four", '4'},
        {"five", '5'},
        {"six", '6'},
        {"seven", '7'},
        {"eight", '8'},
        {"nine", '9'}
    };

    int res = 0;
    while (getline(file, line)) {
        vector<char> nums;
        int l = line.length();
        string curr;
        for (int i = 0; i < l; i ++) {
            curr += line[i];

            if (isdigit(line[i])) {
                nums.push_back(line[i]);
            }

            for (const auto &[key, value] : map) {
                if (curr.ends_with(key)) {
                    nums.push_back(value);
                }
            }
        }

        if (!nums.empty()) {
            string val;
            val.push_back(nums.front());
            val.push_back(nums.back());
            res += stoi(val);
        }
    }
    cout << res << endl;
    
    return 0;
}
