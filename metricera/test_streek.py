#!/usr/bin/python3 

from . import Date, WINTUARY, Streek

def test_streekday():
    date = Date(0, WINTUARY, 1)
    wd = date.streekday
    assert(wd == Streek.MUDDAY)
    for d in range(3652422 * 2):
        nd = date.next()
        assert(nd.streekday == (wd + 1) % 10)
        date = nd
        wd = nd.streekday
