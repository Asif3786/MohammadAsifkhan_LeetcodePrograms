class Solution:
    def isValid(self, s: str) -> bool:
        flag=True
        while flag:
            flag=False
            if '[]' in s:
                s=s.replace('[]','')
                flag=True
            if '()' in s:
                s=s.replace('()','')
                flag=True
            if '{}' in s:
                s=s.replace('{}','')
                flag=True
        return s==""        
        
        
        