
strs = 'www.toutiao.com'

def swap_str(strs):
    N = len(strs)
    left = 0
    right = N
    def exchange(left, right, m, n):
        i = left + m
        j = right
        while 0 < m and 0 < n:
            strs[i], strs[j] = strs[j], strs[i]
            m -= 1
            n -= 1
        if m > 0:


        if n > 0:
            pass

    while left >= right:
        m = 0
        n = 0
        while left + m < N and strs[left+m] != '.':
            m += 1
        while right - n > 0 and strs[right-n] != '.':
            n += 1
        exchange(left, right, m, n)

