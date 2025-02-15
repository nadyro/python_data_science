import time
import datetime as dt


def printSentence(a, b, c):
    print(f"Seconds since {a}: {b} or {c} in scientific notation")


e = time.gmtime(0)
minYear = dt.datetime(e.tm_year, e.tm_mon, e.tm_mday).strftime("%B %-d, %Y")

totalSeconds = time.time()
totalSecondsStr = "{:,.4f}".format(totalSeconds)
notation = "{:.2e}".format(totalSeconds)

printSentence(minYear, totalSecondsStr, notation)
print(dt.datetime.now().strftime("%b %d %Y"))
