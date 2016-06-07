
##The GIS class

<hr/>

<code><b>class gis.GIS<b>(<i>url=None, username=None, password=None</i>)</code>

Constructs a GIS object given a url and user credentials to ArcGIS Online 
        or an ArcGIS Portal. If no url is provided, ArcGIS Online is used. If username
        and password are not provided, anonymous access is used.

A GIS is representative of ArcGIS Online or an ArcGIS Portal site. The GIS object provides helper objects (as properties) to manage (search, create, retrieve) GIS resources:
* **users**
* **groups**
* **content**
* **datastores**
* **tools**, including
  * geocoder
  * analysis
  * rasters
  * geoanalytics  
  * geometry

Additionally, the GIS object has properties as well as methods to display usage statistics and map widgets: 
* **properties**
* **usage()**
* **map()**


    from arcgis.gis import GIS
    
    # Example: connect to ArcGIS Online as an anonymous user 
    gis = GIS()

##map(<i>self, location=None, zoomlevel=None</i>)

Creates a map widget centered at the location (Address) with the specified zoom-level


    #Example: create a map centered on Palm Springs
    map = gis.map('Redlands, CA', 12)
    map

    :0: FutureWarning: IPython widgets are experimental and may change in the future.
    

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/redlands.png" />

<hr>

###users

The resource manager for GIS users


    #Example: query a user from the gis
    gis.users.search('johnsmith')[0]




<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=jes0070' target='_blank'>
                        <img src='http://www.arcgis.com/home/js/arcgisonline/css/images/no-user-thumb.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=jes0070' target='_blank'><b>JOHN SMITH</b>
                        </a>
                        <br><br><b>Bio</b>: Real Estate Services @ Reconassist and 4deeds.com SALESFORCE.COM (SFDC), GPS, GIS, VA. Beach, VA.   @1JohnSmith
                        <br><b>First Name</b>: JOHN
                        <br><b>Last Name</b>: SMITH
                        <br><b>Username</b>: jes0070
                        <br><b>Joined</b>: November 04, 2011
                        
                    </div>
                </div>
                



<hr>

###groups

The resource manager for groups in the GIS


    gis.groups.search('Python')[0]




<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/group.html?id=8f3721913b474c87910c767e717bdc20' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/groups/8f3721913b474c87910c767e717bdc20/info/C_3A_Installs_Scripts_Python_ALF_Data.gif' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/group.html?id=8f3721913b474c87910c767e717bdc20' target='_blank'><b>Aggregated Live Feed Community</b>
                        </a>
                        <br>
                        <br><b>Summary</b>: A collection of tools, scripts, and methodologies that help ArcGIS users better leverage available data. (expand for more detail)
                        <br><b>Description</b>: <p>Use the components found here to build automated update routines that download content from just about anywhere, process it, and produce a consumable data set that can be used by ArcGIS products.</p><p><img alt='ALF-Lite process diagram' src='https://s3.amazonaws.com/tmLiveFeeds/Images/ALF-Lite_Diagram_v1.1.gif' /></p><ul><li>Written in Python, these routines can run on any OS that supports Python, ArcGIS, and ArcPy.</li><li>Using the ALF-Lite architecture will reduce thedemand on Enterprise Resources by leveraging the File Geodatabase.</li><li>Lightweight and simple enough to run on a single User's Desktop, yet powerful enough to scale out to a distributed, multi-tiered environment.Use your Python skills and tailor to your needs!</li><li>The 'Log' files are automatically maintained by the Logger object found inthe<a href='http://www.arcgis.com/home/item.html?id=b01b18bbf0e34338b6a2c71609ea1373' target='_blank'>ALFlib</a> library.</li><li>The 'Deployment' logic is integrated into a user-maintained configuration file. It's up to you how to deploy the data. By default, the Feed Routines copy their workspace to a Live folder, ready for consumption.</li><li>The 'Live' FileGDB can be directly consumed by ArcGIS Desktop or published by ArcGIS Server using a Map Service even while the script updates the underlying data. Eliminating the need to re-cycle live services just to refresh a data source!<br /></li><li>To maintain the Live data on a regular interval, schedule a task or cron job to run the Feed Routine as often as needed to keep the data current.</li></ul><p>Here's an example mapof live Rain fall intensity (precipitation),NOAA Weather Advisories, and Wind Speed and Direction dataall prepared by ALF-Lite routines and publishedusing ArcGIS Server Map Services:</p><p><img alt='ALF-Lite data set example' src='https://s3.amazonaws.com/tmLiveFeeds/Images/ALF-Lite_Example_v1.0.gif' /></p>
                        <br><b>Owner</b>: Esri_Technical_Marketing
                        <br><b>Created</b>: April 10, 2012
                        
                    </div>
                </div>
                



<hr>

###content

The resource manager for content within the GIS


    #Example: List content related to San Diego
    from IPython.display import display
    
    items = gis.content.search('San Diego', max_items=3)
    for item in items:
        display(item)


<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=26f7674a2ad744f3806af0c426531951' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/26f7674a2ad744f3806af0c426531951/info/thumbnail/SDEmergency_portal_Link_toAGO.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=26f7674a2ad744f3806af0c426531951' target='_blank'><b>County of San Diego Emergency Map (Live)</b>
                        </a>
                        <br>Public feed from the County of San Diego Office of Emergency Services and other emergency-related feeds.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by oes_services
                        <br>Last Modified: June 03, 2016
                        <br>11 comments, 3,262,968 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=1966ef409a344d089b001df85332608f' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/1966ef409a344d089b001df85332608f/info/thumbnail/thumbnail_san_diego_map.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=1966ef409a344d089b001df85332608f' target='_blank'><b>San Diego Shortlist</b>
                        </a>
                        <br>Rupert Essinger from the Esri Story Maps team shares a selection of cool places to go in this Southern Californian beach city where he lives.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by RupertEssinger
                        <br>Last Modified: June 05, 2016
                        <br>22 comments, 290,715 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=1fe3292959da4c3d84cbe2def87a89c0' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/1fe3292959da4c3d84cbe2def87a89c0/info/thumbnail/San_Diego_Trolley.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=1fe3292959da4c3d84cbe2def87a89c0' target='_blank'><b>San Diego Trolley</b>
                        </a>
                        <br>Complete trolley lines and stations of the San Diego Trolley using data from San Diego Association of Governments (SANDAG) with several updates applied<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/mapimages16.png' style="vertical-align:middle;">Map Service by RupertEssinger
                        <br>Last Modified: September 11, 2012
                        <br>0 comments, 185,432 views
                    </div>
                </div>
                


<hr>

###datastores

Resource manager for managing GIS data stores. Only available with the portal. Under construction

<hr>

###tools

Collection of helper tools and services available in the GIS


    # User the geocoder tool from the GIS's tool collection to re-center the map above on Times Square
    # scroll up to the map() section
    map.center = gis.tools.geocoder.find_best_match("Times Square, NY")

<hr>

###properties

The properties of the GIS, accessible as a Python dict


    #Excample
    gis.properties['portalName']




    'ArcGIS Online'



<hr>

###usage(<i>startTime, endTime, period, vars, etype, stype, groupby, appId=None<i>)

Usage statistics for the GIS

<hr>
