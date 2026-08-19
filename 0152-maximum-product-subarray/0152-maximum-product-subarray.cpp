class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int minending =nums[0];
        int maxending =nums[0];
        int ans=nums[0];
        for (int i=1;i<nums.size();i++){
            int b1=nums[i];
            int b2=minending*nums[i];
            int b3=maxending*nums[i];
            maxending=max(b1,max(b2,b3));
            minending=min(b1,min(b2,b3));;
            ans=max(ans,max(maxending,minending));
        }
        return ans;
    }
};