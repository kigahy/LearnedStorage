import sys
sys.stdin = open("input_prac_code.txt", "r")

def BFS(start, end) :
    s = start
    queue.append(s) # 시작점 인큐. 큐의 끝에 넣어둠
    visited[s] = 1 # 대체 이 끝값에 왜 1을 체크하는 거죠?

    while queue : # 큐에 값 남아있으면 가야 할 곳 있다는 뜻
        t = queue.pop(0) # 시작점 꺼내서 t에 할당
        print(t)

        for i in arr[t] : # 스타트지점 값의 인접노드 순회(중위순회)
            if visited[i] == 0 : # 인접노드는 여러개일 수 있으니, 이전에 이미 방문했다면 두 번 방문하지 않음
                queue.append(i) # while 돌면서 반복하기 위하여 append
                visited[i] = visited[t] + 1 # 이게 뭔지 잘 모르겠다...ㅠㅠ -> 거리 계산할 때는 필요함

V, E = map(int, input().split())
lst = list(map(int, input().split()))

arr = [[] for _ in range(V+1)]

for i in range(E) :
    v1 = lst[i*2]
    v2 = lst[i*2+1]

    arr[v1].append(v2)
    arr[v2].append(v1)

queue = []
visited = [0] * (V + 1)

BFS(1, V)






























'''시행착오 2. pop과 append 반대로 쓰고 while 아닌 for 씀. stack 아니고 queue
import sys
sys.stdin = open("input_prac_code.txt", "r")

def bfs(start, end) :
    global visited
    print(1)
    visited[start] = 1
    s = start
    stack.append(start)

    for i in arr[s] :
        if visited[i] == 0 :
            visited[i] = 1
            start = stack.pop()


V, E = map(int, input().split()) # 정점 수, 간선 수
lst = list(map(int, input().split())) # 서로 연결된 인접 정점 입력받음

arr = [[] for _ in range(V+1)] # 노드 번호에 해당하는 인접 노드를 저장할 변수
visited = [0] * (V + 1)
stack = []
print(arr)

for i in range(V) :
    v1 = lst[i*2]
    v2 = lst[i*2+1]

    arr[v1].append(v2)
    arr[v2].append(v1)


bfs(1, V)
'''


'''시행착오 1. = 아니고 append
for i in range(V) :
    v1 = lst[i*2]
    v2 = lst[i*2+1]

    arr[v1] = v2
    arr[v2] = v1

    visited = [0] * (V + 1)

bfs(1, V)

V, E = map(int, input().split())  # 정점 수, 간선 수
lst = list(map(int, input().split()))  # 서로 연결된 인접 정점 입력받음

arr = [[] for _ in range(V + 1)]  # 노드 번호에 해당하는 인접 노드를 저장할 변수
stack = []
print(arr)

for i in range(V):
    v1 = lst[i * 2]
    v2 = lst[i * 2 + 1]

    arr[v1] = v2
    arr[v2] = v1

    visited = [0] * (V + 1)

bfs(1, V)
'''



