import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    max_height = 0
    total = 0
    for i in ar:
        if (i > max_height):
            max_height = i
        else:
            continue
    for i in ar:
        if(i == max_height):
            total += 1
        else:
            continue
    return(total)
        

if __name__ == '__main__':
    fptr = sys.stdout 

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
