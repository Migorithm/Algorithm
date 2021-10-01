#https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=""
        for i in zip(*strs):
            if len(set(i)) ==1:
                ans += i[0]
            else:
                break
        return ans



a = Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))
