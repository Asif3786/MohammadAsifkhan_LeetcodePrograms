class Solution:
    def romanToInt(self, s: str) -> int:
        nexts = {"M": 1000,"D": 500,"C": 100,"L": 50,"X": 10,"V": 5,"I": 1,"IV": 4,
            "IX": 9,"XL": 40,"XC": 90,"CD": 400,"CM": 900}
        
        
        def solve(i):
            
            if i == len(s):
                return 0
            
            if i == len(s) - 1:
                return nexts[s[i]]
            
            temp = ""
            while i < len(s) and temp + s[i] in nexts:
                temp += s[i]
                i += 1
            
            return nexts[temp] + solve(i)
        
        return solve(0)
        