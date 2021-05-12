def editDistanceTD(s1, s2, m, n):
    # Base Conditions
    if m == 0:
        return n

    if n == 0:
        return m

    if s1[m - 1] == s2[n - 1]:
        return editDistanceTD(s1, s2, m - 1, n - 1)  # Match

    return 1 + min(editDistanceTD(s1, s2, m, n - 1),  # Insert
                   editDistanceTD(s1, s2, m - 1, n),  # Delete
                   editDistanceTD(s1, s2, m - 1, n - 1)  # Replace
                   )


if __name__ == '__main__':
    str1 = "cacdbd"
    str2 = "ltcabbdb"
    d = editDistanceTD(str1, str2, len(str1), len(str2))
    print(d)
