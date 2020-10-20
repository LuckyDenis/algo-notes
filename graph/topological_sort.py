# coding: utf8
"""
Топологическая сортировка

Слодность: O(V + E)
"""


def dfs(g, start, used, ans):
    path = dict().fromkeys(g, -1)
    queue = [start]
    used[start] = True
    buffer = []
    while queue:
        v = queue.pop()
        for u in g[v]:
            if not used[u]:
                used[u] = True
                path[u] = v
                queue.insert(0, u)
        buffer.append(v)
    return buffer + ans


def top_sort(g):
    used = dict().fromkeys(g, False)
    ans = []
    for v in g:
        if not used[v]:
            ans = dfs(g, v, used, ans)
    return ans
