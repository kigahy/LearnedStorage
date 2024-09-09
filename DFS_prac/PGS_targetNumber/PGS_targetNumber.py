import sys
sys.stdin = open("input_PGS_targetNumber.txt", "r")

def solution(answer, target) :
    global count # 타깃으로 만들어낸 횟수
    global index # 재귀 돌 때마다 하나씩 이동할 numbers의 인덱스

    if answer == target:  # 재귀로 풀어낸 값이 타깃과 같다면
        count += 1 # 카운트로 세어줌

    solution(numbers[index+1] + 1, target)
    solution(numbers[index+1] - 1, target)

for tc in range(1, 3): # 테케 1개 준비함
    target = int(input())
    numbers = list(map(int, input().split()))
    answer = 0 # 재귀 돌면서 만들어낸 값
    count = 0 # 타깃으로 만들어낸 횟수
    index = 0 # 재귀 돌 때마다 하나씩 이동할 numbers의 인덱스
    solution(answer, target)
    print(f'#{tc} {count}')
