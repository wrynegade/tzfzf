from datetime import datetime

from dateutil.parser import parse, ParserError
from pytz import timezone

from .tzinfo import tzinfos


def date_parse(*args, attempts=0, MAX_ATTEMPTS=6):
    '''
    dynamically parses a date
    '''
    if attempts == 0:
        MAX_ATTEMPTS = min(MAX_ATTEMPTS, len(args) -1)

    attempts += 1

    parsed_time = None
    if len(args) == 0:
        parsed_time = datetime.utcnow().replace(tzinfo=timezone('UTC'))

    else:
        try:
            parsed_time = parse(' '.join(args).upper(), tzinfos=tzinfos)
        except ParserError:
            if attempts <= MAX_ATTEMPTS:
                parsed_time = date_parse(
                        *rotate_arguments(args),
                        attempts=attempts+1,
                        MAX_ATTEMPTS=MAX_ATTEMPTS,
                        )
            elif attempts == MAX_ATTEMPTS + 1:
                parsed_time = date_parse(
                        *unzip_arguments(args),
                        attempts=attempts,
                        MAX_ATTEMPTS=MAX_ATTEMPTS,
                        )

    return parsed_time

def rotate_arguments(args):
    return [*args[1::], args[0]]

def unzip_arguments(args):
    return [*args[1::2], *args[0::2]]
