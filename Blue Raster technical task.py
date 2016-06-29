# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 16:25:28 2016

@author: David
"""

'''########################################################
                   For Blue Raster
########################################################'''
                   
print 'Load arcpy'
import arcpy
from arcpy import env
from arcpy.sa import *
print '   ...done'

#define paths and variables
base_dir = "C:/Users/David.Dell1301/Desktop/Blue Raster/"
inCSV = "MODIS_C6_South_America_7d.csv"

arcpy.env.workspace = base_dir
env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")

# convert csv to dbf
#dbf = "MODIS.dbf"
#arcpy.TableToTable_conversion(inCSV, base_dir, dbf)

#convert lat long to points.
try:
    # Set the local variables
    in_Table = dbf
    x_coords = "longitude"
    y_coords = "latitude"
    out_Layer = "MODIS"
    saved_Layer = r"C:/Users/David.Dell1301/Desktop/Blue Raster/MODIS_pts.lyr"
 
    # Set the spatial reference
    spRef = r"C:/Users/David.Dell1301/AppData/Roaming/ESRI/Desktop10.1/ArcMap/Coordinate Systems/WGS 1984.prj"
 
    # Make the XY event layer...
    arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef)
 
    # Print the total rows
    print arcpy.GetCount_management(out_Layer)
 
    # Save to a layer file
    arcpy.SaveToLayerFile_management(out_Layer, saved_Layer)
 
except:
    # If an error occurred print the message to the screen
    print arcpy.GetMessages()
    
#Spatially join features points to countries
countries = base_dir+"World_Countries.shp"
join_1 = "MODIS_country_count.shp"
join_2 = "MODIS_country_one_to_many.shp"

#For count per country in 'Join_field' column in attribute table
arcpy.SpatialJoin_analysis(countries, saved_Layer, join_1, "#", "KEEP_COMMON")

#ONE TO MANY join to preserve information from point layer if needed
arcpy.SpatialJoin_analysis(countries, saved_Layer, join_2, "JOIN_ONE_TO_MANY", "KEEP_COMMON")




print "Finished"