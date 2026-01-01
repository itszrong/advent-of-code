#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

using ll = long long;

ll gcd(ll a, ll b) {
    while (b != 0) {
        ll temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

ll lcm(ll a, ll b) {
    return (a / gcd(a, b)) * b;
}

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
    int no_start = ends_A.size();
    int i = 0;
    ll counter = 0;
    vector<ll> ends_A_cycles(ends_A.size(), 0);
    while (find(ends_A_cycles.begin(), ends_A_cycles.end(), 0) != ends_A_cycles.end()) {
        counter++;
        char c = data[i];
        for (int j = 0; j < no_start; j++) {
            string curr_str = ends_A[j];
            if (c == 'L') {
                ends_A[j] = graph[curr_str][0];
            } else {
                ends_A[j] = graph[curr_str][1];
            }
            if (ends_A[j].back() == 'Z' && ends_A_cycles[j] == 0) {
                ends_A_cycles[j] = counter;
            }
        }
        i = (i+1) % data_length;
    }

    ll res = ends_A_cycles[0];
    for (int j = 0; j < no_start; j++) {
        res = lcm(res, ends_A_cycles[j]);
    }
    cout << res << endl;
    return 0;
}
