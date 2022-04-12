from datetime import datetime

from dateutil.tz import gettz
from pytz import common_timezones, all_timezones, timezone


def get_local_timezone_name():
    return datetime.now().astimezone().tzname()

ALIAS_DICT = {
        'US/Central': [
            'CT', 'CDT', 'CST',
            'AL', 'AR', 'IA', 'IL', 'KS',
            'LA', 'MN', 'MO', 'MS', 'ND',
            'NE', 'OK', 'SD', 'TN', 'TX',
            'WI',
            ],
        'US/Eastern': [
            'ET', 'EDT', 'EST',
            'CT', 'DC', 'DE', 'FL', 'GA',
            'IN', 'MA', 'MD', 'ME', 'MI',
            'NC', 'NH', 'NJ', 'NY', 'OH',
            'PA', 'RI', 'SC', 'VA', 'VT',
            'WV',
            ],
        'US/Mountain': [
            'MT', 'MDT', 'MST',
            'AZ', 'CO', 'ID', 'MT', 'NM',
            'UT', 'WY',
            ],
        'US/Pacific':  [
            'PT', 'PDT', 'PST',
            'WA', 'OR', 'NV', 'CA',
            ],
        }

REVERSE_ALIAS_DICT = {
        alias: name
        for name, aliases in ALIAS_DICT.items()
        for alias in aliases
        }

TZINFOS = {
        **{
            name : gettz(name)
            for name in all_timezones
            },
        **{
            alias.upper() : gettz(name)
            for name, aliases in ALIAS_DICT.items()
            for alias in aliases
            },
        }

TZOFFSETS = {
        datetime.now(timezone(name)).utcoffset().total_seconds()/60/60: gettz(name)
        for name in common_timezones
        }
