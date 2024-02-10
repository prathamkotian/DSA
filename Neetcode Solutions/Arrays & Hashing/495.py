# Teemo Attacking

class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        total=0
        for i in range(len(timeSeries)):
            if i<len(timeSeries)-1:
                if timeSeries[i]+duration-1<timeSeries[i+1]:
                    total+=duration
                else:
                    total+=timeSeries[i+1]-timeSeries[i]
            else:
                total+=duration
        return total