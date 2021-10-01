class Solution:
    def reverse(self, x: int) -> int:
        # initiate answer as zero
        # the way we are gonna solve this is by understanding the simple math behind reversing an integer
        # the objective is to be able to code the mathematical logic; which is why the string approach is totally rubbish and invalid and not the right approach to coding

        ans = 0

        # coding for negative integer

        negative = x < 0

        if negative:
            x = x * -1

        # the logic
        while x > 0:
            rem = x % 10 #remaining
            ans = (ans * 10) + rem #pre rem * 10 + cur rem
            x = x // 10

        # edge case
        if ans > (2 ** 31) - 1 or ans < (-2) ** 31:
            return 0

        # negative int
        elif negative:
            return ans * -1

        else:
            return ans

a = Solution()
print(a.reverse(120))