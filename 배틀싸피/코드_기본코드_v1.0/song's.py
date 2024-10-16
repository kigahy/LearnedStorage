from libs._bridge import init, submit, close
from collections import deque

NICKNAME = '부울경_1반_송동현'
game_data = init(NICKNAME)


# 입력 데이터 분류
char_to_int = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
map_data = [[]]  # 맵 정보. 예) map_data[0][1] - [0, 1]의 지형/지물
allies = {}  # 아군 정보. 예) allies['A'] - 플레이어 본인의 정보
enemies = {}  # 적군 정보. 예) enemies['X'] - 적 포탑의 정보
codes = []  # 주어진 암호문. 예) codes[0] - 첫 번째 암호문

# 입력 데이터를 파싱하여 변수에 저장
def parse_data(game_data):
    # 입력 데이터를 행으로 나누기
    game_data_rows = game_data.split('\n')
    row_index = 0

    # 첫 번째 행 데이터 읽기
    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0])  # 맵의 세로 크기
    map_width = int(header[1])  # 맵의 가로 크기
    num_of_allies = int(header[2])  # 아군의 수
    num_of_enemies = int(header[3])  # 적군의 수
    num_of_codes = int(header[4])  # 암호문의 수
    row_index += 1

    # 기존의 맵 정보를 초기화하고 다시 읽어오기
    map_data.clear()
    map_data.extend([[ '' for c in range(map_width)] for r in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(0, map_width):
            map_data[i][j] = col[j]
    row_index += map_height

    # 기존의 아군 정보를 초기화하고 다시 읽어오기
    allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0)
        allies[ally_name] = ally
    row_index += num_of_allies

    # 기존의 적군 정보를 초기화하고 다시 읽어오기
    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0)
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    # 기존의 암호문 정보를 초기화하고 다시 읽어오기
    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])

# 방향 계산하는 함수
def get_direction(start,end):
    new_direction=[end[0]-start[0],end[1]-start[1]]
    if new_direction == [0,1]:
        return 'R'
    elif new_direction == [0,-1]:
        return 'L'
    elif new_direction == [1,0]:
        return 'D'
    elif new_direction == [-1,0]:
        return 'U'
    else:
        return 'S'

# 최소로 필요한 포탄수와 경로를 계산해주는 함수
def find_min_shoot(start):
    dxy=[[0,1],[1,0],[0,-1],[-1,0]]
    N = len(map_data) # 맵의 세로
    M = len(map_data[0]) # 맵의 가로
    q= deque()
    visited= [[[float('inf')]*2 for _ in range(M)] for _ in range(N)]
    visited[start[0]][start[1]]=[0,0]
    q.append((start[0],start[1],0,0,0,[]))

    while q:
        x,y,cnt,trees,tanks,xy_list=q.popleft()
        for dx, dy in dxy:
            nx = x +dx
            ny = y +dy
            if nx <0 or nx >=N or ny <0 or ny>=M: # 경로 벗어나는 함수
                continue
            new_tile=map_data[nx][ny]
            if new_tile == 'G': #풀을 만났으면
                if visited[nx][ny][0] > trees or (visited[nx][ny][0]== trees and visited[nx][ny][1] >tanks):
                    visited[nx][ny]=[trees,tanks]
                    q.append((nx,ny,cnt+1,trees,tanks,xy_list+[[nx,ny]]))
            elif new_tile == 'T': # 나무를 만났으면
                if visited[nx][ny][0] > trees+1 or (visited[nx][ny][0]== trees+1 and visited[nx][ny][1] >tanks):
                    visited[nx][ny]=[trees+1,tanks]
                    q.append((nx,ny,cnt+1,trees+1,tanks,xy_list+[[nx,ny]]))
            elif new_tile.startswith('E'): # 적탱크를 만났으면
                if visited[nx][ny][0] > trees or (visited[nx][ny][0]== trees and visited[nx][ny][1] >tanks+1):
                    visited[nx][ny]=[trees,tanks+1]
                    q.append((nx,ny,cnt+1,trees,tanks+1,xy_list+[[nx,ny]]))
            elif new_tile == 'X': # 적포탑을 찾았으면
                return [trees,tanks], xy_list+[[nx,ny]]
    return [-1,-1], []

def trans_code(code): # 암호 해독 코드
    text=''
    for c in code:
        new_text= chr((ord(c)-65+9)%26+65)
        text +=new_text
    return text

