'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''
from collections import defaultdict as dd


class Solution:
    '''
    Runtime: 104 ms, faster than 87.19% of Python3 online submissions for Longest Repeating Character Replacement.

    Memory Usage: 14.4 MB, less than 23.59% of Python3 online submissions for Longest Repeating Character Replacement.

    Time: O(n)
    Space: O(n)
    '''

    def characterReplacement(self, s: str, k: int) -> int:
        scnt = dd(lambda: 0)

        start = 0
        final = 0
        freq = 0
        for end, char in enumerate(s):
            scnt[char] += 1
            freq = max(freq, scnt[char])

            while (end - start + 1) - freq > k:
                scnt[s[start]] -= 1
                start += 1

            final = max(final, end - start + 1)
        return final
