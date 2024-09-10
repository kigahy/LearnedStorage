# 반복문 안에 있는 함수호출이 어려웠다. solution함수 반복문에서 myBfs를 호출하는 부분!
# 혜령언니가 추천한 안산학생이 추천한 DFS 연습문제 [백준 11403]와 흡사한 구조이며 난이도이며...

def myBfs(i, N, computers, visited) :  # 컴퓨터 수, 연결 정보
    queue = []
    start = i
    visited[start] = 1  # 시작점 방문체크
    queue.append(start)  # 시작점 인큐

    while queue:  # 더이상 방문할 지점 없을 때까지 반복
        t = queue.pop(0)  # 너비우선순회할 지점 pop
        visited[t] += 1

        for w in range(N) :  # 해당 행과 다른 지점 연결되었는지 확인
            if computers[t][w] == 1 and visited[w] == 0 :  # 해당 행과 연결된 컴퓨터가 있고 방문되지 않았다면
                queue.append(w)  # 인큐
    return  # 혹시 모를 무한루프 방지

def solution(n, computers) :
    answer = 0
    visited = [0] * n  # for 통해 한 행 탐색하므로 일차원 배열

    for i in range(n) :  # 하나의 열에 대하여 반복
        if visited[i] == 0 :  # 아직 방문하지 않았다면
            myBfs(i, n, computers, visited)  # bfs 방문하는데
            answer += 1  # 이 방문은 네트워크 연결 +1을 의미함

    return answer