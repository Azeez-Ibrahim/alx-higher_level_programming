#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    keyList = list(a_dictionary.keys())
    valList = list(a_dictionary.values())
    maxVal = max(valList)
    index = valList.index(maxVal)
    return keyList[index]
