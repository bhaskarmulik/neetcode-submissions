class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #Create a hash as a lookup table
        hashing = Counter(nums)
        max_counter = 0

        #Iterate over the array
        for num in nums:

            counter = 1
            while hashing[num +counter] > 0:
                counter +=1
            
            if counter > max_counter:
                max_counter = counter
        
        return max_counter

        
        