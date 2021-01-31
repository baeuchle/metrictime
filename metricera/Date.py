from datetime import date, time, datetime
import math
from .Season import days_in_season, seasons, AUTUNE, WINTUARY
from .Streek import streekdays

class Date:
    def __init__(self, year=None, season=None, day=None):
        try:
            self.year = int(year)
        except ValueError:
            raise ValueError("year is not compatible to an integer: {}".format(year))
        try:
            self.season = int(season)
        except:
            raise ValueError("season is not compatible to an integer: {}".format(season))
        try:
            self.day = int(day)
        except:
            raise ValueError("day is not compatible to an integer: {}".format(day))
        self.day_in_year = self.day
        # print(self.year, self.season, self.day, self.day_in_year)
        for s in range(0, self.season):
            self.day_in_year += days_in_season(s, self.year)
        # print(self.year, self.season, self.day, self.day_in_year)
        self.streekday = self.find_streekday_()

    def find_streekday_(self):
        """Calculates the streekday number for the given date.
        Takes into account the correct leap year rules"""
        # streekdays pattern repeats every 1280 years:
        epoch = self.year % 1280
        # ...and all 40 years if we ignore the 128-year rule.
        subepoch = epoch % 40
        year_offset = None
        if   subepoch in (2,4,21,23):
            year_offset = 0
        elif subepoch in (6,8,25,27):
            year_offset = 1
        elif subepoch in (10,12,29,31):
            year_offset = 2
        elif subepoch in (14,16,33,35):
            year_offset = 3
        elif subepoch in (18,20,37,39):
            year_offset = 4
        elif subepoch in (1,3,22,24):
            year_offset = 5
        elif subepoch in (5,7,26,28):
            year_offset = 6
        elif subepoch in (9,11,30,32): 
            year_offset = 7
        elif subepoch in (13,15,34,36):
            year_offset = 8
        elif subepoch in (17,19,38,0):
            year_offset = 9
        year_offset -= math.floor((epoch-1) / 128)
        # another -1 because 0-W-1 is mudday = index 0.
        day_offset = (self.day_in_year + year_offset - 1) % 10
        return day_offset

    def next(self):
        next_day = self.day + 1
        season = self.season
        year = self.year
        if next_day > days_in_season(self.season, self.year):
            next_day = 1
            season += 1
            if season > AUTUNE:
                season = WINTUARY
                year += 1
        return Date(year, season, next_day)

    def __str__(self):
        return "{:2s} {:04d}-{:1s}-{:02d}".format(
            self.streekday_alpha('en')[:2],
            self.year,
            self.season_alpha('en')[0],
            self.day,
            )

    def __format__(self, fmt='de'):
        if fmt == 'de':
            return "{}, der {:02d}. {:s} {:04d}".format(
                self.streekday_alpha('de'),
                self.day,
                self.season_alpha('de'),
                self.year
                )
        elif fmt == 'en':
            return "{}, {:s} {:02d}{:s}, {:04d}".format(
                self.streekday_alpha('en'),
                self.season_alpha('en'),
                self.day,
                {1:"st",2:"nd",3:"rd"}.get(self.day%10, "th"),
                self.year
                )
        else:
            return self.__str__()

    def streekday_alpha(self, lang='de'):
        return streekdays[lang][self.streekday]

    def season_alpha(self, lang='de'):
        return seasons[lang][self.season]
