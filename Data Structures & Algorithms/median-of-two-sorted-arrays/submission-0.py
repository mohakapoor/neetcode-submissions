class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1,r1 = 0,len(nums1)-1
        l2,r2 = 0,len(nums2)-1
        res = []
        while l1<len(nums1) and l2 <len(nums2):
            if nums1[l1]<nums2[l2]:
                res.append(nums1[l1])
                l1 += 1
            else:
                res.append(nums2[l2])
                l2 +=1
        res.extend(nums1[l1:])
        res.extend(nums2[l2:])
        print(res)
        if len(res)%2 == 1:
            return res[len(res)//2]
        return (res[(len(res))//2] +res[(len(res))//2-1])/2
        