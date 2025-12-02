import pytest
from src.sorts.counting_sort import counting_sort
from src.errors import NonIntegerArgumentError


def test_empty_list():
    assert counting_sort([]) == []


def test_single_element():
    assert counting_sort([5]) == [5]


def test_already_sorted():
    assert counting_sort([1, 2, 3]) == [1, 2, 3]


def test_reverse_sorted():
    assert counting_sort([3, 2, 1]) == [1, 2, 3]


def test_with_duplicates():
    assert counting_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]


def test_with_negative_numbers():
    assert counting_sort([-1, -3, 0, 2, -1]) == [-3, -1, -1, 0, 2]


def test_all_equal():
    assert counting_sort([7, 7, 7]) == [7, 7, 7]


def test_mixed_large_range():
    assert counting_sort([-5, 10, 0, -2, 3]) == [-5, -2, 0, 3, 10]


def test_type_error_on_non_int():
    with pytest.raises(NonIntegerArgumentError):
        counting_sort([1, 2, 3.5])

    with pytest.raises(NonIntegerArgumentError):
        counting_sort([1, "2", 3])


def test_original_unchanged():
    arr = [3, 1, 2]
    original = arr.copy()
    counting_sort(arr)
    assert arr == original