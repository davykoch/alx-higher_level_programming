#!/usr/bin/python3
import sys


def main():
    # Start with a total of 0
    total = 0
    # Iterate over the arguments excluding the first one (script name)
    for arg in sys.argv[1:]:
        # Add the integer value of each argument to the total
        total += int(arg)
    # Print the total sum
    print(total)


if __name__ == "__main__":
    main()
