import sys
sys.stdin = open("input_4835.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) #정수 개수, 구간 개수
    lst = list(map(int, input().split()))

    max = 0 # 최댓값
    min = 9999999999 # 최솟값에 정말정말 큰 임의의 정수 할당
    temp = 0 # 구간합 구할 임시변수
    val = 0 # 최댓값-최솟값

    for i in range(0, N-M+1) : # 리스트를 벗어나지 않기 위하여, 0부터 리스트길이-구간길이+1
        temp = 0
        for j in range(i, i+M) : # 해당 구간을 구하기 위하여 i부터 구간까지
            temp += lst[j] # 임시변수에 해당 구간의 값 더함
        # print(temp) #디버깅
        if temp > max : # 리스트 인덱스를 이동하며 한 구간 당 최댓값 구함
            max = temp
        if temp < min : # 리스트 인덱스를 이동하며 한 구간 당 최솟값 구함
            min = temp

    # print(max, min)
    val = max - min
    print(f'#{tc} {val}')
