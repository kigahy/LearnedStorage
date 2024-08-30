import sys
sys.stdin = open("input_5176.txt", "r")

T = int(input())

def myTree(value) :
    if value > N :
        return 0
    global count
    myTree(value*2)
    tree[value] = count
    count += 1
    myTree(value*2+1)

for tc in range(1, T+1) :
    N = int(input())
    tree_index = N+1
    tree = [0]*tree_index
    count = 1

    myTree(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')

'''  정석 코드. count 0으로 하고 count넣기 전에 +1 하는 것.
def myTree(value):
    if value > N:
        return 0
    global count
    myTree(value * 2)
    count += 1
    tree[value] = count
    myTree(value * 2 + 1)


for tc in range(1, T + 1):
    N = int(input())
    tree_index = N + 1
    tree = [0] * tree_index
    count = 0
'''

''' 시행착오
import sys
sys.stdin = open("input_5176.txt", "r")

T = int(input())

def myTree(value) :
    if value > N+1 : # 여기서부터 잘못됐다 노드 N개까지 되는데 먼 N+1인지...
        return 0
    global count
    myTree(value*2)
    tree[value] = count
    count += 1 # 1부터잖아. 음 그런데 위치가 잘못 된건가...?
    myTree(value*2+1)

for tc in range(1, T+1) :
    N = int(input())
    tree_index = N+1
    tree = [0]*tree_index
    count = 1

    myTree(1)

    print(tree[N//2])
'''