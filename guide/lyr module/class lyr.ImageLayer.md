
##The ImageLayer class

<hr/>

<code><b>class lyr.ImageLayer<b>(<i>item</i>)</code>

Bases: OrderedDict

Represents an ArcGIS image layer.

The image layer is backed by an image service.

The image layer is represented as a Python dictionary, and provides access to image service parameters such as rasterFunctionInfos.


    #Example: Loading an image service from the GIS and visualizing it using MapView widget
    
    from arcgis.gis import *
    from arcgis.lyr import *
    from arcgis.viz import *
    from IPython.display import display
    
    gis = GIS()
    items = gis.content.search("Landsat 8 Views", max_items=2)
    for item in items:
        display(item)


<div class="item_container">
                    <div class="item_left">
                       <a href='http://www.arcgis.com/home/item.html?id=a5fef63517cd4a099b437e55713d3d54' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/a5fef63517cd4a099b437e55713d3d54/info/thumbnail/Imagery.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right">
                        <a href='http://www.arcgis.com/home/item.html?id=a5fef63517cd4a099b437e55713d3d54' target='_blank'><b>Imagery</b>
                        </a>
                        <br>This LYR file combines the World Imagery map service and World Transportation and World Boundaries and Places reference overlay services in one convenient group layer<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/layers16.png' style="vertical-align:middle;">Layer by esri
                        <br>Last Modified: January 16, 2012
                        <br>2 comments, 322,191 views
                    </div>
                </div>
                



<div class="item_container">
                    <div class="item_left">
                       <a href='http://www.arcgis.com/home/item.html?id=4ca13f0e4e29403fa68c46d188c4be73' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/4ca13f0e4e29403fa68c46d188c4be73/info/thumbnail/ago_downloaded.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right">
                        <a href='http://www.arcgis.com/home/item.html?id=4ca13f0e4e29403fa68c46d188c4be73' target='_blank'><b>Landsat 8 Views</b>
                        </a>
                        <br>Landsat 8 OLI, 30m Multispectral 8 band scenes with visual renderings and indices. Updated daily.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/imagery16.png' style="vertical-align:middle;">Image Service by esri
                        <br>Last Modified: October 22, 2015
                        <br>0 comments, 101,496 views
                    </div>
                </div>
                



    landsat = items[1]
    imglyr = ImageLayer(landsat)

    http://landsat2.arcgis.com/arcgis/rest/services/Landsat8_Views/ImageServer
    

We can access properties of the ImageLayer. Eg. accessing the raster functions published with the layer:


    for fn in imglyr['rasterFunctionInfos']:
        print(fn['name'])

    Agriculture with DRA
    Bathymetric with DRA
    Color Infrared with DRA
    Natural Color with DRA
    Short-wave Infrared with DRA
    Geology with DRA
    Agriculture
    Bathymetric
    Color Infrared
    Geology
    Natural Color
    Short-wave Infrared
    NDVI Colorized
    Normalized Difference Moisture Index Colorized
    NDVI Raw
    NBR Raw
    None
    

We can visualize an image layer using the map widget:


    map = gis.map("Pallikaranai", 13)
    map

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/rasteranalytics.gif"/>


    map.add_layer(imglyr)

In the example below, we visualize the different raster functions published with the image service by cycling through the raster functions:


    import time
    
    for fn in imglyr['rasterFunctionInfos'][:6]:
        print(fn['name'])
        map.remove_layers()
        map.add_layer(imglyr, {"imageServiceParameters" :{ "renderingRule": { "rasterFunction": fn['name']}}})
        time.sleep(5)

    Agriculture with DRA
    Bathymetric with DRA
    Color Infrared with DRA
    Natural Color with DRA
    Short-wave Infrared with DRA
    Geology with DRA
    

We can also apply a **raster function chain** composed as a Python dictionary and apply it to the image service:


    raster_fn = {
                   "rasterFunction": "Stretch",
                   "rasterFunctionArguments":{
                        "Raster":{
                            "rasterFunction": "ExtractBand",
                            "rasterFunctionArguments":{"BandIds": [4,5,3]}
                        },
                        "StretchType": 6,
                        "DRA": True,
                        "Gamma": [1,1,1],
                        "UseGamma": True
                    },
                   "outputPixelType":"U8"
                  }
    
    


    map.add_layer(landsat, {"imageServiceParameters" :{ "renderingRule": raster_fn }})

    http://landsat2.arcgis.com/arcgis/rest/services/Landsat8_Views/ImageServer
    

<hr>
