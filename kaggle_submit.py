#!/usr/bin/env python
import fileinput


def format():
    print "Id,Predicted"
    for iline in fileinput.input():
        id, p = iline.split(',')
        id = id.strip()
        p = p.strip()
        print "%s,%s" % (id, p)


if __name__ == "__main__":
    format()
