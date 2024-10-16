# 실패사유 : 문제의 유형을 파악하지 못했다
# 처음 문제를 받고 DFS라고 확신했으나, 문제를 풀어나가면서 완전탐색으로 바뀌고 있는 코드를 보았습니다...
# 그렇게 완전탐색으로 풀이 방법을 바꾸어 보았습니다. 연속되는 벌통의 최대합을 구하기 위하여 itertools를 써보았으나...
# 1. combinations 문법에 미숙했습니다. 24행 C보다 작은 것을 확인했으면 조합의 개별 값의 제곱을 뽑아내야 하는데, 그러지 못했습니다.
# 2. 52행부터 두 번째 벌통을 선택하기 위하여 visited를 사용하려 했으나, 첫 번째 벌통의 column 값을 뽑아내지 못했습니다.
# 풀이 과정은 올려놓은 사진에 있는데 장황하네요 ㅠㅠ 문제를 읽은 다음 명확한 목표를 설정하는 게 중요하다는 것을 깨닫게 되었습니다!

from itertools import combinations
import sys
sys.stdin = open("input_2115.txt", "r")
T = int(input())

def Search(M, C, row, col):
    col_lst = []

    # 해당 행에서 M만큼의 꿀을 수집
    for col_plus in range(M):
        col_lst.append(beehive[row][col + col_plus])

    max_val = 0
    # 조합 생성하여 허용량 이하의 최대 합을 찾음
    for comb in combinations(col_lst, M):
        current_sum = sum(comb)
        if current_sum <= C and current_sum > max_val:
            max_val = current_sum

    return max_val, row, col

for tc in range(1, T+1) :

    # 각 벌통 크기, 벌통 수, 꿀의 최대 양 그리고 벌집 정보
    N, M, C = map(int, input().split())
    beehive = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    # 리스트 0번:행, 1번:열 정보
    max_temp_lst = [0]*2
    maximum = 0
    max_temp = 0

    for row in range(N):
        for col in range(N-M+1) :
            result, result_row, result_col = Search(M, C, row, col)

            if max_temp < result :
                max_temp = result
                max_temp_lst[0] = result_row
                max_temp_lst[1] = result_col

    # 두 번째 벌통에서 벌 채취하기 위하여 첫 번째 벌통 위치에 방문체크
    for i in range(M) :
        for j in range(M) :
            visited[max_temp_lst[0]][max_temp_lst[1]+j] = 1