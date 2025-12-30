#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <array>
#include <algorithm>

using namespace std;
using ll = long long;

static int card_value(char c) {
    // Part 1 order: 2..A
    const string order = "23456789TJQKA";
    return (int)order.find(c); // 0..12
}

static int hand_type(const string& s) {
    // returns 0..6 where 0 is weakest (high card), 6 is strongest (five of a kind)
    array<int, 13> cnt{};
    for (char c : s) cnt[card_value(c)]++;

    vector<int> freq;
    freq.reserve(5);
    for (int x : cnt) if (x) freq.push_back(x);
    sort(freq.begin(), freq.end(), greater<int>());

    if (freq[0] == 5) return 6;                 // five of a kind
    if (freq[0] == 4) return 5;                 // four of a kind
    if (freq[0] == 3 && freq.size() > 1 && freq[1] == 2) return 4; // full house
    if (freq[0] == 3) return 3;                 // three of a kind
    if (freq[0] == 2 && freq.size() > 1 && freq[1] == 2) return 2; // two pair
    if (freq[0] == 2) return 1;                 // one pair
    return 0;                                   // high card
}

struct Hand {
    string cards;
    ll bid;
    int type;
    array<int, 5> ranks; // card values left-to-right for tie-breaking
};

int main() {
    ifstream file("day7/data.txt");
    if (!file.is_open()) {
        cerr << "Error opening file\n";
        return 1;
    }

    vector<Hand> hands;
    string cards;
    ll bid;

    while (file >> cards >> bid) {
        Hand h;
        h.cards = cards;
        h.bid = bid;
        h.type = hand_type(cards);
        for (int i = 0; i < 5; i++) h.ranks[i] = card_value(cards[i]);
        hands.push_back(h);
    }

    sort(hands.begin(), hands.end(), [](const Hand& a, const Hand& b) {
        if (a.type != b.type) return a.type < b.type;           // weaker first
        return a.ranks < b.ranks;                                // lexicographic
    });

    ll res = 0;
    for (int i = 0; i < (int)hands.size(); i++) {
        ll rank = (ll)i + 1; // 1-based
        res += hands[i].bid * rank;
    }

    cout << res << "\n";
    return 0;
}
