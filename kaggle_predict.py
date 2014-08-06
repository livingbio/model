#!/usr/bin/env python
from sklearn.externals import joblib
import fileinput
from itertools import izip

def predict():
    clf = joblib.load('train.pkl')

    ids = []
    tests = []
    for iline in fileinput.input():
        vs = iline.split(',')
        t = vs[0]
        v = vs[1:]
        
        ids.append(t)
        tests.append(v)
    
    p_test = []
    while tests:
        p_test.extend( clf.predict_proba(tests[:10000]))
        del tests[:10000]        

    for a, b in izip(ids, p_test):
        print ','.join(map(str, [a, b[1]]))
        

if __name__ == "__main__":
    predict()