import pytest

@pytest.fixture
def inc():
    return 1

def test_answer(inc):
    assert inc == 4

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_resversd():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }