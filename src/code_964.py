#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """
        # 计算获取target的x进制数倒排结果
        m_list = []
        while target >= x:
            tmp = target % x
            target = target / x
            m_list.append(tmp)
        m_list.append(target)
        # 遍历计算需要的字符数，同时判断是否需要进位
        is_upgrade = 0
        total = 0
        print x, m_list
        for n in xrange(len(m_list)):
            m = m_list[n] + is_upgrade
            is_upgrade = 0
            flag = self.check_if_upgrade(x, m, n)
            if flag:
                is_upgrade = 1
                m = x - m
            if n == 0:
                tmp = m * 2
            else:
                tmp = m * n
            # if m != 0:
            #     tmp += 1
            print m, n, is_upgrade, tmp
            total += tmp
        if is_upgrade:
            total += n + 1
        return total - 1

    def check_if_upgrade(self, x, m, n):
        """[判断是否需要进位]

        Args:
            x ([int]]): [当前x值]
            m ([int]): [当前阶数对应的系数]
            n ([int]): [当前阶数]

        Returns:
            [bool]: [是否进位]
        """
        if n == 0:
            y = 2 * x + 1 - 4 * m
        else:
            y = (x + 1 - 2 * m) * n + 1
        return y < 0

obj = Solution()
import sys
x = int(sys.argv[1])
target = int(sys.argv[2])
print obj.leastOpsExpressTarget(x, target)
