class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        different_char_count = 0
        for i in range(len(s1)) : 
            if s1[i] != s2[i] :
                different_char_count += 1
        return True if different_char_count <= 2 and sorted(s1) == sorted(s2) else False
                
        
            
        
        
            
                
            
        