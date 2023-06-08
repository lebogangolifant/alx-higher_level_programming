#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *

    names = [name for name in dir() if not name.startswith("__")]
    names.sort()

    for name in names:
        print("{}".format(name))
