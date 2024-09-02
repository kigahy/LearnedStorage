path = []

# 주사위 몇개 던졌는지 알아야 함. 합은 몇인지 알아야 함
def recur(level, total):
    if total > 10 : # 가지치기. 백트래킹과 흡사
        return
    if level == 3 : # 주사위 던진 횟수를 level로 기저조건 만듦
        # total이 10이 넘는지도 확인
        if total <= 10 :
            print(path)
        return
    for i in range(1, 7):
        # i의 의미 : 주사위 눈
        path.append(i)
        recur(level + 1, total + i) # 주사위 결과 더하여 전달
        path.pop()



recur(0, 0) # 0개를 던진 걸로 시작