class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(n,l,r):
            while l<r:
                n[l],n[r] = n[r],n[l]
                l += 1
                r -= 1

        val = k%len(nums)
        if val==0:
            return

        nums[:] = nums[::-1] 
        reverse(nums,0,val-1)
        reverse(nums,val,len(nums)-1)