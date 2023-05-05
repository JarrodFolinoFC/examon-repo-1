from examon_core.quiz_item import quiz_item

@quiz_item(choices=[], tags=['built in functions'])
def question_01():
    return type(hash((10, 'alpha', (1, 2))))


def question_02():
    return type(hash((10, 'alpha', [1, 2])))

@quiz_item(choices=[], tags=['sets'])
def question_04():
    x = {"apple", "banana", "cherry"}
    try:
        hash(x)
    except Exception:
        return 'error'
    return 'ok'


@quiz_item(choices=[], tags=['sets'])
def question_05():
    x = frozenset(["apple", "banana", "cherry"])
    try:
        hash(x)
    except Exception:
        return 'error'
    return 'ok'