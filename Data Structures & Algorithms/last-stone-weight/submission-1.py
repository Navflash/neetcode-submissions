class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)
        #print(maxheap)
        while len(maxheap) > 1:
            a = abs(heapq.heappop(maxheap))
            b = abs(heapq.heappop(maxheap))
            if a == b:
                continue
            elif a > b:
                heapq.heappush(maxheap,-(a-b))
            else:
                heapq.heappush(maxheap,-(b-a))

        return -maxheap[0] if len(maxheap)==1 else 0