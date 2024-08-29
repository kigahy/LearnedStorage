import sys

sys.stdin = open('input.txt')

N = int(input())  # 스위치 개수 입력받음
switches = list(map(int, input().split()))  # 스위치 상태 입력받음
students = int(input())  # 학생 수 입력받음
information = [list(map(int, input().split())) for _ in range(students)]  # 한 학생이 받은 성별과 숫자. [[1,3],[2,3]]

# information[i][0] 에서 i는 학생 수만큼, 0은 성별
for i in range(students):  # 학생 수만큼 작업 반복. 성별에 따라 솔루션 다름
    if information[i][0] == 1:  # 남학생이라면
        number = information[i][1]  # 배수로 곱할 숫자 값만 추출
        for j in range(number - 1, len(switches), number):  # 스위치 수만큼 반복

            if switches[j] == 1:  # 0을 1로 바꾸고 1을 0으로 바꿈
                switches[j] = 0
            elif switches[j] == 0:
                switches[j] = 1

    index = []
    if information[i][0] == 2:  # 여학생이라면
        number = information[i][1]  # 중심으로 잡을 숫자 반환

        x = 0  # 양쪽으로 인덱스 영역 넓힐 숫자

        while True:
            if number - x - 1 < 0 or number + x - 1 >= N:
                break

            elif switches[number - x - 1] == switches[number + x - 1]:  # 스위치 값이 같다면
                if switches[number - x - 1] == 1:  # 0을 1로 바꾸고 1을 0으로 바꿈
                    switches[number - x - 1] = 0
                    switches[number + x - 1] = 0
                elif switches[number - x - 1] == 0:
                    switches[number - x - 1] = 1
                    switches[number + x - 1] = 1
                x += 1

            else: #switches[number - x - 1] != switches[number + x - 1]:
                break

i = 0 # 20개씩 출력
for a in switches:
    i += 1
    print(a, end=' ')
    if i % 20 == 0:
        print()
print()
