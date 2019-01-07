#!python3
# updateProduce.py - Corrects costs in produce sales spreadsheet.

import os, openpyxl

# Opening up excel sheet with product sales 
os.chdir("C:/Users/sherm/OneDrive/Desktop/automate_online-materials")
wb = openpyxl.load_workbook('produceSales.xlsx')
ws = wb.active

# Key: product to have price updated, value: price to be updated 
price_updates = {'Garlic': 3.07,
                'Celery': 1.19,
                'Lemon': 1.27}

# iterating through rows of sheet to update prices 
for row in ws.iter_rows(min_row=2, max_col=2):
    product_cell = row[0]
    price_cell = row[1]
    # Iterate through price updates dictionary
    if product_cell.value in price_updates:
        # If the row's product is in the dictionary, the product's price will be updated 
        price_cell.value = price_updates[product_cell.value]

# Saving the new document in the same folder as the program (just a personal preference)
os.chdir("C:/Users/sherm/OneDrive/Desktop/ATBS-Python/chapter-12-excel")
wb.save('updatedProduceSales.xlsx')            
