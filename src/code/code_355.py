#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
问题: https://leetcode-cn.com/problems/design-twitter/

注意点：各种存在性处理，获取最近10条状态部分可以优化（多个有序数组排序的问题）
优化后从O(N*log(N))优化为O(N)

Authors: fanzijian
Date:    2020-04-13 23:50:56

"""
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.index = 0

    def checkUserId(self, userId):
        if userId not in self.users:
            self.users[userId] = {'follow': set(), 'tweet': []}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.checkUserId(userId)
        self.users[userId]['tweet'].append((self.index, tweetId))
        self.index += 1


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.users:
            return []
        followee_ids = list(self.users[userId]['follow'])
        all_news = self.users[userId]['tweet'][:]
        for follower_id in followee_ids:
            all_news.extend(self.users[follower_id]['tweet'][-10:])
        all_news.sort(key=lambda ele: ele[0], reverse=True)
        return [news[1] for news in all_news[:10]]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId == followeeId:
            return
        self.checkUserId(followerId)
        self.checkUserId(followeeId)
        self.users[followerId]['follow'].add(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.checkUserId(followerId)
        self.checkUserId(followeeId)
        if followerId in self.users and followeeId in self.users[followerId]['follow']:
            self.users[followerId]['follow'].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
