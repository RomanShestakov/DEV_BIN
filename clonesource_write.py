#!/usr/bin/python

#import sys
##import time
# Let's create a file and write it to disk.
# filename = sys.argv[ 1 ]
# Let's create some data:
done = 0
#books = [ "Book1", "Book2", "Book3" ]
counter = 0

for counter in range(1, 20):
    print 'tag:=%s book:=Book%s' % (counter, counter)
    #sys.stdout.write(line)

    #print "tag:=",counter,  "book:=",book
# print "Start : %s" % time.ctime()
# time.sleep( 5 )
# print "End : %s" % time.ctime()
# # Create a file object:
# # in "write" mode
# FILE = open(filename,"w")

# # Write all the lines at once:
# FILE.writelines(namelist)
# # Alternatively write them one by one:
# for name in namelist:
#     FILE.write(name)
# print "pyth: closing name %s " % filename
# FILE.close()

#     # And finally, lets flush stdout because we are communicating with
#     # Erlang via a pipe which is normally fully buffered.
#     #sys.stdout.flush()
#sys.exit()
