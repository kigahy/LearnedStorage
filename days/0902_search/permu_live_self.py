path = [] # 경로 기록을 출력하기 위함
level = 0
used = [0] * 7 # 1~7숫자의 사용 여부를 기록할 리스트

def recur(level): # 0부터 시작, 3개를 뽑은 경우 종료
    if level == 3 :
        print(*path)
        return

    for i in range(1, 7):

        if used[i] == 1:
            continue

        used[i] = 1 # in 빼고 추가함
        path.append(i)
        recur(level + 1)
        path.pop() # 사용했던 경로 삭제
        used[i] = 0
        # if i in path : # 중복 제거된 순열
        #     continue 브랜치 많을 때 쓰면 시간초과 ㄽㄱ

        if used[i] == 1 :
            continue

recur(0) # 호출 : 대부분 시작점을 같이 전달해줌


# def first(one, two, three) :
#     if three == 3:
#         return
#     for i in range(3) :
#         print(one, two, three)
#         three += 1
#         first(one, two, three)
#
#
#
# first(1, 1, 1)