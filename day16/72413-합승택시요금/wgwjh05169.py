from collections import deque

def solution(n, s, a, b, fares):
    adj_list = [[] for _ in range(n)]
    shortest = [[float('INF') for j in range(n)] for i in range(n)]
    for u, v, f in fares:
        adj_list[u-1].append((v-1, f))
        adj_list[v-1].append((u-1, f))
        shortest[u-1][v-1] = f
        shortest[v-1][u-1] = f
        
    find_shortest(n, shortest, adj_list)
    
    answer = BFS(n, s-1, a-1, b-1, adj_list, shortest)
    
    return answer


def BFS(n, s, a, b, adj_list, shortest):
    result = float('INF')
    queue = deque()
    queue.append([s, 0, [False] * n])
    while queue:
        v, dist, visited = queue.popleft()
        visited[v] = True
            
        adist = 0 if v == a else shortest[v][a]
        bdist = 0 if v == b else shortest[v][b]
        total = dist + adist + bdist
        if total < result:
            result = total
            
        for w, f in adj_list[v]:
            if not visited[w] and dist + f < result and shortest[v][a] < float('INF') and shortest[v][b] < float('INF'):
                queue.append((w, dist + f, visited[:]))
    
    return result



def find_shortest(n, shortest, adj_list):
    # u -> v -> w
    for v in range(n):
        for u in range(n):
            for w in range(n):
                if shortest[u][v] + shortest[v][w] < shortest[u][w]:
                    shortest[u][w] = shortest[u][v] + shortest[v][w]
