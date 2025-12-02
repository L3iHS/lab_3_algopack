import pytest
from src.sorts.bucket_sort import bucket_sort
from src.errors import NonNumericElementError, InvalidParameterError


def test_empty_list():
    assert bucket_sort([]) == []


def test_single_element():
    assert bucket_sort([3.14]) == [3.14]


def test_already_sorted_integers():
    arr = [1, 2, 3, 4, 5]
    assert bucket_sort(arr) == [1, 2, 3, 4, 5]


def test_reverse_sorted_integers():
    arr = [5, 4, 3, 2, 1]
    assert bucket_sort(arr) == [1, 2, 3, 4, 5]


def test_with_floats():
    arr = [0.5, 0.1, 0.9, 0.3, 0.7]
    assert bucket_sort(arr) == sorted(arr)


def test_mixed_int_and_float():
    arr = [1.5, 2, 0.5, 3, 2.5]
    assert bucket_sort(arr) == sorted(arr)


def test_with_duplicates():
    arr = [3.0, 1.0, 2.0, 1.0, 3.0]
    assert bucket_sort(arr) == [1.0, 1.0, 2.0, 3.0, 3.0]


def test_all_equal_values():
    arr = [2.2, 2.2, 2.2, 2.2]
    assert bucket_sort(arr) == [2.2, 2.2, 2.2, 2.2]


def test_original_unchanged():
    arr = [3.2, 1.1, 4.8, 2.0]
    original = arr.copy()
    result = bucket_sort(arr)
    assert arr == original
    assert result == sorted(arr)


def test_invalid_element_type():
    with pytest.raises(NonNumericElementError):
        bucket_sort([1.0, "2.0", 3.0])


def test_invalid_buckets_param_type():
    arr = [0.1, 0.2, 0.3]
    with pytest.raises(InvalidParameterError):
        bucket_sort(arr, buckets=1.5)
    with pytest.raises(InvalidParameterError):
        bucket_sort(arr, buckets="10")


def test_invalid_buckets_param_value():
    arr = [0.1, 0.2, 0.3]
    with pytest.raises(InvalidParameterError):
        bucket_sort(arr, buckets=0)
    with pytest.raises(InvalidParameterError):
        bucket_sort(arr, buckets=-5)


def test_custom_buckets_param():
    arr = [0.9, 0.1, 0.5, 0.7, 0.3]
    expected = sorted(arr)
    assert bucket_sort(arr, buckets=2) == expected
    assert bucket_sort(arr, buckets=10) == expected