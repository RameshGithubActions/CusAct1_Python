import sys


def multiplication_from_system_arguements():
    result = 1
    n = len(sys.argv)
    for i in range(1, n):
        result *= float(sys.argv[i])
    return result


if __name__ == "__main__":
    print("Result from Python File: " + str(multiplication_from_system_arguements()))   
