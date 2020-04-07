#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        rst = []
        new_coins = set(coins)
        for coin in coins:
            base = 0
            p = amount
            new_coins.remove(coin)
            # 有base 个coin面值
            while p > 0:
                p -= coin
                base += 1
                cnt = self.coinChange(list(new_coins), p)
                # -1表示无法组成target
                if cnt == -1:
                    continue
                rst.append(base + cnt)
        if rst:
            return min(rst)
        return -1
coins = [1,2,5]
amount = 11
obj = Solution()
print obj.coinChange(coins, amount)
