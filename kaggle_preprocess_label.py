#!/usr/bin/env python

import fileinput
from sklearn import preprocessing
from sklearn.externals import joblib
from collections import Counter


def label():
    threshold = 1000
    vs = []
    c = Counter()

    for iline in fileinput.input():
        iline = iline.strip().split(',')
        c.update(iline)

        vs.append(iline)

    c.pop('')
    c = {label: index for index, (label, freq) in enumerate(c.most_common()) if freq > threshold}
    print c
    # Label
    for iline in vs:
        print ",".join(map(lambda k: str(c.get(k,"")), iline))

if __name__ == "__main__":
    label()
