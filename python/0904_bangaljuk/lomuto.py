def lomuto_partition(left, right) : # 호어와 같지만 파티셔닝이 다름
    idx = left - 1 # idx는 조사대상. -1은 모든 상황에 대해 동일하게 코드 작성. 에러 안남
    pivot = arr[right] # lomuto 방식은 for문으로 처리함. 왼 -> 오까지 조사해나가기 때문.

    # pivot을 오른쪽에 둠. left right는 범위일 뿐이고 next와 p로 조사함
    for next in range(left, right) : # 왼부터 오까지. right번째:pivot. pivot은 안들어감
        if arr[next] < pivot : # 피봇보다 next 값이 작으면 인덱스를 증가시킴
            idx += 1
            arr[idx], arr[next] = arr[next], arr[idx]
            # 조사하다가 next값이 pivot보다 큰 값을 발견할 때까지 idx 증가 안함
            # next 값이 pivot보다 작은 경우가 발생하면 idx를 1 증가시키고 idx와 next를 swap
            # next는 p보다 작은애 찾음
            # idx는 p보다 큰 애 찾음
            # 그러면 오름차순으로 됨

            # for문이 종료된 시점 기준, idx가 가리키고 있는 대상은 pivot보다 작은 값
            # idx보다 오른쪽은 무조건 pivot보다 큰 값이 있을 것
            # 이후 idx를 오른쪽으로 한 칸 옮김
            # pivot과 idx를 swap

    arr[idx + 1], arr[right] = arr[right], arr[idx + 1]
    return idx + 1 # 그 인덱스 번호값을 기준으로 다시 quick sort






def quick_sort(left, right) :
    if left < right :
        pivot_idx = lomuto_partition(left, right)

        quick_sort(left, pivot_idx - 1)
        quick_sort(pivot_idx + 1, right)


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(0, len(arr)-1)