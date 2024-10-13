import sys
sys.stdin = open('input.txt')

T = int(input())

def enqueue(target) : # 매개변수와 저장된 값을 비교하며 정렬
    while target // 2 :
        parent = target//2
        if tree[target] <= tree[parent] :
            tree[target], tree[parent] = tree[parent], tree[target]
        target = parent

for tc in range(1, T+1) :
    N = int(input())
    lst = map(int, input().split())

    tree = [0]
    last = 0

    for item in lst: # 리스트 값 하나씩 돌며 정렬 함수에 넣음
        tree.append(item)
        last += 1
        enqueue(last)

    result = 0
    while last :
        parent = last // 2
        result += tree[parent]
        last = parent

    print(result)