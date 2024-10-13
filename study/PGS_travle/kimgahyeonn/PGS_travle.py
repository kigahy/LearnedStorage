<<<<<<< HEAD
def myBfs(j, tickets, answer, N, visited):
    queue = []
    answer.append(tickets[j][0])
    answer.append(tickets[j][1])
    queue.append(tickets[j][2])  # 고유번호를 저장
    visited[tickets[j][2]] = 1

    while queue:  # 더 돌 곳 없을 때까지
        if len(tickets) == N + 1: # 만약 횟수만큼 여행 완료되면 끝냄
            return
=======
def myBfs(tickets, answer, N, visited):
    queue = []
    answer.append(tickets[0][0])
    answer.append(tickets[0][1])
    queue.append(tickets[0][2])  # 고유번호를 저장
    visited[tickets[0][2]] == 1

    while queue:  # 더 돌 곳 없을 때까지
>>>>>>> a7796d91e927460b13fbbd4d482e3bcefba68add
        t = queue.pop(0)  # 고유번호 빼냄
        visited[t] = 1  # 해당 여행경로는 방문함
        # answer.append(tickets[t][1])

        for w in range(N):  # 모든 여행경로를 순회
            # 고유번호를 통하여 몇번째 경로인지 알아냄. 현재 경로의 도착지점과 for문 돌린 경로의 시작지점이 같다면
<<<<<<< HEAD
            if tickets[t][1] == tickets[w][0] and visited[tickets[w][2]] == 0:  # 그리고 아직 방문하지 않았다면
                answer.append(tickets[w][1])  # 경로를 추가
=======
            if tickets[t][1] == tickets[w][0] and visited[w] == 0:  # 그리고 아직 방문하지 않았다면
                answer.append(tickets[w][1])
>>>>>>> a7796d91e927460b13fbbd4d482e3bcefba68add
                queue.append(w)  # 고유번호를 인큐


def solution(tickets):
<<<<<<< HEAD
    tickets.sort(key=lambda a: a[1])  # 람다식 도와준 진문님 땡큐!
=======
    tickets.sort(key=lambda a: a[1])
    print(tickets)
>>>>>>> a7796d91e927460b13fbbd4d482e3bcefba68add
    answer = []  # 방문한 여행지 저장할 배열
    N = len(tickets)  # 총 여행의 수
    visited = [0] * N  # 방문체크

<<<<<<< HEAD
    for i in range(N):  # 방문체크나 bfs 쉽게 하려고 고유번호 부여
        tickets[i].append(i)

    for j in range(N):
        if tickets[j][0] == 'ICN':  # 출발지가 ICN인 경로 찾아서 그 지점을 첫 경로로 설정
            myBfs(j, tickets, answer, N, visited)
            break  # ICN 처음 한 번만 찾고 Bfs돌 거라서 break 걸어줌
    return answer
=======
    for i in range(N):  # 방문체크나 bfs 쉽게 하려고 티켓의 index 순서대로 고유번호 부여
        tickets[i].append(i)

    myBfs(tickets, answer, N, visited)
    return answer

# def myBfs(tickets, answer, N, visited):
#     queue = []
#     answer.append(tickets[0][0])
#     # answer.append(tickets[0][1])
#     queue.append(tickets[0][2])  # 고유번호를 저장
#     visited[tickets[0][2]] == 1
#
#     while queue:  # 더 돌 곳 없을 때까지
#         t = queue.pop(0)  # 고유번호 빼냄
#         visited[t] = 1  # 해당 여행경로는 방문함
#         answer.append(tickets[t][1])
#
#         for w in range(N):  # 모든 여행경로를 순회
#             # 고유번호를 통하여 몇번째 경로인지 알아냄. 현재 경로의 도착지점과 for문 돌린 경로의 시작지점이 같다면
#             if tickets[t][1] == tickets[w][0] and visited[w] == 0:  # 그리고 아직 방문하지 않았다면
#                 queue.append(w)  # 고유번호를 인큐
#
#
# def solution(tickets):
#     answer = []  # 방문한 여행지 저장할 배열
#     N = len(tickets)  # 총 여행의 수
#     visited = [0] * N  # 방문체크
#
#     for i in range(N):  # 방문체크나 bfs 쉽게 하려고 티켓의 index 순서대로 고유번호 부여
#         tickets[i].append(i)
#
#     myBfs(tickets, answer, N, visited)
#     return answer


# def myBfs(tickets, answer, N, visited):
#     queue = []
#     answer.append(tickets[0][0])
#     answer.append(tickets[0][1])
#     queue.append(tickets[0][2])  # 고유번호를 저장
#     visited[tickets[0][2]] == 1
#
#     while queue:  # 더 돌 곳 없을 때까지
#         t = queue.pop(0)  # 고유번호 빼냄
#         visited[t] = 1  # 해당 여행경로는 방문함
#         # answer.append(tickets[t][1])
#
#         for w in range(N):  # 모든 여행경로를 순회
#             # 고유번호를 통하여 몇번째 경로인지 알아냄. 현재 경로의 도착지점과 for문 돌린 경로의 시작지점이 같다면
#             if tickets[t][1] == tickets[w][0] and visited[w] == 0:  # 그리고 아직 방문하지 않았다면
#                 answer.append(tickets[w][1])
#                 queue.append(w)  # 고유번호를 인큐
#
#
# def solution(tickets):
#     answer = []  # 방문한 여행지 저장할 배열
#     N = len(tickets)  # 총 여행의 수
#     visited = [0] * N  # 방문체크
#
#     for i in range(N):  # 방문체크나 bfs 쉽게 하려고 티켓의 index 순서대로 고유번호 부여
#         tickets[i].append(i)
#
#     myBfs(tickets, answer, N, visited)
#     return answer


# 버려야될 내새끼같은 코드
# def myBfs(tickets, answer, N, visited):
#     queue = []
#     visited.append(tickets[0][0])
#     visited.append(tickets[0][1])
#     queue.append(tickets[0][1])  # 도착지 저장
#     visited[tickets[0][2]] == 1
#
#     while queue:  # 더 돌 곳 없을 때까지
#
#
# def solution(tickets):
#     answer = []  # 방문한 여행지 저장할 배열
#     N = len(tickets)  # 총 여행의 수
#     visited = [0] * N  # 방문체크
#
#     for i in range(N):  # 방문체크나 bfs를 쉽게 하기 위하여 티켓의 index 당 순서대로 고유번호를 부여함
#         tickets[i].append(i)
#
#     myBfs(tickets, answer, N, visited)
#     return answer
>>>>>>> a7796d91e927460b13fbbd4d482e3bcefba68add
