from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = 0
        dict = Counter(s1)
        c = len(dict)
        k = len(s1)
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
                return True
            j+=1
        return False
            





                