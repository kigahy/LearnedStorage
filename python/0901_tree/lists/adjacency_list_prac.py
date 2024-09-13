import sys
sys.stdin = open('input_adja.txt')

N = int(input())
lst = list(map(int, input().split()))
arr = [[] for _ in range(N+1)]

def DFS(start) :
    s = start

    if start == -1 :
        return

    DFS(arr[s][0]) # 자식의 왼쪽 값을 재귀로
    ino.append(s) #
    DFS(arr[s][1]) # 자식의 오른쪽 값을 재귀로


for i in range(N-1) :
    p = lst[i*2]
    c = lst[i*2+1]
    arr[p].append(c)

for i in range(N+1) :
    while len(arr[i]) < 2 : # 자식노드가 없거나 하나인 경우
        arr[i].append(-1) # -1 채워줌


pre = []
ino = []
pos = []

DFS(1)

print(pre)
print(ino)
print(pos)

