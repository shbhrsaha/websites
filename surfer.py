import os, sys, csv

file_path = sys.argv[1]
file  = open(file_path, "rb")
reader = csv.reader(file)

for row in reader:
    
    netid = row[0]
    code = int(row[1])
    state = row[2]

    if state != "N" and code == 200:
        print "\""+netid+"\","