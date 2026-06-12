class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //Optimal method
        //Cretae a map to store previous elements and their indices
        //Takes care of the duplicate problem

        unordered_map<int, int> hashmap;
        int n = nums.size();
        int diff=0;

        for(int i=0; i<n; i++){
            diff = target - nums[i];

            if(hashmap.find(diff) != hashmap.end()){

                return {hashmap[diff], i};
            }

            hashmap.insert({nums[i], i});

        }

        return {};
        

        
    }
};
