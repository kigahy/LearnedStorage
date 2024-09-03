import sys
sys.stdin = open("input.txt", "r")

for tc in range(10) :

    length, start = map(int, input().split()) # 정점 수, 시작점
    lst = list(map(int, input().split())) # from, to, from, to
    dict = {}

    for i in range(0, len(lst)-1, 2) :
        v1 = lst[i*2] # lst의 i번째 값을 v1 변수에 할당
        v2 = lst[i*2+1] # lst의 i+1번째 값을 v2 변수에 할당

        dict[v1] = v2

    print(dict)

