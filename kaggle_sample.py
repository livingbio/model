#!/usr/bin/env python

import fileinput
import random

def sample():
    ratio = 0.01
    with open('train.samples.csv', 'w') as train, open('test.samples.csv', 'w') as test:
        for iline in fileinput.input():
            if random.random() < ratio:
                test.write(iline)
            else:
                train.write(iline)


if __name__ == "__main__":
    sample() 

