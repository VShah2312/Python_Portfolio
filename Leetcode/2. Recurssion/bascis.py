count = 1


def func():
    global count
    print(count)
    if count == 5:
        return
    count += 1
    func()


func()
