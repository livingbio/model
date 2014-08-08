#!/usr/bin/env python
from scipy.optimize import minimize
from dpipe import dio
import kaggle_evl
from functools import partial
import fileinput 
import scipy as sp
import numpy

def bound(y):
    if y < 0:
        return 0
    elif y > 1:
        return 1
    return y

def transform(act, X):
    a, b, c = X
    
    Y = act ** 2 * a + act * b + c
    if isinstance(Y, numpy.ndarray):
        return sp.array([bound(k) for k in Y])   
    return bound(Y)

def object(act, pred, X):
    v = transform(pred, X)
    return abs(kaggle_evl.llfun(act, v))

def predict():
    with open('min.model') as ifile:
        X = map(float, ifile.read().split(','))
        
    for iline in dio.io():
        vs = map(float, iline.split(','))
        act, p = vs

        new_p = transform(p, X)
        print act, ',', new_p    

def train():
    act = []
    pred = []

    for iline in dio.io():
        vs = iline.split(',')
        if len(vs) == 2:
            vs = map(float, vs)
            act.append(vs[0])
            pred.append(vs[1])

    obj = partial(object, sp.array(act), sp.array(pred))
    
    x0 = [0, 1, 0]
    res = minimize(obj, x0, method='nelder-mead', options={'xtol': 1e-8, 'disp': True})

    for a, p in zip(act, pred):
        print a, ',' , transform(p, res.x)

    with open('min.model', 'w') as ofile:
        ofile.write(','.join(map(str, res.x)))
   
if __name__ == "__main__":
    dio.now()
