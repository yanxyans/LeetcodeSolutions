class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = [1] + [0] * n
        if 1 <= int(s[0]) <= 9:
            dp[1] = 1
        for i in range(2, n + 1):
            single_decode = int(s[i - 1])
            double_decode = int(s[i - 2:i])
            if 1 <= single_decode <= 9:
                dp[i] += dp[i - 1]
            if 10 <= double_decode <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("226"))
    assert s.numDecodings("226") == 3
    print(s.numDecodings("12"))
    assert s.numDecodings("12") == 2
    print(s.numDecodings("06"))
    assert s.numDecodings("06") == 0