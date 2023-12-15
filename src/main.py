import sys
n = len(sys.argv)
result = 1
for i in range(1, n):
    result *= int(sys.argv[i])
print("Result:", result)
