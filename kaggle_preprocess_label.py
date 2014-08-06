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

#    c.pop('')
    threshold = threshold or len(c) / 10
#    print threshold
    c = {label: index for index, (label, freq) in enumerate(c.most_common()[:threshold])}
    
    vs = [[c.get(i,0) for i in k] for k in vs]

    enc = preprocessing.OneHotEncoder()
    vs = enc.fit_transform(vs)       

    for v in vs:
#        print v.toarray()[0]
        print ",".join(map(lambda i: str(int(i)), list(v.toarray()[0])))

    #row = []
    #col = []
    #data = []
    #for i, v in enumerate(vs):
    #    for j, k in enumerate(v):
    #        if c.get(k) != None:
    #            data.append(1)
    #            row.append(i)
    #            col.append(c.get(k))
            
    
#    m = csr_matrix((data,(row,col)), shape=(len(vs), threshold))
#    mmwrite(open('a.m','w'), m)
#    print m
#    print m.todense()
#    print c
    # Label
    #for iline in vs:
    #    print ",".join(map(lambda k: str(c.get(k,"")), iline))

if __name__ == "__main__":
    label()
