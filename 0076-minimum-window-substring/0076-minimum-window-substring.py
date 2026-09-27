from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        j = 0
        dict = Counter(t)
        c = len(dict)
        ans= float("inf")
        start = 0
        while j < len(s):
            
            if s[j] in dict:
                dict[s[j]] -=1
                if dict[s[j]] ==0:
                    c-=1
            if c > 0:
                j+=1
            elif c == 0:
                if j-i+1 < ans:
                    ans = j-i+1
                    start = i
                while c ==0:
                    if s[i] not in dict:
                        i+=1
                        if j-i+1 < ans:
                            ans = j-i+1
                            start = i
                    else:
                        dict[s[i]]+=1
                        if dict[s[i]] >0:
                            i+=1
                            c+=1
                        else:
                            i+=1
                            if j-i+1 < ans:
                                ans = j-i+1
                                start = i
                j+=1
        return s[start:start + ans] if ans != float('inf') else ""
                   
            
                