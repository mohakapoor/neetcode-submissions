import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        h = []
        for i in nums:
            if d.get(i,"n") == "n":
                d[i] = 0
            d[i] += 1
        for i,j in d.items():
            heapq.heappush(h,(j,i))
            if len(h)>k:
                heapq.heappop(h)
        return [num for freq,num in h]
        