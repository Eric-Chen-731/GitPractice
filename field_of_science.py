#!/usr/bin/python

# field_of_science.py
# Authors: Rich Knepper,
# date: 12/12/2019

# pull in the XSEDE award listing and extract a list of fields of science
#
# file structure:
# 0. Organization
# 1. Charge_number
# 2. FOS
# 3. Resource
# 4. Start_Date
# 5. End_Date
# 6. Allocation amount
# 7. Remaining SUs

# pull in modules that we use
import sys
import csv

# get filename from command-line arguments

filename = sys.argv[1]

# debug: print filename

fields_of_science = {}

with open(filename) as csvfile:
    allocations = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(allocations)
    for row in allocations:
        if row[2] not in fields_of_science:
            fields_of_science.append(row[2]) and fields_of_science[row[2]] = 1
        else:
            fields_of_science[row[2]] += 1 

fields_of_science.sort()

for field in fields_of_science:
    print field



  Alternatively (list into dictionary):
with open(filename) as csvfile:
    allocations = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(allocations)
    for row in allocations:
        fields_of_science.append(row[2])
fields_of_science.sort()

FOSfrequency = {}
for field in fields_of_science:
    if field not in FOSfrequency:
        FOSfrequency[field] = 1
    else:
        FOSfrequency[field] += 1
print(FOSfrequency)

sort_FOS = sorted(FOS.items(),
key = lambda x: x[1], reverse = True)

for element in sort_FOS:
    print(element[0],"::",element[1])
    wdwjowjkwodkowkowdokd