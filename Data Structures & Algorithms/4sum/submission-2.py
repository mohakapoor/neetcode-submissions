class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        out = []
        # for i in range(len(nums)):
        #     if i>0 and nums[i] == nums[i-1]:
        #         continue
        #     for j in range(i+1,len(nums)-1):
        #         if j>i+1 and nums[j] == nums[j-1]:
        #             continue
        #         left = j+1
        #         right = len(nums)-1
        #         while left<right:
        #             total = nums[i]+nums[j]+nums[left]+nums[right]

        #             if total <target:
        #                 left+=1
        #             elif total>target:
        #                 right-=1
        #             else:
        #                 out.append([nums[i],nums[j],nums[left],nums[right]])
        #                 left+=1
        #                 right-=1
        #                 while left<right and nums[left] == nums[left-1]:
        #                     left +=1
        #                 while left<right and nums[right] == nums[right+1]:
        #                     right -= 1
        s = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for l in range(k+1,len(nums)):
                        if nums[i]+nums[j]+nums[k]+nums[l] == target:
                            s.add((nums[i],nums[j],nums[k],nums[l]))
        out = [list(_) for _ in s]
        return out

        