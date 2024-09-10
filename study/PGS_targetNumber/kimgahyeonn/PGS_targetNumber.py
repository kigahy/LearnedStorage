import sys
sys.stdin = open("input_PGS_targetNumber.txt", "r")

def solution(num, index, target) :
    global count # 타깃으로 만들어낸 횟수

    if index == len(numbers) : # 하나씩 옮긴 인덱스가 수의 길이와 같아졌다면
        if num == target:  # 거기다가 재귀로 풀어낸 값이 타깃과 같다면
            count += 1 # 카운트로 세어줌
        return
    solution(num + numbers[index], index + 1, target)
    solution(num - numbers[index], index + 1, target)

    return count # 그냥 return만 쓰면 오류남

for tc in range(1, 3): # 테케 2개 준비함
    target = int(input())
    numbers = list(map(int, input().split()))
    count = 0 # 타깃으로 만들어낸 횟수
    sol = 0 # 최종 count를
    index = 0 # 재귀 돌 때마다 하나씩 이동할 numbers의 인덱스
    sol = solution(0, index, target)
    print(f'#{tc} {sol}')
