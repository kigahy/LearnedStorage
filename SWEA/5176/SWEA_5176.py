import sys
sys.stdin = open("input_5176.txt", "r")

T = int(input())

def node(num) :
    global count

    if num < V : # 노드 안의 값이 V값을 넘어서지 않을 때까지.
        node(num*2)
        count += 1 # 순서에 주의. 값 추가 전 1 추가!
        tree[num] = count
        node(num*2+1)

for i in range(1, T+1):
    N = int(input())
    V = N + 1
    tree = [0] * V
    count = 0
    node(1)

    print(tree[N//2])

'''
import sys
sys.stdin = open("input_5176.txt", "r")

T = int(input())

def node(num) :
    global count

    if num < V : # 노드 안의 값이 V값을 넘어서지 않을 때까지.
        node(tree[num*2])
        tree[num] = count
        count += 1
        node(tree[num*2+1])

for i in range(1, T+1):
    N = int(input())
    V = N + 1
    tree = [0] * V
    count = 0
    node(1)

    print(node[N//2])
'''


















'''이진탐색 첫 번째 공부. 이딴 것도 코드라고...ㅉㅉ
import sys
sys.stdin = open("input_5176.txt", "r")

def myTree(node) :
    tree[node] = node

    node(tree[i*2])

    node(tree[i*2+1])

for i in range(1, T+1) :
    N = int(input)
    V = N + 1 # 노드는 1부터 N+1까지
    tree = [0] * V

    val = myTree(1)

    print(f'#{tc} {val}')
'''