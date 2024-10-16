from libs._bridge import init, submit, close

NICKNAME = '통신테스트'
game_data = init(NICKNAME)

while game_data is not None:
    output = 'C'
    game_data = submit(output)
    break

close()