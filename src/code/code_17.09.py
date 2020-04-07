class Solution(object):
    def getKthMagicNumber(self, k):
        """
        :type k: int
        :rtype: int
        """
        def check(n):
            if n % 3 == 0:
                return n/3
            if n % 5 == 0:
                return n/5
            if n % 7 == 0:
                return n/7
            return -1

        index = 1
        i = 1
        while index < k:
            i += 1
            n = i
            while True:
                n = check(n)
                # print n, index, i
                if n in [1, -1]:
                    if n == 1:
                        index += 1
                    break
            # print n, index, i
            # break
        return i

obj = Solution()
print obj.getKthMagicNumber(643)
