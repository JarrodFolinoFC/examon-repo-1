from examon_core.quiz_item import quiz_item


@quiz_item(choices=[1, 2, 3, 4, 5, 6], tags=['itertools'])
def question():
    from itertools import accumulate
    GFG = [5, 3, 6, 2, 1, 9, 1]
    iter = accumulate(GFG, max)
    next(iter)
    next(iter)
    return next(iter)


@quiz_item(choices=[1, 2, 3, 4, 5, 6], tags=['itertools'])
def question():
    from itertools import count
    iter = count(1, 3)
    next(iter)
    next(iter)
    return next(iter)


@quiz_item(choices=[1, 2, 3, 4, 5, 6], tags=['itertools'])
def question():
    from itertools import groupby
    return [list(i[1]) for i in groupby('12216')]


@quiz_item(choices=[1, 2, 3, 4, 5, 6], tags=['itertools'])
def question():
    from itertools import dropwhile
    return list(dropwhile(lambda x: x < 6, [1, 2, 2, 1, 6, 18, 9]))


@quiz_item(choices=[True, False], tags=['itertools'])
def question():
    import itertools
    gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
    return list(gen)

@quiz_item(choices=[True, False], tags=['itertools'])
def question():
    import itertools
    def vowel(c):
        return c.lower() in 'aeiou'

    return list(itertools.filterfalse(vowel, 'Aardvark'))

@quiz_item(choices=[True, False], tags=['itertools'])
def question():
    import itertools
    def vowel(c):
        return c.lower() in 'aeiou'

    return list(itertools.dropwhile(vowel, 'Aardvark'))

@quiz_item(choices=[True, False], tags=['itertools'])
def question():
    import itertools
    def vowel(c):
        return c.lower() in 'aeiou'

    return list(itertools.takewhile(vowel, 'Aardvark'))

@quiz_item(choices=[True, False], tags=['itertools'])
def question():
    import itertools

    return list(itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1)))

@quiz_item(choices=[True, False], tags=['itertools'])
def question():
    import itertools

    return list(itertools.islice('Aardvark', 4))

@quiz_item(choices=[True, False], tags=['itertools'])
def question():
    import itertools

    return list(itertools.islice('Aardvark', 4, 7))

@quiz_item(choices=[True, False], tags=['itertools'])
def question():
    import itertools

    return list(itertools.islice('Aardvark', 1, 7, 2))


@quiz_item(choices=[True, False], tags=['itertools'])
def question():
    import itertools
    sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
    return list(itertools.accumulate(sample))

@quiz_item(choices=[True, False], tags=['itertools'])
def question():
    import itertools
    sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
    return list(itertools.accumulate(sample, min))

@quiz_item(choices=[True, False], tags=['itertools'])
def question():
    import itertools
    sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
    return list(itertools.accumulate(sample, max))

@quiz_item(choices=[True, False], tags=['itertools'])
def question():
    import itertools
    import operator
    sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
    return list(itertools.accumulate(sample, operator.mul))

@quiz_item(choices=[True, False], tags=['itertools'])
def question():
    import itertools
    return list(itertools.groupby('LLLLAAGGG'))