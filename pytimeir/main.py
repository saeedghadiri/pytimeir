from month_events_extractor import MonthEventsExtractor
import pandas as pd


def get_holidays(start_year, end_year=None):
    """
    Get holidays from start_year to end_year
    """
    if end_year is None:
        end_year = start_year

    df = get_events(start_year, end_year)
    df = df[df['is_holiday']].reset_index(drop=True)

    return df


def get_events(start_year, end_year=None):
    """
    Get events from start_year to end_year
    """
    events = []
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            events.append(MonthEventsExtractor(year, month).get_events())
    events = pd.concat(events)
    return events


if __name__ == "__main__":
    ev_0 = get_holidays(1397, 1400)
    ev_1 = get_events(1397, 1400)

    print()
