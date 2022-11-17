class Solution:
    def climbStairs(self, n: int) -> int:
        fibo = [1,1]
        for i in range(n-1):
            fibo.append(fibo[-1]+fibo[-2])
        return fibo[-1]