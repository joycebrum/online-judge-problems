import sys
from heapq import *

def edmonds_karp(C, source, sink):
    n = len(C) # C is the capacity matrix
    F = [[0] * n for _ in range(n)]
    # residual capacity from u to v is C[u][v] - F[u][v]

    while True:
        path = bfs(C, F, source, sink)
        if not path:
            break
        # traverse path to find smallest capacity
        u,v = path[0], path[1]
        flow = C[u][v] - F[u][v]
        for i in range(len(path) - 2):
            u,v = path[i+1], path[i+2]
            flow = min(flow, C[u][v] - F[u][v])
        # traverse path to update flow
        for i in range(len(path) - 1):
            u,v = path[i], path[i+1]
            F[u][v] += flow
            F[v][u] -= flow
    return sum([F[source][i] for i in range(n)])

def bfs(C, F, source, sink):
    P = [-1] * len(C) # parent in search tree
    P[source] = source
    queue = [source]
    while queue:
        u = queue.pop(0)
        for v in range(len(C)):
            if C[u][v] - F[u][v] > 0 and P[v] == -1:
                P[v] = u
                queue.append(v)
                if v == sink:
                    path = []
                    while True:
                        path.insert(0, v)
                        if v == source:
                            break
                        v = P[v]
                    return path
    return None


if __name__ == '__main__':
    test = 0
    while True:
        test += 1
        n = int(sys.stdin.readline())
        if n == 0: break
        s, t, c = [int(x) for x in sys.stdin.readline().split()]
        s, t = s -1, t-1

        C = []
        for x in range(0, n):
            C.append([0] * n)
        
        for i in range(0, c):
            x, y, b = [int(x) for x in sys.stdin.readline().split()]
            C[x-1][y-1] += b
            C[y-1][x-1] += b
        print('Network', test)
        print('The bandwidth is %s.' % edmonds_karp(C, s, t))
        print('')
        
