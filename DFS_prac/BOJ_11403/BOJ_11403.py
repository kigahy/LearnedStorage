import sys
sys.stdin = open("input_11403.txt", "r")
T = int(input())

def DFS(row) :
    global N
    for i in range(N) :
        if matrix[row][i] == 1 and visited[i] == 0 :
            visited[i] = 1 # 방문체크한 다음
            DFS(i) # 깊이우선탐색

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    visited = [0]*N
    for i in range(N) :
        DFS(i)
        for j in range(N) :
            if visited[j] == 1 :
                print(1, end = ' ')
            else :
                print(0, end = ' ')

        visited = [0] * N # visited 초기화
        print()

