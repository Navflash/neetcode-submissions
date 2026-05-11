class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int>umap;
        for(int num : nums){
            if(umap.find(num)!=umap.end()){
                return true;
            }
            umap[num] += 1;
        }
        return false;
    }
};
