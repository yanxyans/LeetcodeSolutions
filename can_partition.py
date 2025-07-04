def can_partition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    total = total // 2
    
    n = len(nums)
    dp = [[True] + [False for _ in range(total)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, total + 1):
            dp[i][j] = dp[i - 1][j]
            if nums[i - 1] <= j:
                dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]
    return dp[n][total]

if __name__ == '__main__':
    print(can_partition([1, 2, 3]))
    assert can_partition([1, 2, 3]) == True
    assert can_partition([1, 2, 3, 4, 5]) == False
    assert can_partition([1, 5, 11, 5]) == True