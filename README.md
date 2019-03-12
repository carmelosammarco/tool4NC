# tool4nc

Python module containing functions for simplifing the netCDF files manipulations. It is designed to work in Unix operative systems. if you wish use this module in a Windows operative environment please to refer to [tool4nc-win](https://pypi.org/project/tool4nc-win/).

## Dependencies:

The dependencies required are listed below:

- [x] netCDF4>=1.4.2
- [x] csv342>=1.0.0 
- [x] pandas>=0.23.4 
- [x] xarray>=0.11.0 
- [x] shapely>=1.6.4.post2
- [x] fiona>=1.8.4
- [x] cdo>=1.4.0


## Be aware that:

The tool is in development so it can be possible find bugs, errors and imprecisions. Please to report them if you find one.
 

## Installation:

To use this module is suggested python ~=3.6. Following the command to install the module:

```
pip install tool4nc
```

## Functions included:


### nctocsv ("path_input file", "path_output folder")

This function converts a netCDF file to a csv file. It will generate two csv files called file.csv and file_cleaned.csv respectively. The file_cleaned.csv is cleaned by all the NAN values and it is considered the final output file of this function.


### nctoshape ("path_input file", "path_output folder", "variable_name")

This function converts a netCDF file into a shape file (Point features). Firstly, it will generate two csv files called file.csv and file_cleaned.csv respectively. After that, the file_cleaned.csv (purified by all the NAN values) is used to extract the corresponding shapefile representing a variable’s values which is the third argument of this function.

### nctogdr ("path_input file", "path_output folder")

This fuction convert a netCDF file to a GRD file which is required for some computations.


### concatnc ("path_input folder")

This function is qble to concatenate segments of data coming from the same dataset but at different time steps. It will generate a file called concatenated.nc as final result. The only argument needed is the folder where the files are located.


### splitnc ("path_input file",  "path_output folder", "type", "suffix")

This function can split the data by type; DAY (DD), MONTH (YYYYMM) and YEAR (YYYY). It gives the option to add a suffix to the generated data. 


# Case examples:

## I have many netCDF files and I would like to convert all of them in CSV: 

```
import os
from tool4nc import nctocsv

Input_DIR = 'the/directory/you/want/to/use'
Out_DIR = 'the/directory/you/want/to/use'

for filename in os.listdir(Input_DIR):
    if filename.endswith(".nc"):
       nctocsv (filename, Out_DIR)
```

## I want to overlay in my GIS project (as shape-file) data from a variable which is contained in my netCDF file:

```
import os
from tool4nc import nctoshape

Input_DIR = 'the/directory/you/want/to/use'
Out_DIR = 'the/directory/you/want/to/use'
Variable = ‘Variable name’

for filename in os.listdir(Input_DIR):
    if filename.endswith(".nc"):
       nctoshape (filename, Out_DIR, Variable)
```

## I have a folder with a month of data divided in daily files. These files are downloaded from the same dataset and I would like to concatenate all the daily files in a montly one:

```
from tool4nc import concatnc, plotintime

Input_DIR = 'the/directory/where/you/store/the/daily/file'

concatnc (Input_DIR) #it will generate the concatenated.nc file
```

## I have many netCDF files and I would like to convert all of them in GRD: 

```
import os
from tool4nc import nctogrd

Input_DIR = 'the/directory/you/want/to/use'
Out_DIR = 'the/directory/you/want/to/use'

for filename in os.listdir(Input_DIR):
    if filename.endswith(".nc"):
       nctogdr (filename, Out_DIR)
```

## I have one year file but i realised that it is better have the data organised by Month. Furthermore, I would like also add a suffix to each file:

```
from tool4nc import slitnc

Input_file = 'the/path/of/your/input/file'
Out_DIR = 'the/directory/you/want/to/output/the/results'
type = "MONTH"
suffix = "text/to/append/at/each/file"


splitnc (Input_file, Out_DIR, type, suffix)
```










