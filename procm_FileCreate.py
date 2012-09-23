#!/usr/bin/python

import requests
import sys
import optparse
import time
#import datetime
import random
import os
from dateutil.parser import *

def get_run_date():
    if os.environ.has_key('RUN_DATE'):
        datestring = os.environ['RUN_DATE']
        return parse(datestring).date()
    else:
        raise Exception('env variable RUN_DATE not defined')

def main(opts, rundate = get_run_date()):
    from cfg_bf_GetActiveEvents import config
    filename = opts.book
    print "Run Date %s" % rundate
    print "pyth: name %s " % filename
    print "Start : %s" % time.ctime()
    time.sleep( random.randrange(0, 50, 2) )
    FILE = open(filename,"w")
    FILE.write(filename)
    FILE.close
    print "End : %s" % time.ctime()
    sys.stdout.flush()


#sys.argv = [sys.argv[0], '--book', 'TestBook1' ]
#start processing
if __name__ == "__main__":
    try:
        parser = optparse.OptionParser()
        parser.add_option('--book', dest='book')
        (opts, args) = parser.parse_args()

        # Making sure all mandatory options appeared.
        mandatories = ['book']
        for m in mandatories:
            if not opts.__dict__[m]:
                raise Exception("mandatory option {0} is missing".format(m))

        # call main
        sys.exit(main(opts))
    except Exception, e:
        print e
        sys.exit(1)
