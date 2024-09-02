# 시작조건, 종료조건 중요
# 0에서 시작, 6에서 종료

# def func(start, end) :
#     print(start)
#     start += 1
#
#     if start < end :
#         start += 1
#         print(start)
#         func(start, end)
#     else :
#         start -= 1
#         print(start)
#         func(start, end)
#
# func(0, 6)


def func1(start, end) :
    if start > end :
        return
    print(start, end=' ')
    start += 1
    func1(start, end)

def func2(end, start) :

    if end<start :
        return
    print(end,  end=' ')
    end -= 1
    func2(end, start)

start = 0
end = 6

func1(start, end)
func2(end, start)
