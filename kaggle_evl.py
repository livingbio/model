#!/usr/bin/env python
import scipy as sp
import fileinput

def llfun(act, pred):
    epsilon = 1e-15
    pred = sp.maximum(epsilon, pred)
    pred = sp.minimum(1-epsilon, pred)
    ll = sum(act*sp.log(pred) + sp.subtract(1,act)*sp.log(sp.subtract(1,pred)))
    ll = ll * -1.0/len(act)
    return ll

def evl():
    act = []
    pred = []

    for iline in fileinput.input():
        vs = iline.split(',')
        if len(vs) == 2:
            vs = map(float, vs)
            act.append(vs[0])
            pred.append(vs[1])

    return llfun(sp.array(act), sp.array(pred))

if __name__ == "__main__":
    print evl()
