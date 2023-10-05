#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    l = len(argv) - 1
    if l == 0:
        print("0 arguments.")
    elif l == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(l))
        i = 1
        for i in range(l):
            print("{}: {}".format(i, argv[i]))
