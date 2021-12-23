# Given a string s, find the length of the longest substring without repeating characters.

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        highlen = 0
        highstr = ''
        currstr = ''
        for char in s:
            if char in currstr:
                curlen = len(currstr)
                if curlen > highlen:
                    highlen = curlen
                    highstr = currstr
                currstr = currstr[currstr.find(char)+1:] + char
            else:
                currstr += char
        curlen = len(currstr)
        if curlen > highlen:
            highlen = curlen
            highstr = currstr
        return (highlen, highstr)


sol = Solution()
# print(sol.lengthOfLongestSubstring(' '))
print(sol.lengthOfLongestSubstring('aab'))
print(sol.lengthOfLongestSubstring('dvdf'))
print(sol.lengthOfLongestSubstring('abcabcbb'))
print(sol.lengthOfLongestSubstring('pwwkew'))
print(sol.lengthOfLongestSubstring('jbpnbwwd'))
# print(sol.lengthOfLongestSubstring('gauranga'))
# print(sol.lengthOfLongestSubstring('nityananda'))
# print(sol.lengthOfLongestSubstring('gadadhara'))
# print(sol.lengthOfLongestSubstring('krishna'))
