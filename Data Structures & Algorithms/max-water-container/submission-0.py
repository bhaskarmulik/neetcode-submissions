class Solution:

    def area(self, arr : List[int], indices : (int, int)) -> int:

        width = max(indices) - min(indices)
        height = min(arr[indices[0]], arr[indices[1]])

        return width * height

    def maxArea(self, heights: List[int]) -> int:

        start =0
        end = len(heights)-1

        max_area = 0

        while start < end:

            temp = self.area(heights, [start, end])

            if temp > max_area:
                max_area = temp
            
            if heights[start] > heights[end]:
                end -=1
            else:
                start +=1
        
        return max_area