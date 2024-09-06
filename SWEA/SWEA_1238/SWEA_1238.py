import sys
sys.stdin = open("input.txt", "r")

def BFS(s) : # 시작점 입력받음
    queue = [] # bfs 선입선출을 위한 큐
    used[s] = 1 # 시작점 방문체크
    queue.append(s)

    while queue :
        t = queue.pop(0)
        for w in arr[t] : # 선입한 queue의 정점
            if used[w] == 0: # 방문하지 않았다면
                queue.append(w) # 그 정점 큐에 삽입
                used[w] = used[t] + 1 # 방문체크

for tc in range(1, 11) :

    length, start = map(int, input().split()) # 데이터의 길이, 시작점
    lst = list(map(int, input().split())) # from, to, from, to
    used = [0] * 101 # 인덱스에 따라 방문체크할 visited

    arr = [[] for _ in range(101)]

    for i in range(length//2) : # from, to, ... 의 횟수만큼 반복
        v1 = lst[i*2] # lst의 i번째 값을 v1 변수에 할당
        v2 = lst[i*2+1] # lst의 i+1번째 값을 v2 변수에 할당

        arr[v1].append(v2)

    BFS(start)
    print(used)
    result = 0

    for i in range(101) :
        # if used[i] == max(used) :
        #     result = max(result, i)
        if used[i] == max(used) and i > result :
            result = i

    print(f'#{tc} {result}')

