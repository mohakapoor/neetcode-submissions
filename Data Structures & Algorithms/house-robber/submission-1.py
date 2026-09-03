class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def looted(n,memo):
            if n==0:
                return nums[0]
            elif n==1:
                return max(nums[0],nums[1])
            if n in memo:
                return memo[n]

            take = nums[n] + looted(n-2,memo)
            skip = looted(n-1,memo)

            memo[n] = max(take,skip)
            return memo[n]
        return looted(len(nums)-1,{})