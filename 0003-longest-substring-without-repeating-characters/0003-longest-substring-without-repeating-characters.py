class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        ans = 0
        dict = {}
        while j < len(s):
            dict[s[j]] = dict.get(s[j],0)+1
            while len(dict) < j-i+1:
                    
                dict[s[i]] -=1
                if dict[s[i]] == 0:
                    del dict[s[i]]
                i+=1
            if len(dict) == j-i+1:
                ans = max(ans,j-i+1)
            j+=1
                
        return ans
                   