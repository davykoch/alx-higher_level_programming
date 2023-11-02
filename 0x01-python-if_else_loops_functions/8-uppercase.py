#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        print("{}".format(char), end='')
    print()


if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
