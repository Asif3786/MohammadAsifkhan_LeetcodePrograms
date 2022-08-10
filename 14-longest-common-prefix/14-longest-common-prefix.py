class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        for i in strs:
            print("before while loop",i)
            while len(word)!=0 and not i.startswith(word):
                word = word[:-1]
        return word

                
            