class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        if x<0 or (x%10==0 and x!=0):
            return False
        reverse=0
        while x!=0:
            reverse=reverse*10+x%10
            x=x//10
        return num==reverse
            
            