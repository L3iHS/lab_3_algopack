from src.sorts.quick_sort import quick_sort
import pytest


def test_quick_sort_empty():
    assert quick_sort([]) == []


def test_quick_sort_single_element():
    assert quick_sort([42]) == [42]


def test_quick_sort_already_sorted():
    assert quick_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_quick_sort_reverse_order():
    assert quick_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_quick_sort_with_duplicates():
    assert quick_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]


def test_quick_sort_with_negative_numbers():
    assert quick_sort([0, -1, 5, -3, 2]) == [-3, -1, 0, 2, 5]


def test_quick_sort_mixed_numbers():
    assert quick_sort([10, -5, 0, 3, -5, 3]) == [-5, -5, 0, 3, 3, 10]


def test_quick_sort_does_not_mutate_input():
    original = [3, 1, 2, 3]
    copy_original = original.copy()
    quick_sort(original)
    assert original == copy_original