import sys
sys.stdin = open("input_SWEA_1227.txt", "r")

def findPoints(s) : # 미로의 시작점 찾는 함수
    for i in range(100) : # 행마다
        for j in range(100) : # 열마다
            if arr[i][j] == s :
                return i, j
            else :
                continue

def BFS(start, end, s_row, s_col) : # 시작값, 끝값, 시작행, 시작열
    s = start

for tc in range(1, 10) :
    arr = [list(map(int, input().split())) for _ in range(100)]
    start = 2 # 시작할 지점
    end = 3 # 찾을 지점 (도착)

    s_row = 0 # 시작점의 행 열
    s_col = 0

    dxy = [[1, 0], [0, 1], [-1, 0], [1, 0]]

    s_row, s_col = findPoints(start) # 미로의 시작과 도착점의 좌표



