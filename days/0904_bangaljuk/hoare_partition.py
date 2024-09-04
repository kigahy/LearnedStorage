# left : 왼쪽 정렬 대상 시작 지점
# right : 오른쪽 정렬 대상 시작 시점

def hoare_partition(left, right) : # 호어 방식의 배열조개기. 개념적으로 배운 quick sort
    pivot = arr[left] # left의 한 칸 앞에서 잡음.
    left += 1

    while True : # 조사시작.
        while left <= right and arr[left] < pivot : # l ind가 r id보다 작고 그 l번째 값이 p보다 작다면
            left += 1 # 멈춘 기준은 p보다 큰 애

        while left <= right and arr[right] > pivot :# 그 반대
            right -= 1 # 멈춘 기준은 p보다 작은 애

        if left >= right : # 바뀌면 안되는 자리가 엇갈렸다면 right를 리턴함
            return right # 이것을 pivot_index로 사용

        # 그렇다면 무조건 left는 right보다 큰 지점에 있을 수밖에 없음. swap
        arr[left], arr[right] = arr[right], arr[left]

def quick_sort(left, right) :
    if left >= right : return # 조사 대상이 하나 이사가 된다면 더이상 조사 불가
    # 호어 방식의 파티션 구분 결과로 얻은 인덱스를 p로 봄

    pivot_index = hoare_partition(left, right) # 어떠한 함수를 통하여 피봇 정보를 도출해냄
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
    # print(arr)

    quick_sort(left, pivot_index -1)
    quick_sort(pivot_index + 1, right)


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(0, len(arr)-1)
print(arr)