# import sys
# sys.stdin = open("input.txt", "r")

def Find(used) :
    result = 0
    for i in range(101) : # used의 길이 즉 해당하는 사람의 번호까지 반복
        if visited[i] == max(visited) and i > result : # visited에서 가장 멀리 간 노드에 해당하는 거리라면
            result = i # 해당 인덱스값을 result에 넣음

    return result

def BFS(start) :
    queue = [] # 방문시 선입선출할 큐
    visited[start] = 1 # 시작점 방문체크
    queue.append(start) # 큐에 시작점 append

    while queue : # 더이상 방문할 지점 없을 때까지
        t = queue.pop(0) # queue에 지점 있으면 pop함
        for w in arr[t] : # t의 인접노드 순회
            if visited[w] == 0 : # 아직 방문하지 않았다면
                visited[w] = visited[t] + 1 # 방문체크에 거리체크도 함께 하여 제일 마지막 방문지점이 어느지점인지 알게 함
                queue.append(w) # 큐에 값 추가

for tc in range(1, 11) :
    length, start = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = [[] for _ in range(101)]
    visited = [0]*101

    for i in range(length//2) : # 인접리스트 형성
        v1 = lst[i*2]
        v2 = lst[i*2+1]

        arr[v1].append(v2)

    # print(arr) # 디버깅
    BFS(start)

    # 너비우선탐색 완료했고, 이제 최고값 구해야 함
    result = Find(visited)
    print(f'#{tc} {result}')