import csv

with open('PeriodicTable.csv', newline='') as File:  
    reader = csv.reader(File)
    c = 0
    for row in reader:
        while c < 28:
            print(row[c])
            c += 1
        break
