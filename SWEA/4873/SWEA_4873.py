import sys
sys.stdin = open("input_4873.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    words = list(input())
    stack = []

    for word in words :
        if stack and word == stack[-1]: # if stack 안쓰면? stack[-1] 읽어서 out of range남 주의
            stack.pop() # pop에 인자 안 주면 가장 마지막 값 빼냄
            continue

        stack.append(word) #continue로 위 구문 실행 안 되면 스택에 문자 추가. else 안써도 되어 좋음

    print(f'#{tc} {len(stack)}')
