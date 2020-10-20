# coding: utf8
import pytest
from structs.map_reduce import Queue
from structs.map_reduce import Map
from structs.map_reduce import Reduce


"""
resource 	date 
index 		Jan 20 2010 4:30 
index 		Jan 20 2010 5:30 
about 		Jan 20 2010 6:00 
index 		Jan 20 2010 7:00 
about 		Jan 21 2010 8:00 
about 		Jan 21 2010 8:30 
index 		Jan 21 2010 8:30 
about 		Jan 21 2010 9:00 
index 		Jan 21 2010 9:30 
index 		Jan 22 2010 5:00 
"""


HITS = [
    ["index", 2010, 1, 20],
    ["index", 2010, 1, 20],
    ["about", 2010, 1, 20],
    ["index", 2010, 1, 20],
    ["about", 2010, 1, 21],
    ["about", 2010, 1, 21],
    ["index", 2010, 1, 21],
    ["about", 2010, 1, 21],
    ["index", 2010, 1, 21],
    ["index", 2010, 1, 22]
]

CORRECT = {
    "['index', 2010, 1, 20]": 3,
    "['about', 2010, 1, 20]": 1,
    "['about', 2010, 1, 21]": 3,
    "['index', 2010, 1, 21]": 2,
    "['index', 2010, 1, 22]": 1
}


@pytest.mark.structs
def test__map_reduce():
    queue_st = Queue()
    queue_st.make(HITS)

    map_st = Map()
    map_st.emit(queue_st.storage)

    reduce_st = Reduce()
    reduce_st.merge(map_st.storage)

    result = reduce_st.storage
    assert result == CORRECT
