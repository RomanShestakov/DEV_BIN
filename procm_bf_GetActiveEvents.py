#!/usr/bin/python

#import ConfigParser
import requests
import sys
import optparse


def main(opts):
    from cfg_bf_GetActiveEvents import config
    print opts
    r = requests.get(config['link'])
    print r.content
    sys.stdout.flush()

#start processing
if __name__ == "__main__":
    try:
        parser = optparse.OptionParser()
        parser.add_option('--book', dest='BookName', default='TestBook')
        parser.add_option('--isbook', dest='isBook', default=False,\
                          action='store_true')
        (opts, args) = parser.parse_args()
        sys.exit(main(opts))
    except Exception, e:
        print e
        sys.exit(1)
