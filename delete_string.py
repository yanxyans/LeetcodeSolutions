def delete_string(costs: list[int], s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    def get_cost(char):
        return costs[ord(char) - ord('a')]

    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + get_cost(s1[i - 1])
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + get_cost(s2[j - 1])

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(get_cost(s1[i - 1]) + dp[i - 1][j], get_cost(s2[j - 1]) + dp[i][j - 1])
    return dp[m][n]

if __name__ == "__main__":
    # costs = [int(x) for x in input().split()]
    # s1 = input()
    # s2 = input()
    costs = [1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    s1 = "abb"
    s2 = "bba"
    assert delete_string([1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "abb", "bba") == 2
    assert delete_string([4, 2, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], "dzzbdb", "dbdbzz") == 0
    assert delete_string([1, 1, 3, 2, 5, 10, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], "abcdefgh", "hgfedcba") == 30