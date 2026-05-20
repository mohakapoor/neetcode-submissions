class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1 
        best = 0
        while left<right:
            length = min(heights[left],heights[right])
            width = right - left
            best = max(best,length*width)   
            if heights[left]<=heights[right]:
                    left += 1
            elif heights[right]<=heights[left]:
                    right -= 1
            # length = min(heights[left],heights[right])
            # width = right - left
            # best = max(best,length*width)            
        return best
        