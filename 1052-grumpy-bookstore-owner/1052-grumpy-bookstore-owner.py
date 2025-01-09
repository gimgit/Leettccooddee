class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        feels_good = 0
        can_be_good = 0
        happy_happy_happy = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                feels_good += customers[i]
                customers[i] = 0
            else: 
                can_be_good += customers[i]
            if i>=minutes: 
                can_be_good -= customers[i-minutes]
            happy_happy_happy = max(happy_happy_happy, can_be_good)

        return feels_good+happy_happy_happy