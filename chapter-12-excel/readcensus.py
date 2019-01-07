#!python3

import os, openpyxl, pprint

# Setting census excel sheet as a sheet object
os.chdir("C:/Users/sherm/OneDrive/Desktop/automate_online-materials")
censusWb = openpyxl.load_workbook("censuspopdata.xlsx")
censusSheet = censusWb.active


countyData = {}

# Iterating through each row in the census data 
for row in list(censusSheet.rows)[1:]:
    state = row[1].value
    county = row[2].value
    pop = row[3].value 
    # Checking whether countyData contains the state and getting it. If not, set the key as state with a value of an empty dict
    countyData.setdefault(state, {})
    # Checks whether countyData[state] contains the county and getting it. If not, set the county as a new key with a value of 0 censustract, and 0 population.
    countyData[state].setdefault(county, {'censustract': 0, 'pop': 0})
    # Adding 1 to censustract for the county 
    countyData[state][county]['censustract'] += 1
    # Adding population count to county's population  
    countyData[state][county]['pop'] += pop 

# Writing it to a txt file 
# Creating & writing to the file (censusdata in same folder as py file)

# os.chdir("C:/Users/sherm/OneDrive/Desktop/ATBS-Python/chapter-12-excel")
# censusFile = open('censusdata.txt', 'w')

# print("Writing results...")
# for state in countyData:
#     censusFile.write(state)
#     censusFile.write("\n=======================\n")
#     for county in countyData[state]:
#         censusFile.write("{}: Total census tracts = {}, population = {}.\n".format(county, countyData[state][county]['censustract'], countyData[state][county]['pop']))
#     censusFile.write("=======================\n\n\n")        
# print("Done.")
# censusFile.close()

# Writing it to a py file to be imported and used using pprint
os.chdir("C:/Users/sherm/OneDrive/Desktop/ATBS-Python/chapter-12-excel")
censusFile = open('censusdata.py', 'w')
print("Writing results...")
censusFile.write("allData = " + pprint.pformat(countyData))
print("Done.")
censusFile.close()