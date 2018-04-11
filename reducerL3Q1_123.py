#!/usr/bin/python

import sys

salesTotal = 0.0
salesNumber = 0.0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    thisSale = float(thisSale)

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey;
        #Q1 & Q3: to compute total sales and total number of sales across all stores
        #salesTotal = 0.0

    oldKey = thisKey
    #Q1 & Q3: to compute total sales per store
    salesTotal += float(thisSale)
    salesNumber += 1.0
    #Q2: to compute highest sale per store
    #if salesTotal < thisSale:
    #    salesTotal = thisSale

if oldKey != None:
	#Q1 & Q2: print key value and sales value
    #print oldKey, "\t", salesTotal
	#Q3: print sales number and total sales value
    print salesNumber, "\t", salesTotal

