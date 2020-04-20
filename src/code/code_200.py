#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/number-of-islands/

深度优先（广度优先遍历）结合

Authors: fanzijian
Date:    2020-04-20 23:33:56

"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0]) if M else 0
        if N == 0:
            return 0
        # 找到所有陆地
        lands = [(i, j) for i in range(M) for j in range(N) if grid[i][j] == '1']
        # print lands, M, N
        lands = set(lands)
        def getIsland(i, j):
            # 遍历获取以（i,j）为种子的所有连通区域
            is_visited = set()
            queue = set()
            queue.add((i, j))
            while queue:
                i,j = queue.pop()
                is_visited.add((i, j))
                if i-1 >= 0 and grid[i-1][j] == '1' and (i-1, j) not in is_visited:
                    queue.add((i-1, j))
                if i+1 < M and grid[i+1][j] == '1' and (i+1, j) not in is_visited:
                    queue.add((i+1, j))
                if j-1 >= 0 and grid[i][j-1] == '1' and (i, j-1) not in is_visited:
                    queue.add((i, j-1))
                if j+1 < N and grid[i][j+1] == '1' and (i, j+1) not in is_visited:
                    queue.add((i, j+1))
            return is_visited
        count = 0
        while lands:
            i,j = lands.pop()
            # print i, j
            island = getIsland(i, j)
            # print island
            count += 1
            lands = lands - island
        return count
