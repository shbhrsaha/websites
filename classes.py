import os, sys, csv

# LOAD CLASSES INTO LOOKUP DICTIONARY
file_path = sys.argv[2]
file  = open(file_path, "rU")
reader = csv.reader(file)

header = True
classLookup = {}

for row in reader:
    
    if header:
        header = False
        continue
    
    netid = row[2].split("@")[0]
    classes = row[3]

    classLookup[netid] = classes


# COMPUTE CLASS FREQUENCY

classCounts = {}

file_path = sys.argv[1]
file  = open(file_path, "rb")
reader = csv.reader(file)

for row in reader:
    
    netid = row[0]
    code = int(row[1])
    state = row[2]

    if state != "N" and code == 200:

        classes = classLookup[netid]

        if classes in classCounts.keys():
            classCounts[classes] += 1
        else:
            classCounts[classes] = 1

# PRINT CLASS FREQUENCY
print "class,frequency"
for c in classCounts.keys():

    print c + "," + str(classCounts[c])