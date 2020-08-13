# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:59:45 2020

@author: atma6951
"""
from arcgis.gis import GIS
from arcgis.raster import RasterCollection
from arcgis.raster import functions
import arcpy

crf_path = r'\\Mac\Home\Documents\GIS_data\Imagery\sentinel-5p\ny-2019-2020\ny_crf\ny_19_20.crf'

# read crf
no2_rc = RasterCollection(crf_path)

# extract
no2_2019 = no2_rc.filter_by_calendar_range('YEAR',2019,2019)
no2_2020 = no2_rc.filter_by_calendar_range('YEAR',2020,2020)
no2_19_no2 = no2_2019.filter_by_attribute(field_name='Variable', 
                                          operator='CONTAINS', 
                                          field_values='nitrogendioxide')

no2_19_qa_value = no2_2019.filter_by_attribute(field_name='Variable', 
                                          operator='CONTAINS', 
                                          field_values='qa_value')

# sample raster
r1 = no2_19_no2[0]['Raster']