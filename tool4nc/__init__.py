import numpy  as np
import pandas as pd
import xarray as xr
import os
import csv342 as csv 
from shapely.geometry import Point, mapping
from fiona import collection
import cdo
import sys

import moviepy.editor as mpy
import glob
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap
from matplotlib.dates import date2num, num2date
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

#########################################################################

def nctocsv(filein,out):
    ''' This fuction convert a netCDF file to a csv file. It will generate
        two csv files called file.csv and file_cleaned.csv respectively.
        The file_cleaned.csv is cleaned by all the NAN values and it is
        considered the final output file of this fuction.

        -USE:

        nctocsv("path_file_input", "path_output_folder")
        '''
    ds = xr.open_dataset(filein, decode_times=False)
    df = ds.to_dataframe()
    df.to_csv(out + "/" + filein + ".csv")
    data = pd.read_csv(out + "/" + filein + ".csv")
    data.dropna().to_csv(out + "/" + filein + "_Cleaned" + ".csv", index = False)

#############################################################################


def nctoshape(filein,out,variable):
    ''' This fuction convert a netCDF file into a shape file(Point features). Firsly It will generate
        two csv files called file.csv and file_cleaned.csv respectively. After that
        the file_cleaned.csv ( purified by all the NAN values) is used to extract
        the corresponding shapefile rappresenting a variable's values which is the
        third argument of this fuction.

        -USE:

        nctoshape("path_file_input", "path_output_folder", "variable")
        '''
    ds = xr.open_dataset(filein, decode_times=False)
    df = ds.to_dataframe()
    df.to_csv(out + "/" + filein + ".csv")
    data = pd.read_csv(out + "/" + filein + ".csv")
    data.dropna().to_csv(out + "/" + filein + "_Cleaned" + ".csv", index = False)

    filecsv = open(out + "/" + filein + "_Cleaned" + ".csv")
    listed=[]
    line = filecsv.readline()
    for u in line.split(','):
        listed.append(u)
    
    if 'lat' in listed:
        schema = { 'geometry': 'Point', 'properties': { variable : 'float' } }
        with collection(out +"/" + filein + ".shp", "w", "ESRI Shapefile", schema) as output:
            with open(out + "/" + filein + "_Cleaned" + ".csv", 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    point = Point(float(row['lon']), float(row['lat']))
                    output.write({
                          'properties': {
                              variable: row[ variable ]
                          },
                          'geometry': mapping(point)
                    })
                
    elif 'Lat' in listed:
        schema = { 'geometry': 'Point', 'properties': { variable : 'float' } }
        with collection(out +"/" + filein + ".shp", "w", "ESRI Shapefile", schema) as output:
            with open(out + "/" + filein + "_Cleaned" + ".csv", 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    point = Point(float(row['Lon']), float(row['Lat']))
                    output.write({
                          'properties': {
                              variable: row[ variable ]
                          },
                          'geometry': mapping(point)
                    })
                
    elif 'Latitude' in listed:
        schema = { 'geometry': 'Point', 'properties': { variable : 'float' } }
        with collection(out +"/" + filein + ".shp", "w", "ESRI Shapefile", schema) as output:
            with open(out + "/" + filein + "_Cleaned" + ".csv", 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    point = Point(float(row['Longitude']), float(row['Latitude']))
                    output.write({
                        'properties': {
                            variable : row[ variable ]
                        },
                        'geometry': mapping(point)
                    })
                
    elif 'latitude' in listed:
        schema = { 'geometry': 'Point', 'properties': { variable : 'float' } }
        with collection(out +"/" + filein + ".shp", "w", "ESRI Shapefile", schema) as output:
            with open(out + "/" + filein + "_Cleaned" + ".csv", 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    point = Point(float(row['longitude']), float(row['latitude']))
                    output.write({
                        'properties': {
                            variable : row[ variable ]
                        },
                        'geometry': mapping(point)
                    })
                
    else:
        print("Need to be added a new text format. Please contact Carmelo!")
    

#######################################################################################

def nctogdr(filein,out):
    ''' This fuction convert a netCDF file to a GRD file. 

        -USE:

        nctogdr("path_file_input", "path_output_folder")
    '''
    command = "cdo  -f grb copy  " + filein  + "   " + out + "/" + filein + ".grb"
    print(command)
    os.system(command)



########################################################################################


def concatnc(folderimput):
    ''' This fuction is able to concatenate segments of data coming from the same dataset 
        but at different time steps. It will generate a file called "concatenated.nc" as 
        final result. The only atgument needed is the folder where the files are located.

        -USE:

        concatenate("path_folder_input")
    '''
    command = "cdo mergetime  " + folderimput +"/*.nc  " +  folderimput + "/Concatenated.nc"
    print(command)
    os.system(command)

###########################################################################################

def splitnc(filein,out,types,suffix):
    '''This fuction is able to split the data by type: DAY(DD), MONTH(YYYYMM) and YEAR(YYYY). It 
       gives the option to add a suffix to the so generated data.

       -USE

        splitnc("path_file_input", "path_output_folder", "Types"[DAY,MONTH or YEAR], Suffix")
    '''

    if types == "DAY":
        command = "cdo splitday" +"  " + filein + "  " + out +"/"+ suffix
        print(command)
        os.system(command)

    elif types == "MONTH":
        command = "cdo splityearmon" +"  " + filein + "  " + out +"/"+ suffix
        print(command)
        os.system(command)

    elif types == "YEAR":
        command = "cdo splityear" +"  " + filein + "  " + out +"/"+ suffix
        print(command)
        os.system(command)
    
    else:
        print("Please to insert DAY, MONTH or YEAR option")


###########################################################################################

def plotintime(filein,var,out,fps):
    '''This fuction is able to generate a dynamic plot showing the variation of the selected 
       variable in fuction of the time steps recorded into. 

       -USE

        plotintime ("path_input file","variable_name","path_output folder",frame_for_second)
    '''

    with xr.open_dataset(filein) as ds:
       #print(title)
        minvar = eval("ds."+var+".min()")
        maxvar = eval("ds."+var+".max()")
        print (minvar)
        print (maxvar)

        for t in range(ds.time.shape[0]):

            da = eval("ds."+var+".isel(time=t)")
    
            num = date2num(ds.time[t])
            date = num2date(num)

            title = ds.title+"-"+str(date)
            
            plt.figure(figsize=(10,5))
            
            lat  = ds.variables['lat'][:]
            lon  = ds.variables['lon'][:]
            
            plt.title(title, fontsize=10)
            #plt.xlabel("Longitude", fontsize=30)
            #plt.ylabel("Latitude", fontsize=30)
            
            m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), \
            urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
            resolution='l')
            
            m.drawcoastlines()
            m.fillcontinents()
            m.drawmapboundary()
            
            m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
            m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

            x, y = m(*np.meshgrid(lon,lat))

            col = m.pcolormesh(x,y,da,shading='flat',cmap=cm.get_cmap("jet"), vmin=minvar, vmax=maxvar)
        
            cbar = plt.colorbar(col)
            
            cbar.ax.yaxis.set_ticks_position('left')
            for I in cbar.ax.yaxis.get_ticklabels():
                I.set_size(10)
            
            cbar.set_label(var, size = 10)
            
            plt.savefig(out + '/frame{}.png'.format(t), dpi=300)    
        
        a = int(fps)

        gif_name = "PlotinTime" + "_" + var 

        file_list = glob.glob(out +'/*.png') # Get all the pngs in the current directory
        file_list.sort(key=os.path.getmtime) # Sort the images by time, this may need to be tweaked for your use case

        clip = mpy.ImageSequenceClip(file_list, fps=a)
        clip.write_gif('{}.gif'.format(gif_name), fps=a)

        clip2 = mpy.VideoFileClip("PlotinTime" + "_" + var + ".gif")
        clip2.write_videofile("PlotinTime" + "_" + var +  ".mp4")

        path = str(out+"/")
        folder = os.listdir(path)
        for item in folder:
            if item.endswith(".png"):
                os.remove(os.path.join(path, item))

###########################################################################################





