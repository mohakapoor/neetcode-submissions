class Solution:
    def climbStairs(self, n: int) -> int:
        
        def steps_taken(n,memo):
            if n<2:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = steps_taken(n-1,memo) + steps_taken(n-2,memo)
            return memo[n]

        return steps_taken(n,{})