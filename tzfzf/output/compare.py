from pytz import utc
from rich import print as rich_print
from rich.panel import Panel
from rich.align import Align


from ..smart.math import shift
from ..smart.tzinfo import REVERSE_ALIAS_DICT, get_local_timezone_name

def compare(timezone, timezones=None):
    '''
    compare indicated datetime to local timezone ±3 hours
    '''
    panels = [
            get_panel(tz)
            for tz in [shift(timezone, x) for x in range(-3, 4)]
            ]

    panels.append(get_panel(timezone.astimezone(utc)))


    for p in panels:
        rich_print(p)

def get_panel(tz):
    return Panel(
            Align.center(tz.strftime('%I:%M %p')),
            title = get_name(tz),
            )

def get_name(tz):
    tzname = tz.tzname()

    name = REVERSE_ALIAS_DICT.get(tzname, tzname)

    if tzname == get_local_timezone_name():
        color = 'green'
    elif tzname == 'UTC':
        color = 'yellow'
    else:
        color = 'red'

    return f'[{color}]{name}[/{color}]'
