class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 1:
            return 0

        dp = [0] * (n + 2)

        dp[0] = 0

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n]


        #n = 1 1 way
        #n=2 2 ways

        #n = 3 3 ways

        #n = 4 5 ways



        