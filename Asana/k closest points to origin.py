# 973. K Closest Points to Origin

import heapq
class Solution:
    def kClosest(self, points, K):
        distance_heap = []
        heapq.heapify(distance_heap)
        for ele in points:
            heapq.heappush(distance_heap, [abs(ele[0]) + abs(ele[1]), ele])
        res = []
        while K > 0:
            res.append(heapq.heappop(distance_heap)[1])
            K -= 1
        return res


import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance_heap = []

        for ele in points:
            if len(distance_heap) == K:
                heapq.heappush(distance_heap, [-ele[0] ** 2 - ele[1] ** 2, ele])
                heapq.heappop(distance_heap)
            else:
                heapq.heappush(distance_heap, [-ele[0] ** 2 - ele[1] ** 2, ele])
        return [ele[1] for ele in distance_heap]

points = [[1,3],[-2,2]]
K = 1
x = Solution()
print(x.kClosest(points, K))

# 因为K elements returned can be in any order
# 考虑用binary search
