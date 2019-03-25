#!/usr/bin/python
import csv

provides = {}
demands = {}
avgs = {'cardcost':[], 'goldcost':[], 'contract':[], 'provisions':[]}
businesses = {}
events = {}
opposers = {}
cards = 0

def printstats(age):
    global businesses, provides, demands, events, cards, opposers

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

    print "Opposers: ",
    for d in opposers:
        sortedProvisions = ''.join(sorted(opposers[d]))
        print "%s: %s"%(d, sortedProvisions),
    print
    opposers = {}

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
        provisionFields = ['provides1*=blank', 'provides2*=blank', 'provides3*=blank']
        for p in provisionFields:
            if row[p]:
                provisions += 1
                provides.setdefault(row[p], 0)
                provides[row[p]] += 1
                if row[p] == row['demands=blank']:
                    samesames.append(row['name'])
        avgs['provisions'].append(provisions)

        d = 'demands=blank'
        if row[d]:
            opposers.setdefault(row[d], '')
            for p in provisionFields:
                if row[p] == 'food':
                    opposers[row[d]] += 'f'
                elif row[p] == 'science':
                    opposers[row[d]] += 's'
                elif row[p] == 'happiness':
                    opposers[row[d]] += 'h'
                elif row[p] in ['clubs', 'spears', 'axes', 'swords']:
                    opposers[row[d]] += 'w'
                elif row[p] == 'hides':
                    opposers[row[d]] += '1'
                elif row[p] == 'stone':
                    opposers[row[d]] += '2'
                elif row[p] == 'bronze':
                    opposers[row[d]] += '3'
                elif row[p] == 'iron':
                    opposers[row[d]] += '4'


    printstats(prevAge)

    print "\nCards that demand what they provide:"
    for s in samesames:
        print s,
    print

