def editDistanceBU(s1, s2, m, n):
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            # Base Conditions
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Match
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Delete
                                   dp[i - 1][j - 1])  # Replace

    return dp


if __name__ == '__main__':
    str1 = "cacdbd"
    str2 = "ltcabbdb"
    d = editDistanceBU(str1, str2, len(str1), len(str2))
    print(d[len(str1)][len(str2)])
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in d]))
