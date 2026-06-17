class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k%len(nums)==0:
            return

        nums[:] = nums[::-1] 
        p1 = nums[:k%len(nums)] 
        p1 = p1[::-1]
        p2 =nums[k%len(nums):]
        p2 = p2[::-1]
        nums[:] = p1
        nums.extend(p2)