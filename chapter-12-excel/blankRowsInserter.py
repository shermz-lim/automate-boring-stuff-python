# !python3
# blankRowInserter.py takes two integers and a filename string as command
# line arguments. Let’s call the first integer N and the second integer M. 
# Starting at row N, the program should insert M blank rows into the spreadsheet.

import os, sys, openpyxl

# Make sure command line argument is valid 

try:
    assert len(sys.argv) == 4
    assert (type(int(sys.argv[1])) == int and type(int(sys.argv[2])) == int)
    assert (os.path.exists(sys.argv[3]))
    assert sys.argv[3].endswith('.xlsx')
except AssertionError:
    print("Command line argument is not valid. Try again. Insert 3 arguments: Row number to start insertion, Number of rows to insert, and excel file you want to have rows inserted.") 
    quit()   

filename = sys.argv[3]

N = int(sys.argv[1])
M = int(sys.argv[2])
# Moving to directory with the file 
directory = os.path.dirname(os.path.abspath(filename))
os.chdir(directory)

# Opening up worksheet 
wb = openpyxl.load_workbook(filename)
ws = wb.active 
newWb = openpyxl.Workbook()
newSheet = newWb.active

print("Starting to insert rows...")
for row in ws.iter_rows(min_row=1, max_row=N):
    for cell in row:
        coordinates = cell.coordinate 
        newSheet[coordinates] = cell.value 
print("Inserting rows...")
for row in ws.iter_rows(min_row=N+1):
    for cell in row:
        newCellRow = str(int(cell.row) + M) 
        newSheet[cell.column + newCellRow] = cell.value

# Overrides the existing file 
newWb.save(filename)        
print("Done.")



