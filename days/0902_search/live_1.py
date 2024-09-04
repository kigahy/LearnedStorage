def iter(start, end):
    global first
    global second

    second += 1
    print(first, second)
    iter(first, second)


first = 0
second = 0

iter(first, second)