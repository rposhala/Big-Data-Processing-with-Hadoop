import sys
import os

for line in sys.stdin:

    temp_list = line.strip().split('\t')
    if len(temp_list) == 2:
        print("{}\t{}\n".format(temp_list[0],temp_list[1]))
