class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,
        }
        last = len(s) - 1
        i = last - 1
        c = roman[s[last]]
        while i >= 0:
            if roman[s[i]] < roman[s[i + 1]]: c -= roman[s[i]]
            else: c += roman[s[i]]
            i -= 1
        return c
