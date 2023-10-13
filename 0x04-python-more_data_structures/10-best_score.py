#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    mx = 0
    ky = ""
    for k, i in a_dictionary.items():
        mx = max(i, mx)
        if mx == i:
            ky = k
    return ky
