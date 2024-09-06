import sys
sys.stdin = open("input.txt", "r")

def BFS(start) :
    visited = [0]*101
    queue = [] # 방문시 선입선출할 큐
    visited[start] = 1 # 시작점 방문체크
    queue.append(start) # 큐에 시작점 append

    while queue : # 더이상 방문할 지점 없을 때까지
        t = queue.pop(0) # queue에 지점 있으면 pop함

        for i in arr[t] : # t의 인접노드 순회
            if visited[i] == 0 : # 아직 방문하지 않았다면
                visited[i] = visited[t] + 1 # 방문체크에 거리체크도 함께 하여 제일 마지막 방문지점이 어느지점인지 알게 함
                queue.append(i) # 큐에 값 추가
            

for tc in range(1, 11) :
    length, start = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = [[] for _ in range(101)]

    for i in range(length//2) : # 인접리스트 형성
        v1 = lst[i*2]
        v2 = lst[i*2+1]

        arr[v1].append(v1)

    # print(arr) # 디버깅
    BFS(start)