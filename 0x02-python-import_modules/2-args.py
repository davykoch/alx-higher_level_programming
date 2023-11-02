#!/usr/bin/python3
import sys


def main():
    arg_count = len(sys.argv) - 1  # Exclude the script name
    if arg_count == 0:
        print("Number of arguments: 0.")
    elif arg_count == 1:
        print("Number of argument: 1:")
    else:
        print("Number of arguments: {}:".format(arg_count))

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
