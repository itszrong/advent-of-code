#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <utility>
#include <set>
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
        for (int j = 0; j < c; j++) {
            constexpr array<pair<int, int>, 8> dirs {{
                {1,0}, {-1,0}, {0,1}, {0,-1}, {1, 1}, {1,-1}, {-1, -1}, {-1, 1}
            }};
           if (grid[i][j] == '*') {
                set<pair<int, int> > visited;
                vector<string> gears;
                for (auto [dx, dy] : dirs) {
                    int nx = i+dx;
                    int ny = j+dy;
                    string gear = "";
                    if (inGrid(nx, ny, r, c)) {
                        if (visited.count(make_pair(nx, ny)) > 0) continue;
                        visited.insert(make_pair(nx, ny));
                        if (isdigit((unsigned char) grid[nx][ny])) {
                            gear += grid[nx][ny];
                            int ny_less = ny-1;
                            int ny_more = ny+1;
                            while (inGrid(nx, ny_less, r, c) && isdigit((unsigned char) grid[nx][ny_less])) {
                                if (visited.count(make_pair(nx, ny_less))) continue;
                                visited.insert(make_pair(nx, ny_less));
                                gear = grid[nx][ny_less] + gear;
                                ny_less--;
                            }
                            while (inGrid(nx, ny_more, r, c) && isdigit((unsigned char) grid[nx][ny_more])) {
                                if (visited.count(make_pair(nx, ny_more))) continue;
                                visited.insert(make_pair(nx, ny_more));
                                gear = gear + grid[nx][ny_more];
                                ny_more++;
                            }
                        }
                    }
                    if (!gear.empty()) {
                        gears.push_back(gear);
                    };
                }
                if (gears.size() == 2) {
                    res += stoi(gears[0]) * stoi(gears[1]);
                    gears.clear();
                }
           }
        }
    };
    cout << res << endl;

    return 0;
};
