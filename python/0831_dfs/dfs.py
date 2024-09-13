import sys
sys.stdin = open("input_prac_code.txt", "r")

def DFS(start, end) :

    s = start
    stack.append(s)
    visited[s] = 1
    print(s)

    while True :
        for i in arr[s] : # 시작점의 인접노드 순회
            if visited[i] == 0 :
                stack.append(s) # 다시 돌아갈 시작정점 어펜드
                s = i # 해당 인접노드를 탐색
                print(s)
                visited[s] = 1  # 방문쳌
                break

        else : # 인접노드를 모두 순회했다면
            if stack :
                s = stack.pop() # 돌아갈 부모 노드를 시작점으로
            else :
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

'''주의.. 순서 이렇게 했더니 안됨
stack.append(s) # 다시 돌아갈 시작정점 어펜드
print(s)
visited[s] = 1 # 방문쳌
s = i # 해당 인접노드를 탐색
break
'''