from examon_core.quiz_item import quiz_item


@quiz_item(choices=[], tags=['dunder'])
def question_08():
    from functools import reduce

    def factorial(n):
        return reduce(lambda a, b: a * b, range(1, n + 1))

    return factorial(3)


@quiz_item(choices=[], tags=['dunder'])
def question_09():
    from functools import reduce

    def add_together(nums):
        return reduce(lambda a, b: a + b, nums)

    return add_together([1, 2, 3, 4, 5, 6])


@quiz_item(choices=[], tags=['dunder'])
def question_10():
    from functools import reduce
    from operator import mul

    def factorial(n):
        return reduce(mul, range(1, n + 1))

    return factorial(3)