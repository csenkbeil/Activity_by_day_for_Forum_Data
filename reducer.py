#!/usr/bin/python

# This reducer  outputs,
#   Key: Date %Y-%m-%d, the date of the post, and
# Value: Sum for posts for the day.
# Output format:
# Date \t postsTotal

# The reducer can also act as a combiner between mapping and reducing.

import sys

postsTotal = 0
oldDate = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisDate, thisPosts = data_mapped

    if oldDate and oldDate != thisDate:
        print oldDate, "\t", postsTotal
        oldDate = thisDate;
        postsTotal = 0

    oldDate = thisDate
    postsTotal += int(thisPosts)

if oldDate != None:
    print oldDate, "\t", postsTotal

