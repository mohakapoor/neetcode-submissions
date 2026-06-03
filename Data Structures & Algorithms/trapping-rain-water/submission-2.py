class Solution:
    def trap(self, height: List[int]) -> int:

        
        total_area = 0
        for i in range(1,len(height)-1):
            left = max(height[:i+1])
            right = max(height[i:])
            total_area += min(left,right) - height[i]
        return total_area