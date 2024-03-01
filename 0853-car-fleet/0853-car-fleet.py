class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        cars = sorted(cars, reverse=True)
        
        for position, speed in cars:
            new_car = (target-position)/speed
            stack.append(new_car)
            
            if len(stack) >= 2 and new_car <= stack[-2]:
                stack.pop()

        return len(stack)