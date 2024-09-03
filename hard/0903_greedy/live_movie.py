arr = ['O', 'X']
path = []
# lev = 3 집합의 원소 3개임

def run(lev) : # lev : lev번째 요소. 0, 1, 2번째 요소
    if lev == 3 : # 원소 3개를 모두 고려함
        print(path) # 골랐단 것을 출력
        return

for i in range(2) : # 후보군 반복하는 재귀호출 로직. branch만큼 반복 돎.. 2가지 경우의 수
    path.append(arr[i]) # 다음 재귀 호출 전 경로에 추가
    run(lev + 1) # 다음 lev 고려하라는 뜻
    path.pop() # 다시 돌아왔다면 경로 삭제

run(0)