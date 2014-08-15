#!/usr/bin/env python

import json
import fileinput
import csv
import sys

fields = ['user', 'imp', 'type', 'publisher', 'advertiser', 'slot', 'creative', 'qm', 'qp', 'features', 'time', 'device_type', 'device', 'touch', 'browser', 'os']

def parser():
    import fileinput
    write = csv.DictWriter(sys.stdout, fields)
#    write.writeheader()
    for line in fileinput.input():
    #for line in datas:
        data = json.loads(line)
        tmp = {}
        try:
            

            tmp['device_type'], tmp['touch'], tmp['device'], tmp['os'], tmp['browser'] = data.get('user_agent').split(':')
            tmp['advertiser'] = data['items'].pop()['advertiser']
            tmp['publisher'] = data.get('publisher', 'none')
            tmp['features'] = ".".join((data.get('features', [])))
            tmp['time'] = data.get('start_time')
            tmp['imp'] = data.get('imp')
            tmp['user'] = data.get('user')
            tmp['slot'] = data.get('slot')
            tmp['creative'] = data.get('creative')
            tmp['qm'] = data.get('qm')
            tmp['qp'] = data.get('qp')
            
            assert tmp['imp'], 'no imp id'

            if data['type'] == 'event' and data['ext'] == 'content_click':
                tmp['type'] = 'click'
            elif data['type'] == 'page':
                tmp['type'] = 'imp'
            else:
                raise Exception('none')
            write.writerow(tmp)

        except Exception as e:
            pass

parser()
