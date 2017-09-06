import csv
'''\
with open('random.csv', 'r') as c:
    r = csv.reader(c)
    for lines in r:
        print(lines)
'''

'''\
with open('random.csv', 'w') as random:
    wr = csv.writer(random, delimiter=',')
    wr.writerow(['raunak', 'joshi'])
    wr.writerow(['mritunjay', 'musale'])
    wr.writerow(['sanket', 'shelar'])

'''

with open('dict.csv', 'r') as d:
    r = csv.DictReader(d)
    for rows in r:
        print(rows['firstname'])
'''\
with open('dict.csv', 'w') as dictf:
    f = ['firstname', 'lastname']
    wd = csv.DictWriter(dictf, fieldnames=f)
    wd.writeheader()
    wd.writerow({'firstname':'raunak', 'lastname':'joshi'})
    wd.writerow({'firstname':'amit', 'lastname':'dubey'})
'''    
