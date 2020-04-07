import sys

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]
        dp.extend([sys.maxint for i in range(n)])
        for i in xrange(0, n+1, 1):
            for j in xrange(1, n+1, 1):
                if i+j*j <= n:
                    dp[i+j*j] = min(dp[i] + 1, dp[i+j*j])
        return dp[n]

obj = Solution()

print obj.numSquares(1)
