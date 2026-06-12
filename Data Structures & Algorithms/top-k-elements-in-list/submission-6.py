class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hm = Counter(nums)  #Store the num-freq
        arr = list()
        bucket_sort = [[] for _ in range(len(nums))]
        #Bucket sort done
        for val, freq in hm.items():
            bucket_sort[freq-1].append(val)

        #Returning the k most freq elements
        for i in range(len(bucket_sort)-1,-1,-1):
            if bucket_sort is not None:
                if len(bucket_sort[i]) <= k - len(arr):
                    arr.extend(bucket_sort[i])
                else:
                    arr.extend(bucket_sort[i][:k - len(arr)])
        return arr