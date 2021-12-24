'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''
import itertools as it
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        pList = []
        pList.append(nums)


        for idx in range(len(list)):

    
sol = Solution()

print(sol.permute([1,2,3])) #[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]