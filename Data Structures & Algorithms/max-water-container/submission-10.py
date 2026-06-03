class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        left = 0
        right = len(heights)-1
        while left<right:
            area = min(heights[left],heights[right])*(right-left)
            best = max(best,area)
            if heights[left]>heights[right]:
                right -= 1
            else:
                left += 1
        return best

        