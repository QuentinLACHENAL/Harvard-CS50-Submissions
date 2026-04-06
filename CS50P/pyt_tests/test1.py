from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = len(strs[0])
        for word in strs:
            length = len(word)
            if longest > length:
                longest = length
            for i in range(longest):
                if word[i] != strs[0][i]:
                    longest = i
                    if longest <= 0:
                        return ""
        print(longest)
        return strs[0][:longest]

strs=["flower","flow","flight"]
sol = Solution()
print(strs)
print(sol.longestCommonPrefix(strs))
