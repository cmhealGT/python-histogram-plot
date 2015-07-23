import csv
f = open('Raw.csv')
csv_f = csv.reader(f)

for row in csv_f:
    print row