def solution(n, s, a, b, fares):
    answer = 987654321
    INF=987654321
    graph=[[INF]*(n+1)for _ in range(n+1)]
    
    for i in range(1,n+1):
        graph[i][i]=0
    
    for fare in fares:
        A,B,f=fare
        graph[A][B]=f
        graph[B][A]=f
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    
    for taxi in range(1,n+1):
        if answer>graph[s][taxi]+graph[taxi][b]+graph[taxi][a]:
            answer=graph[s][taxi]+graph[taxi][b]+graph[taxi][a]
    
    return answer

# A의 집은 6번 지점에 있으며 B의 집은 2번 지점에 있고 두 사람이 모두 귀가하는 데 소요되는 예상 최저 택시요금이 얼마인 지 계산하려고 합니다.

# 1. 완탐? n<=200 모든 노드를 택시를 타고 최단거리? 모든 노드에서 노드까지 최단거리 구하기 n*n*n 8000000 플로이드 워셜
#9:20
#9:40