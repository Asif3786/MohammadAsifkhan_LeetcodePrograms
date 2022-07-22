class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        i=0
        j=1
        result=0
        diff=arr[j]-arr[i]
        for i in range(len(arr)):
            if j>len(arr)-1:
                    break
            if j<=len(arr)-1 and arr[j]-arr[i]==diff:
                
                result=1
                j=j+1
            else:
                result=0
                break       
        if result==0:
            return False
        else:
            return True
            