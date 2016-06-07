
# The map widget

The gis object includes a map widget for displaying geographic locations, visualizing GIS content, as well as the results of your analysis. To use the map widget, call gis.map() and assign it to a variable, that you can then query to bring up the widget in the notebook:


    from arcgis.gis import GIS
    
    gis = GIS()
    map = gis.map('Paris')
    map

    :0: FutureWarning: IPython widgets are experimental and may change in the future.
    

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/02-nb-paris.png"/>

The map widget has several properties that you can query and set, such as zoom level, it's basemap, height, etc:


    map.zoom




    12




    map.zoom = 10


    map.basemap




    'topo'




    map.basemap = 'streets'


    map.height = 600


    map.center




    [48.853408154000476, 2.348798511000439]




    location = gis.tools.geocoder.find_best_match('Times Square, NY')
    print(location)
    map.center = location
    map.zoom = 15

    (40.7564756590005, -73.98617618599962)
    

#Basemaps

ArcGIS Online includes several basemaps from Esri that you can use in your maps.


    from IPython.display import display
    
    basemaps = gis.content.search("tags:esri_basemap owner:esri", "web map")
    for basemap in basemaps:
        display(basemap)


<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=8bf7167d20924cbf8e25e7b11c7c502c' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/8bf7167d20924cbf8e25e7b11c7c502c/info/thumbnail/world_street_map.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=8bf7167d20924cbf8e25e7b11c7c502c' target='_blank'><b>Streets</b>
                        </a>
                        <br>Presents highway-level data for the world and street-level data for North America, Europe and more.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by esri
                        <br>Last Modified: December 21, 2015
                        <br>0 comments, 2,199,077 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=d5e02a0c1f2b4ec399823fdd3c2fdebd' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/d5e02a0c1f2b4ec399823fdd3c2fdebd/info/thumbnail/topo_map_2.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=d5e02a0c1f2b4ec399823fdd3c2fdebd' target='_blank'><b>Topographic</b>
                        </a>
                        <br>Topographic map which includes boundaries, cities, water features, physiographic features, parks, landmarks, transportation, and buildings.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by esri
                        <br>Last Modified: December 21, 2015
                        <br>2 comments, 1,252,501 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=716b600dbbac433faa4bec9220c76b3a' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/716b600dbbac433faa4bec9220c76b3a/info/thumbnail/Imagery_Labels.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=716b600dbbac433faa4bec9220c76b3a' target='_blank'><b>Imagery with Labels</b>
                        </a>
                        <br>Satellite and high-resolution aerial imagery for the world with political boundaries and place names. You can turn on transportation including street names.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by esri
                        <br>Last Modified: December 12, 2014
                        <br>2 comments, 1,169,999 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=fe44cf9a739848939988addfeba473e4' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/fe44cf9a739848939988addfeba473e4/info/thumbnail/Terrain_Labels.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=fe44cf9a739848939988addfeba473e4' target='_blank'><b>Terrain with Labels</b>
                        </a>
                        <br>Basemap features shaded relief, bathymetry and coastal water features that provide neutral background with political boundaries and placenames.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by esri
                        <br>Last Modified: December 12, 2014
                        <br>0 comments, 1,019,042 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=8b3d38c0819547faa83f7b7aca80bd76' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/8b3d38c0819547faa83f7b7aca80bd76/info/thumbnail/light_canvas.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=8b3d38c0819547faa83f7b7aca80bd76' target='_blank'><b>Light Gray Canvas</b>
                        </a>
                        <br>This web map draws attention to your thematic content by providing a neutral background with minimal colors, labels, and features.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by esri
                        <br>Last Modified: May 12, 2016
                        <br>44 comments, 326,737 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=d94dcdbe78e141c2b2d3a91d5ca8b9c9' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/d94dcdbe78e141c2b2d3a91d5ca8b9c9/info/thumbnail/natgeo.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=d94dcdbe78e141c2b2d3a91d5ca8b9c9' target='_blank'><b>National Geographic Map</b>
                        </a>
                        <br>This map is designed to be used as a general reference map for informational and educational purposes as well as a basemap by GIS professionals and other users for creating web maps and web mapping applications.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by esri
                        <br>Last Modified: December 12, 2014
                        <br>4 comments, 304,999 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=3c93bbf238424a3e85aae19823fc92ea' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/3c93bbf238424a3e85aae19823fc92ea/info/thumbnail/relief_labels.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=3c93bbf238424a3e85aae19823fc92ea' target='_blank'><b>Shaded Relief with Labels</b>
                        </a>
                        <br>Displays surface elevation as shaded relief with political boundaries and placenames.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by esri
                        <br>Last Modified: December 12, 2014
                        <br>0 comments, 266,208 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=d802f08316e84c6592ef681c50178f17' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/d802f08316e84c6592ef681c50178f17/info/thumbnail/Imagery_Labels_Trans.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=d802f08316e84c6592ef681c50178f17' target='_blank'><b>Imagery with Labels and Transportation</b>
                        </a>
                        <br>Satellite and high-resolution aerial imagery for the world with political boundaries, roads, and labels for places and roads.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by esri
                        <br>Last Modified: December 12, 2014
                        <br>2 comments, 262,749 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=5ae9e138a17842688b0b79283a4353f6' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/5ae9e138a17842688b0b79283a4353f6/info/thumbnail/oceans_5_0_gulf.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=5ae9e138a17842688b0b79283a4353f6' target='_blank'><b>Ocean Basemap</b>
                        </a>
                        <br>The Ocean Basemap includes bathymetry, surface and subsurface feature names, and derived depths. This map is designed to be used as a basemap by marine GIS professionals and as a reference map by anyone interested in ocean data.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by esri
                        <br>Last Modified: December 21, 2015
                        <br>6 comments, 172,184 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=1970c1995b8f44749f4b9b6e81b5ba45' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/1970c1995b8f44749f4b9b6e81b5ba45/info/thumbnail/ago_downloaded.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=1970c1995b8f44749f4b9b6e81b5ba45' target='_blank'><b>Dark Gray Canvas</b>
                        </a>
                        <br>This web map draws attention to your thematic content by providing a dark, neutral background with minimal colors, labels, and features.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by esri
                        <br>Last Modified: May 12, 2016
                        <br>0 comments, 57,409 views
                    </div>
                </div>
                


