from collections import deque

def findEnemy(maps, length):
    visited = [[0] * length for _ in range(length)]  # 방문체크
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 델타 탐색
    count = 0  # 칸수 셀 변수
    minimum = 0  # 여러가지 길 중 가장 작은 칸수 저장할 변수
    queue = deque()  # 경로 저장할 덱
    queue.append((0, 0))  # 큐에 행과 열 동시에 저장
    visited[0][0] = 1  # 방문쳌
    # distance = [] # 거리

    while queue:  # 방문할 지점 거덜날 때까지
        x, y = queue.popleft()

        if x == 4 and y == 4:
            return visited[4][4]  # 거리 정보가 저장되어 있음

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 > nx or 0 > ny or nx >= length or ny >= length:
                continue  # 범위 벗어나면 다른곳 탐색
            if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1  # 방문체크를 거리로 저장함
                queue.append((nx, ny))

    return -1  # 큐가 다 떨어질 때까지 x=4 혹은 y=4에 도달하지 못했을 때 -1 반환


def solution(maps):
    answer = 0
    length = len(maps)  # 입력값의 가로길이
    answer = findEnemy(maps, length)
    return answer