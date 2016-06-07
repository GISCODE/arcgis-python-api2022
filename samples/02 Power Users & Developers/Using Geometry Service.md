
This notebook uses the GIS's Geometry service to compute the length of a path that the user draws on the map.

The particular scenario is of a jogger who runs in the Central Park in New York (without gizmos like GPS watches to distract him), and wants a rough estimate of his daily runs based on the path he takes. The notebook starts out with a satellite map of Central Park in New York:


    from arcgis.gis import GIS
    from arcgis.viz import MapView


    gis = GIS()


    map = MapView(basemap="satellite")


    map

    Length:3854.7253839796153 m.
    

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/04-geometry-service.png"/>


    map.zoom = 15


    map.center=gis.tools.geocoder.find_best_match("Central Park, New York")


    map.height=900

We want the user to draw a freehand polyline to indicate the paths that he takes for his runs. When the drawing operation ends, we use the GIS's Geometry service to compute the length of the drawn path. We can do this by adding an event listener to the map widget that gets called when drawing is completed (i.e. on_draw_end). The event listener then computes the geodesic length of the drawn geometry using the geometry service and prints it out:


    def calc_dist(map, g):
        length = gis.tools.geometry.lengths(g['spatialReference'], [g], "", "geodesic")
        print("Length:" + str(length[0]) + " m.")
    
    map.on_draw_end(calc_dist)


    map.draw("freehandpolyline")


    map.clear_graphics()
