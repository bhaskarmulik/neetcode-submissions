class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start =0
        end = len(nums)-1

        while start <= end:

            temp = (start + end) // 2

            if nums[temp] == target:
                print(temp)

                return temp
            elif target > nums[temp]:

                start = temp +1
            else:
                end = temp-1
        
        return -1
        