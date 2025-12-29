#include <iostream>
#include <fstream>
#include <string>
#include <regex>
using namespace std;

vector <long long> extract_numbers(const string& s) {
    static const regex re(R"(\d+)");
    vector<long long> nums;
    for (auto it = sregex_iterator(s.begin(), s.end(), re);
         it != sregex_iterator();
         ++it) {
            nums.push_back(stoll(it->str()));
        };
    return nums;
}

int main() {
    ifstream file("day5/data.txt");
    if (!file.is_open()) {
        cerr << "Error opening file" << endl;
        return 1;
    }

    string line;
    vector<vector<vector<long long> > > all_mappings;
    vector<vector<long long> > mappings;
    while (getline(file, line)) {
        if (line.empty()) continue;
        if (line.ends_with(':') && !mappings.empty()) {
            all_mappings.push_back(mappings);
            mappings.clear();
            continue;
        }
        vector<long long> nums = extract_numbers(line);
        mappings.push_back(nums);
    }
    all_mappings.push_back(mappings);

    vector<long long> final_locations;
    int no_seeds = all_mappings[0][0].size();
    int no_mappings = all_mappings.size()-1;
    for (int i = 0; i < no_seeds; i++ ) {
        long long curr = all_mappings[0][0][i];
        for (int j = 1; j <= no_mappings; j++) {
            int no_ranges = all_mappings[j].size();
            for (int k = 0; k < no_ranges; k++) {
                vector<long long> curr_range = all_mappings[j][k];
                int diff = curr - curr_range[1];
                if (diff >= 0 && diff < curr_range[2]) {
                    curr = curr_range[0]+diff;
                    break;
                };
            }
        }
        final_locations.push_back(curr);
    }

    // for (auto num : final_locations) {
    //     cout << num << endl;
    // };
    long long res = *min_element(final_locations.begin(), final_locations.end());
    cout << res << endl;

    return 0;
}
