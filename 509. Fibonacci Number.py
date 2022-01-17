class Solution:
    def fib(self, n: int) -> int:
        res = 0

        if n == 1:
            res = 1
        elif n == 0:
            res = 0 
        else:
            res = self.fib(n-1)+self.fib(n-2)
        return res
