#!/usr/bin/env python3

def sequence_search(sequence, target):
    #for i in range(len(sequence)):
    #    if target == sequence[i]:
    #        return i
    #    else:
    #        return None
    i = 0
    while i <= len(sequence):
        if target == sequence[i]:
            return i
        else:
            i += 1
        if i == len(sequence):
            return None

if __name__ == '__main__':
    sequence = [99,12,33,74,521,13,14]
    target = 44
    print(sequence_search(sequence, target))
