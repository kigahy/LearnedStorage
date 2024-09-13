import sys
sys.stdin = open("input_1220.txt", "r")
T = 10

for tc in range(1, T+1) :
    N = int(input()) # 행 열 길이
    matrix = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for i in range (N) :
        for j in range(N) :
            if matrix[i][j] == 1 : # 현재가 1이라면 (내려가야함
                if i + 1 >= N : #아래쪽이 인덱스 범위 벗어나면
                    matrix[i][j] = 0 #
                elif matrix[i+1][j] == 0 : # 아래쪽이 0이라면(이동할 수 있다면)
                    matrix[i][j] = 0 # 현재를 0으로 만들고
                    matrix[i+1][j] = 1 # 아래쪽을 1로 만듦
                elif matrix[i+1][j] == 2 : # 아래쪽이 2라면 (충돌한다면)
                    count += 1 # 교착상태이므로 카운트 증가

            # elif matrix[i][j] == 2 : # 현재가 2라면 (올라가야함
            #     if i >= 0 : # 위쪽이 인덱스 범위 벗어나면. 참고: i - 1 < 0 로 적어서 2시간동안 오류 찾음. 이것저것 시도해보다 얻어걸린건데 왜 된건지 모르겠으니까 코드리뷰 도와주세요 ㅠㅠ i + 1 > 0 도 가능
            #         matrix[i][j] = 0 # 그자리 0으로 만듦
            #     elif matrix[i-1][j] == 0 : # 위쪽이 0이라면 (이동할 수 있다면)
            #         matrix[i][j] = 0 # 현재를 0으로 만들고
            #         matrix[i-1][j] = 2 # 위쪽을 2로 만듦
            #     elif matrix[i-1][j] == 1 : # 위쪽이 1이라면 (충돌한다면)
            #         count += 1 # 교착상태이므로 카운트 증가
            #
            # elif matrix[i][j] == 0: # 현재가 0이라면
            #     continue # 다음 열로 이동

    print(f'#{tc} {count}')