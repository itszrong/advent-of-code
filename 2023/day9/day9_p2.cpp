#include <iostream>
#include <fstream>
#include <string>
#include <regex>
using namespace std;

using ll = long long;

bool all_zero(const vector<ll>& nums) {
    for (ll num : nums) {
        if (num != 0) return false;
    }
    return true;
}

ll calc_next_num(const vector<ll>& nums) {
    vector<vector<ll> > diffs;
    diffs.push_back(nums);
    vector<ll> curr_diffs = nums;
    while (!all_zero(curr_diffs)) {
        int no_diffs = curr_diffs.size();
        vector<ll> new_diffs;
        for (int i = 0; i < no_diffs-1; i++) {
            new_diffs.push_back(curr_diffs[i+1] - curr_diffs[i]);
        }
        diffs.push_back(new_diffs);
        curr_diffs = new_diffs;
    }
    int no_layers = diffs.size();
    diffs[no_layers-1].insert(diffs[no_layers-1].begin(), 0);
    for (int i = no_layers - 2 ; i >= 0; i--) {
        diffs[i].insert(diffs[i].begin(), diffs[i].front() - diffs[i+1].front());
    }
    return diffs[0].front();
}

vector <ll> extract_numbers(const string& s) {
    static const regex re("-?\\d+");
    vector<ll> nums;
    for (auto it = sregex_iterator(s.begin(), s.end(), re);
         it != sregex_iterator();
         ++it) {
            nums.push_back(stoll(it->str()));
         };
    return nums;
}

int main() {
    ifstream file("day9/data.txt");
    if (!file.is_open()) {
        cerr << "Error opening file" << endl;
        return 1;
    }

    string line;
    ll res = 0;
    while (getline(file, line)) {
        vector<ll> nums = extract_numbers(line);
        ll next_num = calc_next_num(nums);
        res += next_num;
    }
    cout << res << endl;
    return 0;
}
