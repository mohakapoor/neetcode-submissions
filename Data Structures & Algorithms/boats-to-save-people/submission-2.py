class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        left = 0
        count = 0
        right = len(people)-1
        while left<=right:
            while left<right and people[right]+people[left] > limit:
                count += 1
                right -= 1
            count +=1
            right -=1
            left+=1
        return count