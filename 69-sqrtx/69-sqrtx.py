class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=x
        ans=0
        while low<=high:
            mid=(low+high)//2
            if mid*mid==x:
                ans=mid
                break
            elif mid*mid>=x:
                high=mid-1
            else:
                low=mid+1
                ans=mid
        return ans
           
        