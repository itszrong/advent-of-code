#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <array>

using namespace std;

static constexpr array<pair<int,int>, 4> DELTA {{
    {-1, 0}, { 1, 0}, { 0,-1}, { 0, 1}
}};
static constexpr array<int, 4> OPP {{ 1, 0, 3, 2 }};

vector<string> extract_grid(ifstream& file) {
    vector<string> grid;
    string line;
    while (getline(file, line)) {
        if (!line.empty() && line.back() == '\r') line.pop_back();
        if (!line.empty()) grid.push_back(line);
    }
    return grid;
}

bool in_bounds(const vector<string>& grid, int r, int c) {
    return 0 <= r && r < (int)grid.size() && 0 <= c && c < (int)grid[0].size();
}

pair<int,int> find_start(const vector<string>& grid) {
    for (int r = 0; r < (int)grid.size(); r++) {
        for (int c = 0; c < (int)grid[0].size(); c++) {
            if (grid[r][c] == 'S') return {r, c};
        }
    }
    return {-1, -1};
}

bool connects(char ch, int dir) {
    switch (ch) {
        case '|': return dir == 0 || dir == 1;
        case '-': return dir == 2 || dir == 3;
        case 'L': return dir == 0 || dir == 3;
        case 'J': return dir == 0 || dir == 2;
        case '7': return dir == 1 || dir == 2;
        case 'F': return dir == 1 || dir == 3;
        default:  return false;
    }
}

char deduce_start_pipe(const vector<string>& grid, int sr, int sc) {
    bool ok[4] = {false,false,false,false};
    for (int d = 0; d < 4; d++) {
        int nr = sr + DELTA[d].first;
        int nc = sc + DELTA[d].second;
        if (!in_bounds(grid, nr, nc)) continue;
        if (connects(grid[nr][nc], OPP[d])) ok[d] = true;
    }
    if (ok[0] && ok[1]) return '|';
    if (ok[2] && ok[3]) return '-';
    if (ok[0] && ok[3]) return 'L';
    if (ok[0] && ok[2]) return 'J';
    if (ok[1] && ok[2]) return '7';
    if (ok[1] && ok[3]) return 'F';
    return '?';
}

int main() {
    ifstream file("day10/data.txt");
    if (!file.is_open()) {
        cerr << "Error opening file\n";
        return 1;
    }

    vector<string> grid = extract_grid(file);
    int R = (int)grid.size(), C = (int)grid[0].size();

    auto [sr, sc] = find_start(grid);
    if (sr == -1) {
        cerr << "No start found\n";
        return 1;
    }

    grid[sr][sc] = deduce_start_pipe(grid, sr, sc);

    vector<vector<int>> dist(R, vector<int>(C, -1));
    queue<pair<int,int>> q;
    dist[sr][sc] = 0;
    q.push({sr, sc});

    while (!q.empty()) {
        auto [r, c] = q.front(); q.pop();
        char cur = grid[r][c];
        for (int d = 0; d < 4; d++) {
            int nr = r + DELTA[d].first;
            int nc = c + DELTA[d].second;
            if (!in_bounds(grid, nr, nc)) continue;
            char nb = grid[nr][nc];
            if (!connects(cur, d) || !connects(nb, OPP[d])) continue;
            if (dist[nr][nc] != -1) continue;
            dist[nr][nc] = dist[r][c] + 1;
            q.push({nr, nc});
        }
    }

    vector<vector<bool>> on_loop(R, vector<bool>(C, false));
    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
            on_loop[r][c] = (dist[r][c] != -1);

    int ER = R * 3, EC = C * 3;
    vector<string> exp(ER, string(EC, '.'));

    auto mark = [&](int rr, int cc) {
        if (0 <= rr && rr < ER && 0 <= cc && cc < EC) exp[rr][cc] = '#';
    };

    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            if (!on_loop[r][c]) continue;
            int cr = r * 3 + 1;
            int cc = c * 3 + 1;
            mark(cr, cc);
            char ch = grid[r][c];
            for (int d = 0; d < 4; d++) {
                if (!connects(ch, d)) continue;
                if (d == 0) mark(cr - 1, cc);
                if (d == 1) mark(cr + 1, cc);
                if (d == 2) mark(cr, cc - 1);
                if (d == 3) mark(cr, cc + 1);
            }
        }
    }

    vector<vector<bool>> seen(ER, vector<bool>(EC, false));
    queue<pair<int,int>> fq;

    auto try_push = [&](int r, int c) {
        if (r < 0 || r >= ER || c < 0 || c >= EC) return;
        if (seen[r][c]) return;
        if (exp[r][c] == '#') return;
        seen[r][c] = true;
        fq.push({r, c});
    };

    for (int c = 0; c < EC; c++) {
        try_push(0, c);
        try_push(ER - 1, c);
    }
    for (int r = 0; r < ER; r++) {
        try_push(r, 0);
        try_push(r, EC - 1);
    }

    while (!fq.empty()) {
        auto [r, c] = fq.front(); fq.pop();
        for (auto [dr, dc] : DELTA) try_push(r + dr, c + dc);
    }

    int part2 = 0;
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            if (on_loop[r][c]) continue;
            int cr = r * 3 + 1;
            int cc = c * 3 + 1;
            if (!seen[cr][cc]) part2++;
        }
    }

    cout << part2 << "\n";
    return 0;
}
