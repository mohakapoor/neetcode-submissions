class Solution:
    def trap(self, height: List[int]) -> int:
        def calculate_water(i: int)-> int:
            left = i
            right = i
            max_left = i-1
            max_right = i+1
            while left>0:
                left -= 1
                if height[max_left]<height[left]: max_left = left

            while right<len(height)-1:
                right += 1
                if height[max_right]<height[right]: max_right = right
            print(f"for index {i} max_left :{max_left}, max_right :{max_right} lvl:{min(height[max_left],height[max_right]-height[i])}")
            if height[i]>=height[max_left] or height[i]>= height[max_right]:
                return 0
            return min(height[max_left]-height[i],height[max_right]-height[i])
        area = 0
        for i in range(1,len(height)-1):
            # print(f"water level at index :{i} is :{calculate_water(i)}")
            area += calculate_water(i)
        return area