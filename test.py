from playwright.sync_api import expect

from Python_Project_practice.prac import result


def text_list():
    num_list([5,4,4,3])

def num_list(list1):
    num = list(dict.fromkeys(list1))
    return num

print(text_list())

[(5, 4, 4, 3), (5, 4, 5), (5, 2, 2, 4), (5, 2, 4)]



def str_tup(a,b,c,d):
    return a+b+c+d

@pytest_mark_parametarize([(5,4,4,3),(5,4,5),(5,2,2,4),(5,2,4)])
def test_cal("input, expected"):
    result = calcualte_result(*input)
    assert result == expected
