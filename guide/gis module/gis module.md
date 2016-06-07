
# gis module
- - -

The gis module provides an information model for a GIS hosted within ArcGIS Online or an ArcGIS Portal. This module provides functionality to manage (create, read, update and delete) GIS users, groups, content and datastores and provide access to GIS tools and services. This module is the most important and provides the entry point into the GIS.

![gis module](http://esri.github.io/arcgis-python-api/notebooks/nbimages/gis.png "gis module")
- - -

The main classes in the gis module are:
* [**GIS**](class gis.GIS.ipynb) : represents the GIS, either ArcGIS Online or an ArcGIS Portal
* [**User**](class gis.User.ipynb) : represents a GIS user
* [**Group**](class gis.Group.ipynb) : represents a group in the GIS
* [**Item**](class gis.Item.ipynb) : represents an Item in the GIS
* [**Tools**](class gis.Tools.ipynb) : collection of helper GIS tools and services like geocoder, analysis, geoanalytics, rasters, geometry, ...
* Resource manager classes for managing GIS users, groups, content and datastores:
  * [**UserManager**](class gis.UserManager.ipynb) : to manage users
  * [**GroupManager**](class gis.GroupManager.ipynb) : to manage groups in the GIS 
  * [**ContentManager**](class gis.ContentManager.ipynb) : to access, add, modify, delete GIS content


    
