#!python3 
#program will invert the row and column of the cells in the spreadsheet. 
# For example, the value at row 5, column 3 will be at row 3, column 5 (and vice versa).

import os, sys, openpyxl

try:
    assert (os.path.exists(sys.argv[1]))
    assert sys.argv[1].endswith('.xlsx')
except AssertionError:
    print("Command line argument is not valid. Enter a valid filename")
    quit()

filename = sys.argv[1]

wb = openpyxl.load_workbook(filename)
ws = wb.active

newWorkbook = openpyxl.Workbook()
newSheet = newWorkbook.active

print("Inverting file...")
# Iterating through each cell and assigning its value to the cell with inverted coordinates in new sheet
for row_num in range(1, ws.max_row+1):
    for col_num in range(1, ws.max_column+1):
        cell_value = ws.cell(row=row_num, column=col_num).value 
        # Assigning the cell value with this coordinate to the new sheet with inverted coordinates 
        newSheet.cell(row=col_num, column=row_num, value=cell_value)

newWorkbook.save("inverted" + filename)        
print("Completed.")