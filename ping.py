import os, sys, urllib2

file_path = sys.argv[1]
file  = open(file_path, "rb")

for line in file.readlines():
    
    status = ""
    netid = line.replace("\n","")
    url = "http://www.princeton.edu/~"+netid+"/"

    
    # get status code
    try:

        connection = urllib2.urlopen(url)
        code = connection.getcode()

        if code == 200:
            html = connection.read()
            needle = "Index of /~"+netid
            if needle in html:
                status = "N"

        connection.close()
   
    except urllib2.HTTPError, e:
        code = e.getcode()

    print netid + "," + str(code) + "," + status

    