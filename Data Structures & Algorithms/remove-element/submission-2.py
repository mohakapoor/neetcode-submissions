class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)-1,-1,-1):
            print(i,nums[i])
            if nums[i] == val:
                nums.append(val-1)
                nums.pop(i)
                count +=1
        print(nums)
        return len(nums)-count