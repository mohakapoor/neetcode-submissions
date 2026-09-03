class Solution:
    def rob(self, nums: List[int]) -> int:
        def looted(start,n,memo):
            if n<start:
                return 0
            if n==start:
                return nums[start]
            elif n==start+1:
                return max(nums[start],nums[start+1])
            if n in memo:
                return memo[n]
            rob = nums[n] + looted(start,n-2,memo)
            leave = looted(start,n-1,memo)
            memo[n] = max(rob,leave)
            return memo[n]

        n = len(nums)
        if n == 1:
            return nums[0]
        return max(
            looted(0,n-2,{}),
            looted(1,n-1,{})
        )