import pandas as pd
import requests
from bs4 import BeautifulSoup
from .utils import retry, parse_date
import jdatetime

base_url = 'https://www.time.ir/'
post_str = "Year={year}&Month={month}&Base1=0&Base2=1&Base3=2&Responsive=true"


class EventsExtractor:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.url = base_url + '?' + post_str.format(year=year, month=month)
        self.events = []

    @retry(retry_count=5, retry_delay=1)
    def _extract(self):
        r = requests.post(url=self.url)
        return r.text

    @staticmethod
    def _transform(html):
        soup = BeautifulSoup(html, 'html.parser')
        # find events wrapper in html
        events = soup.find(class_='eventsCurrentMonthWrapper').find(class_="list-unstyled").findAll('li')

        events_list = []
        # extract events
        for event in events:
            spans = event.findAll({'span'})
            date_str = spans[0].text
            date_str = date_str.strip()
            # get date
            event_str = spans[0].next_sibling.text  # get event
            event_str = event_str.strip()

            is_holiday = False
            if 'eventHoliday' in event.attrs['class']:
                is_holiday = True

            events_list.append({'date_str': date_str, 'event': event_str, 'is_holiday': is_holiday})

        return events_list

    def get_events(self):
        html = self._extract()
        events_list = self._transform(html)

        df = pd.DataFrame(events_list)
        df[['day', 'month']] = df.apply(lambda x: parse_date(x['date_str']), axis=1, result_type='expand')
        # check whether the month is correct for all rows
        assert (df['month'] == self.month).all()

        df['jdate'] = df.apply(lambda x: jdatetime.date(self.year, x['month'], x['day']), axis=1)
        df['jalali_date'] = df.apply(lambda x: x['jdate'].strftime('%Y%m%d'), axis=1)
        df['date'] = df.apply(lambda x: x['jdate'].togregorian(), axis=1)

        df = df[['date', 'jalali_date', 'event', 'is_holiday']]
        return df
