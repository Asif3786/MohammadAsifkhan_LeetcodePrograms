class Solution:
    def isHappy(self, n: int) -> bool:
        def validate(n,vis):
            sum=0
            if n==1:
                return True
            if n in vis:
                return False
            vis.add(n)
            for i in str(n):
                sum=sum+int(i)*int(i)
            return validate(sum,vis)
        return validate(n,set())