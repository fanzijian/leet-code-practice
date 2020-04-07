class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        while True:
            if i >= len(s) or j >= len(t):
                break
            if s[i] == t[j]:
                i += 1
            j += 1
        print i
        return i == len(s)

obj = Solution()
print obj.isSubsequence('leeeeetcode', 'leeetcode')
