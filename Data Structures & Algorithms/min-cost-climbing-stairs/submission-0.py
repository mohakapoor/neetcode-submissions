class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def minCost(n,memo):
            if n<2:
                return 0
            if n in memo:
                return memo[n]
            
            memo[n] = min(
                minCost(n-1,memo) + cost[n-1],
                minCost(n-2,memo) + cost[n-2]
            )
            return memo[n]

        return minCost(len(cost),{})