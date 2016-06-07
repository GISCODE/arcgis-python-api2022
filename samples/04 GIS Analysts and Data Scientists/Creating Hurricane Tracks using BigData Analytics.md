
The sample code below uses big data analytics (geoanalytics) to reconstruct hurricane tracks using data registered on a bigdata fileshare datastore in the GIS. Note that this functionality is not available yet with ArcGIS Online and is currently in Beta for ArcGIS Portal 10.5 


    from arcgis.gis import GIS
    from arcgis.viz import MapView
    from arcgis.tools import GeoAnalyticsTools
    
    gis = GIS("https://dev06999.esri.com/portal/", "admin", "changeit")
    gae = GeoAnalyticsTools('https://dev06999.esri.com/server/rest/services/GeoAnalyticsTools/GPServer', gis)

    :0: FutureWarning: IPython widgets are experimental and may change in the future.
    


    tracks = gae.reconstruct_tracks("/server/datastores/bigDataFileShares/gae6/hurricanes", None,
                                    "serial_num", "GEODESIC", None, None)

    Submitted.
    Executing...
    Executing (Reconstruct Tracks): ReconstructTracks /server/datastores/bigDataFileShares/gae6/hurricanes # serial_num GEODESIC # # # # # #
    Start Time: Sun Jun 05 06:50:15 2016
    Using GPString param: /server/datastores/bigDataFileShares/gae6/hurricanes
    valid coordinate range : Envelope: [-400.0, -400.0, 9006799.25474099, 9006799.25474099]
    Writing to managed relational datastore (table=ReconstructTracks_jbc105e52db67406387fd50afe7a995b8)
     * interval=1848-01-11 06:00:00.000 -> 1899-12-26 06:00:00.000
     * count=568
    Created feature service for result: http://Dev06999.esri.com/server/rest/services/Hosted/ReconstructTracks_jbc105e52db67406387fd50afe7a995b8/FeatureServer
    Succeeded at Sun Jun 05 06:50:36 2016 (Elapsed Time: 21.19 seconds)
    {'out_features': {'url': 'http://Dev06999.esri.com/server/rest/services/Hosted/ReconstructTracks_jbc105e52db67406387fd50afe7a995b8/FeatureServer/0'}}
    FL URL: http://Dev06999.esri.com/server/rest/services/Hosted/ReconstructTracks_jbc105e52db67406387fd50afe7a995b8/FeatureServer/0
    FS URL: http://Dev06999.esri.com/server/rest/services/Hosted/ReconstructTracks_jbc105e52db67406387fd50afe7a995b8/FeatureServer
    

    Possible issues were found while reading 'in_features'
     * Some records have no time values or the time values were unable to be parsed
          > [null,[1962272N10161,1962,32,WP,MM,EMMA:FREDA,9/28/1962 12:00,TS,9.5,161.0,0.0,1008,tokyo,-100.0,1.524,main,0,0],null,{"x":161,"y":9.5}]
          > [null,[1962272N10161,1962,32,WP,MM,EMMA:FREDA,9/28/1962 18:00,TS,9.6,160.5,0.0,1006,tokyo,-100.0,4.407,main,0,0],null,{"x":160.5,"y":9.6}]
          > [null,[1962272N10161,1962,32,WP,MM,EMMA:FREDA,9/29/1962 0:00,TS,10.0,160.0,0.0,1008,tokyo,-100.0,1.524,main,0,0],null,{"x":160,"y":10}]
    


    map = MapView()
    map

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/geoanalytics.png"/>


    map.zoom = 2


    map.add_layer(tracks)


    map.set_time_extent('1/1/1887 UTC', '1/1/1888 UTC')
