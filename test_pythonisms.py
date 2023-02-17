import time
import pytest
from pythonisms import read_lines


# example 1 - generator function

def test_read_lines():
    filename = "example.txt"
    expected_lines = ["Hello", "World", "!"]

    with open(filename, "w") as f:
        f.write("\n".join(expected_lines))

    actual_lines = list(read_lines(filename))
    assert actual_lines == expected_lines, f"Expected {expected_lines}, but got {actual_lines}"


