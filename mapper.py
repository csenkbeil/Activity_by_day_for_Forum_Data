#!/usr/bin/python


# This mapper handles stdin text data from forum_node.tsv and outputs,
#   Key: Date %Y-%m-%d, the date of the post, and
# Value: 1, a count of the post for that day.
# Output format:
# Date \t 1

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t', quoting=csv.QUOTE_ALL)

for row in reader:
    if len(row) != 19:    # Skip invalid record (data is stored in 19 columns)
        continue
    added_at = row[8]     # Posted time stamp is added_at, column 9
    
    # Parse added_at and ignore last 3 digits siginifying UTC hour offset and extract the weekday value
    try:
        posted_date = datetime.strptime(added_at[:-3], "%Y-%m-%d %H:%M:%S.%f")
        posted_date_key = posted_date.strftime("%Y-%m-%d")
        
        print posted_date_key, '\t1'
    except ValueError:
        pass # ignore ValueError, skip situations where a header is presented instead of a datetime string.
    
