#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    H = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
     "eleven", "twelve"]
    M = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
     "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
     "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]
    if m == 0:
        return f"{H[h]} o' clock"
    elif m == 15:
        return f"quarter past {H[h]}"
    elif m == 30:
        return f"half past {H[h]}"
    elif m == 45:
        return f"quarter to {H[h + 1]}"
    elif m < 30:
        if m == 1:
            return f"{M[m]} minute past {H[h]}"
        return f"{M[m]} minutes past {H[h]}"
    elif m > 30:
        return f"{M[60 - m]} minutes to {H[h + 1]}"
