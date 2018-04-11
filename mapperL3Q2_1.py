#!/usr/bin/python

# We want 2 elements
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
	data = line.strip().split()
	if len(data) == 10:
		ipAddress, identity, username, time, zone, method, path, query, status, bytes = data
		print "{0}\t{1}".format(path, int(1))

