class Solution(object):
    def maximumOddBinaryNumber(self, s):
        one_cnt = s.count("1")
        zero_cnt = len(s) - one_cnt

        return "1" * (one_cnt - 1) + "0" * zero_cnt + "1"