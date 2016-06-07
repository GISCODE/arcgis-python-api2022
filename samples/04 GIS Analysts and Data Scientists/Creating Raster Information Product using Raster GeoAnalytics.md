
# Creating Raster Information Product using Raster GeoAnalytics

This notebook shows how image services can be used.


    from arcgis.gis import GIS
    from arcgis.lyr import ImageLayer
    from IPython.display import display
    
    gis = GIS()

Here we're searchcing for multispectral landsat imagery layer:


    items = gis.content.search("Landsat 8 Views", max_items=2)


    for item in items:
        display(item)


<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=a5fef63517cd4a099b437e55713d3d54' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/a5fef63517cd4a099b437e55713d3d54/info/thumbnail/Imagery.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=a5fef63517cd4a099b437e55713d3d54' target='_blank'><b>Imagery</b>
                        </a>
                        <br>This LYR file combines the World Imagery map service and World Transportation and World Boundaries and Places reference overlay services in one convenient group layer<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/layers16.png' style="vertical-align:middle;">Layer by esri
                        <br>Last Modified: January 16, 2012
                        <br>2 comments, 338,956 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=4ca13f0e4e29403fa68c46d188c4be73' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/4ca13f0e4e29403fa68c46d188c4be73/info/thumbnail/ago_downloaded.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=4ca13f0e4e29403fa68c46d188c4be73' target='_blank'><b>Landsat 8 Views</b>
                        </a>
                        <br>Landsat 8 OLI, 30m Multispectral 8 band scenes with visual renderings and indices. Updated daily.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/imagery16.png' style="vertical-align:middle;">Image Service by esri
                        <br>Last Modified: October 22, 2015
                        <br>0 comments, 106,506 views
                    </div>
                </div>
                



    landsat = items[1]


    imglyr = ImageLayer(landsat)

This layer has been published with several Raster Functions, that the code below is cycling through, and listing out:


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
    


    map = gis.map("Pallikaranai", 13)

    :0: FutureWarning: IPython widgets are experimental and may change in the future.
    


    map

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/rasteranalytics.gif"/>


    map.add_layer(imglyr)

The utility of raster functions is better seen when we interactively cycle through these raster functions and apply them to the map, like the code below does. This is using on-the-fly image processing at display resolution to cycle through the various raster functions, and showing how the layer can be visualized using these different raster functions published with the layer.


    import time
    
    for fn in imglyr['rasterFunctionInfos'][:6]:
        print(fn['name'])
        map.remove_layers()
        map.add_layer(imglyr, {"imageServiceParameters" :{ "renderingRule": { "rasterFunction": fn['name']}}})
        time.sleep(2)
        

    Agriculture with DRA
    Bathymetric with DRA
    Color Infrared with DRA
    Natural Color with DRA
    Short-wave Infrared with DRA
    Geology with DRA
    


    map = gis.map("Pallikaranai", 13)
    map

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/landwater.png"/>

Developers can create their own raster functions, by chaining different raster functions. For instance, the code below is doing an Extract Band and extracting out the [4,5,3] band combination, and applying a Stretch to get the land-water boundary visualization that makes it easy to see where land is and where water is:


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

#Creating a Raster Information Product using Landsat 8 imagery

This part of the notebook shows how Raster GeoAnalytics (in ArcGIS Portal 10.5 Beta) can be used to generate a raster information product, by applying the same raster function across the extent of an image service on my Portal, at source resolution, and this can create an Information Product, that can be used for further analysis and visualization.


    portal = GIS("https://dev06999.esri.com/portal", "admin", "changeit")


    chennai_ls = portal.content.search("ChennaiMultispectralLandsat")[0]


    map = portal.map("Pallikaranai, Tamil Nadu, India", 13)
    map


    map.add_layer(chennai_ls)

    https://Dev06999.esri.com/server/rest/services/ChennaiMultispectralLandsat/ImageServer
    


    product = portal.rasters.generate(raster_fn, "LandsatWaterBoundary3", chennai_ls)

    Submitted.
    Executing...
    Executing (GenerateRaster): GenerateRaster {"rasterFunctionArguments":{"Raster":{"rasterFunctionArguments":{"BandIds":[4,5,3]},"rasterFunction":"ExtractBand"},"Gamma":[1,1,1],"StretchType":6,"DRA":true,"UseGamma":true},"outputPixelType":"U8","rasterFunction":"Stretch"} {"itemId":"3017b6bf0a824185928ebd80c53617d8"} {"Raster":{"itemId":"2156e1ce07ea40da8a24d36271e03c3d"}} # # #
    Start Time: Tue Dec 15 06:10:55 2015
    Running script GenerateRaster...
    Output item id is: 3017b6bf0a824185928ebd80c53617d8
    Output image service url is: https://Dev06999.esri.com:6443/arcgis/rest/services/Hosted/LandsatWaterBoundary3/ImageServer
    Output image service admin url is: https://Dev06999.esri.com:6443/arcgis/admin/services/Hosted/LandsatWaterBoundary3.ImageServer
    Output cloud raster name is: id_3017b6bf0a824185928ebd80c53617d8
    Raster https://Dev06999.esri.com:6443/arcgis/rest/services/ChennaiMultispectralLandsat/ImageServer
    
    Using input raster dataset's spatial reference.
    Data store URI: \\dev06999\bigdata\data\id_3017b6bf0a824185928ebd80c53617d8
    Updating service: https://Dev06999.esri.com:6443/arcgis/admin/services/Hosted/LandsatWaterBoundary3.ImageServer/edit
    Starting service: https://Dev06999.esri.com:6443/arcgis/admin/services/Hosted/LandsatWaterBoundary3.ImageServer/start
    Succeeded at Tue Dec 15 06:12:14 2015 (Elapsed Time: 1 minutes 18 seconds)
    {'outRaster': {'itemId': '3017b6bf0a824185928ebd80c53617d8'}}
    


    product




<div class="item_container">
                    <div class="item_left">
                       <a href='https://dev06999.esri.com/portal/home/item.html?id=3017b6bf0a824185928ebd80c53617d8' target='_blank'>
                        <img src='http://static.arcgis.com/images/desktopapp.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right">
                        <a href='https://dev06999.esri.com/portal/home/item.html?id=3017b6bf0a824185928ebd80c53617d8' target='_blank'><b>LandsatWaterBoundary3</b>
                        </a>
                        <br><img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/imagery16.png' style="vertical-align:middle;">Image Service by admin
                        <br>Last Modified: December 15, 2015
                        <br>0 comments, 0 views
                    </div>
                </div>
                




    map.add_layer(product)

    http://Dev06999.esri.com/server/rest/services/Hosted/LandsatWaterBoundary3/ImageServer
    
