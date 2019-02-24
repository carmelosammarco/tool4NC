# tool4netcdf Package

Functions available:

## -nctocsv (“path_input file”, “path_output folder”): 

This function converts a netCDF file to a csv file. It will generate two csv files called file.csv and file_cleaned.csv respectively. The file_cleaned.csv is cleaned by all the NAN values and it is considered the final output file of this function.

## -nctoshape (“path_input file”, “path_output folder”, “variable”):

This function converts a netCDF file to a shape file. Firstly It will generate two csv files called file.csv and file_cleaned.csv respectively. After that, the file_cleaned.csv ( purified by all the NAN values) is used to extract the corresponding shapefile representing a variable's values which is the third argument of this function.

## -concatnc (“path_input folder”):

This function can concatenate segments of data coming from the same dataset but at different time steps. It will generate a file called "concatenated.nc" as result. The only argument needed is the folder where the files are located.

## -splitnc(“path_input file”, “path_output folder”,"type", suffix"):

This fuction is able to split the data by day(DD), months(YYYYMM) and years(YYYY).It gives the option to add a suffix to the so generated data.
