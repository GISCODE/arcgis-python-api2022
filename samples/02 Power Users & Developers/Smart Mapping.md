
# Using Classes Color Renderer

The example below shows how a Classes Color Renderer can be used to visualize the population of the different counties in the state of Washington. It also shows how a definition expression can be used to limit the features displayed from the layer, and how the layer opacity can be specified:


    from arcgis.gis import GIS
    
    gis = GIS()
    map = gis.map('Seattle, WA', 6)

    :0: FutureWarning: IPython widgets are experimental and may change in the future.
    


    map

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/05-smart-wa.png"/>


    map.add_layer({"type":"FeatureLayer", 
                   "url":"//sampleserver6.arcgisonline.com/arcgis/rest/services/Census/MapServer/2",
                   "definition_expression" : "STATE_NAME='Washington'",
                   "renderer":"ClassedColorRenderer",
                   "field_name":"POP2007",
                   "opacity":0.75
                  })

#Using Heatmap Renderer

The example below visualizes earthquake of magnitude greather than four between 1963 qnd 2013 in Southern California, using a Heatmap renderer:


    map2 = gis.map('Los Angeles', 8)


    map2

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/05-smart-la.png"/>


    map2.add_layer({"type":"FeatureLayer",
                   "url":"http://services1.arcgis.com/hLJbHVT9ZrDIzK0I/arcgis/rest/services/EQMagGt4/FeatureServer/0",
                   "renderer":"HeatmapRenderer",
                   "opacity":0.75})
