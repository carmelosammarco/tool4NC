from tool4nc import * 
import os
import glob

test_folder = "Test/"
Output_folder = "Test/OUT"

file_to_use = "VHM0.nc"
Variable = "VHM0"

nctocsv(file_to_use, Output_folder)
nctoshape(file_to_use, Output_folder, Variable)
nctogdr(file_to_use, Output_folder)
splitnc(file_to_use, Output_folder, "DAY", "Test")

results = glob.glob("Test/OUT/*")
for f in results:
    os.remove(f)





