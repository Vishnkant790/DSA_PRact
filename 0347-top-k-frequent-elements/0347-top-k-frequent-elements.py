from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        pq = []
        for i,v in c.items():
            heapq.heappush(pq,(v,i))
            if len(pq) > k:
                heapq.heappop(pq)

        ans = []
        while pq:
            ans.append(heapq.heappop(pq)[1])
        return ans