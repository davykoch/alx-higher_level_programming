#!/usr/bin/python3
from sys import argv


def main():
    arg_count = len(argv) - 1  # Exclude the script name
    if arg_count == 0:
        print("Number of arguments: 0.")
    elif arg_count == 1:
        print("Number of argument: 1:")
    else:
        print("Number of arguments: {}:".format(arg_count))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]), end=' ')


if __name__ == "__main__":
    main()
