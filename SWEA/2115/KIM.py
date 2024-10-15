from itertools import combinations

import sys
sys.stdin = open("input_2115.txt", "r")
T = int(input())

def DFS(row, col, N, M, C):
    pass

for tc in range(1, T+1) :

    # 각 벌통 크기, 벌통 수, 꿀의 최대 양 그리고 벌집 정보
    N, M, C = map(int, input().split())
    beehive = [list(map(int, input().split())) for _ in range(N)]

    max_honey = 0
    first_max = 0
    second_max = 0

    first_row = 0
    first_col = 0

    second_row = 0
    second_col = 0

    for row in range(N):
        for col in range(N) :
            DFS(row, col, N, M, C)
