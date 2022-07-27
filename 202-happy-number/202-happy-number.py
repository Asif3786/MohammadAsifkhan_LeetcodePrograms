class Solution:
    def isHappy(self, n: int) -> bool:
        def validate(n,vis):
            sm=0
            if n==1:
                return True
            if n in vis:
                return False
            vis.add(n)
            for i in str(n):
                sm+=int(i)*int(i)
            return validate(sm,vis)
        return validate(n,set())