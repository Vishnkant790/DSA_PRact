from collections import Counter
class Solution:
    def findAnagrams(self, s2: str, s1: str) -> list[int]:
        i = 0
        j = 0
        dict = Counter(s1)
        c = len(dict)
        k = len(s1)
        l =[]
        while j < len(s2):
            if s2[j] in dict:
                dict[s2[j]] -=1
                if dict[s2[j]] ==0:
                    c-=1

            if j-i+1 > k:
                if s2[i] in dict:
                    if dict[s2[i]] == 0:
                        c+=1
                    dict[s2[i]] +=1
                i+=1
            if c== 0:
                l.append(i)
                
            j+=1
        return l
            





                
