from examon_core.quiz_item import quiz_item
@quiz_item(tags=['very_easy', 'string'])
def question_01():
    return 'hello'

@quiz_item(choices=[None, ''], tags=['very_easy', 'string'])
def question_01():
    return 'hello'

@quiz_item(param1=list(range(0, 5)), tags=['basic', 'input_parameter', 'very_easy', 'string'])
def question_04(param1):
    return 'hi there'[0:param1]

@quiz_item(choices=[None, ''], tags=['basic', 'very_easy', 'string'])
def question_01():
    return 'hello'[:1]