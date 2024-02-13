import sys
sys.setrecursionlimit(10**6)

pre = []
post = []

def solution(nodeinfo):
    nodeinfo = [[i + 1, *nodeinfo[i], None, None] for i in range(len(nodeinfo))]
    nodeinfo.sort(key = lambda x: [-x[2], x[1]])
    
    tree = get_tree(nodeinfo)
    
    order(tree)
    
    return pre, post


def get_tree(nodeinfo):
    tree = None
    for node in nodeinfo:
        if not tree:
            tree = node
            continue
            
        parent = tree
        while parent:
            if node[1] < parent[1]:
                if not parent[3]:
                    parent[3] = node
                    parent = parent[3]
                parent = parent[3]
            else:
                if not parent[4]:
                    parent[4] = node
                    parent = parent[4]
                parent = parent[4]
                    
    return tree
    
    
def order(node):
    pre.append(node[0])
    if node[3]:
        order(node[3])
    if node[4]:
        order(node[4])
    post.append(node[0])


# tree 만들기 오랜만이라 삽질 좀 했네요
# 전위 중위 후위 순회도 오랜만
# 재귀 제한 안 늘려줘서 채점 시 두 개 런타임 났었다... 재귀 풀이엔 set recursion limit 기억하기!
