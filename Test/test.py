from tool4nc import * 
import os
import glob

test_folder = os.path.join("Test")
Output_folder = os.path.join("Test", "OUT")

file_to_use = test_folder + "/VHM0.nc"
Variable = "VHM0"

#nctocsv(file_to_use, Output_folder)
#nctoshape(file_to_use, Output_folder, Variable)
#nctogdr(file_to_use, Output_folder)
#splitnc(file_to_use, Output_folder, "DAY", "Test")

files = glob.glob(Output_folder + "/*")
for f in files:
    os.remove(f)





