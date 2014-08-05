#!/usr/bin/env python

import fileinput
import random

def sample():
    with open('train.samples.csv', 'w') as train, open('test.samples.csv', 'w') as test:
        for iline in fileinput.input():
            if random.random() < 0.1:
                test.write(iline)
            else:
                train.write(iline)


if __name__ == "__main__":
    sample() 

