from examon_core.quiz_item import quiz_item

@quiz_item(choices=[True, False], tags=['generators'])
def question():
    def gen_123():
        yield 1
        yield 2
        yield 3

    g = gen_123()
    return next(g), next(g), next(g)


@quiz_item(choices=[True, False], tags=['generators'])
def question():
    import re
    RE_WORD = re.compile(r'\w+')

    class Sentence:
        def __init__(self, text):
            self.text = text

        def __iter__(self):
            for match in RE_WORD.finditer(self.text):
                yield match.group()

    i = iter(Sentence('the quick brown fox'))
    return next(i)

@quiz_item(choices=[True, False], tags=['generators'])
def question():
    def aritprog_gen(begin, step, end=None):
        result = type(begin + step)(begin)
        forever = end is None
        index = 0
        while forever or result < end:
            yield result
            index += 1
            result = begin + step * index

    i = aritprog_gen(0.5, 1)
    return next(i), next(i)



@quiz_item(choices=[True, False], tags=['generators'])
def question():
    def vowel(c):
        return c.lower() in 'aeiou'

    return list(filter(vowel, 'Aardvark'))


@quiz_item(choices=[True, False], tags=['generators'])
def question():
    return (
        all([1, 2, 3]),
        any([1, 2, 3]),
    )

@quiz_item(choices=[True, False], tags=['generators'])
def question():
    def sub_gen():
        yield 1.1
        yield 1.2

    def gen():
        yield 1
        for i in sub_gen():
            yield i
        yield 2

    i = iter(gen())
    return [next(i), next(i), next(i), next(i)]

@quiz_item(choices=[True, False], tags=['generators'])
def question():
    def sub_gen():
        yield 1.1
        yield 1.2

    def gen():
        yield 1
        for i in sub_gen():
            yield i
        yield 2

    i = iter(gen)
    return [next(i), next(i), next(i), next(i)]

@quiz_item(choices=[True, False], tags=['generators'])
def question():
    from collections.abc import Iterable
    FromTo = tuple[str, str]

    def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
        for from_, to in changes:
            text = text.replace(from_, to)
        return text

    return zip_replace('abadeaghij', [('a', 'b'), ('b', 'a')])


@quiz_item(choices=[], tags=['generators'])
def question():
    def check_name_exists():
        names = ["Dennis", "Nick", "Fury", "Tony", "Stark"]
        while True:
            name = yield
        if name in names:
            Global.push(f'{name}')
        else:
            Global.push(f'-{name}')

    coro = check_name_exists()
    coro.send(None)
    coro.send('Nick')
    result = coro.send('Nick')
    return result
