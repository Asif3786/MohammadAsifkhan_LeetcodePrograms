class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(0,len(nums)):
            for y in range(0,len(nums)):
                if nums[x]+nums[y]==target and x!=y:
                    return [x,y]
                
                    
                    