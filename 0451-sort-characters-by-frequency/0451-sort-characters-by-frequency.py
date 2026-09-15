from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        pq = []
        for i, v in c.items():
            i = i*v
            heapq.heappush(pq,(v,i))
        ans = []
        while pq:
            ans.append(heapq.heappop(pq)[1])
        ans.reverse()
        return "".join(ans)
            
        