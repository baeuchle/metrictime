import datetime
from .Date import Date
from .Season import days_in_season, WINTUARY, LENTUARY, THERANTER, AUTUNE

def from_ce_time(time):
    pass

def get_yearstart_(ce_year):
    """This is valid between 1941CE and 2068CE, only."""
    # for CE leap years and the one after, solstice is at
    # Dec 21, so the new ME year starts at Dec 22
    if ce_year % 4 in (0,1):
        return datetime.date(ce_year, 12, 22)
    # for the other two years (ME leap years and the next),
    # solstice is at Dec 22 and ME year starts at Dec 23:
    return datetime.date(ce_year, 12, 23)

def from_ce_date(*args):
    """Returns a Date from arguments that build a CE datetime"""
    ce_date = None
    if len(args) == 3:
        ce_date = datetime.date(*args)
    elif type(args[0]) == datetime.date:
        ce_date = args[0]
    elif type(args[0]) == datetime.datetime:
        ce_date = datetime.date(args[0].year, args[0].month, args[0].day)
    ce_year = ce_date.year
    yearstart = get_yearstart_(ce_year)
    if yearstart > ce_date:
        yearstart = get_yearstart_(ce_year - 1)
    year = yearstart.year + 7530 + 1
    day_in_year = (ce_date - yearstart).days + 1
    if day_in_year <= days_in_season(WINTUARY, year):
        season = WINTUARY
        day = day_in_year
    elif day_in_year <= days_in_season(WINTUARY, year) + days_in_season(LENTUARY, year):
        season = LENTUARY
        day = day_in_year - days_in_season(WINTUARY, year)
    elif day_in_year <= days_in_season(WINTUARY, year) + days_in_season(LENTUARY, year) + days_in_season(THERANTER, year):
        season = THERANTER
        day = day_in_year - days_in_season(WINTUARY, year) - days_in_season(LENTUARY, year)
    else:
        season = AUTUNE
        day = day_in_year - days_in_season(WINTUARY, year) - days_in_season(LENTUARY, year) - days_in_season(THERANTER, year)
    year = yearstart.year + 7530 + 1
    return Date(year=year, season=season, day=day)

def from_ce_datetime(dt):
    pass

def today():
    return from_ce_date(datetime.date.today())

def now():
    pass
