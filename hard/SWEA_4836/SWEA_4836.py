import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N = int(input()) # 칠할 영역의 개수

    for _ in range(N) :
        r1, c1, r2, c2, color = map(int, input().split())

        if color == 1 :

        elif color == 2 :
