arr = ['A', 'B', 'C' ,'D' ,'E']
n = len(arr)

# 총 몇개의 bit가 1로 되어있는지 확인하는 함수
def get_count(tar) : # 하나의 부분집합인지 확인
    cnt = 0 # 최소 2명 이상을 고르기 위함. 1의 개수 셈
    for i in range(n) :
        if tar & 0x1 : # 하나하나 비트 옮기면서 1이면 출력
            # print(arr[i], end = ' ')
            cnt += 1
        tar << 1
    return cnt

result = 0
for tar in range(0, 1 << n) : # 존나틀림 arr만큼
    if get_count(tar) >= 2 : #bit가 2개 이상 1이라면,
        result += 1 # 1 이하인 것 빼도 됨

print(result)
