#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *

    listmodule = dir()
    for i in listmodule:
        # if listmodule[i][0:2] != "__":
        print("{}".format(listmodule[i]))
