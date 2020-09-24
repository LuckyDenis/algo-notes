# coding: utf8
import pytest
import graph


@pytest.mark.graph
def test__prima_mst():
    GRAPH = {
        0: {1: 1, 2: 6, 3: 8},
        1: {0: 1, 2: 7, 5: 2, 6: 2},
        2: {0: 6, 1: 7, 4: 5, 5: 6, 6: 4},
        3: {0: 8},
        4: {2: 5},
        5: {1: 2, 2: 6, 6: 5, 7: 9},
        6: {1: 2, 2: 4, 5: 5, 7: 1},
        7: {5: 9, 6: 1}
    }
    START_VERTEX = 0
    COST = {0: 1, 1: 1, 2: 4, 3: 8, 4: 5, 5: 2, 6: 2, 7: 1}
    PATH = {0: 1, 1: 0, 2: 6, 3: 0, 4: 2, 5: 1, 6: 1, 7: 6}

    cost, path = graph.prima_mst(GRAPH, START_VERTEX)
    assert cost == COST
    assert PATH == PATH


@pytest.mark.graph
def test__dijkstra():
    GRAPH = {
        0: {4: 3},
        1: {0: 1, 2: 3, 3: 5},
        2: {0: 7, 1: 2},
        3: {1: 4, 5: 5, 7: 8},
        4: {2: 2, 6: 6},
        5: {6: 9},
        6: {7: 1},
        7: {}
    }
    START_VERTEX = 0
    COST = {0: 0, 1: 7, 2: 5, 3: 12, 4: 3, 5: 17, 6: 9, 7: 10}
    PATH = {0: -1, 1: 2, 2: 4, 3: 1, 4: 0, 5: 3, 6: 4, 7: 6}

    cost, path = graph.djs(GRAPH, START_VERTEX)
    assert cost == COST
    assert path == PATH
