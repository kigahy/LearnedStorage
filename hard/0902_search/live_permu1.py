def func(x) :
    if x == 2 :
        return

    for i in range(3) :
        path.append(i)
        func(x+1)
        path.pop()

path = []
func(0)

