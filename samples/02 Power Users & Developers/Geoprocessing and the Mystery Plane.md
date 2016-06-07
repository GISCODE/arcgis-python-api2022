
This sample notebooks shows how geoprocessing tools can be used in an analysis. The analysis below uses a geoprocessing tool to  deduce the path that the debris of a crashed airplane would take if it went down at different places in the southern Indian Ocean. It should be noted that this tool is for the purpose of demonstrating GIS functionality and the results should not be treated as authorotative.


    from arcgis.gis import GIS


    gis = GIS()
    map = gis.map()
    map

    :0: FutureWarning: IPython widgets are experimental and may change in the future.
    

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/03-gp.png"/>

There have been speculations that the unfortunate disappearance of MH370 is tied to Diego Garcia, in addition to the search location in southern Indian Ocean west of Australia. The code below plots the locations of these in the map:


    diegogarcia = gis.tools.geocoder.find_best_match("Diego Garcia")
    map.center = diegogarcia


    map.draw(gis.tools.geocoder.find_best_match("La Reunion"), {"title": "Reunion Island", "content": "Debris found"})
    map.draw(diegogarcia, {"title": "Diego Garcia", "content": "Naval Support Facility Diego Garcia"})
    map.draw([-43.5, 90.5], {"title":"Search Location", "content":"Predicted crash location"})
    
    #Source: http://www.amsa.gov.au/media/incidents/images/DIGO_00718_01_14.jpg
    map.add_layer({"type":"FeatureLayer", "url" : "http://services.arcgis.com/WQ9KVmV6xGGMnCiQ/arcgis/rest/services/MH370Search/FeatureServer/1"})

We can search ArcGIS Online for content related to the missing airliner, and bring in layers that we want to use for our analysis and visualization:


    from IPython.display import display
    
    mh370items = gis.content.search("MH370", "feature service", max_items=6)
    for item in mh370items:
        display(item)


<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=86a1b6e71af74979ba38095543d48f07' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/86a1b6e71af74979ba38095543d48f07/info/thumbnail/thumbnail.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=86a1b6e71af74979ba38095543d48f07' target='_blank'><b>MH370_Flight_Path</b>
                        </a>
                        <br>MH370 Flight Path<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/featureshosted16.png' style="vertical-align:middle;">Feature Service by bflanagan_bureau
                        <br>Last Modified: February 25, 2015
                        <br>0 comments, 21,922 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=cad4c67f0139406fb9c8d3ee8581fd1d' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/cad4c67f0139406fb9c8d3ee8581fd1d/info/thumbnail/thumbnail.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=cad4c67f0139406fb9c8d3ee8581fd1d' target='_blank'><b>Arc</b>
                        </a>
                        <br>Lastknownlocationarc<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/featureshosted16.png' style="vertical-align:middle;">Feature Service by bflanagan_bureau
                        <br>Last Modified: March 02, 2015
                        <br>0 comments, 13,397 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=aab7322704084ae1abe1a3d591a8bf72' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/aab7322704084ae1abe1a3d591a8bf72/info/thumbnail/thumbnail.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=aab7322704084ae1abe1a3d591a8bf72' target='_blank'><b>MH370Search</b>
                        </a>
                        <br>MH370Search<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/featureshosted16.png' style="vertical-align:middle;">Feature Service by bflanagan_bureau
                        <br>Last Modified: March 02, 2015
                        <br>0 comments, 7,487 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=6867dcf7b4214fcfa78e846f4b666a53' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/6867dcf7b4214fcfa78e846f4b666a53/info/thumbnail/ago_downloaded.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=6867dcf7b4214fcfa78e846f4b666a53' target='_blank'><b>ActualFlightRoute</b>
                        </a>
                        <br><img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/featureshosted16.png' style="vertical-align:middle;">Feature Service by bflanagan_bureau
                        <br>Last Modified: February 26, 2015
                        <br>0 comments, 4,536 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=7615f1a27fd2410d9452762f94582ff7' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/7615f1a27fd2410d9452762f94582ff7/info/thumbnail/thumbnail.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=7615f1a27fd2410d9452762f94582ff7' target='_blank'><b>SatelliteLocation</b>
                        </a>
                        <br>SatelliteLocation<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/featureshosted16.png' style="vertical-align:middle;">Feature Service by bflanagan_bureau
                        <br>Last Modified: February 26, 2015
                        <br>0 comments, 4,486 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=599726f0009a4dd38c06abf036b663c7' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/599726f0009a4dd38c06abf036b663c7/info/thumbnail/ago_downloaded.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=599726f0009a4dd38c06abf036b663c7' target='_blank'><b>mh370debris</b>
                        </a>
                        <br>mh370 imagery debris<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/featureshosted16.png' style="vertical-align:middle;">Feature Service by bflanagan_bureau
                        <br>Last Modified: March 02, 2015
                        <br>0 comments, 2,873 views
                    </div>
                </div>
                


Let's add the layers that we want to use for our analysis to the map:


    map.add_layer(mh370items[0])
    map.add_layer(mh370items[4])
    map.add_layer(mh370items[5])


    map.zoom = 6

# Using geoprocessing tool

We search ArcGIS Online for the Ocean Currents geoprocessing tool that calculates the path of an unpowered vessel drifiting in ocean currents from a user defined point. This tool is for demonstration of GIS functionality only and excludes wind or atmospheric conditions, which are critical for a real-world analysis:


    gpsvcs = gis.content.search("Ocean Currents", "geoprocessing service", max_items=1)
    for gpsvc in gpsvcs:
        display(gpsvc)


<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=383c2039b89d43baa0010c3bf243b144' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/383c2039b89d43baa0010c3bf243b144/info/thumbnail/Ocean_Currents.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=383c2039b89d43baa0010c3bf243b144' target='_blank'><b>Ocean Currents</b>
                        </a>
                        <br>Calculates the path of an unpowered vessel drifiting in ocean currents from a user defined point. Excludes wind or atmospheric conditions.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/layers16.png' style="vertical-align:middle;">Geoprocessing Service by esri_apac
                        <br>Last Modified: August 25, 2014
                        <br>0 comments, 152 views
                    </div>
                </div>
                



    from arcgis.tools import GeoprocessingTool
    
    gptool = GeoprocessingTool(gpsvcs[0])

    URL: http://sampleserver1.arcgisonline.com/ArcGIS/rest/Services/Specialty/ESRI_Currents_World/GPServer
    Task: MessageInABottle
    Input_Point : GPFeatureRecordSetLayer
    Days : GPDouble
    

When we click the map, we want to invoke the geoprocessing tool and pass in the clicked location. We can do this by adding an event listener to the map using map.on_click() that calls the tool with the clicked location. The ArcGIS Python API dynamically adds methods (in this case, the message_in_a_bottle method) based on the tool that is contructed. The method is added with documentation strings that can be queried in the notebook using intellisense.

This tool would return the paths tat debris would take if the plane went down at that path, which we draw on the map using map.draw() in the code below:


    def do_analysis(m, g):
        ret = gptool.message_in_a_bottle(g, 150)
        for geom in ret:
            map.draw(geom)
    
    map.on_click(do_analysis)

Click around on the map, near Diego Garcia as well as the search location to find the paths the debris could have taken and if could it have reached La Reunion if the plane indeed went down in these locations.
