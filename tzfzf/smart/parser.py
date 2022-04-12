from datetime import datetime

from dateutil.parser import parse, ParserError
from pytz import timezone

from .exceptions import DateParseError
from .tzinfo import TZINFOS


def date_parse(*args, attempts=0, MAX_ATTEMPTS=6):
    '''
    parses a timezone-sensitive date from a variety of standard
    and semantic datetime strings

    with no arguments, gets the current, UTC time
    '''
    if len(args) == 0:
        return datetime.utcnow().replace(tzinfo=timezone('UTC'))

    try:
        d = parse(' '.join(args).upper(), tzinfos=TZINFOS)
        if d.tzinfo is not None and d.tzinfo.utcoffset(d) is not None:
            return d
        return d.astimezone()

    except ParserError as e:
        if attempts > MAX_ATTEMPTS:
            raise DateParseError() from e

        func = _rotate if attempts < MAX_ATTEMPTS else _unzip

        return date_parse(
                *func(args),
                attempts = attempts + 1,
                MAX_ATTEMPTS = min(MAX_ATTEMPTS, len(args)),
                )

def _rotate(args):
    return [*args[1::], args[0]]

def _unzip(args):
    return [*args[1::2], *args[0::2]]
