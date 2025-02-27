import pytest

# Define a fixture
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

# Test function using the fixture
def test_sum(sample_data):
    assert sum(sample_data) == 15

# Another test function using the same fixture
def test_max(sample_data):
    assert max(sample_data) == 5



@pytest.fixture
def simple_string():
    return "  Hello  World  "

def test_split(simple_string):
    String_split= simple_string.split()
    print(String_split)

def test_strip(simple_string):
    string_strip = simple_string.strip()
    print(string_strip)