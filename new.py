fname = input("Enter file name ")
if len(fname) < 1:
    fname = "regex_sum_749333.txt"
fhandle = open(fname)
import re
inp = fhandle.read()
x = re.findall('[0-9]+',inp)
num = len(x) - 1
while num >= 0:
    x[num] = int(x[num])
    num = num - 1
print(sum(x))
