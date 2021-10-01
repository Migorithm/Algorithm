#https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        dic1= {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        dic2={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in dic1.keys():
            if s.__contains__(i):
                ans += dic1[i]
                s = s.replace(i,"")

        for j in s:
            ans += dic2[j]
        return ans


a = Solution()
print(a.romanToInt("MCMXCIV"))

