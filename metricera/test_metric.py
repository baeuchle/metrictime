#!/usr/bin/python3 

from . import *
import datetime

def test_from_ce():
    cedate = datetime.date(2020, 12, 22)
    for d in range(1, 91):
        date = from_ce_date(cedate)
        assert(date.year == 9551)
        assert(date.season == WINTUARY)
        assert(date.day == d)
        cedate += datetime.timedelta(1)
    for d in range(1, 93):
        date = from_ce_date(cedate)
        assert(date.year == 9551)
        assert(date.season == LENTUARY)
        assert(date.day == d)
        cedate += datetime.timedelta(1)
    for d in range(1, 93):
        date = from_ce_date(cedate)
        assert(date.year == 9551)
        assert(date.season == THERANTER)
        assert(date.day == d)
        cedate += datetime.timedelta(1)
    for d in range(1, 92):
        date = from_ce_date(cedate)
        assert(date.year == 9551)
        assert(date.season == AUTUNE)
        assert(date.day == d)
        cedate += datetime.timedelta(1)
    date = from_ce_date(cedate)
    assert(date.year == 9552)
    assert(date.season == WINTUARY)
    assert(date.day == 1)

def test_today():
    date = today()
    assert(date)

def test_now():
    time = now()
    assert(time)
