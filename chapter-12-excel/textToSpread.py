#!python3 
# program to read in the contents of several text files (you can make the text files yourself) 
# and insert those contents into a spreadsheet, with one line of text per row. The lines of the 
# first text file will be in the cells of column A, the lines of the second text file will be in the cells of column B, and so on.
# program will be executed via the command line. Give command line arguments for text files to be read 

import os, sys, openpyxl

try:
    assert len(sys.argv) > 1
    for file in sys.argv[1:]:
        assert file.endswith('.txt')
        assert (os.path.exists(file))
except AssertionError:
    print("Command line argument is not valid. Enter at least one valid text file")
    quit()

files = sys.argv[1:]

wb = openpyxl.Workbook()
ws = wb.active 

col = 1 
for file in files:
    print("Converting file: " + file)
    fileObj = open(os.path.abspath(file), "r")
    row = 1 
    for line in fileObj.readlines():
        ws.cell(row=row, column=col, value=line)
        row += 1 
    col += 1 

fileObj.close()
wb.save("newspread.xlsx")
print("Done.")
