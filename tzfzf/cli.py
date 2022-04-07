#!/usr/bin/env python
from argparse import ArgumentParser

from .smart.parser import date_parse


def main():
    argument_parser = ArgumentParser('magically get a datetime')
    argument_parser.add_argument(
            'time',
            nargs='*',
            help='dynamic time string',
            )
    args = argument_parser.parse_args()

    datetime = date_parse(*args.time)
    print(datetime)


if __name__=='__main__':
    main()
