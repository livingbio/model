#!/usr/bin/env python

import fileinput
from sklearn import preprocessing
from sklearn.externals import joblib
from collections import Counter
from scipy.sparse import csr_matrix
from scipy.io import mmwrite

def label(threshold=None):
    vs = []
    c = Counter()

    for iline in fileinput.input():
        iline = iline.strip().split(',')
        c.update(iline)

        vs.append(iline)

    c.pop('')
    threshold = threshold or len(c) / 10
#    print threshold

    c = {label: index for index, (label, freq) in enumerate(c.most_common()[:threshold])}
    
    vs = [[c[i] for i in k if i in c] for k in vs]

    for v in vs:
        print ','.join(map(str, v))

    with open('label.model', 'w') as ofile:
        for label in c:
            ofile.write('%s,%s\n'%(label, c[label]))

if __name__ == "__main__":
    label()
