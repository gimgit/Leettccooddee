class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts_cnt = [0] * (n+1)
        trusted_cnt = [0] * (n+1)

        for person in trust:
            trusts_cnt[person[0]] += 1
            trusted_cnt[person[1]] += 1

        for i in range(1, n+1):
            if trusted_cnt[i] == n-1 and trusts_cnt[i] == 0:
                return i
                
        return -1