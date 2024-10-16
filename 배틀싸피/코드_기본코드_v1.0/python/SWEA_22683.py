T = int(input)

for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]