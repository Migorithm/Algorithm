#https://leetcode.com/problems/valid-parentheses/


class Solution(object):
    PAIRS = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    def isValid(self, s):
        opens = []
        for x in s:             #iterate through keys of s.
            if x in self.PAIRS: #If it's (, { or [
                opens.append(x) #insert them into a list
            else:
                                #if it's ),} or ]
                if len(opens) == 0:
                    return 0
                if self.PAIRS[opens.pop()] != x: #paring.
                    return 0
        return len(opens) == 0






a = Solution()
print(a.isValid( "{[]}"))

"""


"""