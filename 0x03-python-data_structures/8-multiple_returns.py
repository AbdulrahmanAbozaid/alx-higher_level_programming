#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0 if not sentence else len(sentence)
    return length, None if not length else sentence[0]
