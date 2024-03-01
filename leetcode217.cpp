#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
// #include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    bool containsDuplicate(vector<int>& nums) { 
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            if (map.find(nums[i]) != map.end()) {
                return true;
            }
            map[nums[i]] = 1;
        }
        return false;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1,1,1,3,3,4,3,2,4,2};
    cout << sol.containsDuplicate(nums) << endl;
    return 0;
}

// terminnal command: g++ leetcode217.cpp -o leetcode217 -std=c++11 && ./leetcode217