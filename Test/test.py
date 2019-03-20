from tool4nc import *
from pathlib import Path, PureWindowsPath 
import os
import glob

test_folder = Path("Test/")
Output_folder = Path("Test/OUT")

test_folder_pathwindow = PureWindowsPath(test_folder)
OUT_pathwindow = PureWindowsPath(Output_folder)

file_to_use = test_folder / "VHM0.nc"
Variable = "VHM0"

nctocsv(file_to_use, Output_folder)
nctoshape(file_to_use, Output_folder, Variable)
nctogdr(file_to_use, Output_folder)
splitnc(file_to_use, Output_folder, "DAY", "Test")

files = glob.glob(Output_folder + "/*")
for f in files:
    os.remove(f)





