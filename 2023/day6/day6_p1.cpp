#include <iostream>
#include <fstream>
#include <string>
#include <regex>
using namespace std;

vector <int> extract_numbers(const string& s) {
    static const regex re(R"(\d+)");
    vector<int> nums;
    for (auto it = sregex_iterator(s.begin(), s.end(), re);
         it != sregex_iterator();
         ++it) {
            nums.push_back(stoi(it->str()));
         };
    return nums;
}

int main() {
    ifstream file("day6/data.txt");
    if (!file.is_open()) {
        cerr << "Error opening file" << endl;
        return 1;
    }

    string line;
    vector<vector<int> > data;
    while (getline(file, line)) {
        data.push_back(extract_numbers(line));
    }
    vector<int> times = data[0];
    vector<int> distances = data[1];
    int no_races = times.size();
    int res = 1;
    for (int i = 0; i < no_races; i++) {
        int time = times[i];
        int distance = distances[i];
        int p1 = 0, p2 = time;
        bool p1_found = false;
        bool p2_found = false;
        while (!p1_found) {
            int v = p1;
            int remaining_t = time - p1;
            int final_d = remaining_t*v;
            if (final_d > distance) {
                p1_found = true;
            } else p1++;
        };
        while (!p2_found) {
            int v = p2;
            int remaining_t = time - p2;
            int final_d = remaining_t*v;
            if (final_d > distance) {
                p2_found = true;
            } else p2--;
        };
        res *= (p2-p1+1);
    }
    cout << res << endl;
    return 0;
}
