# 暴力尝试 m, n大的情况内存超限
def road(m, n):
    if m == 1 or n == 1:
        return 1

    _pre = [[1, 1]]
    _next = []

    for i in range(2, m + n):
        for pair in _pre:
            if pair[0] + 1 <= m:
                _next.append([pair[0] + 1, pair[1]])
            if pair[1] + 1 <= n:
                _next.append([pair[0], pair[1] + 1])
        _pre, _next = _next, []
    return len(_pre)

# 根据递推关系 (m, n) = (m - 1, n) + (m, n - 1)
def road_recur(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return road_recur(m - 1, n) + road_recur(m, n - 1)

# 暂时能想到的最优解
def road_non_recur(m, n):
    m, n = min(m, n), max(m, n)
    arr = [1 for i in range(n - 1)]
    for i in range(m - 1):
        for j in range(i, n - 1):
            if i == j:
                arr[j] = 2 * arr[j]
            else:
                arr[j] = arr[j] + arr[j - 1]
    return arr[j]


m, n = 30, 50
ret = road_recur(m, n)
r = road_non_recur(m, n)
print(ret)
print(r)

