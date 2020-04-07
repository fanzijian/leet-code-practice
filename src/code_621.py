class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        num_list = [0 for i in range(26)]
        for task in tasks:
            num_list[ord(task) - ord('A')] += 1
        max_val = max(num_list)
        space = (max_val-1) * (n + 1)
        total = sum(num_list)
        for n in num_list:
            if n >= max_val:
                space += 1
            space -= n
        if space > 0:
            total += space
        return total


obj = Solution()
print obj.leastInterval(
    tasks=["A", "A", "A", "B", "B", "B", "C", "C", "D", "D"], n=2)
