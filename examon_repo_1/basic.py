from examon_core.quiz_item import quiz_item
from examon_core.print_ext import print

@quiz_item(choices=[23], tags=['basic', 'very_easy', 'addition'])
def question_02():
    print('My first question')
    result = 2 + 3
    print(result)
    return result

@quiz_item(choices=[70, None], tags=['basic', 'very_easy', 'addition'])
def question_03():
    return 7 - 0

@quiz_item(choices=[70, 2, 8], tags=['basic', 'very_easy', 'addition'])
def question_03():
    return 7 - 4

@quiz_item(param1=list(range(0, 10)), tags=['basic', 'input_parameter', 'very_easy'])
def question_04(param1):
    return 7 - param1

