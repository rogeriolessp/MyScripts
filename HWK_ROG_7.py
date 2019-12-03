import argparse
import os.path as op
import csv
import matplotlib.pyplot as plt
import numpy as np 
import re

def convert_type(data_val):
    try:
        return int(data_val)
    except ValueError:
        try:
            return float(data_val)
        except ValueError:
            return data_val

def lines_to_dict(lines, header = False)
if header:
    column_titless = lines [0]
    lines = lines [1:]
 else:
    column_titless = list(range(1, len(lines[0])+1))

data_dict = {}
for idx, column in enumerate(column_titles):
    data_dict[column] = []
    for row in lines:
        data_dict[column] += [row[idx]]
    return data_dict

def parse_file(data_file, delimiter, debug = False):
    #check if file exists
    isFile = os.path.isfile(path)
    assert(op.isfile(data_file))
   
    print (isFile)

# using Tibault interesting way to deal with delimiters

def format_row(row):
    if "," in row:
        row = row
    else:
        row = " ".join(row.split())
        row = row.replace(" ", ",")
    return row

    #opening a csv and checking the delimiters, etc.
with open(data_file, 'r') as fhandler:
    reader = csv.reader(fhandler, delimiter = delimiter)
        #reader = csv.reader(f)
    for row in reader:
        print (row)
  


    #adding each line in the file to a list:
    lines = []
    if debug:
        count = 0
    for line in reader:
        if debug:
            if count > 2:
                break
            count += 1
        newline = []
        for value in line:
            newline += [convert_type(value)]

        if len(newline) > 0:
            lines += [newline]
return lines # this part is being a headache because it is giving me all sorts of errors
    #returns alll contentes to a file
# argparse arguments:


def generete_points(coefs, min_val, max_val):
    xs = np.arange(min_val, max_val, (max_val-min_val)/100)
    return xs, np.polyval(coefs, xs)

def plot_data(dd, debug=False, polys=[1,2,3,4]): # dd = data_dict., debug does not plot
    if debug:
        number_combinations = 0

    ncols = len(dd.keys())

    if not debug:
        fig = plt.Figure(figsize = (30,30))
    for i1, column1 in enumerate(dd.keys()):
        for i2, column2 in enumerate(dd.keys():)
        if debug:
            number_combinations += 1
            print(column1, column2) # this gave me unexpected ident errors and a non defined function then it worked fine
            # import pdb (ver)
            # pdb.set_trace() (ver)
        else:
            # if my grid is:
            # 1 2 3 4 5 
            # 6 7 8 9 10
            # 11 12 13 14 15
            # in this case I index at i1*ncols + i2 (+1)
            loc = i1*ncols = i2 + 1
            plt.subplot(ncols, ncols, loc)
            x = data_dict[column1]
            y = data_dict[column2]
            
            plt.scatter(x,y)
            plt.xlabel(column1)
            plt.ylabel(column2)
            plt.title("{0} x {1}".format(column1, column2))

            for poly_order in polys:
                coefs = np.polyfit(x, y, poly_order)
                xs, new_line = generete_points(coefs, min(x)) ########
                plt.plot(xs, new_line)

        if not debug:
            plt.legend()
            plt.tight_layout()
            plt.show()
            plt.savefig("./my_plairs_of_plots.png")
        if debug:
            print(len(data_dict.keys())), number_combinations)
            return 0

def main():
    parser = argparser.ArgumentParser()
        parser.add_argument('input_data_file', type = str,
                        help = 'Input CSV data file for plotting')
    parser.add_argument('delimiter', type = str,
                        help = 'delimiter used in file')
    parser.add_argument('-x', '--debug', action = 'store_true',
                        help = 'determs if there is a header')
    args = parser.parse_args()
    my_data = parse_file(args.data_file, args.delimiter, debug = args.debug)
    data_dict = lines_to_dict(my_data, header = args.header)
    print(data_dict)
    plot_data(data_dict, debug = args.debug)

if __name__ == "__main__":
    main()









