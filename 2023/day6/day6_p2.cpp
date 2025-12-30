#include <iostream>
#include <fstream>
#include <string>
#include <regex>
using namespace std;

using ll = long long;

vector <ll> extract_numbers(const string& s) {
    string num = "";
    int length = s.length();
    for (int i = 0; i < length; i++) {
        char c = s[i];
        if (isdigit(c)) {
            num += c;
        };
    };
    vector <ll> res;
    res.push_back(stoll(num));
    return res;
}

int main() {
    ifstream file("day6/data.txt");
    if (!file.is_open()) {
        cerr << "Error opening file" << endl;
        return 1;
    }

    string line;
    vector<vector<ll> > data;
    while (getline(file, line)) {
        data.push_back(extract_numbers(line));
    }
    
    vector<ll> times = data[0];
    vector<ll> distances = data[1];
    ll no_races = times.size();
    ll res = 1;
    for (int i = 0; i < no_races; i++) {
        ll time = times[i];
        ll distance = distances[i];
        ll p1 = 0, p2 = time;
        bool p1_found = false;
        bool p2_found = false;
        while (!p1_found) {
            ll v = p1;
            ll remaining_t = time - p1;
            ll final_d = remaining_t*v;
            if (final_d > distance) {
                p1_found = true;
            } else p1++;
        };
        while (!p2_found) {
            ll v = p2;
            ll remaining_t = time - p2;
            ll final_d = remaining_t*v;
            if (final_d > distance) {
                p2_found = true;
            } else p2--;
        };
        res *= (p2-p1+1);
    }
    cout << res << endl;
    return 0;
}
