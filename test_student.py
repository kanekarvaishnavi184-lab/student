import pytest
from main import calculate_grade


@pytest.mark.parametrize(
    "average, expected",
    [
        (95, "S"),
        (85, "A"),
        (70, "B"),
        (55, "C"),
        (45, "D"),
        (35, "F"),
        (89.9, "A"),
        (64.9, "C"),
    ],
)
def test_calculate_grade(average, expected):
    assert calculate_grade(average) == expected
