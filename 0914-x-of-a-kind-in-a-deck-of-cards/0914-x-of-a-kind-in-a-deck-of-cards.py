class Solution(object):
    def hasGroupsSizeX(self, deck):
        count = list(collections.Counter(deck).values())
        n = len(deck)
        for i in range(2, n+1):
            if n % i == 0:
                if all(value % i == 0 for value in count):
                    return True
        return False