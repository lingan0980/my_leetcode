# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 14:51:17 2017

@author: Administrator
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i,v in enumerate(nums):
            if target-v in d:
                return [d[target-v],i+1]
        d[v]=i+1