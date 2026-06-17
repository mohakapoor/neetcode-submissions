class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        out = []
        left = 0
        count = 0
        right = len(people)-1
        print(people)

        while left<=right:
            while left<right and people[right]+people[left] > limit:
                count += 1
                right -= 1
                print(count,"while loop stop",left,right)
            print(left,right)
            count +=1
            right -=1
            left+=1
        return count