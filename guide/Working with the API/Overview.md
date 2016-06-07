
# ArcGIS Python API



##Introduction

The ArcGIS Python API is a modern, easy to use and powerful Pythonic library to perform GIS visualization and analysis, spatial data management and GIS system administration tasks that can run both in an interactive fashion, as well as using scripts.

It enables power users, system administrators and developers to leverage the rich SciPy ecosystem for automating their workflows and performing repetitive tasks using scripts. It integrates well with the IPython Notebook and enables academics, data scientists, GIS analysts and visualization enthusiasts to share geo-enriched literate programs and reproducible research with others.



## Modules

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/modules.png" />

The <code><b>arcgis package</b></code> has a modularized design that makes it simple to use and understand. These modules contain classes, functions and types for managing and working with the different elements of the GIS:

* ### gis
The <code><b>arcgis.gis</b></code> module provides an information model for GIS hosted within ArcGIS Online or an ArcGIS Portal. This module provides functionality to manage (create, read, update and delete) GIS users, groups and content. This module is the most important and provides the entry point into the GIS.

* ### viz
The <code><b>arcgis.viz</b></code> module provides components for visualizing GIS data and analysis. This module provides components such as MapView - an IPython Notebook widget for working with maps, as well as WebMap and WebScene components that enable 2D and 3D mapping and visualization in ArcGIS Online and on ArcGIS Portals.

* ### tools
The <code><b>arcgis.tools</b></code> module is used for consuming the GIS functionality exposed from ArcGIS Online 
or Portal web services. It has implementations for Spatial Analysis tools, GeoAnalytics tools,
Raster Analysis tools, Geoprocessing tools, Geocoders and Geometry Utility services. 
These tools primarily operate on items and layers from the GIS. 

* ### lyr
The <code><b>arcgis.lyr</b></code> module is used for accessing layers exposed from ArcGIS Online 
or Portal.



    
