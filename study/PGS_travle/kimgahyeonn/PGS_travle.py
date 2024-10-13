def myBfs(j, tickets, answer, N, visited):
    queue = []
    answer.append(tickets[j][0])
    answer.append(tickets[j][1])
    queue.append(tickets[j][2])  # 고유번호를 저장
    visited[tickets[j][2]] = 1

    while queue:  # 더 돌 곳 없을 때까지
        if len(tickets) == N + 1: # 만약 횟수만큼 여행 완료되면 끝냄
            return
        t = queue.pop(0)  # 고유번호 빼냄
        visited[t] = 1  # 해당 여행경로는 방문함
        # answer.append(tickets[t][1])

        for w in range(N):  # 모든 여행경로를 순회
            # 고유번호를 통하여 몇번째 경로인지 알아냄. 현재 경로의 도착지점과 for문 돌린 경로의 시작지점이 같다면
            if tickets[t][1] == tickets[w][0] and visited[tickets[w][2]] == 0:  # 그리고 아직 방문하지 않았다면
                answer.append(tickets[w][1])  # 경로를 추가
                queue.append(w)  # 고유번호를 인큐


def solution(tickets):
    tickets.sort(key=lambda a: a[1])  # 람다식 도와준 진문님 땡큐!
    answer = []  # 방문한 여행지 저장할 배열
    N = len(tickets)  # 총 여행의 수
    visited = [0] * N  # 방문체크

    for i in range(N):  # 방문체크나 bfs 쉽게 하려고 고유번호 부여
        tickets[i].append(i)

    for j in range(N):
        if tickets[j][0] == 'ICN':  # 출발지가 ICN인 경로 찾아서 그 지점을 첫 경로로 설정
            myBfs(j, tickets, answer, N, visited)
            break  # ICN 처음 한 번만 찾고 Bfs돌 거라서 break 걸어줌
    return answer