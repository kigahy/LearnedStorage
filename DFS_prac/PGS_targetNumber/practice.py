

def solution(numbers, target):

    global count
    numbers = list(map(int, input().split()))  # 더하고 뺄 숫자들
    target = int(input())  # 최종으로 만들어낼 타깃값
    count = 0  # 경우의 수

    solution(numbers, target)

    return count


