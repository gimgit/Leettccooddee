class Solution:
    def climbStairs(self, n: int) -> int:
        z = [0, 1, 2]
        for i in range(n - 2):
            z.append(z[-1] + z[-2])
        return z[n]