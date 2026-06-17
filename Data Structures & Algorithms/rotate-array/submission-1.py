class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k%len(nums)==0:
            return

        nums[:] = nums[::-1] 
        p1 = nums[:k%len(nums)] 
        print("p1 before",p1)
        p1 = p1[::-1]
        print("p1 after",p1)
        p2 =nums[k%len(nums):]
        print("p2 before",p2)
        p2 = p2[::-1]
        print("p2 after",p2)
        nums[:] = p1
        print(nums)
        nums.extend(p2)
        print(nums)
        