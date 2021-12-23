# Given a string s, return the longest palindromic substring in s.


class Solution:

    # This was 9 times faster than the first solution
    # O(n)
    def longestPalindrome(self, s: str) -> str:
        pali = s[::-1]
        if pali == s:
            return s
        strlen = len(s)
        highlen = 1
        highstr = s[0]
        curstr = ''
        charmap = {}
        for cidx in range(strlen):
            char = s[cidx]
            chars = charmap.get(char)
            if chars == None:
                charmap[char] = [cidx]
            else:
                chars.append(cidx)
                if len(chars) > 0:
                    for idx in chars:
                        if idx <= cidx:
                            temp = s[idx:cidx+1]
                            pali = temp[::-1]
                            isPali = temp == pali
                            if isPali:
                                templen = len(temp)
                                if templen > highlen:
                                    highlen = templen
                                    highstr = temp
        return (highlen, highstr)

    # This works but it's quite slow.
    # Runs in O(n^2)
    # def longestPalindrome(self, s: str) -> str:
    #     highlen = 0
    #     highstr = ''
    #     strlen = len(s)
    #     for cidx in range(0, strlen):
    #         idxarr = [i for i, c in enumerate(s) if i >= cidx and c == s[cidx]]
    #         for idx in idxarr:
    #             temp = s[cidx:idx+1]
    #             pali = temp[::-1]
    #             isPali = temp == pali
    #             if isPali:
    #                 templen = len(temp)
    #                 if templen > highlen:
    #                     highlen = templen
    #                     highstr = temp
    #     return (highlen, highstr)


sol = Solution()

# print(sol.longestPalindrome('babad'))
# print(sol.longestPalindrome('cbbd'))
# print(sol.longestPalindrome('f'))
print(sol.longestPalindrome('ac'))
# print(sol.longestPalindrome("abcba"))
# print(sol.longestPalindrome("aacabdkacaa"))
# print(sol.longestPalindrome("xaabacxcabaaxcabaax"))  # "xaabacxcabaax"
