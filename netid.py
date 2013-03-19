
import os, sys, csv

file_path = sys.argv[1]
file  = open(file_path, "rU")
reader = csv.reader(file)

header = True
netids = []

for row in reader:
    
    if header:
        header = False
        continue

    netid = row[2].split("@")[0]
    netids.append(netid)

for netid in netids:

    print netid