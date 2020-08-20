def edit_distance_r(one, two):
    '''
    递归。
    '''

    len1 = len(one)
    len2 = len(two)
    if len1 == 0:
        return len2
    if len2 == 0:
        return len1
    if one == two:
        return 0

    d = 0 if one[len1 - 1] == two[len2 - 1] else 1
    return min(
        edit_distance_r(one, two[:-1]) + 1,
        edit_distance_r(one[:-1], two) + 1,
        edit_distance_r(one[:-1], two[:-1]) + d
    )

def edit_distance(one, two):
    '''
    动态规划。
    '''

    len1 = len(one)
    len2 = len(two)
    m = [[ i + j for j in range(len2 + 1)] for i in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            d = 0 if one[i - 1] == two[j - 1] else 1
            m[i][j] = min(
                m[i - 1][j] + 1,
                m[i][j - 1] + 1,
                m[i - 1][j - 1] + d
            )
    return m[len1][len2]

r = edit_distance_r('hello', 'helio-world')
r2 = edit_distance('hello', 'helio-world')
print(r)
print(r2)