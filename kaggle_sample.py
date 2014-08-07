#!/usr/bin/env python

import dio
import random

def sample(name='sample', ratio=0.99):
    with open('%s.train.csv'%name, 'w') as train, open('%s.test.csv'%name, 'w') as test:
        for iline in dio.io():
            if random.random() < ratio:
                test.write(iline)
            else:
                train.write(iline)


if __name__ == "__main__":
    dio.now('sample')
