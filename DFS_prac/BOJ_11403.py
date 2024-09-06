import sys
sys.stdin = open("input_11403.txt", "r")
T = int(input())

for tc in range(1, T+1):
    dxy = [[1, 0], [0, 1]] # 오른쪽과 아래쪽으로만 갈 수 있음

