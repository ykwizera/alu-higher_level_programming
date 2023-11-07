#!/usr/bin/python3
def multiple_returns(sentence):
    for item in sentence:
        length = len(item)
        first = sentence[0] if length > 0 else None
        return length, first
