
##The MapView widget

<hr/>

<code><b>class viz.MapView<b>(<i>**kwargs</i>)</code>

Bases: IPython.html.widgets.widget.DOMWidget

Constructs a map widget for visualization of geographic information as well as the results of GIS analysis.

**Arguments:**
<table border="1" class="docutils">
<colgroup>
<col width="27%">
<col width="73%">
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><strong>Argument</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="row-even"><td>basemap</td>
<td>optional string, one of "streets", "satellite", "hybrid", "topo", "gray", "dark-gray", "oceans", "national-geographic", "terrain", "osm"</td>
</tr>
<tr class="row-odd"><td>width</td>
<td>optional string, representing width of widget in pixels eg. '900px'</td>
</tr>
<tr class="row-even"><td>height</td>
<td>optional string, representing width of widget in pixels eg. '900px'</td>
</tr>
<tr class="row-odd"><td>zoom</td>
<td>optional int, specifying zoom level</td>
</tr>
<tr class="row-odd"><td>id</td>
<td>optional string, specifying webmap id to be loaded</td>
</tr>
<tr class="row-odd"><td>center</td>
<td>optional list containing latitude and longitude in degrees, eg. [28.7124568, 77.1175102], can also use gis.tools.geocoder.find_best_match('address') to specify center</td>
</tr>
<tr class="row-odd"><td>start_time</td>
<td>optional string, specifying start_time extent of map, eg '1/1/1989 UTC'</td>
</tr>
<tr class="row-odd"><td>end_time</td>
<td>optional string, specifying end_time extent of map, eg '1/1/1989 UTC'</td>
</tr>
</tbody>
</table>

These arguments are also available as gettable/settable properties of the widget.


    from arcgis.gis import GIS
    from arcgis.viz import MapView
    
    gis = GIS()
    map = MapView()
    map.center = gis.tools.geocoder.find_best_match('Redlands, CA')
    map

    :0: FutureWarning: IPython widgets are experimental and may change in the future.
    

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/redlands.png" />

<hr>

##add_layer(<i>item, options=None</i>)

Adds a layer from the provided item, using the specified options.

The first parameter is a portal item that represents a layer from the GIS. It can be an item of type "Feature Service", "Feature Collection", "Image Service", or an instance of FeatureService, FeatureCollection, Layer, ImageLayer or a python dict of the format { 
                "type" : item['type'], 
                "url" : item['url'],
                "definition_expression" : item['definition_expression'],
                "opacity" : 0.75"
                } 
                
options is a python dict containing optional keys. The supported keys are "opacity", "definition_expression", "renderer" (one of ClassedColorRenderer, ClassedSizeRenderer, HeatmapRenderer), "field_name" (used with "renderer") 


    # Example
    
    map = gis.map("Seattle, WA", 6)
    map

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/05-smart-wa.png" />


    map.center = gis.tools.geocoder.find_best_match("Seattle, WA", 6)
    map.add_layer({"type":"FeatureLayer", 
                   "url":"//sampleserver6.arcgisonline.com/arcgis/rest/services/Census/MapServer/2",
                   "definition_expression" : "STATE_NAME='Washington'",
                   "renderer":"ClassedColorRenderer",
                   "field_name":"POP2007",
                   "opacity":0.75
                  })

<hr>

###draw(<i>shape, popup=None, symbol=None, attributes=None</i>)

Draws a shape.

**Arguments:**
**shape** is one of [“circle”, “downarrow”, “ellipse”, “extent”, “freehandpolygon”, “freehandpolyline”, “leftarrow”, “line”, “multipoint”, “point”, “polygon”, “polyline”, “rectangle”, “rightarrow”, “triangle”, “uparrow”, or geometry dict object]

**popup** is a dict containing “title” and “content” as keys that will be displayed when the shape is clicked

**symbol** is a symbol specified in json format as described at http://resources.arcgis.com/en/help/arcgis-rest-api/index.html#//02r3000000n5000000 a default symbol is used is one is not specified

**attributes** is a dict containing name value pairs of fields and field values associated with the graphic.



    # Example
    
    gis = GIS()
    map = MapView()
    map

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/circle.png" />


    map.draw("circle")

<hr>

###on_click(<i>callback, remove=False</i>)

Register a callback to execute when the map is clicked.

The callback will be called with one argument, the clicked widget instance.

**remove** : bool (optional), set to true to remove the callback from the list of callbacks.

<hr>

###on_draw_end(<i>callback, remove=False</i?>)

Register a callback to execute when something is drawn

The callback will be called with two argument, the clicked widget instance, and the geometry drawn

**remove** : bool (optional), set to true to remove the callback from the list of callbacks.

<hr>

###remove_layers()

Removes all layers from the map.

<hr>

###set_time_extent(<i>start_time, end_time</i>)

Sets the time extent of all layers within the map widget. The strart_time and end_time parameters are specified as strings in this format: '1/1/1989 UTC'

<hr>
