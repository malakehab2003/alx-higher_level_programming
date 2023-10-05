#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv) - 1
    result = 0

    for i in range(length):
        result += int(sys.argv[i + 1])
    print("{}".format(result))
