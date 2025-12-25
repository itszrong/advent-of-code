#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

int main() {
    std::ifstream file("day2/data.txt");
    if (!file.is_open()) {
        std::cerr << "Error opening file" << std::endl;
        return 1;
    }

    std::string line;
    int res = 0;
    map<string, int> mapping = {
        {"red", 0},
        {"green", 1},
        {"blue", 2},
    };
    while (std::getline(file, line)) {
        vector<int> bag = {0, 0, 0};
        string temp;
        bool valid = true;
        int l = line.length();
        string curr;
        for (int i = 7; i < l; i++) {
            if (valid == false) {
                break;
            };
            if (line[i] == ';') {
                temp = "";
            }
            if (line[i] == ',' || line[i] == ';') {
                curr = "";
            }
            if (isdigit(line[i])) {
                curr += line[i];
            }; 
            temp += line[i];
            for (const auto &[key, value]: mapping) {
                if (temp.ends_with(key)) {
                    bag[value] = max(stoi(curr), bag[value]);
                    };
                };
            };
            int power = 1;
            int m = bag.size();
            for (int j = 0; j < m; j ++) {
                if (bag[j] != 0) {
                    power *= bag[j];
                };
            };
            res += power;
        };
        cout << res << endl;
        return 0;
    }