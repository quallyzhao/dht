#!/usr/bin/env python

"""
Read in a simple file of the format
    epochtime	event	IP_address
where epochtime is an int, event is "join" or "fail" and IP_address is
something like "18.72.0.3" (such as generated by plupdown.py).
Generate a bunch of events corresponding to vnodes that might have
something to do with that plus a corresponding number of inserts.

We will still simulate by the "minute".
"""

import sha
import sys
from utils import random_id, random_interval, make_chordID

mu_i	= 5
sd_i	= 5
maxblocks = 1000

def str2bigint(s):
    a = map(ord, s)
    v = 0L
    for d in a:
	v = v << 8
	v = v | d
    return v

inserted = {}
def random_blockid ():
    s = sha.sha("%d" % random_id ())
    id = str2bigint (s.digest ())
    while id in inserted:
	# Damn birthdays.
	s = sha.sha("%d" % random_id ())
	id = str2bigint (s.digest ())
    inserted[id] = 1
    return id


firsttime = None
lasttime  = 0
fh = open (sys.argv[1])
for line in fh.readlines ():
    (t, e, ip) = line.strip ().split ()

    # normalize time
    t = int (t)
    if not firsttime:
	firsttime = t
	nnode = make_chordID (ip, 11977, 0)
    t = t - firsttime
    t /= 60

    if t != lasttime and t > 200 :
	if maxblocks > 0:
	    for t in xrange(lasttime+1,t-1):
		ni = random_interval (mu_i, sd_i)
		while ni > 0 and maxblocks > 0:
		    print t, "insert", nnode, random_blockid ()
		    ni -= 1
		    maxblocks -= 1
	lasttime = t
    print t, e, make_chordID (ip, 11977, 0)
