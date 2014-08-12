#!/usr/bin/env python

import json
import fileinput
import csv
import sys

fields = ['user', 'imp', 'type', 'publisher', 'advertiser', 'slot', 'creative', 'qm', 'qp', 'features', 'time', 'device_type', 'device', 'touch', 'browser', 'os']



def merge():
    import fileinput
    write = csv.DictWriter(sys.stdout, fields+['click'])
#    write.writeheader()
    reader = csv.DictReader(iter(sys.stdin.readline, ""), fields)
    last = {}
    click = 0
    for data in reader:
        if data['type'] == 'click': 
            click += 1

        if last.get('imp') != data['imp']:
            last['click'] = click
            last['type'] = 'imp'
            write.writerow(last)
            last = data
            click = 0

merge()
