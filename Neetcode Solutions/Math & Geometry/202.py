# Happy Numbers

class Solution:
    def isHappy(self, n: int) -> bool:

        seen=set()
        while True:
            sum=0

            while n!=0:
                res=n%10
                sum=sum+res*res
                n=n//10

            if sum==1:
                return True
            elif sum in seen:
                return False

            seen.add(sum)
            n=sum

        