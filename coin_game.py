def coin_game(coins: list[int], amount: int) -> int:
    n = len(coins)
    dp = [[1] + [0 for _ in range(amount)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            dp[i][j] = dp[i - 1][j]
            if coins[i - 1] <= j:
                dp[i][j] += dp[i][j - coins[i - 1]]
    return dp[n][amount]

if __name__ == '__main__':
    assert coin_game([1, 2, 3], 2) == 2
    print(coin_game([1, 2, 5], 5))
    assert coin_game([1, 2, 5], 5) == 4
    assert coin_game([2], 3) == 0
