#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

vector<string> extract_non_special(const string& s) {
    vector<string> res;
    string cur;
    for (char c : s) {
        if (isalnum(c)) {
            cur += c;
        } else {
            if (!cur.empty()) {
                res.push_back(cur);
                cur.clear();
            }
        }
    }
    if (!cur.empty()) res.push_back(cur);
    return res;
}

int main() {
    ifstream file("day8/data.txt");
    if (!file.is_open()) {
        cerr << "Error opening file" << endl;
        return 1;
    }

    string line;
    vector<vector<string> > rows;
    while (getline(file, line)) {
        if (line.empty()) continue;
        vector<string> non_special = extract_non_special(line);
        rows.push_back(non_special);
    }
    map<string, vector<string> > graph;
    string data = rows[0][0];
    int data_length = data.length();
    int no_rows = rows.size();
    vector<string> ends_A;
    vector<string> ends_Z;
    for (int i = 1; i < no_rows; i++) {
        graph[rows[i][0]].push_back(rows[i][1]);
        graph[rows[i][0]].push_back(rows[i][2]);
        if (rows[i][0].back() == 'A') {
            ends_A.push_back(rows[i][0]);
        } else if (rows[i][0].back() == 'Z') {
            ends_Z.push_back(rows[i][0]);
        }
    }
    int curr = 0;
    int no_start = ends_A.size();
    int i = 0;
    int counter = 0;
    while (curr != no_start) {
        char c = data[i];
        curr = 0;
        for (int j = 0; j < no_start; j++) {
            string curr_str = ends_A[j];
            if (c == 'L') {
                ends_A[j] = graph[curr_str][0];
            } else {
                ends_A[j] = graph[curr_str][1];
            }
            if (ends_A[j].back() == 'Z') {
                curr++;
            }
        }
        if (i == data_length-1) {
            i = 0;
        } else {
            i++;
        }
        counter++;
    }
    cout << counter << endl;
    return 0;
}
