from collections import Counter

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) % 2 is not 0:
            return False
        else:
            counter = Counter(moves)
            isUpDownSame = counter['U'] == counter['D']
            isLeftRightSame = counter['R'] == counter['L']
            return isUpDownSame and isLeftRightSame