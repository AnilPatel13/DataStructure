def funcThree():
    print("This Function 3")


def funcTwo():
    funcThree()
    print("This is Function 2")


def funcOne():
    funcTwo()
    print("This is Function 1")


funcOne()
