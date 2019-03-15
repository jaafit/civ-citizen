#!/usr/bin/python
import csv

provides = {}
demands = {}
avgs = {'cardcost':[], 'goldcost':[], 'contract':[], 'provisions':[]}
businesses = {}
events = {}
cards = 0

def printstats(age):
    global businesses, provides, demands, events, cards

    print "\nAge ",age,cards,'cards'
    cards = 0
    print 'Provides:',
    for p in provides:
        print "(%s: %s)"%(p, provides[p]),
    print
    provides = {}
    print "Demands:",
    for d in demands:
        print "(%s: %s)"%(d, demands[d]),
    print
    demands = {}
    print "Averages:",
    for a in avgs:
        print "%s:"%a, round(sum(avgs[a])/float(len(avgs[a])), 1),
        avgs[a] = []
    print

    print "Businesses:",
    for b in businesses:
        if businesses[b] > 1:
            print "%d %s, "%(businesses[b], b),
        else:
            print "%s, "%(b),
    print
    businesses = {}


    print "Events:",
    for b in events:
        if events[b] > 1:
            print "%d %s, "%(events[b], b),
        else:
            print "%s, "%(b),
    print
    events = {}


with open('../cards/civcitizen.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    prevAge = None

    samesames = []

    for row in reader:

        if prevAge is not None and row['age*'] != prevAge:
            printstats(prevAge)

        prevAge = row['age*']

        cards += 1

        businesses.setdefault(row['name'], 0)
        businesses[row['name']] += 1

        events.setdefault(row['event'], 0)
        events[row['event']] += 1

        for a in ['cardcost', 'goldcost', 'contract']:
            if row[a]:
                avgs[a].append(float(row[a]))

        for d in ['demands=blank', 'demands2=blank']:
            if row[d]:
                demands.setdefault(row[d], 0)
                demands[row[d]] += 1

        provisions = 0
        for p in ['provides1*=blank', 'provides2*=blank', 'provides3*=blank']:
            if row[p]:
                provisions += 1
                provides.setdefault(row[p], 0)
                provides[row[p]] += 1
                if row[p] == row[d]:
                    samesames.append(row['name'])
        avgs['provisions'].append(provisions)

    printstats(prevAge)

    print "Cards that demand what they provide:"
    for s in samesames:
        print s,
    print

