class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        words_map = {}
        max_len = 0
        i = 0
        low = 0
        for word in s:
            i += 1
            if word in words_map and words_map[word] >= low:
                low = words_map[word]
            if i - low > max_len:
                max_len = i - low
            words_map[word] = i
        return max_len

obj = Solution()
print obj.lengthOfLongestSubstring("abcabcbb")
