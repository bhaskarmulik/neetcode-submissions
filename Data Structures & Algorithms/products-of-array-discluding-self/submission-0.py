class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #First, let's go for the brute force approach

        prod_list = []
        for i in range(len(nums)):
            
            prod = 1
            for j in range(len(nums)):

                if i == j:
                    continue
                else:
                    prod *= nums[j]
            
            prod_list.append(prod)
        
        return prod_list