The Esri basemaps are included with the arcgis Map widget, and you can assign them dynamically:


    map = gis.map('New York')


    map.basemaps




    ['streets',
     'satellite',
     'hybrid',
     'topo',
     'gray',
     'dark-gray',
     'oceans',
     'national-geographic',
     'terrain',
     'osm']




    map

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/02-nb-basemaps.gif"/>


    import time
    
    for basemap in map.basemaps:
        map.basemap = basemap
        time.sleep(3)

Some partners and other users have also shared their basemaps for everyone to use:


    gis = GIS()
    with gis:
        stamenbasemaps = gis.content.search("tags:partner_basemap stamen", "web map", max_items=3)
        for basemap in stamenbasemaps:
            display(basemap)


<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=25bfb9bba81043ca89889516d3741527' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/25bfb9bba81043ca89889516d3741527/info/thumbnail/ago_downloaded.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=25bfb9bba81043ca89889516d3741527' target='_blank'><b>2015 San Antonio VBS List</b>
                        </a>
                        <br>Stylish VBS map<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by Furyk
                        <br>Last Modified: April 17, 2016
                        <br>0 comments, 4,417 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=25b5b923fbbb49cf9a39150d3a3150d5' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/25b5b923fbbb49cf9a39150d3a3150d5/info/thumbnail/watercolor.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=25b5b923fbbb49cf9a39150d3a3150d5' target='_blank'><b>Stamen Watercolor</b>
                        </a>
                        <br>Reminiscent of hand drawn maps, our watercolor maps apply raster effect area washes and organic edges over a paper texture to add warm pop to any map.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by dkensok
                        <br>Last Modified: January 02, 2015
                        <br>0 comments, 4,387 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=93b06911c103408e80fe6dea0f621648' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/93b06911c103408e80fe6dea0f621648/info/thumbnail/stamen_terrain.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=93b06911c103408e80fe6dea0f621648' target='_blank'><b>Stamen Terrain</b>
                        </a>
                        <br>Orient yourself with our terrain maps, featuring hill shading and natural vegetation colors. Available in the USA only.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by dkensok
                        <br>Last Modified: January 02, 2015
                        <br>0 comments, 3,993 views
                    </div>
                </div>
                


# The MapView class

The MapView class in the arcgis.viz module has additional methods to create a map widget, such as by specifying a web map item.

We can use these other basemaps in the Map widget as well by providing the basemap item to the MapView constructor:


    from arcgis.viz import MapView
    
    map2 = MapView(item=stamenbasemaps[2])
    map2

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/02-nb-stamenterrain.png"/>


    map2.zoom = 12


    location = gis.tools.geocoder.find_best_match('Mount St Helens')
    print(location)
    map2.center = location

    (46.191196893000495, -122.19439879099968)
    
