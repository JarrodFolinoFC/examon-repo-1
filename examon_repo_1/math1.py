from examon_core.quiz_item import quiz_item


from math import ceil, floor, trunc, factorial, hypot, sqrt


@quiz_item(choices=[1,2,3,4,5], tags=['math'])
def question():
    return 1 + 3


@quiz_item(choices=[1,2,3,4,5, 13], tags=['julian'])
def question():
    return 1 + 3 * 4

@quiz_item(choices=[1,2,3,4,5], tags=['math'])
def question():
    from math import sqrt
    return sqrt(9)


@quiz_item(choices=[1,2,3,4,5], tags=['math'])
def question():
    from math import floor
    return floor(9.6665456456)



@quiz_item(choices=[1,2,3,4,5], tags=['math'])
def question():
    from math import ceil
    return ceil(9.6665456456)


@quiz_item(choices=[], tags=['math'])
def question():
    from math import trunc
    return trunc(9.6665456456)


@quiz_item(choices=[], tags=['math'])
def question():
    from math import hypot
    return hypot(5, 10)


@quiz_item(choices=[], tags=['math'])
def question():
    from math import factorial
    return factorial(9)
