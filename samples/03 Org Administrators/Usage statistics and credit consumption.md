
# Usage statistics and credit consumption

GIS administrators can query the GIS object for usage statistics and credit consumption, and plot them using Python plotting libraries right in the IPython Notebook to spot trends and take take action. Note that this functionality isn't available in pre-10.5 portals. The example below queries an ArcGIS Portal for usage counts of Geocoding.


    from arcgis.gis import *
    
    gis = GIS("https://dev04875.esri.com/arcgis", "portaladmin", "portaladmin")
    
    usage = gis.usage(startTime=1432209600, endTime=1437480000, period='1d', vars='num', 
                      etype='geocodecnt', stype='geocode', groupby='username,stype,type')
    

Having taken the usage date, we can use Python libraries such as Numpy and Bokeh to plot the usage of the Geocoding service and plot trends:


    import numpy as np
    from bokeh.plotting import figure, output_notebook, show
    
    npa = np.array(usage['data'][0]['num'], 'i8')
    npb = np.array(usage['data'][1]['num'], 'i8')
    npc = np.array(usage['data'][2]['num'], 'i8')
    
    timestamps = npa[:,0]
    vala = npa[:,1]
    valb = npb[:,1]
    valc = npc[:,1]
    valtot = vala + valb + valc
    
    output_notebook()
    
    # create a new plot with a title and axis labels
    p = figure(title="Geocoding usage", x_axis_label='Date', y_axis_label='Geocode count', x_axis_type="datetime",plot_width=810)
    
    # add a line renderer with legend and line thickness
    p.line(timestamps, valtot, legend="Total", line_width=6)
    p.line(timestamps, vala, legend="anonymous", line_width=2, line_color="red")
    p.line(timestamps, valb, legend=usage['data'][1]['username'], line_width=2, line_color="green")
    p.line(timestamps, valc, legend=usage['data'][2]['username'], line_width=2, line_color="orange")
    
    # show the results
    show(p)

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/bokeh.png">

In the example above, we see that anonymous users were the top consumer of geocoding credits. The GIS administrator was able to visualize this using the usage plot, and turned off geocoding for anonymous users, thereby saving on ArcGIS credits.
