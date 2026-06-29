class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #heap = [float('inf')]*k
        heap = []
        res = []

        for p in points:
            #print(p)
            dist = math.sqrt(p[0]*p[0]+p[1]*p[1])
            heap.append((dist,p))

        heapq.heapify(heap)

        while k != 0:
            out = heapq.heappop(heap)
            res.append(out[1])
            k-=1

        return res
