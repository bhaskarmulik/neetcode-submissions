class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #Sort the list
        nums.sort()

        #Result
        res = []

        #Iterate
        for i, a in enumerate(nums):

            #If a >0 => all the nums are greater than 0, so we cant have any triplet
            if a > 0:
                break
            
            #If same number, multiple sample triplets formed which can't be hashed
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1

            while l < r:

                threeSum = nums[l] + nums[r] + a
                if threeSum > 0:

                    r-=1
                elif threeSum < 0:
                    l+=1
                else:

                    res.append([nums[l], nums[r], a])
                    l+=1
                    r-=1

                    while nums[l] == nums[l-1] and l < r:

                        l+=1
            
        return res