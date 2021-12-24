'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
'''
import itertools as it
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # slist = list(s1)
        # slen = len(slist)

        # for end in range(len(s2)):
        #     if s2[end] in slist:
        print(list(it.permutations(s1)))

sol = Solution()

print(sol.checkInclusion('ab', 'eidbaooo'))