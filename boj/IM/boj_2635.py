first = int(input())
num_lst = []

for second in range(1, 30001) : # 뺄셈할 첫 번째 수를 반복
    temp_lst = []
    third = 0
    temp_lst.append(first)
    i = 1
    while third >= 0 :
        third = first - second #
        temp_lst.append(second) # third는 음수가 될 수 있기 때문에 second를 결과 리스트에 저장
        first = second # 뺄셈할 대상 숫자가 다음 숫자로 넘어감
        second = third # 첫째에서 뺄 값도 다음 숫자로 넘어감

        i += 1
    if len(num_lst) < len(temp_lst) :
        num_lst = []
        num_lst = temp_lst
    print(len(num_lst))
    print(*num_lst)


''' 안됨1
first = int(input())
second = 62
lst = [0]*30000
val = 0
lst[0] = first
i = 1

while val >= 0 :
    val = first - second
    lst[i] = second

    first = second
    second = val

    i += 1

print(i)
print(*lst[:i])
'''

'''안됨2 append로 푸는 법
first = int(input())
second = 60
lst = []
val = 0
i = 1
lst.append(first)

while val >= 0 :
    val = first - second
    lst.append(second)

    first = second
    second = val
    i += 1

print(i)
print(*lst)
'''