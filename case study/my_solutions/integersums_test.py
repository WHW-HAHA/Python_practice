import pytest

def setup_function():
    print("start...")

def teardown_function():
    print("finished...")

@pytest.fixture(scope="function")
def sum_up(request):
    try:
        list_num = list(range(0, int(request.param) + 1))
    except:
        list_num = [0]
    return sum(list_num)

@pytest.mark.parametrize("sum_up", ["somthing"], indirect=True)
def test_string(sum_up):
    print('running case 1')
    assert sum_up == 0

@pytest.mark.parametrize("sum_up",  [0, 1, 2, 3], indirect=True)
def test_num(sum_up):
    print('running case 2')
    print(sum_up)

@pytest.mark.parametrize("sum_up",  [-10], indirect=True)
def test_negative(sum_up):
    print('running case 3')
    assert sum_up == 0



