class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left<right:
            while left<right and numbers[right]> target - numbers[left]:
                right -= 1
            if numbers[right] == target - numbers[left]:
                return [left+1,right+1]
            left += 1
            
        