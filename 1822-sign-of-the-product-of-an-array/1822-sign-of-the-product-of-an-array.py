class Solution:
    def arraySign(self, nums: List[int]) -> int:
        return 0 if 0 in nums else prod(list(map(lambda x: -1 if x < 0 else 1, nums)))
            
            
       
        
            
            