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
    int j = 1;
    int res = 0;
    int bag[3] = {12, 13, 14};
    map<string, int> mapping = {
        {"red", 0},
        {"green", 1},
        {"blue", 2},
    };
    while (std::getline(file, line)) {
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
                    if (stoi(curr) > bag[value]) {
                        valid = false;
                        break;
                    }
                }
            };
        };
        if (valid) {
            res += j;
        }
        j++;
    }
    cout << res << endl;
    return 0;
}
