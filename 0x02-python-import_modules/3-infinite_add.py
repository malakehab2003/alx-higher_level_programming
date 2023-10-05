#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    for i in len(sys.argv) - 1:
        result += int(sys.argv[i + 1])
    print("{}".format(result))
