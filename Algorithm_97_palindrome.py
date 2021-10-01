#https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x:int)->bool:
        """
        :type x: int
        :rtype: bool
        """
        negative = x<0
        if negative:
            return False

        original = x

        #logic
        #log-1 initalize answer
        ans = 0
        while x>0:
            rem = x %10
            ans = (ans*10) + rem
            x = x//10


        return ans == original




a = Solution()
print(a.isPalindrome(123))