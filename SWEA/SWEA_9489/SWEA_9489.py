import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split()) # 가로길이(열개수) 세로길이(행개수)
    arr = [list(map(int, input().split())) for _ in range(M)]

    total = 0
    for i in range(N) :
        count = 0
        for j in range(M) :
            if arr[i][j] == 1 :
                count += 1
            else :
                count = 0
            if count > total :
                total = count

    for j in range(M) :
        count = 0
        for i in range(N) :
            if arr[i][j] == 1 :
                count += 1
            else :
                count = 0
            if count > total :
                total = count

    print(total)

# for tc in range(1, T+1) :
#     N, M = map(int, input().split()) # 가로길이(열개수) 세로길이(행개수)
#     arr = [list(map(int, input().split())) for _ in range(M)]
#     dxy = [[1, 0], [0, 1]]
#
#     total = 0
#     for i in range(N) : # 가로
#         for j in range(M) : # 세로
#             count = 0
#             for dx, dy in dxy : # 가로 탐색
#                 nx = i + dx
#                 ny = j
#                 if nx < 0 or ny < 0 or nx >= N or ny >= M :
#                     break
#                 if arr[nx][ny] == 1 :
#                     count += 1
#                 else :
#                     break
#
#             for dx, dy in dxy : # 세로 탐색
#                 nx = i
#                 ny = i + dy
#                 if nx < 0 or ny < 0 or nx >= N or ny >= M :
#                     break
#                 if arr[nx][ny] == 1 :
#                     count += 1
#                 else :
#                     break
#
#                 total = count
#         if total < count :
#             total = count
#     print(total)




