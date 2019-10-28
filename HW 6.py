# importing libraries:

import argparse
import os.path as op
import os
import csv
import matplotlib.pyplot as plt
import numpy as np

# converting a function to make data usable

def convert_type (data_value):
    try:
        return int(data_value)
    except ValueError:
        try:
            return float(data_value)
        except ValueError:
            return data_value

# Getting headers, from Clara's homework:
def top_headers(list_of_lists):
    need_header = True
    for row in list_of_lists[1:]:
        if type(list_of_lists[0][0]) = type(row[0]):
            continue
        else:
            need_header = False
            break
    if need_header == True:
        header_fn []
        row=list_of_lists[0]
        for counter,value in enumerate(row):
            header_fn += ["Column " + str(counter + 1)]
            return header_fn
        else:
            return None

# checking if the filepath exists because I have been having to much throuble with filepaths,
#  which cost me the time to finish the homework and learn from it:

    path = "C:\\Users\\Rogerio\\Documents\\Big Data Diploma\\CEBD 1100\\Homework\\Homework week 6\\hwk4_data\\wpbc.data"

isFile = os.path.isfile(path)
print (isFile)

# since the path is correct let's keep going:


filenames = ["C:\\Users\\Rogerio\\Documents\\Big Data Diploma\\CEBD 1100\\Homework\\Homework week 6\\hwk4_data\\wpbc.data"]
#filenames = ["C:\\Users\\Rogerio\\Documents\\Big Data Diploma\\CEBD 1100\\Homework\\Homework week 6\\hwk4_data\\wbpc.names"]

if len(filenames) > 1:
        data = open(filenames[0], 'r')
        names = open(filenames[1], 'r')
else:
    data = open(filenames[0], 'r')
    names = None
my_read_data = data.read()
print(my_read_data)

my_read_dataS = my_read_data.split('\n')

outer_list = []
for row in my_read_dataS:
    row_list = []
    for element in row.split(" "):
        new_element = convert_type(element)
        if new_element is not None:
            row_list.append(new_element)
        print(element, end = "\t")
        print(new_element, type(new_element))
        print(row_list)
    if len(row_list) > 0:
        outer_list += [row_list]


def parse_files(data_file, delimiter, debug=False):
    # Checking the files:
    assert(op.isfile(data_file))
    
    # Oppening as csv:
    csv_reader = csv.reader(fhandle, delimiter = delimiter)

"""
# Dictionary of lists:
our_dictionary = {}

for location, colunm_headings in enumerate(outer_list[0]):
    print(colunm_headings)
    our_dictionary[colunm_headings] = list()
    for row in outer_list[1:]:
        our_dictionary[colunm_headings] += [row[location]]
print(our_dictionary)



