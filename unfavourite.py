#!/usr/bin/env python

import argparse
import csv
import sys
import time
import os
import twitter
from dateutil.parser import parse

__author__ = "Jonas Malmlof"
__version__ = "0.3"


def print_there(x, y, text):                
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y+5, x+10, text))
     sys.stdout.flush()


def delete(api, date):
    with open("like.js") as file:

        count = 0
        limit = 0
        errors = 0
        duplicate = 0
        inarow = 0
        lockdowns = 0

        for row in csv.DictReader(file):
            fileDone = open("like-done.js", "r+")
            fileError = open("like-error.js", "r+")
            tweet_id = int(row["tweet_id"])

            if str(tweet_id) in fileDone.read() or str(tweet_id) in fileError.read():
                duplicate += 1

            else:
                try:
                    time.sleep(6)
                    limit += 1
                    api.DestroyFavorite(status_id=tweet_id)
                    fileDone.write(str("%d\n" % tweet_id))
                    count += 1
                    inarow = 0

                except twitter.TwitterError as err:
                    errors += 1

                    print_there(0, 6, "                                                                                             ")
                    if str(err) == "{'Unknown error: '}":
                        inarow += 1
                        limit -= 1
                        errors -= 1
                        print_there(0, 6, ("%d %s" % (inarow, str(err))))

                    elif "already" in str(err):
##                        print_there(0, 6, err)
                        try:
                            time.sleep(6)
                            errors -= 1
                            limit += 1
                            api.DestroyFavorite(status_id=tweet_id)
                            fileDone.write(str("%d\n" % tweet_id))
                            count += 1
                            inarow = 0
                        except twitter.TwitterError as errTwo:
                            errors += 1
                            fileError.write("\"%s\" %s\n" % (str(tweet_id), str(errTwo)))
                            print_there(0, 6, "                                                                                             ")
                            print_there(0, 6, errTwo)
                            continue

                    else:
                        print_there(0, 6, err)
                        inarow = 0
                        fileError.write("\"%s\" %s\n" % (str(tweet_id), str(err)))

# ('{:4d}'.format(count))
# str(count).zfill(4))

            print_there(0, 0, ('{:7d}'.format(count)))
            print_there(0, 1, ('{:7d}'.format(duplicate)))
            print_there(0, 2, ('{:7d}'.format(errors)))
#            print_there(0, 3, ('{:7d}'.format(limit)))
            print_there(0, 3, ('{:7d}'.format(inarow)))
            print_there(90, (lockdowns-3), ('{:7d}'.format(limit)))


            print_there(9, 0, "tweets unliked.")
            print_there(9, 1, "duplicates found.")
            print_there(9, 2, "errors.")
            print_there(9, 3, "unknown errors")
#            print_there(9, 3, "out of 1900 calls reached.")
#            print_there(9, 4, "calls before rate-limit.")


            if limit >= 1900:
                inarow = 10
            if inarow >= 10:
                inarow = 0
                fileError.write("Limit: %s. Count: %s. Errors: %s\n" % (str(limit), str(count), str(errors)))
                fileError.flush()
                lockdowns += 1
                print_there(0, 8, "Waiting   :  . Rate-limit reached.")
                limit = 0
                errors = 0
                count = 0
                for h in range(20, -1, -1):
                    print_there(8, 8, str(h).zfill(2))
                    for m in range(59, -1, -1):
                        print_there(11, 8, str(m).zfill(2))
                        time.sleep(60)
                print_there(0, 8, "                                        ")

    print ("Number of unliked tweets: %s\n" % count)


def error(msg, exit_code=1):
    sys.stderr.write("Error: %s\n" % msg)
    exit(exit_code)

def main():
    parser = argparse.ArgumentParser(description="Delete old tweets.")
    parser.add_argument("-d", dest="date", required=True,
                        help="Delete tweets until this date")

    args = parser.parse_args()

    api = twitter.Api(consumer_key="",
                      consumer_secret="",
                      access_token_key="",
                      access_token_secret="")

    delete(api, args.date)

if __name__ == "__main__":
    print(chr(27) + "[2J")
    main()
