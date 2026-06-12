class Solution:

    def binary_search(self, arr : List[int], target : int) -> bool:

        start =0
        end = len(arr)-1

        while start <= end:

            temp = (start + end) //2

            if arr[temp] == target:
                return True
            elif arr[temp] > target:
                end = temp-1
            else:
                start = temp +1
        
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        final_arr = []

        for arr in matrix:

            final_arr.extend(arr)

        return self.binary_search(final_arr, target)

        
        