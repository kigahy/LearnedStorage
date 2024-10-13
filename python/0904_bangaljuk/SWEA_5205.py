import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1) : # sorted써라 개고생하지 말고
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {sorted(arr)[N//2]}')
    # 정렬은 sort.. 그런데 병합정렬은 sorted로 해결 불가능