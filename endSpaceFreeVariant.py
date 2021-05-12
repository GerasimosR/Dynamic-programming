def endSpaceFreeVariant(s1, s2, m, n, matchesScore, mismatchesScore, spaceScore):
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                dp[i][j] = 0
            elif j == 0:
                dp[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + matchesScore
            else:
                dp[i][j] = max(dp[i][j - 1] + spaceScore,
                               dp[i - 1][j] + spaceScore,
                               dp[i - 1][j - 1] + mismatchesScore)

    return dp


if __name__ == '__main__':
    str1 = "cacdbd"
    str2 = "ltcabbdb"
    d = endSpaceFreeVariant(str1, str2, len(str1), len(str2), 10, -4, -7)
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in d]))
