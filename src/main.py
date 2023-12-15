import sys
import os

n = len(sys.argv)
for i in range(1, n):
    print(sys.argv[i])
result = 1
for i in range(1, n):
    result *= float(sys.argv[i])
print("Result:", result)
os.environ["RESULT"] = str(result)
