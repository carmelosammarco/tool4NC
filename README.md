
# tool4NC

[![Build Status](https://app.travis-ci.com/carmelosammarco/tool4NC.svg?branch=master)](https://app.travis-ci.com/carmelosammarco/tool4NC.svg?branch=master) [![Build status](https://ci.appveyor.com/api/projects/status/58ppa5otfl06rd1h?svg=true)](https://ci.appveyor.com/project/carmelosammarco/tool4nc) [![PyPi](https://img.shields.io/badge/PyPi-Project-yellow.svg)](https://pypi.org/project/tool4nc/)  

**I developed this software because motivated to improve my efficiency and productivity. It is just an attemp/idea/prototype and it is not fully optimased or considered stable.**

**This project gave me also ideas to develop other tools** as [MerOC](https://github.com/carmelosammarco/MerOC), [JupLab4NetCDF](https://github.com/carmelosammarco/JupLab4NetCDF) and [ads4MO](https://github.com/carmelosammarco/ads4MO). To know more about them just visit the projects web pages which are hyperlinked above.

Many thanks to visit this page and try this software.

**Carmelo Sammarco**

## Introduction:
Python module containing functions for simplifing the netCDF files manipulations.

## Be aware that:

The tool is in development so it can be possible find bugs, errors and imprecisions. Please to report them if you find one.

## Dependencies:

The dependencies required are listed below:

- [x] netCDF4>=1.4.2
- [x] csv342>=1.0.0 
- [x] pandas>=0.23.4 
- [x] xarray>=0.11.0 
- [x] Shapely>=1.6.4.post1
- [x] Fiona>=1.8.4
- [x] cdo>=1.4.0


## Installation for Unix users (Linux distros and Mac-OSX systems):

As first things please install [cdo - climate data operator](https://code.mpimet.mpg.de/projects/cdo). It is required to run few functions contained in the python module. You can use the following command:

```
sudo apt-get install cdo
```

Also please consider to install [Anaconda](https://www.anaconda.com) 3.* version (Be aware that to use this software is suggested python ~=3.6). Once the Anaconda bash file (.sh) is downloaded, you can execute it in the terminal using the following command:

```
bash file_installation_Anaconda_downloaded.sh
```

 Furthermore, an update of pip, setuptools and wheels is suggested. You can do it executing the following command:

```
python -m pip install --upgrade pip setuptools wheel
```

After that run the software installation with:

```
pip install tool4NC
```

## Installation for Windows users:

As first things please install [cdo - climate data operator](https://code.mpimet.mpg.de/projects/cdo). It is required to run few functions inside the "TAB2:netCDF-Manipulations". From the product web page you can download the version which satisfy your system characteristics. Once de-compressed the folder downloaded just run the .exe file to install cdo in your Windows OS system.

Also please consider to install [Anaconda](https://www.anaconda.com) 3.* version (Be aware that to use this software is suggested python ~=3.6). The file from you downloaded will be a stardard executable (.exe). Before run the installation please be sure to tick the option for add in the Windows PATH environment variable the path of the anaconda package. 

Furthermore, an update of pip, setuptools and wheels is suggested. You can do it executing the following command:

```
python -m pip install --upgrade pip setuptools wheel
```

Before start with the python module installlation it is mandatory to manually configure and install few python dependencies that are not correctly managed by the stardard 'pip' Windows installation. The dependencies that I am speaking of are “shapely” and “fiona”. They are essential Python modules for geospatial operations contained in this python package (exporting a netCDF variable as shapefile just to cite one). In this particular scenario, and especially in a Windows OS, be able to install the required modules using the Python wheels can be very handy. In fact they are already pre-compiled and then easily digested from the Windows OS. Christoph Gohlke, at the Laboratory for Fluorescence Dynamics at UC Irvine, maintains a large [Python wheels library](https://www.lfd.uci.edu/~gohlke/pythonlibs/). Be aware that for each module you need to choose the one maching your Python version and the pc processor characteristics (32 or 64-bit). If we consider as example "Shapely-1.6.4.post1-cp37-cp37m-win32.whl" the "cp37" indicate the python version which is 3.7.* while "win32" the processor type which is 32-bit. The python version can be indicated also as "py3" or "py2" or "py2.py3". the latter when both the 2.* and 3.* python version can be used. To install a wheel file you just need to run "pip install [wheel_file]"  in the same location where the wheel is located. To succeed within the installation of "shapely" and "fiona" you must execute the following steps, in the same order as they are listed below:

1. Install [Visual studio C++](https://www.microsoft.com/en-us/download/details.aspx?id=48145).
 
2. Download [gdal](https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal), [click](https://www.lfd.uci.edu/~gohlke/pythonlibs/#click), [cligj](https://www.lfd.uci.edu/~gohlke/pythonlibs/#cligj), [click_plugin](https://www.lfd.uci.edu/~gohlke/pythonlibs/#click), [attrs](https://www.lfd.uci.edu/~gohlke/pythonlibs/#attrs), [munch](https://www.lfd.uci.edu/~gohlke/pythonlibs/#munch), [fiona](https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona), [pyproj](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyproj), [rtree](https://www.lfd.uci.edu/~gohlke/pythonlibs/#rtree) and [shapely](https://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely) from the [Python wheels library](https://www.lfd.uci.edu/~gohlke/pythonlibs/). Now you have what you need for the following steps.

3. Install the gdal wheel. I suggest you to don't use gdal module alongside OSGeo4W or other similar distributions because they could go in conflict and then generate errors and malfuctions. Also add the gdal library path to the Windows PATH environment variable (which will be something like "C:\pyhon_version\Lib\site-packages\osgeo".To know in which way add the gdal path variable  you can check [here](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/). Finally we can now test the gdal module. Before do that please to close and then re-open the command prompt and from whatever path location execute this command:

```
gdalinfo --help-general
```
 
If gdal is correctly configured it will display its usage instructions.
 
4. Install the others Python wheels modules, previously downloaded (gdal excluded), and following the list order (from the top to the bottom):

- click
- cligj
- click plugin
- attrs
- munch
- fiona
- pyproj
- rtree
- shapely

Now that the all the most nasty dependencies are installed (at least for Windows OS), you can execute:

```
pip install tool4NC
```
At this point, after the installation you are ready to import the tool4nc module as:

```
from tool4NC import *              --->  #Import all the fuctions
from tool4NC import [name_fuction] --->  #Import just one fuction 
```
For the list of fucntions avaiable a in "tool4nc" module please continue to read below.

## Functions included:


### nctocsv ("input file", "path_output folder")

This function converts a netCDF file to a csv file. It will generate two csv files called file.csv and file_cleaned.csv respectively. The file_cleaned.csv is cleaned by all the NAN values and it is considered the final output file of this function.


### nctoshape ("input file", "path_output folder", "variable_name")

This function converts a netCDF file into a shape file (Point features). Firstly, it will generate two csv files called file.csv and file_cleaned.csv respectively. After that, the file_cleaned.csv (purified by all the NAN values) is used to extract the corresponding shapefile representing a variable’s values which is the third argument of this function.

### nctogdr ("input file", "path_output folder")

This fuction convert a netCDF file to a GRD file which is required for some computations.


### concatnc ("path_input folder")

This function is qble to concatenate segments of data coming from the same dataset but at different time steps. It will generate a file called "concatenated.nc" as final result. The only argument needed is the folder where the files are located.


### splitnc ("input file",  "path_output folder", "type", "suffix")

This function can split the data by type; DAY (DD), MONTH (YYYYMM) and YEAR (YYYY). It gives the option to add a suffix to the generated data. 


# Case examples:

## I have many netCDF files and I would like to convert all of them in CSV: 

```
import os
from tool4NC import nctocsv

Input_DIR = 'the/directory/you/want/to/use'
Out_DIR = 'the/directory/you/want/to/use'

for filename in os.listdir(Input_DIR):
    if filename.endswith(".nc"):
       nctocsv (filename, Out_DIR)
```

## I want to overlay in my GIS project (as shape-file) data from a variable which is contained in my netCDF file:

```
import os
from tool4NC import nctoshape

Input_DIR = 'the/directory/you/want/to/use'
Out_DIR = 'the/directory/you/want/to/use'
Variable = ‘Variable name’

for filename in os.listdir(Input_DIR):
    if filename.endswith(".nc"):
       nctoshape (filename, Out_DIR, Variable)
```

## I have a folder with a month of data divided in daily files. These files are downloaded from the same dataset and I would like to concatenate all the daily files in a montly one:

```
from tool4NC import concatnc

Input_DIR = 'the/directory/where/you/store/the/daily/file'

concatnc (Input_DIR) #it will generate the concatenated.nc file
```

## I have many netCDF files and I would like to convert all of them in GRD: 

```
import os
from tool4NC import nctogrd

Input_DIR = 'the/directory/you/want/to/use'
Out_DIR = 'the/directory/you/want/to/use'

for filename in os.listdir(Input_DIR):
    if filename.endswith(".nc"):
       nctogdr (filename, Out_DIR)
```

## I have one year file but i realised that it is better have the data organised by Month. Furthermore, I would like also add a suffix to each file:

```
from tool4NC import splitnc

Input_file = 'my_input_file.nc'
Out_DIR = 'the/directory/you/want/to/output/the/results'
type = "MONTH"
suffix = "text/to/append/at/each/file"


splitnc (Input_file, Out_DIR, type, suffix)
```










