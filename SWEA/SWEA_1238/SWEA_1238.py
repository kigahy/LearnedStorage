import sys
sys.stdin = open("input.txt", "r")

def BFS(start) :
    count = 0



for tc in range(10) :

    length, start = map(int, input().split()) # 데이터의 길이, 시작점
    lst = list(map(int, input().split())) # from, to, from, to

    arr = [[] for _ in range(101)]

    for i in range(length//2) : # from, to, ... 의 횟수만큼 반복
        v1 = lst[i*2] # lst의 i번째 값을 v1 변수에 할당
        v2 = lst[i*2+1] # lst의 i+1번째 값을 v2 변수에 할당

        arr[v1].append(v2)

    result = BFS(start, )

