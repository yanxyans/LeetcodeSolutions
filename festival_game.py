def festival_game(target: list[int]) -> int:
    target = [1] + target + [1]
    n = len(target)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for interval_size in range(1, n - 1):
        for start in range(n - interval_size - 1):
            end = start + interval_size + 1
            max_score = 0
            for pick in range(start + 1, end):
                score = target[start] * target[pick] * target[end]
                score += dp[start][pick]
                score += dp[pick][end]
                max_score = max(max_score, score)
            dp[start][end] = max_score
    return dp[0][n - 1]

if __name__ == '__main__':
    assert festival_game([1, 3, 1, 5]) == 40
    assert festival_game([2, 3]) == 9
    assert festival_game([1, 2]) == 4
    assert festival_game([1, 2, 3]) == 12
    assert festival_game([1, 5, 4]) == 30
    assert festival_game([3, 1, 5]) == 35
    print('done')