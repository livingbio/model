#!/usr/bin/env python

import dio
import random

def sample(ratio):
    ratio = 0.99
    with open('train.samples.csv', 'w') as train, open('test.samples.csv', 'w') as test:
        for iline in dio.io():
            if random.random() < ratio:
                test.write(iline)
            else:
                train.write(iline)


if __name__ == "__main__":
    import clime.now()

