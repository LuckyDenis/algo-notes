# coding: utf8

import pytest
import structs


@pytest.mark.structs
def test__linked_list():
    DATA = [1, 2, 3, 4, 5]
    INDEX = 1

    ll = structs.LinkedList()
    for d in reversed(DATA):
        ll.push(d)

    assert len(ll) == len(DATA)
    assert list([d for d in ll]) == DATA
    assert ll[INDEX] == DATA[INDEX]

    for d in DATA:
        assert ll.pop() == d

    assert ll.len == 0
