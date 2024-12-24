class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        number = (int(''.join(map(str,num))))
        summed = number + k
        array = list(map(int,str(summed)))
        return array
