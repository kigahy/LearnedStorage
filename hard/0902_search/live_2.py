def func(x) :
    x+= 1
x = 10
func(x)
print(x)
print()

def func2(x):
    x[0] = 1
x = [10]
func2(x)
print(x)
print()

def func3(x) :
    print(x)
    x += 1
    print(x)
x = 3
func3(x + 1) # 값을 더해서 파라미터로 던져준 것 뿐
print(x) # 원본이 바뀌지 않기 때문에 위 x는 5여도 여기는 3이다
print()

