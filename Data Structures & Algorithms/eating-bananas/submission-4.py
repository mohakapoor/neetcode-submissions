class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_taken(piles,k):
            hours = 0
            for i in piles:
                hours += i//k if i%k == 0 else i//k+1
            return hours
        l,r = 1,max(piles)

        while l<=r:
            m = (l+r)//2
            print(l,m,r)
            if hours_taken(piles,m)<=h:
                r = m-1
            else:
                l = m+1

        return l