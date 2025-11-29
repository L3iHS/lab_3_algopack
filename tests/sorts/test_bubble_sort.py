from src.sorts.bubble_sort import bubble_sort


def test_bubble_sort_empty():
    assert bubble_sort([]) == []


def test_bubble_sort_single_element():
    assert bubble_sort([42]) == [42]


def test_bubble_sort_already_sorted():
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_bubble_sort_reverse_order():
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_bubble_sort_with_duplicates():
    assert bubble_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]


def test_bubble_sort_with_negative_numbers():
    assert bubble_sort([0, -1, 5, -3, 2]) == [-3, -1, 0, 2, 5]


def test_bubble_sort_does_not_mutate_input():
    data = [3, 2, 1]
    original = data.copy()
    result = bubble_sort(data)

    assert data == original      # входной список не меняется
    assert result == [1, 2, 3]   # результат отсортирован