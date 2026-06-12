class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        temp = float("inf")
        for n in nums:

            if n < temp:

                temp = n


        return temp
