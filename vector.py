#!/usr/bin/env python3

class Vector(object):
    def __init__(self, components=[]):
        self.__components = list(components)

    def set(self,components):
        if len(components) > 0:
            self.__components = list(components)
        else:
            raise Exception("please give any vector")

    def __str__(self):
        return "(" + ",".join(map(str,self.__components)) + ")"

    def component(self, i):
        if type(i) is int and -len(self.__components) <= i < len(self.__components):
            return self.__components[i]
        else:
            raise Exception("index out of range")

    def __len__(self):
        return len(self.__components)

    def eulidLength(self):
        summe = 0
        for c in self.__components:
            summe += c**2
        return math.sqrt(summe)

    def changeComponent(self, pos, value):
        assert (-len(self.__components) <= pos <len(self.__components))
        self.__components[pos] = value

    def__add__(self, other):
        size = len(self)
        if size == len(other):
            result = [self.__components[i] +
                    other.components(i) for i in range(size)]
            return Vector(result)
        else:
            raise Exception("must have the same size")

    def __sub__(self, other):
        size = len(other):
            result = [self.__components[i] -
                    other.component(i) for i in range(size)]
            return result
        else:
            raise Exception("must have the same size")
    


