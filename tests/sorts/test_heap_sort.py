import pytest
from src.sorts.heap_sort import heap_sort
from src.errors import NonIntegerArgumentError


def test_empty_list():
    assert heap_sort([]) == []


def test_single_element():
    assert heap_sort([7]) == [7]


def test_already_sorted():
    arr = [1, 2, 3, 4, 5]
    assert heap_sort(arr) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    arr = [5, 4, 3, 2, 1]
    assert heap_sort(arr) == [1, 2, 3, 4, 5]


def test_with_duplicates():
    arr = [3, 1, 2, 3, 1]
    assert heap_sort(arr) == [1, 1, 2, 3, 3]


def test_with_negative_numbers():
    arr = [0, -1, 5, -3, 2]
    assert heap_sort(arr) == [-3, -1, 0, 2, 5]


def test_with_large_numbers():
    arr = [10**6, 5, 10**3, 0, -10**5]
    assert heap_sort(arr) == sorted(arr)


def test_random_examples():
    arr1 = [11, 3, 7, 0, -2, 5]
    arr2 = [100, 1, 50, -10, 0, 50]
    assert heap_sort(arr1) == sorted(arr1)
    assert heap_sort(arr2) == sorted(arr2)


def test_error_on_non_int():
    with pytest.raises(NonIntegerArgumentError):
        heap_sort([1, 2.5, 3])

    with pytest.raises(NonIntegerArgumentError):
        heap_sort([1, "2", 3])


def test_original_unchanged():
    arr = [4, 1, 3, 2]
    original = arr.copy()
    result = heap_sort(arr)
    assert arr == original
    assert result == [1, 2, 3, 4]