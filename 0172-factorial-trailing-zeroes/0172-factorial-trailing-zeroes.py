class Solution(object):
    def trailingZeroes(self, n):
        trailing = 0
        while(n >= 5):
            n //= 5
            trailing += n
        return trailing
