

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci(10)


import pytest

@pytest.mark.parametrize("a", [1, 2, 3])
@pytest.mark.parametrize("b", [4, 5])
def test_multiplication(a, b):
    result = a * b
    print(f"Testing: {a} * {b} = {result}")
    assert result == a * b
