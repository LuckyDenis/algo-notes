# coding: utf8


def dfs(gph, v, used, h, d, p=-1):
    used[v] = True
    d[v] = h[v] = 0 if p == -1 else h[p] + 1
    for u in gph[v]:
        if u == p:
            continue
        if used[u]:
            d[v] = min(d[v], h[u])
        else:
            dfs(gph, u, used, h, d, v)
            d[v] = min(d[v], d[u])
            if d[u] > d[v]:
                print(f'bridge: {v} - {u}')


def find_bridges(gph, s):
    used = dict().fromkeys(gph, False)
    h = dict().fromkeys(gph, -1)
    d = dict().fromkeys(gph, -1)
    dfs(gph, s, used, h, d)


"""
5
1 2
2 3
2 4
4 5
"""


g = {
    1: [2],
    2: [3, 4],
    3: [2],
    4: [2, 5],
    5: [4]
}
find_bridges(g, 1)

print('-' * 20)
g = {
    1: [2, 3, 4],
    2: [1],
    3: [1],
    4: [1]
}
find_bridges(g, 1)

