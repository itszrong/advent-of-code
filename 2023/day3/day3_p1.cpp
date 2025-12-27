#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <utility>
using namespace std;

bool inGrid(int x, int y, int r, int c) {
    if (0 <= x && x < r && 0 <= y && y < c ) return true;
    return false;
};

int main() {

    ifstream file("day3/data.txt");
    if (!file.is_open()) {
        cerr << "Error opening file" << endl;
        return 1;
    }

    vector<vector<char> > grid;
    string line;
    while (getline(file, line)) {
        vector<char> row;
        for (unsigned char c : line) {
            row.push_back(c);
        };
        grid.push_back(row);
    }

    int r = grid.size();
    int res = 0;
    for (int i = 0; i < r; i++ ) {
        vector<char> row = grid[i];
        int c = row.size();
        bool valid = false;
        string curr = "";
        for (int j = 0; j < c; j++) {
            if (isdigit((unsigned char) grid[i][j])) {
                curr += grid[i][j];
            } else {
                if (valid && curr != "") {
                    res += stoi(curr);
                }
                curr = "";
                valid = false;
                continue;
            }
            constexpr array<pair<int, int>, 8> dirs {{
                {1,0}, {-1,0}, {0,1}, {0,-1}, {1, 1}, {1,-1}, {-1, -1}, {-1, 1}
            }};
            for (auto [dr, dc] : dirs) {
                int nx = i+dr;
                int ny = j+dc;
                if (inGrid(nx, ny, r, c)) {
                    if (!isdigit((unsigned char) grid[nx][ny]) && grid[nx][ny] != '.') {
                        valid = true;
                    }
                } else {
                    continue;
                }
                
            }
        }
        if (valid && !curr.empty()) res += stoi(curr);
    }
    cout << res << endl;

    return 0;
}
