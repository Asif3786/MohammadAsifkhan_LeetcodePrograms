class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res= [-1] * len(nums1)
        for i in  range(len(nums1)):
            k=nums2.index(nums1[i])
            for j in range(k,len(nums2)):
                if nums2[j]>nums1[i]:
                    res[i]=nums2[j]
                    break
        return res            
    
     








                    
                