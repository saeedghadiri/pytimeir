import pandas as pd
import requests
from .utils import retry, parse_date
import jdatetime

base_url = "https://api.time.ir/v1/event/fa/events/calendar?year={year}&month={month}&day=0&base1=0&base2=1&base3=2"
api_key = 'ZAVdqwuySASubByCed5KYuYMzb9uB2f7'


class EventsExtractor:
    """
    Extracts events from time.ir

    Parameters
    ----------
    year : int
        Year of events
    month : int
        Month of events

    """

    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month
        self.url = base_url.format(year=year, month=month)
        self.headers = {'X-Api-Key': api_key}

    @retry(retry_count=5, retry_delay=1)
    def _extract(self):
        """
        Extracts html from time.ir

        Returns
        -------
        html : str
        """
        r = requests.get(url=self.url, headers=self.headers)
        return r.json()

    @staticmethod
    def _transform(data: dict):
        events_list = []
        # extract events
        for event in data['data']['event_list']:
            jalali_date = str(event['jalali_year']).zfill(4) + str(event['jalali_month']).zfill(2) + str(
                event['jalali_day']).zfill(2)
            d_date = jdatetime.datetime.strptime(jalali_date, '%Y%m%d').togregorian()
            events_list.append({'date': d_date, 'jalali_date': jalali_date, 'event': event['title'],
                                'is_holiday': event['is_holiday']})

        return events_list

    def get_events(self):
        """
        Extracts events from time.ir

        Returns
        -------
        events : pd.DataFrame
        """
        data = self._extract()
        events_list = self._transform(data)

        df = pd.DataFrame(events_list)
        df = df[['date', 'jalali_date', 'event', 'is_holiday']]

        return df
