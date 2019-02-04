#!/usr/bin/python

import csv

with open('../cards/civcitizen.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    provides = {}
    demands = {}
    avgs = {'cardcost':[], 'goldcost':[], 'contract':[]}
    prevAge = None

    for row in reader:
        if prevAge and row['age*'] != prevAge:
            print "\nAge ",prevAge
            print 'Provides:',
            for p in provides:
                print "(%s: %s)"%(p, provides[p]),
            print
            print "Demands:",
            for d in demands:
                print "(%s: %s)"%(d, demands[d]),
            print
            print "Averages:",
            for a in avgs:
                print "%s:"%a, round(sum(avgs[a])/float(len(avgs[a])), 1),
                avgs[a] = []
            print

        prevAge = row['age*']


        for a in avgs:
            avgs[a].append(float(row[a]))

        for p in ['provides1*=blank', 'provides2*=blank', 'provides3*=blank']:
            if row[p]:
                provides.setdefault(row[p], 0)
                provides[row[p]] += 1

        d = 'demands=blank'
        if row[d]:
            demands.setdefault(row[d], 0)
            demands[row[d]] += 1

        d = 'barb?'
        if row[d]:
            demands.setdefault(d, 0)
            demands[d] += 1


