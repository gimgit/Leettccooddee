class Solution:
    def romanToInt(self, s: str) -> int:
        a = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        j = 0
        for i in range(len(s) -1):
            print(i)
            if a[s[i]] < a[s[i + 1]]:
                j -= a[s[i]]
            else:
                j += a[s[i]]
        return j + a[s[-1]]