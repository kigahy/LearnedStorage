import sys
sys.stdin = open("input_prac_code.txt", "r")

def DFS(start, end) :
    s = start
    stack.append(s) # 해당 정점 스택에 넣음
    print(s)

    while True:
        for i in arr[s] : # 정점과 인접한 노드 순회
            if visited[i] == 0 : # 아직 방문하지 않았다면
                stack.append(i) # 스택에 넣음
                print(i)
                s = i
                visited[i] = 1
                break

        else : #남은 인접정점이 없다면
            if stack :
                s = stack.pop() # 스택 값 pop하여 새로운 정점으로 만듦
            else : # 스택에 남은 값 없다면
                break # while문 탐색 종료




V, E = map(int, input().split())
lst = list(map(int, input().split()))
visited = [0] * (V+1)
arr = [[] for _ in range(V+1)]
stack = []

for i in range(E) :
    v1 = lst[i*2]
    v2 = lst[i*2+1]

    arr[v1].append(v2)
    arr[v2].append(v1)

DFS(1, V)