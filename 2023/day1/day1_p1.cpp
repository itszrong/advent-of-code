#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main() {
    std::ifstream file("day1/data.txt");
    if (!file.is_open()) {
        std::cerr << "Error opening file" << std::endl;
        return 1;
    }

    
    std::string line;
    int res = 0;
    while (std::getline(file, line)) {
        std::vector<char> nums;
        int l = line.length();
        for (int i = 0; i <= l; i ++) {
            if (std::isdigit(line[i])) {
                nums.push_back(line[i]);
            }
        }
        res += std::stoi(std::string(1, nums[0])+nums.back());
    }
    std::cout << res << std::endl;
    
    return 0;
}
