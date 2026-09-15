class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            dict[i] = dict.get(i,0)+1
        pq = []
        for i,v in dict.items():
            heapq.heappush(pq,(v,i))
            if len(pq) > k:
                heapq.heappop(pq)

        ans = []
        while pq:
            ans.append(heapq.heappop(pq)[1])
        return ans