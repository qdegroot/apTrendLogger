import argparse
import shelve
import datetime
from dateutil import rrule


# Accepts command line input
def get_args():
    parser = argparse.ArgumentParser(
        description='Get change in AP number over time. Please format dates as YYYY-MM-DD')

    parser.add_argument('-s', '--start',
                        required=True,
                        action='store',
                        help='Use to set startdate for period of change')

    parser.add_argument('-e', '--end',
                        required=True,
                        action='store',
                        help='Use to set enddate for period of change')

    parser.add_argument('-t', '--trend',
                        choices=['day','week', 'month', 'year', 'delta'],
                        required=True,
                        action='store',
                        help='Set granularity of trend data')

    args = parser.parse_args()
    return args


#Begin main
args = get_args()
start = datetime.datetime.strptime(args.start, '%Y-%m-%d')
end = datetime.datetime.strptime(args.end, '%Y-%m-%d')

with shelve.open("AP Log\AP History") as log:
    if args.start in log and args.end in log:
        if args.trend == 'delta':
            print("Total change: " + str(log[args.end]-log[args.start]))
        elif args.trend == 'year':
            for dt in rrule.rrule(rrule.YEARLY, dtstart=start, until=end):
                dt = datetime.datetime.strftime(dt, '%Y-%m-%d')
                print(dt + ": " + str(log[dt]))
        elif args.trend == 'month':
            for dt in rrule.rrule(rrule.MONTHLY, dtstart=start, until=end):
                dt = datetime.datetime.strftime(dt, '%Y-%m-%d')
                print(dt + ": " + str(log[dt]))
        elif args.trend == 'week':
            for dt in rrule.rrule(rrule.WEEKLY, dtstart=start, until=end):
                dt = datetime.datetime.strftime(dt, '%Y-%m-%d')
                print(dt + ": " + str(log[dt]))
        elif args.trend == 'day':
            for dt in rrule.rrule(rrule.DAILY, dtstart=start, until=end):
                dt = datetime.datetime.strftime(dt, '%Y-%m-%d')
                print(dt + ": " + str(log[dt]))
    else:
        print('Start or end date not available in log')