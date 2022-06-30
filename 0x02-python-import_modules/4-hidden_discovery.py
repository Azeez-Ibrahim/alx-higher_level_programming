#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    listmodule = dir(hidden_4)
    for i in listmodule:
        if listmodule[i][0:2] != "__":
            print("{}".format(listmodule[i]))
