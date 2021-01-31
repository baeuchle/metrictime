WINTUARY = 0
LENTUARY = 1
THERANTER = 2
AUTUNE = 3

# 90/91 days of Wintuary (Wintuar)
# 92 days of Lentuary (Lenter) (Niederländisch)
# 92 days of Theranter (Verant) (Altgriechisch / Spanisch)
# 91 days of Autune (Herbster) (Englisch / Deutsch)
seasons = {
    'en': ('Wintuary', 'Lentuary', 'Theranter', 'Autune'),
    'de': ('Wintuar', 'Lenter', 'Verant', 'Herbster')
}

def days_in_season(season, year):
    if season == WINTUARY:
        if year % 4 == 0 and year % 128 != 0:
            return 91
        return 90
    if season == LENTUARY:
        return 92
    if season == THERANTER:
        return 92
    if season == AUTUNE:
        return 91
    raise ValueError("Invalid season ({}, {}, {} or {}, got {})".format(
        WINTUARY, LENTUARY, THERANTER, AUTUNE, season
    ))
