
##The Tools class

<hr/>

##<b>class gis.Tools<b>(<i>gis</i>)

Bases: builtins.dict

Collection of GIS tools. This class holds references to the helper services and tools available in the GIS. This class is not created by users directly. An instance of this class, called ‘tools’, is available as a property of the GIS object. Users access the GIS tools, such as the geocoder, spatial analysis tools, geoanalytics, raster geoanalysis tools, etc through the gis.tools object.

Example: We create a map widget and center it at the location of the Esri User Conference, San Diego, CA.


    from arcgis.gis import GIS
    
    gis = GIS()
    map = gis.map('San Diego, CA', 12)
    map

We can use the geocoder tool to re-center the map on Palm Springs - the location of Esri's Dev Summit


    map.center = gis.tools.geocoder.find_best_match('Palm Springs, CA')

<hr>

The gis tools are available as properties of the gis.tools object:

* ###analysis
  the portal’s spatial analysis tools, if available and configured
* ###geoanalytics
  the portal’s geoanalytics tools, if available and configured
* ###geocoder
  the portal's geocoder, if available and configured
* ###geometry
  the portal’s geometry tools, if available and configured
* ###rasters
  the portal’s raster analysis tools, if available and configured


    
