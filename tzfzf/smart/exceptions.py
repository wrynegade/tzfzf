class DateParseError(Exception):
    def __init__(self, **kwargs):
        super().__init__('Failed to parse datetime', **kwargs)
