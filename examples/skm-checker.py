#!/usr/bin/env python
# -*- coding: utf-8 -*-


import csv
import datetime

skm_data = []

with open('skm.csv','r') as f1:
    reader = csv.reader(f1, delimiter='\t',lineterminator='\n',)

    #read skm data
    for row in reader:
        data_row = row[:]
        train_time = row[0].split(':')
        if datetime.datetime.now().time() <= datetime.time(hour=int(train_time[0]), minute=int(train_time[1])):
            skm_data.append(data_row)


with open('skm.csv','w') as f1:
    writer = csv.writer(f1, delimiter='\t',lineterminator='\n',)

    #write data to csv
    for index, el in enumerate(skm_data):
        writer.writerow(el)
