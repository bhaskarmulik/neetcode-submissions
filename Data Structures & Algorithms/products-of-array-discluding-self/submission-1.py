class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #First, let's go for the brute force approach

        # prod_list = []
        # for i in range(len(nums)):
            
        #     prod = 1
        #     for j in range(len(nums)):

        #         if i == j:
        #             continue
        #         else:
        #             prod *= nums[j]
            
        #     prod_list.append(prod)
        
        # return prod_list

        #Now, using teh division operator

        # tot = 1
        # flag = 0
        # for num in nums:

        #     if num != 0:
        #         tot *= num
        #     else:
        #         flag=1
        
        # if flag ==1:

        #     return [0 if num != 0 else tot for num in nums]
        # else:
        #     return [int(tot/num) for num in nums]

        #Now the optimal method using prefix and postfix

        #Constructing a prefix arr
        final_arr = []
        fix = 1
        for i, n in enumerate(nums):

            final_arr.append(fix)
            fix *= n
        # print(final_arr)
        #Multiplying the postfix
        fix = 1
        for i in range(len(nums)-1, -1, -1):

            final_arr[i] *= fix
            fix *= nums[i]
        # print(final_arr)

        return final_arr
            
        