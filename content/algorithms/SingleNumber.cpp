class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for(int i=0; i<nums.size();  i++){
            res ^= nums[i];
        }
        return res;
    }
};

// xor연산을해서 계속 누적.
// 같은게 나온다면 xor연산으로 없어지겠지? 같은건 0으로 나오니까!