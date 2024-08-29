#coordinate = [list(map(int, input().split())) for _ in range(4)]
#bool_index = [[0] * 100]*100 # 인덱스 당 면적 1로 계산할 빈 인덱스 선언
bool_index = [[0]*100 for _ in range(100)]

sum = 0

for x in range(4):
    col1, row1, col2, row2 = map(int, input().split())
    for i in range(col1, col2) :
        for j in range(row1, row2) :
            bool_index[j][i] = 1

for i in range(100) :
    for j in range(100) :
        sum += bool_index[j][i]

print(sum)

'''시행착오
bool_index = [[0]*100 for _ in range(100)]

boolean = False
sum = 0

for x in range(4):
    for i in range(coordinate[x][0], coordinate[x][2]) :
        for j in range(coordinate[x][1], coordinate[x][3]) :
            bool_index[j][i] = 1
'''
