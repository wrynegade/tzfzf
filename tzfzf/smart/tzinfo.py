from dateutil.tz import gettz
from pytz import all_timezones


alias_dict = {
        'US/Central':  ['CT', 'CDT', 'CST'],
        'US/Eastern':  ['ET', 'EDT', 'EST'],
        'US/Mountain': ['MT', 'MDT', 'MST'],
        'US/Pacific':  ['PT', 'PDT', 'PST'],
        }

tzinfos = {
        **{
            timezone : gettz(timezone)
            for timezone in all_timezones
            },
        **{
            alias.upper() : gettz(name)
            for name, aliases in alias_dict.items()
            for alias in aliases
            },
        }
