#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
// #include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        unordered_map<char, int> map;
        for (int i = 0; i < s.size(); i++) {
            map[s[i]]++;
            map[t[i]]--;
        }
        for (auto m : map) {
            if (m.second != 0) {
                return false;
            }
        }
        return true;

        
    }
};

int main() {
    Solution sol;
    string s = "anagram", t = "nagaram";
    cout << sol.isAnagram(s, t) << endl;
    return 0;
}

// terminnal command: g++ leetcode217.cpp -o leetcode217 -std=c++11 && ./leetcode217