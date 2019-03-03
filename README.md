# tool4nc 

Python module (in Development) containing functions for simplifing the netCDF files manipulations/visualization.

## Dependencies:

In the setup.py it is possible have a look to all the dependencies required and they are listed below:

[x] netCDF4>=1.4.2
[x] csv342>=1.0.0 
[x] pandas>=0.23.4 
[x] xarray>=0.11.0 
[x] csv342>=1.0.0
[x] shapely>=1.6.4.post2
[x] fiona>=1.8.4
[x] cdo>=1.4.0

## Be aware that:

The tool is in development so it can be possible find bugs, errors and imprecisions. Please to report them if you find one. In the speciphic the major improvment need to be done with:
   
## Installation:

To use this software is suggested the creation of a python environment (python ~=3.6). It becames mandatory if your python version is part of the 2.* family. Following few basic instructions if interesed to install the module in a new ad-hoc environment.

### Procedure for the Anaconda python distribution:

- conda update conda (To update the Anaconda distribution)

- conda create -n {your_env_name} python=3.6 (For the creation of a python environment)

- conda list (List all the environments installed)

- conda activate {your_env_name} (Activate the chosen environment)

- conda activate (Come back to the initial environment)

### Procedure for the standard python distribution:

- pip install pipenv (installation of the package needed)

- create project folder 

- pipenv pipenv --python 3.6 (Install the python environment inside the project folder)


### tool4nc installation using:

- pip install tool4nc: 

For Anaconda users and the command can be executed from every path locations. 
 
- pipenv install tool4nc:

For python standard distribution users. The command needs to be run inside the project folder.


## Functions included:

### nctocsv ("path_input file", "path_output folder")

This function converts a netCDF file to a csv file. It will generate two csv files called file.csv and file_cleaned.csv respectively. The file_cleaned.csv is cleaned by all the NAN values and it is considered the final output file of this function.


### nctoshape ("path_input file", "path_output folder", "variable_name")

This function converts a netCDF file into a shape file (Point features). Firstly, it will generate two csv files called file.csv and file_cleaned.csv respectively. After that, the file_cleaned.csv (purified by all the NAN values) is used to extract the corresponding shapefile representing a variable’s values which is the third argument of this function.


### concatnc ("path_input folder")

This function can concatenate segments of data coming from the same dataset but at different time steps. It will generate a file called “concatenated.nc” as result. The only argument needed is the folder where the files are located.


### splitnc ("path_input file",  "path_output folder", "type", "suffix")

This function can split the data by type; DAY (DD), MONTH (YYYYMM) and YEAR (YYYY). It gives the option to add a suffix to the generated data.


### plotintime ("path_input file","variable_name","path_output folder",frame_for_second)

This fuction is able to generate a dynamic plot showing the variation of the selected variable in fuction of the time steps recorded into. 


## Case examples:


### I have many netCDF files and I would like to convert all of them in CSV: 

```
import os
from tool4nc import nctocsv

Input_DIR = 'the/directory/you/want/to/use'
Out_DIR = 'the/directory/you/want/to/use'

for filename in os.listdir(Input_DIR):
    if filename.endswith(".nc"):
       nctocsv (filename, Out_DIR)

```

### I want to overlay in my GIS project (as shape-file) data from a variable which is contained in my netCDF file:

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

### I have a folder with a month of data divided in daily files. These files are downloaded from the same dataset (which contains just one depth information). I would like to concatenate all the daily files in a montly one. I also would like realise an animated plot showing the variation of a variable in fuction of the time:


```
from tool4nc import concatnc, plotintime

Input_DIR = 'the/directory/where/you/store/the/daily/file'
Out_DIR = 'the/directory/you/want/to/output/the/results'
Variable_name = "name-variable-to-investigate"
frame_for_second = 9  

concatnc (Input_DIR) #it will generate the concatenated.nc file

plotintime ("path_to/concatenated.nc", Variable_name, Out_DIR, frame_for_second) #This function produces both an animated .gif and an .mp4 video

```

### I have one year file but i realised that it is better have the data organised by Month. Furthermore, I would like also add a suffix to each file:

```
from tool4nc import slitnc

Input_file = 'the/path/of/your/input/file'
Out_DIR = 'the/directory/you/want/to/output/the/results'
type = "MONTH"
suffix = "text/to/append/at/each/file"


splitnc (Input_file, Out_DIR, type, suffix)

```










