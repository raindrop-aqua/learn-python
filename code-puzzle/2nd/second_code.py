# -*- coding: utf-8 -*-
class SimpleBars(list):
    __rules = {
        "iTi": "xix",
         "iT":  "x ",
         "Ti":  " x",
         "T":   "i",
         "i i": "x x",
         "i ":  "xi",
         " i":  "ix",
         " ":   " ",
         "i":   "T"
    }

    def __init__(self, text):
        list.__init__(self, text)

    def __str__(self):
        return "".join(self)

    def next(self):
        return "".join(self)

    def _calc_next(self):
        for start_pos in range(len(self)):
            for rule in self.__rules.iterkeys():
                if self._transfer(start_pos, rule) == True:
                    break

    def _transfer(self, start_pos, rule):
        pass
