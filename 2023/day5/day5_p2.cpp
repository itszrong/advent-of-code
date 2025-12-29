#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <vector>
#include <algorithm>

using namespace std;

using ll = long long;

vector<ll> extract_numbers(const string& s) {
    static const regex re(R"(\d+)");
    vector<ll> nums;
    for (auto it = sregex_iterator(s.begin(), s.end(), re);
         it != sregex_iterator();
         ++it) {
        nums.push_back(stoll(it->str()));
    }
    return nums;
}

struct Rule {
    ll dst, src, len;
};

static vector<pair<ll,ll>> merge_ranges(vector<pair<ll,ll>> ranges) {
    if (ranges.empty()) return ranges;
    sort(ranges.begin(), ranges.end());
    vector<pair<ll,ll>> out;
    out.push_back(ranges[0]);
    for (size_t i = 1; i < ranges.size(); i++) {
        auto [s,e] = ranges[i];
        auto &back = out.back();
        if (s <= back.second) {
            back.second = max(back.second, e);
        } else {
            out.push_back({s,e});
        }
    }
    return out;
}

static vector<pair<ll,ll>> apply_section(const vector<pair<ll,ll>>& ranges, vector<Rule> rules) {
    sort(rules.begin(), rules.end(), [](const Rule& a, const Rule& b){
        return a.src < b.src;
    });

    vector<pair<ll,ll>> out;
    out.reserve(ranges.size() * 2);

    for (auto [a,b] : ranges) {
        ll cur = a;

        for (const auto& r : rules) {
            ll rs = r.src;
            ll re = r.src + r.len;

            if (re <= cur) continue;
            if (rs >= b) break;

            if (cur < rs) {
                ll gap_end = min(b, rs);
                out.push_back({cur, gap_end});
                cur = gap_end;
                if (cur >= b) break;
            }

            ll ov_start = max(cur, rs);
            ll ov_end   = min(b, re);
            if (ov_start < ov_end) {
                ll delta = r.dst - r.src;
                out.push_back({ov_start + delta, ov_end + delta});
                cur = ov_end;
                if (cur >= b) break;
            }
        }

        if (cur < b) out.push_back({cur, b});
    }

    return merge_ranges(std::move(out));
}

int main() {
    ifstream file("day5/data.txt");
    if (!file.is_open()) {
        cerr << "Error opening file\n";
        return 1;
    }

    string line;

    if (!getline(file, line)) {
        cerr << "Empty file\n";
        return 1;
    }
    vector<ll> seed_nums = extract_numbers(line);
    vector<pair<ll,ll>> ranges;
    for (size_t i = 0; i + 1 < seed_nums.size(); i += 2) {
        ll start = seed_nums[i];
        ll len   = seed_nums[i+1];
        ranges.push_back({start, start + len});
    }
    ranges = merge_ranges(ranges);

    vector<vector<Rule>> sections;
    vector<Rule> current;

    while (getline(file, line)) {
        if (line.empty()) continue;

        if (!line.empty() && line.back() == ':') {
            if (!current.empty()) {
                sections.push_back(current);
                current.clear();
            }
            continue;
        }

        vector<ll> nums = extract_numbers(line);
        if (nums.size() == 3) {
            current.push_back(Rule{nums[0], nums[1], nums[2]});
        }
    }
    if (!current.empty()) sections.push_back(current);

    for (auto& sec : sections) {
        ranges = apply_section(ranges, sec);
    }

    ll ans = ranges.empty() ? 0 : ranges[0].first;
    for (auto [s,e] : ranges) ans = min(ans, s);

    cout << ans << "\n";
    return 0;
}
