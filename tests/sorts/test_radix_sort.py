import pytest
from src.sorts.radix_sort import radix_sort
from src.errors import NonIntegerArgumentError, NegativeArgumentError, InvalidParameterError


def test_empty_list():
    assert radix_sort([]) == []


def test_single_element():
    assert radix_sort([7]) == [7]


def test_already_sorted():
    assert radix_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_reverse_sorted():
    assert radix_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_with_duplicates():
    assert radix_sort([5, 1, 3, 1, 2, 5]) == [1, 1, 2, 3, 5, 5]


def test_with_zeros():
    assert radix_sort([0, 5, 0, 3]) == [0, 0, 3, 5]


def test_large_numbers():
    assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]


def test_random_examples():
    assert radix_sort([11, 3, 101, 56, 0, 7]) == sorted([11, 3, 101, 56, 0, 7])
    assert radix_sort([1000, 1, 10, 100]) == [1, 10, 100, 1000]


def test_error_non_int():
    with pytest.raises(NonIntegerArgumentError):
        radix_sort([1, "2", 3])

    with pytest.raises(NonIntegerArgumentError):
        radix_sort([1, 2.5, 3])


def test_error_negative_values():
    with pytest.raises(NegativeArgumentError):
        radix_sort([1, -5, 2])


def test_original_unchanged():
    arr = [17, 3, 9, 0]
    original = arr.copy()
    radix_sort(arr)
    assert arr == original


def test_radix_base_2():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert radix_sort(arr, base=2) == sorted(arr)


def test_radix_base_16():
    arr = [15, 1, 255, 16, 32, 7, 128]
    assert radix_sort(arr, base=16) == sorted(arr)


def test_radix_different_bases_same_result():
    arr = [0, 5, 10, 3, 7, 100, 42]
    expected = sorted(arr)
    assert radix_sort(arr, base=10) == expected
    assert radix_sort(arr, base=2) == expected
    assert radix_sort(arr, base=8) == expected


def test_invalid_base():
    arr = [1, 2, 3]
    with pytest.raises(InvalidParameterError):
        radix_sort(arr, base=1)
    with pytest.raises(InvalidParameterError):
        radix_sort(arr, base=0)