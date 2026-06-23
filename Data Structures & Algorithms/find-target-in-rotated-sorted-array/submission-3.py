class Solution:

    def normal_binary(self, nums: List[int], ind1: int, ind2: int, t: int) -> int:

        l,r = ind1, ind2

        while l <= r:

            m = (l+r) // 2
            print(f"Middle: {m}")

            if nums[m] == t:
                return m
            elif t <= nums[m]:
                r = m-1
            else:
                l = m+1
        
        return -1


    def search(self, nums: List[int], target: int) -> int:


        l, r = 0, len(nums)-1

        while l <= r:

            m = (l+r) // 2

            if nums[l] < nums[m]:
                l = m
            elif nums[r] > nums[m]:
                r= m
            else:
                break
        
        r1 = self.normal_binary(nums, 0, m, target)
        r2 = self.normal_binary(nums, m+1, len(nums)-1, target)

        return r1 if r2 == -1 else r2
        