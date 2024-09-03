import sys
sys.stdin = open("input_prac_code.txt", "r")

def bfs(start, N) :
    s = start
    visited[s] = 1
    queue.append(s) # 시작점 값 어펜드

    while queue : # 큐에 값 없으면 모두 순회했으므로 종료
        t = queue.pop(0) # 큐의 첫 번째 값 pop
        print(t)

        for i in arr[t] :
            if visited[i] == 0 : # 해당 노드를 방문하지 않았다면
                queue.append(i) # 해당 정점 큐에 넣은 후
                visited[i] = 1
                break

N, E = map(int, input().split())
lst = list(map(int, input().split()))
arr = [[] for _ in range(E)]
visited = [0] * (N + 1)
queue = []
result = []

for i in range(E) :
    v1 = lst[i*2]
    v2 = lst[i*2+1]

    arr[v1].append(v2)
    arr[v2].append(v1)

bfs(1, N)