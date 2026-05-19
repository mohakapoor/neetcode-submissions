class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        while left<len(numbers)-1:
            right = left +1
            while right<len(numbers)-1 and not numbers[right] == target - numbers[left]:
                right +=1
            if numbers[right] == target - numbers[left]:
                return [left+1,right+1]
            left += 1
        