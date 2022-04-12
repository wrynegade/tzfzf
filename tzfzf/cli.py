#!/usr/bin/env python
from argparse import ArgumentParser

from .smart.parser import date_parse
from .output import MODES


def main():
    parser = ArgumentParser('timezone translation CLI')

    parser.add_argument(
            'time',
            nargs='*',
            help='standard or semantic date string',
            )

    parser.add_argument(
            '--mode',
            type=str,
            help='set parse mode : (compare)',
            default='compare',
            )

    parser.add_argument(
            '--timezones',
            type=str,
            help='comma-separated list of timezones for output',
            default=None,
            )

    args = parser.parse_args()

    MODES[args.mode](
            timezone = date_parse(*args.time),
            timezones = args.timezones,
            )


if __name__=='__main__':
    main()
