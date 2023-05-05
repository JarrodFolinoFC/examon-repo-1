from examon_core.quiz_item import quiz_item


@quiz_item(choices=[1, 2, 3, 4, 5, 6, 7], tags=['fa'])
def question_01():
    def a(array):
        return array[1]

    return a([1, 2, 3, 4, 5, 6, 7])


@quiz_item(choices=[1, 2, 3, 4, 5, 6, 7], tags=['fa'])
def question_01():
    def a(array):
        sorted(array)
        return array[-1]

    return a([1, 2, 3, 4, 5, 6, 7])


@quiz_item(choices=[1, 2, 3, 4, 5, 6, 7], tags=['fa'])
def question_01():
    def a(array):
        return [a for a in array]

    return a([1, 2, 3, 4, 5, 6, 7])


@quiz_item(choices=[1, 2, 3, 4, 5, 6, 7], tags=['fa'])
def question_01():
    def a(array):
        return [a for a in array if isinstance(a, int)]

    return a([1, 2, 3, '4', 5, 6, 7, None])[2]

@quiz_item(choices=[1, 2, 3, 4, 5, 6, 7], tags=['fa'])
def question_01():
    def filter(array):
        return [a for a in array if isinstance(a, int)]

    a = filter([1, 2, 3, '4', 5, 6, 7, None])
    sorted(a)
    return a[-2]

@quiz_item(choices=[1, 2, 3, 4, 5, 6, 7], tags=['fa'])
def question_01():
    def my_filter(array):
        return [a for a in array if isinstance(a, int)]

    def my_sort(a):
        sorted(a)

    a = my_filter([1, 2, 3, '4', 5, 6, 7, None])
    my_sort(a)
    return a[-3]