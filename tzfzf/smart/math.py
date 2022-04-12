from .tzinfo import TZOFFSETS


def shift(timezone, count):
    '''
    returns the timezone-aware datetime shifted [+count] (1hr) timezones
    '''
    offset = timezone.utcoffset().total_seconds()
    new_offset = (((offset/60/60 + (count)) + 11) % 24) - 11

    new_tz = TZOFFSETS[new_offset]
    return timezone.astimezone(new_tz)
