from structures.stack import LinkedListStack


def _test_empty_stack():
    s = LinkedListStack()
    assert s.is_empty()
    assert len(s) == 0

    try:
        s.pop()
        assert False, "pop на пустом стеке должен кидать исключение"
    except IndexError:
        pass

    try:
        s.peek()
        assert False, "peek на пустом стеке должен кидать исключение"
    except IndexError:
        pass

    try:
        s.min()
        assert False, "min на пустом стеке должен кидать исключение"
    except IndexError:
        pass


def _test_push_pop_order_and_len():
    s = LinkedListStack()
    s.push(1)
    s.push(2)
    s.push(3)

    assert not s.is_empty()
    assert len(s) == 3
    assert s.peek() == 3

    assert s.pop() == 3
    assert len(s) == 2
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()
    assert len(s) == 0


def _test_min_behavior():
    s = LinkedListStack()
    s.push(3)
    assert s.min() == 3

    s.push(5)
    assert s.min() == 3  # минимум не меняется

    s.push(2)
    assert s.min() == 2  # новый минимум

    s.push(2)
    assert s.min() == 2  # минимум тот же

    s.push(4)
    assert s.min() == 2  # 4 не влияет на минимум

    # теперь начинаем pop и проверяем, как меняется минимум
    assert s.pop() == 4
    assert s.min() == 2

    assert s.pop() == 2
    assert s.min() == 2  # ещё один 2 остался

    assert s.pop() == 2
    assert s.min() == 3  # оба минимальных 2 ушли, минимум стал 3

    assert s.pop() == 5
    assert s.min() == 3

    assert s.pop() == 3
    assert s.is_empty()


def _run_all_tests():
    _test_empty_stack()
    _test_push_pop_order_and_len()
    _test_min_behavior()
    print("All LinkedListStack tests passed!")


if __name__ == "__main__":
    _run_all_tests()