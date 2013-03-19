import os, sys, csv

# LOAD MAJORS INTO LOOKUP DICTIONARY
file_path = sys.argv[2]
file  = open(file_path, "rU")
reader = csv.reader(file)

header = True
majorLookup = {}

for row in reader:
    
    if header:
        header = False
        continue
    
    netid = row[2].split("@")[0]
    major = row[5]

    majorLookup[netid] = major


# COMPUTE MAJOR FREQUENCY

majorCounts = {}

file_path = sys.argv[1]
file  = open(file_path, "rb")
reader = csv.reader(file)

for row in reader:
    
    netid = row[0]
    code = int(row[1])
    state = row[2]

    if state != "N" and code == 200:

        major = majorLookup[netid]

        if major in majorCounts.keys():
            majorCounts[major] += 1
        else:
            majorCounts[major] = 1

# PRINT MAJOR FREQUENCY
print "major,frequency"
for m in majorCounts.keys():

    print m + "," + str(majorCounts[m])