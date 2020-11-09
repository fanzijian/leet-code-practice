class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        N = len(points)
        if K >= N:
            return points
        h = []
        for i in xrange(0, N, 1):
            if i < K:
                heappush(h, (-points[i][0]**2-points[i][1]**2, points[i]))
            else:
                heappushpop(h, (-points[i][0]**2-points[i][1]**2, points[i]))
        return [item[1] for item in h]
