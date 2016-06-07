
##The WebMap class

<hr/>

<code><b>class viz.WebMap<b>(<i>webmapitem</i>)</code>

Bases: collections.OrderedDict

Represents a webmap and provides access to it’s basemaps and operational layers as well as functionality to visualize and interact with them. See http://resources.arcgis.com/en/help/arcgis-web-map-json/index.html#/Web_map_format_overview/02qt00000007000000/

The webmap is represented as a Python dictionary with <a href="http://resources.arcgis.com/en/help/arcgis-web-map-json/index.html#/Web_map_format_overview/02qt00000007000000/
">this format</a>.

<hr>

##update()

Updates the webmap item on the portal, writing back the properties that may have been modified since the webmap was last retrieved.

<hr>
