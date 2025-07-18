class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * (n)
        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]

if __name__ == '__main__':
    sol = Solution()
    assert sol.numSquares(6) == 3
    assert sol.numSquares(5) == 2
    assert sol.numSquares(13) == 2
