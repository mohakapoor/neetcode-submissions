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
            print(f"Area: {min(heights[left],heights[right])*(right-left)} left = {heights[left]} and right = {heights[right]} and breadth = {right-left}")
            length = min(heights[left],heights[right])
            width = right - left
            best = max(best,length*width)            
            # left += 1
        return best
        