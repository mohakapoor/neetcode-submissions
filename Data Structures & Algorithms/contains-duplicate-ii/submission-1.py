class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
                if i-k>=0:
                    s.remove(nums[i-k])
                
        return False
