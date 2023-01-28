from topping import topping


def step1():
    step2()


def step2():
    step3()


def step3():
    step4()


def step4():
    step5()


@topping
def main(a, b):
    step1()
    return a + b


main(1, 4)
