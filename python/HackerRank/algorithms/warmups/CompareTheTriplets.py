#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    aliceScore = 0
    bobScore = 0
    for i in range(0, 3):
        if a[i] > b[i]:
            aliceScore += 1
        elif a[i] < b[i]:
            bobScore += 1
    result = [aliceScore, bobScore]
    return result
