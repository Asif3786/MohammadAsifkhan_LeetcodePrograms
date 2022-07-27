class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n,vis):
            sm=0
            if n==1:
                return True
            if n in vis:
                return False
            vis.add(n)
            for i in str(n):
                sm+=int(i)*int(i)
            return helper(sm,vis)
        return helper(n,set())