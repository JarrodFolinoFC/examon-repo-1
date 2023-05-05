from examon_core.quiz_item import quiz_item



@quiz_item(choices=[True, None, {}], tags=['sets', 'very_easy'])
def question_01():
    l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
    return len(list(set(l)))


@quiz_item(choices=[{"apple", "banana", "cherry", "google", "microsoft"}],
           tags=['sets', 'very_easy'])
def question_02():
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    return x & y


@quiz_item(choices=[], tags=['sets', 'very_easy'])
def question_03():
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    return x | y


