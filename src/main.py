import sys

result = 1
n = len(sys.argv)
for i in range(1, n):
    result *= float(sys.argv[i])

print(result)    
