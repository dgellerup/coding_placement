
import pytest

@pytest.fixture(scope="function")
def fruit_list():
    return ['apples', 'banana', 'apple', 'pear', 'mango', 'pear', 'watermelon', 'banana', 'apple']

@pytest.fixture(scope="function")
def color_list():
    return ['green', 'red', 'blue', 'brown', 'green', 'green', 'yellow', 'blue', 'orange', 'red']

@pytest.fixture(scope="function")
def test_file_1():
    return 'test_files/test_file_1.fasta'

@pytest.fixture(scope="function")
def test_file_2():
    return 'test_files/test_file_2.fasta'