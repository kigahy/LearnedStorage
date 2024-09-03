import sys
sys.stdin = open("input_prac_code.txt", "r")

def DFS(start, end) :
    s = start
    visited[s] = 1
    stack.append(s)
    print(s)
    while True:
        for i in arr[s] :
            if visited[i] == 0 :
                stack.append(s) # 일단 인접정점 탐색해야 하니 돌아갈 이 노드를 저장
                s = i # 깊이우선탐색. 위치 break 위에 올리니 안멈춤 ㅅ바
                visited[s] = 1
                print(s)
                break

        # while True: 아직까지 이거랑 뭔차이인지 모르겠음 ㅠ
        #         for i in arr[s] :
        #             if visited[i] == 0 :
        #                 stack.append(s) # 일단 인접정점 탐색해야 하니 돌아갈 이 노드를 저장
        #                 visited[i] = 1
        #                 print(i)
        #                 s = i # 깊이우선탐색
        #                 break

        else : # 인접노드를 방문했다면 예전에 저장해둔 stack의 정점을 빼내 남은 노드 탐색
            if stack :
                s = stack.pop()
            else:
                break

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