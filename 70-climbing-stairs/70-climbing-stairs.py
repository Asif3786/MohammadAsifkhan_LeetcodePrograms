class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        step=0
        prev=2
        prevprev=1
        for i in range(3,n+1):
            step=prev+prevprev
            prevprev=prev
            prev=step
        return step
        
            
        