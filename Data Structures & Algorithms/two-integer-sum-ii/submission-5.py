class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force
        d = {}
        for i in range(len(numbers)):
            if numbers[i] not in d:
                d[numbers[i]] = i
        print(d)
        for i in range(len(numbers)):
            if target - numbers[i] in d:
                print([i,d[target-numbers[i]]],target-numbers[i])
                return[i+1,d[target-numbers[i]]+1]

        

        