class Solution(object):
    def fib(self,n):
        if n<=1:
            return n
        first=0
        second=1
        for i in range(2,n+1):
            current=first+second
            first=second
            second=current
        return second
