
# Using The GIS 

The GIS object is the most important object when working with the Arcgis Python API. The GIS object represents the online GIS you are working with, be it ArcGIS Online or an ArcGIS Portal. You use the GIS object to consume and publish GIS content and administrators may use it to manage GIS users, groups and datastores. The GIS object also includes a number of tools, including spatial analysis tools, big-data analytics tools, raster analytics tools as well as helper services such as geocoding and geometry to help in your workflows.

To use the GIS object, import GIS from the arcgis.gis module:


    from arcgis.gis import GIS

To create the GIS object, we pass in the url and our login credentials:


    gis = GIS("https://deldev.maps.arcgis.com", "demo_deldev", "P@ssw0rd")

Here, we're connecting to ArcGIS Online (the default GIS used when the url is not provided) as an anonymous user:


    gis = GIS()

Adding a '?' mark in front of an object and querying it brings up help for that object in the notebook:


    gis?

The notebook provides intellisense and code-completion. Typing a dot after an object and hitting tab brings up a drop-down with it's properties and methods:
![dropdown showing members of GIS class](http://esri.github.io/arcgis-python-api/notebooks/nbimages/01-dropdown.png)

The GIS object provides helper objects to manage the GIS resources, i.e. the users, groups, content and datastores. These helper utilities are in the form of helper objects named users, groups, content and datastore respectively. 

Each such helper object has similar patterns of usage: there are methods to get(), search() and create() the respective resources.


    user = gis.users.get('rxsingh')

The Arcgis Python API is integrated with IPython Notebook to make it easy to visualize and interact with GIS resources. The user object has a rich representation that can be queried like this:


    user




<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=rxsingh' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/rxsingh/info/rohit150.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=rxsingh' target='_blank'><b>Rohit Singh</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: Rohit
                        <br><b>Last Name</b>: Singh
                        <br><b>Username</b>: rxsingh
                        <br><b>Joined</b>: July 02, 2014
                        
                    </div>
                </div>
                



The resources are implemented as Python dictionaries. You can query for the resource properties using the <b><code>resource['property']</code></b> notation:


    user['firstName']




    'Rohit'



The properties are also available as properties on the resource object, so you can use the dot notation to access them:


    user.lastName




    'Singh'



The resources provide methods to update(), delete() and use the object.

The GIS object includes a map widget that can be used to visualize the content of your GIS as well as see the results of your analysis. Let's bring up a map of Palm Springs, CA:


    map = gis.map("Palm Springs, CA")
    map

    :0: FutureWarning: IPython widgets are experimental and may change in the future.
    

![Sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/01-palm-springs-map.png "(Sample output)")

We can search for content in our GIS. Let's search for Hiking Trails in the Palm Springs region. We do that by calling gis.content.search() and for each web map or web layers that gets returned, we can display it's rich representation within the notebook:


    from IPython.display import display
    
    items = gis.content.search('Palm Springs Trails')
    for item in items:
        display(item)


<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=cdc1938091924d0c9241b6a6a106a062' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/cdc1938091924d0c9241b6a6a106a062/info/thumbnail/CIP_ALL2.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=cdc1938091924d0c9241b6a6a106a062' target='_blank'><b>Lee County Capital Improvement Projects</b>
                        </a>
                        <br>This webmap shows the locations of the CIP projects located in Lee County & budgets allocated per each project over the CIP years.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/layers16.png' style="vertical-align:middle;">Web Mapping Application by roblovell
                        <br>Last Modified: January 27, 2016
                        <br>0 comments, 1,108 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=9cd004f756c2402595a339a7d8560a4e' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/9cd004f756c2402595a339a7d8560a4e/info/thumbnail/CIP_ALL2.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=9cd004f756c2402595a339a7d8560a4e' target='_blank'><b>Lee County CIP Projects</b>
                        </a>
                        <br>This webmap shows the locations of the CIP projects located in Lee County & budgets allocated per each project over the CIP years.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by roblovell
                        <br>Last Modified: February 09, 2016
                        <br>0 comments, 810 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=302669bf6dcd484eb049c1ba8f9fe6fb' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/302669bf6dcd484eb049c1ba8f9fe6fb/info/thumbnail/CIP_ALL2.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=302669bf6dcd484eb049c1ba8f9fe6fb' target='_blank'><b>Lee County CIP Projects</b>
                        </a>
                        <br>This webmap shows the locations of the CIP projects located in Lee County & budgets allocated per each project over the CIP years.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/layers16.png' style="vertical-align:middle;">Web Mapping Application by roblovell
                        <br>Last Modified: February 09, 2016
                        <br>0 comments, 646 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=89a56535e8514a8e96e1d91a9d5aa260' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/89a56535e8514a8e96e1d91a9d5aa260/info/thumbnail/thumbnail.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=89a56535e8514a8e96e1d91a9d5aa260' target='_blank'><b>Trails</b>
                        </a>
                        <br>PS trails<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/featureshosted16.png' style="vertical-align:middle;">Feature Service by Rupert_Essinger
                        <br>Last Modified: March 10, 2015
                        <br>0 comments, 417 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=306d9e194b434d419445f1c996a618d3' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/306d9e194b434d419445f1c996a618d3/info/thumbnail/joshuatreeflower.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=306d9e194b434d419445f1c996a618d3' target='_blank'><b>Joshua Tree - Lost Palms Oasis Trail</b>
                        </a>
                        <br>This map tour will take you on a hike through Joshua Tree National Park.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/layers16.png' style="vertical-align:middle;">Web Mapping Application by JenniferBell_UO
                        <br>Last Modified: May 19, 2016
                        <br>0 comments, 530 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=df112d43295440938d1b6f5ea065f033' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/df112d43295440938d1b6f5ea065f033/info/thumbnail/ago_downloaded.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=df112d43295440938d1b6f5ea065f033' target='_blank'><b>Skyline Trail</b>
                        </a>
                        <br>Short trail run that starts from Ramon Rd in Palm Springs and runs down the Skyline Trail.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by Kelly
                        <br>Last Modified: May 22, 2013
                        <br>0 comments, 373 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=c147af1450c94e3daf00503916431aba' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/c147af1450c94e3daf00503916431aba/info/thumbnail/thumbnail.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=c147af1450c94e3daf00503916431aba' target='_blank'><b>cactus to clouds trail</b>
                        </a>
                        <br>Hiking Trail from Palm Springs to San Jacinto Peak<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by cjosephmayfield
                        <br>Last Modified: April 06, 2012
                        <br>0 comments, 107 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=ae4b4dfe6d944f63a40d6044014b9392' target='_blank'>
                        <img src='http://static.arcgis.com/images/desktopapp.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=ae4b4dfe6d944f63a40d6044014b9392' target='_blank'><b>Albert E. Davies Wetland Trail at Lake Newport. Mill Creek Park, Boardman, OH</b>
                        </a>
                        <br>Lake Newport and the wetland at its southern end are both man-made, dating from the 1920s. Together they cover about 100 acres and in summer attract recreational kayakers, picnickers, and others. Its rarely crowded, however, and from September to April, it can sometimes be completely deserted. The trail itself is only a few hundred meters long. Winding through reed-beds it dead-ends at a lookout on the lake facing an array of small islands, some of which are accessible only by kayak. The viewing platform is located at 410309.76N and 804034.05W. Parking is available a few hundred yards from the trail head; toilets are also provided. Access to the parking lot is from West Newport Drive in Mill Creek Park. 
The wetlands are a good all-round bird-watching spot. A wide variety of warblers can be encountered during Spring and Fall migration. Ive seen Palm, Yellow-Rumped, Black-Throated Green, and many others. On the east side of the viewing platform, across a few tens of meters of water, there is a mud-flat. Depending on the water level it varies considerably in size, occasionally disappearing altogether. Although small, its often a good place to look for wading birds, particularly in late summer and early fall. Among the ubiquitous Killdeer and Canada Geese, I have seen Least, Spotted, and Solitary Sandpipers and Lesser Yellowlegs on several occasions. Bald Eagles often can be spotted in the trees just across the water. 
Visit year-round
This is my favorite "home patch." It's located between my home in Boardman and YSU, where I teach, so this is the place I bird most often  by far! During the academic year I usually stop in for twenty or thirty minutes early in the morning on the way to work at least every other day. By now I know pretty much every tree, bush, and mud-patch! 
<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by bbonhomme
                        <br>Last Modified: December 03, 2014
                        <br>0 comments, 64 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=de5e98e0d4b54ffd9fe0165e3d51107a' target='_blank'>
                        <img src='http://static.arcgis.com/images/desktopapp.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=de5e98e0d4b54ffd9fe0165e3d51107a' target='_blank'><b>Albert E. Davies Wetland Trail at Lake Newport. Mill Creek Park, Boardman, OH</b>
                        </a>
                        <br>Lake Newport and the wetland at its southern end are both man-made, dating from the 1920s. Together they cover about 100 acres and in summer attract recreational kayakers, picnickers, and others. Its rarely crowded, however, and from September to April, it can sometimes be completely deserted. The trail itself is only a few hundred meters long. Winding through reed-beds it dead-ends at a lookout on the lake facing an array of small islands, some of which are accessible only by kayak. The viewing platform is located at 410309.76N and 804034.05W. Parking is available a few hundred yards from the trail head; toilets are also provided. Access to the parking lot is from West Newport Drive in Mill Creek Park. 
The wetlands are a good all-round bird-watching spot. A wide variety of warblers can be encountered during Spring and Fall migration. Ive seen Palm, Yellow-Rumped, Black-Throated Green, and many others. On the east side of the viewing platform, across a few tens of meters of water, there is a mud-flat. Depending on the water level it varies considerably in size, occasionally disappearing altogether. Although small, its often a good place to look for wading birds, particularly in late summer and early fall. Among the ubiquitous Killdeer and Canada Geese, I have seen Least, Spotted, and Solitary Sandpipers and Lesser Yellowlegs on several occasions. Bald Eagles often can be spotted in the trees just across the water. 
Visit year-round
This is my favorite "home patch." It's located between my home in Boardman and YSU, where I teach, so this is the place I bird most often  by far! During the academic year I usually stop in for twenty or thirty minutes early in the morning on the way to work at least every other day. By now I know pretty much every tree, bush, and mud-patch! 
<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/layers16.png' style="vertical-align:middle;">Web Mapping Application by bbonhomme
                        <br>Last Modified: December 03, 2014
                        <br>0 comments, 59 views
                    </div>
                </div>
                



<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/item.html?id=fbe6713d6aa94e0fb4fec08952949119' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/fbe6713d6aa94e0fb4fec08952949119/info/thumbnail/palm_springs.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/item.html?id=fbe6713d6aa94e0fb4fec08952949119' target='_blank'><b>Palm Springs Trails</b>
                        </a>
                        <br>Trails in the Palm Springs area affected by the BLM - Agua Caliente land exchange<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/featureshosted16.png' style="vertical-align:middle;">Feature Service by paniello_geodesign
                        <br>Last Modified: March 13, 2015
                        <br>0 comments, 73 views
                    </div>
                </div>
                


We can add then add the returned web layers to our map. To add the last layer returned above, we call map.add_layer() and pass in the layer for Palm Springs Trail:


    map.add_layer(items[9])
