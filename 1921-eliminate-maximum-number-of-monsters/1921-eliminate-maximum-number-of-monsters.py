import math
class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        t = []
        for i in range(len(dist)):
            t.append(math.ceil(dist[i]/speed[i]))
        t.sort()

        time = 0
        count = 0
        for i in range(len(t)):
            if (t[i] - time <=0):
                return count
            count+=1
            time +=1
        return count
            
            