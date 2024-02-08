import heapq
def solution(n, s, a, b, fares):
    #방향없음
    
    graph = [[] for _ in range(n+1)]
    for u,v,c in fares:
        graph[u].append((v,c))
        graph[v].append((u,c))
    
    #각각 따로 갈 때
    dist = dj(s,graph,n)
    a_d = dist[a]
    b_d = dist[b]
    #같이 갈 때
    min_dist = [float('inf')] * (n+1)
    for v in range(1,n+1):
        min_dist[v] = get_dist(v,a,b,graph,n) + dist[v]
    index = min_dist.index(min(min_dist))
    p = min(min_dist)
    print(index,p)
    if a_d < b_d:
        p,d = a,b
    else:
        p,d = b,a
    a_to_b = dj(p,graph,n)[d]
    return min_dist[index]
    # print(a_d,b_d,a_to_b)
    # print(min(a_d+b_d,a_d + a_to_b))
    #다익스트라
    # return answer

def dj(v,graph,n):
    heap = []
    dist = [float('inf')] * (n+1)
    visited = [False] * (n+1)
    dist[v] = 0
    heapq.heappush(heap,(v,0))
    while heap:
        v,c = heapq.heappop(heap)
        # print(graph[v])
        for x in graph[v]:
            nxt, nc = x
            if c + nc < dist[nxt]:
                visited[nxt] = True
                dist[nxt] = nc + c
                heapq.heappush(heap,(nxt,nc+c))
    return dist

def get_dist(v,a,b,graph,n):
    #v : a랑 b까지 거리 측정할 노드
    v_d = dj(v,graph,n)
    return v_d[a] + v_d[b]
#n : 개수
#s : 출발지점
# 최저 예상 택시요금 (합승 안해도 됨)
#fares [지점1,지점2,가격]

