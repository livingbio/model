#!/usr/bin/env python

from sklearn.preprocessing import Imputer
from sklearn import preprocessing
from sklearn.decomposition import PCA
import scipy.sparse as sp
import fileinput
import numpy
from itertools import izip
from dpipe import dio


def imputer():
    vs = []
    for iline in dio.io():
        iline = iline.strip().split(',')
        vs.append([int(x) if x else numpy.NaN for x in iline])

    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    vs = imp.fit_transform(vs)

    for v in vs:
        print ",".join(map(str, map(int, v)))


def label(threshold=0.1):
    vs = []
    c = Counter()

    for iline in fileinput.input():
        iline = iline.strip().split(',')
        c.update(iline)

        vs.append(iline)

    c.pop('')
    if isinstance(threshold, int):
        threshold = threshold
    elif isinstance(threshold, float):
        threshold = int(len(c) * threshold)
    else:
        raise

    c = {label: index for index, (label, freq) in enumerate(c.most_common()[:threshold])}

    vs = [[c[i] for i in k if i in c] for k in vs]

    for v in vs:
        print ','.join(map(str, v))

    with open('label.model', 'w') as ofile:
        for label in c:
            ofile.write('%s,%s\n'%(label, c[label]))



if __name__ == "__main__":
    dio.now('imputer')
