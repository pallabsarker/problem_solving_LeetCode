class Solution:
    def reverse(self, x: int) -> int:
        rev, digit = 0, 0
        if x > 0: c = 1
        else: c = -1
        x = abs(x)
        while x != 0:
            digit = x % 10
            x //= 10
            if rev > 2147483647/10 or rev < -2147483648/10: return 0
            rev = (rev * 10) + digit
        return c * rev

# class Solution:
#     def reverse(self, x: int) -> int:
#         rev = 0
#         a = abs(x)
#         while a > 0:
#             digit = a % 10
#             rev = (rev * 10) + digit
#             a //= 10
#         if x < 0: rev = -rev
#         if rev >= -2**31 and rev <= 2**31 - 1: return rev
#         return 0
