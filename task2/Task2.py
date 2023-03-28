import math
import sys
file_path = sys.argv[1]
args = []
with open(file_path, 'r') as file:
  for arg in file:
    args.append(int(arg))
result_digit = math.ceil((max(args))/2)
count = 0
for id, i in enumerate(args):
    while i != result_digit:
        if i < result_digit:
            i += 1
            count += 1
        elif i > result_digit:
            i -= 1
            count += 1
        else:
            args[id] = i
print(count)
