class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(houses)
        heaters = sorted(heaters)
        radius = 0
        idx = 0

        if houses == heaters:
            return 0

        for house in houses:
            while idx < len(heaters) -1 and  abs(heaters[idx] - house) > abs(heaters[idx + 1] - house):
                idx += 1
            radius = max(radius, abs(heaters[idx] - house))
        
        return radius

    