class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=[str(i) for i in digits]
        s=''.join(s)
        s1=int(s)+1
        out=[int(i) for i in str(s1)]
        return out
       
        
            
        