def find_min_supply(start): #가장가까운 보급 창고를 찾는 함수
    dxy=[[0,1],[1,0],[0,-1],[-1,0]]
    N = len(map_data) # 맵의 세로
    M = len(map_data[0]) # 맵의 가로
    q= deque()
    visited= [[[0]*(my_tan+1) for _ in range(M)] for _ in range(N)]
    visited[start[0]][start[1]][my_tan]=1
    q.append((start[0],start[1],0,0,[]))

    while q:
        x,y,cnt,block,xy_list=q.popleft()
        for dx, dy in dxy:
            nx = x +dx
            ny = y +dy
            if nx <0 or nx >=N or ny <0 or ny>=M: # 경로 벗어나는 함수
                continue
            new_tile=map_data[nx][ny]
            if new_tile == 'G': #풀을 만났으면
                visited[nx][ny][block]=1
                q.append((nx,ny,cnt+1,block,xy_list+[[nx,ny]]))
            elif new_tile == 'T': # 나무를 만났으면
                if block and visited[nx][ny][block-1]==0:
                    visited[nx][ny][block-1]=1
                    q.append((nx,ny,cnt+1,block-1,xy_list+[[nx,ny]]))
            elif new_tile == 'F': # 적포탑을 찾았으면
                return xy_list+[[nx,ny]]
    return []



# while 반복문: 배틀싸피 메인 프로그램과 클라이언트(이 코드)가 데이터를 계속해서 주고받는 부분
while game_data is not None:
    # 자기 차례가 되어 받은 게임정보를 파싱
    print(f'----입력데이터----\n{game_data}\n----------------')
    parse_data(game_data)

    # 파싱한 데이터를 화면에 출력하여 확인
    print(f'\n[맵 정보] ({len(map_data)} x {len(map_data[0])})')
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            print(f'{map_data[i][j]} ', end='')
        print()

    print(f'\n[아군 정보] (아군 수: {len(allies)})')
    for k, v in allies.items():
        if k == 'A':
            print(f'A (내 탱크) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 대전차 포탄: {v[3]}개')
        elif k == 'H':
            print(f'H (아군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (아군 탱크) - 체력: {v[0]}')

    print(f'\n[적군 정보] (적군 수: {len(allies)})')
    for k, v in enemies.items():
        if k == 'X':
            print(f'H (적군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (적군 탱크) - 체력: {v[0]}')

    print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
    for i in range(len(codes)):
        print(codes[i])


   
    output = 'S'  # 알고리즘 결괏값이 없을 경우를 대비하여 초기값을 S로 설정

    # 유닛들 위치 파악하기
    my_position = [-1, -1]
    my_H=[-1,-1]
    en_position = []
    en_X =[-1,-1]
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if map_data[i][j] == 'A':
                my_position[0] = i
                my_position[1] = j  
            elif map_data[i][j] == 'H': # 내포탑 발견시
                my_H[0]=i
                my_H[1]=j
            elif map_data[i][j].startswith('E'):
                en_position.append([i,j])
            elif map_data[i][j]== 'X':
                en_X[0]=i
                en_X[1]=j

    # 내 탱크가 적 포탑을 파괴하기 위해 필요한 포탄 수 구하기
    min_shoot,route = find_min_shoot(my_position)
    print(f'최소경로로 가기 위해 필요한 일반 포탄 수 : {min_shoot[0]}, 대전차 포탄 수: {min_shoot[1]}')
    # print(route)
    my_tan = int(allies['A'][2]) # 현재 일반 포탄 수
    my_big_tan = int(allies['A'][3]) # 현재 대전차 포탄 수
    
    if my_tan -1 >= min_shoot[0] and my_big_tan >= min_shoot[1]: # 탄이 충분하거나 장애물이 없다면
        if len(route) >0:
            for next_position in route:
                new_tile=map_data[next_position[0]][next_position[1]]
                direction=get_direction(my_position, next_position)
                if new_tile =='T': # 나무를 만난다면
                    if my_tan > 0: # 탄이 있으면
                        output = f'{direction} F M' # 일반 포탄 발사
                    break
                elif new_tile.startswith('E'): # 적탱크를 만난다면
                    if my_big_tan >0:
                        output = f'{direction} F S' # 대전차 포탄 발사
                    break
                elif new_tile=='X': # 적포탑이라면
                    if my_tan >0: 
                        output = f'{direction} F M' # 일반 포탄 발사
                    break
                elif new_tile=='G': # 풀이라면
                    output = f'{direction} A' 
                    break
                else:
                    output ='S'
                    break

    else: # 아직 탄이 충분하지 않다면 
        supply_route = find_min_supply(my_position)
        print(supply_route)
        if len(supply_route) >0:
            for next_position in supply_route:
                direction=get_direction(my_position, next_position)
                if codes: # 보급시설과 인접해서 암호문을 받았으면
                    for code in codes:
                        word =trans_code(code)
                        print(word)
                        output= f'{direction} G {word}'
                        # output= f'G {word}'
                        break
                else: # 아직 이동해야 한다면
                    output = f'{direction} A'
                    break
                

    # while 문의 끝에는 다음 코드가 필수로 존재하여야 함
    # output에 담긴 값은 submit 함수를 통해 배틀싸피 메인 프로그램에 전달
    game_data = submit(output)


# 반복문을 빠져나왔을 때 배틀싸피 메인 프로그램과의 연결을 완전히 해제하기 위해 close 함수 호출
close()