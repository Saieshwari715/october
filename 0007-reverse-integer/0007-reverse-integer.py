class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x != 0:
            r = x % 10
            if rev > (INT_MAX - r) // 10:
                return 0
            rev = rev * 10 + r
            x = x // 10
        return sign * rev



        