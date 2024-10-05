class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int x = nums.size();

        vector<int> ans(x * 2);

        for(int i = 0; i< x; i++){
            ans[i] = nums[i];
            ans[i + x ] = nums[i];
        } 
        return ans;
    }
};
