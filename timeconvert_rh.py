import os
import sys
import re

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    x = re.findall("PM$", s)
    ans = ":"
    if x:
        rem_AMPM = re.sub("PM", "", s)
        arr = rem_AMPM.split(":")
        if(int(arr[0]) < 12):
            arr[0] = str(int(arr[0])+12)
        ans = ans.join(arr)

        return(ans)
    else:
        rem_AMPM = re.sub("AM", "", s)
        arr = rem_AMPM.split(":")
        if(arr[0] == "12"):
            arr[0] = "00"
        ans = ans.join(arr)
        return(ans)

if __name__ == '__main__':
    f = sys.stdout

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
