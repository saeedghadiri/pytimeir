from time import sleep
from unidecode import unidecode
import jdatetime

month_list = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'اَمرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']


def parse_date(date_str):
    # get day
    day = date_str.split(' ')[0]
    day = unidecode(day)
    day = int(day)
    # get month
    month = date_str.split(' ')[1]
    month = month_list.index(month) + 1
    return day, month


def retry(retry_count, retry_delay, verbose=False, return_last_exception=True):
    """
    this decorator is used to recalling a function in failure cases
    Parameters
    ----------
    retry_count: int required
        number of retries
    retry_delay: int required
        delay between two consecutive try
    verbose: bool, optional default False
        flag to whether printing the reason of exception or not
    return_last_exception: str, optional default ''
        flag to whether returning the last exception or not
    """

    def actual_decorator(func):
        def inner(*args, **kwargs):
            current_try = 0
            last_exception = None

            while current_try < retry_count:
                try:
                    result = func(*args, **kwargs)
                    return result
                    # break

                except Exception as e:
                    last_exception = e
                    if verbose:
                        print('retry func:{} exception:{} '.format(func.__name__, e.__str__()))
                    current_try += 1
                    sleep(retry_delay)

                if current_try == retry_count:
                    print('maximum number of retries reached func:{} exception:'.format(func.__name__,
                                                                                        last_exception.__str__()))
                    if return_last_exception:
                        raise last_exception
                    else:
                        return None

        return inner

    return actual_decorator



