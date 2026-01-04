#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream file("day11/data_ex.txt");
    if (!file.is_open()) {
        cerr << "Error opening file" << endl;
        return 1;
    }

    string line;
    while (getline(file, line)) {
        cout << line << endl;
    }

    return 0;
}
