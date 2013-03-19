
INTRODUCTION
============
These are the Python scripts used in the "Who at Princeton has a web site?" project at http://www.princeton.edu/~saha/websites/

USAGE
=====

Percentage of Students Who Have Web Site
----------------------------------------
- Run "python netid.py everyone.csv > netid.txt"
- Run "python ping.py netid.txt > netidstatus.txt"
- Use surfer.py and count lines to make SVG

Student Website Surfer
----------------------
- Generate netidstatus.txt, as described above
- Run "python surfer.py netidstatus.txt > surfer.txt"
- Paste that into explorer.html

Web Sites by Major
------------------
- Run "python majors.py netidstatus.txt everyone.csv > majors.csv"
- Use Nodebox

Web Sites by Class
------------------
- Run "python classes.py netidstatus.txt everyone.csv > classes.csv"
- Use Nodebox