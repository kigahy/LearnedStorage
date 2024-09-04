import sys
sys.stdin = open("sample_input.txt", "r")

def quick_sort(div_arr):
    if len(div_arr) <= 1 :
        return div_arr # 배열 길이 1 될때까지 반복

    else :
        pivot = div_arr[0] # 왼쪽을 피봇으로
        left, right = [], []

        for i in range(1, len(div_arr)) :
            if div_arr[i] < pivot : # 작으면 left에
                left.append(div_arr[i])
            else :
                right.append(div_arr[i])
        return [*quick_sort(left), pivot, *quick_sort(right)] # 퀵소트 다시 호출

T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    arr = list(map(int, input().split()))
    result = quick_sort(arr)
    print(result)