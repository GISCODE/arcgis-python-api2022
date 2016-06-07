
##The Item class

<hr/>

##<b>class gis.Item<b>(<i>portal, itemid, itemdict=None</i>)

Bases: builtins.dict

An item (a unit of content) in the GIS. Each item has a unique identifier and a well known URL that is independent of the user owning the item. An item can have associated binary or textual data that’s available via the item data resource. For example, an item of type Map Package returns the actual bits corresponding to the map package via the item data resource.

An instance of this class is not created directly by users. It is returned from the gis.content ContentManager object as a result of an add() or search() operation. Several GIS tools, such as the Analysis tools, also return Items representing Layers in the GIS.


    from arcgis.gis import GIS
    
    gis = GIS()
    item = gis.content.search('stamen watercolor')[0]

The item object has a rich representation in the IPython notebook environment:


    item




<div class="item_container">
                    <div class="item_left">
                       <a href='http://www.arcgis.com/home/item.html?id=80003c63c97548899d858fc3c380370f' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/content/items/80003c63c97548899d858fc3c380370f/info/thumbnail/watercolorthumb.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right">
                        <a href='http://www.arcgis.com/home/item.html?id=80003c63c97548899d858fc3c380370f' target='_blank'><b>Stamen Watercolor</b>
                        </a>
                        <br>Stamen's Watercolor tileset<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/maps16.png' style="vertical-align:middle;">Web Map by cartogeek
                        <br>Last Modified: April 01, 2013
                        <br>0 comments, 10,093 views
                    </div>
                </div>
                



The item object is a Python dict. Item properties can be accessed using subscript notation:


    item['title']




    'Stamen Watercolor'



The item properties can also be accessed using the dot(.) notation, as properties of the class:


    item.numViews




    10093



 <hr>

###delete()

Deletes an item.

<div class="alert alert-success">
This function does not apply to those using enterprise accounts that come from an enterprise such as ActiveDirectory, LDAP, or SAML. It only has an effect on built-in users.

If a new security question is specified, a new security answer should be provided.
</div>

**Arguments:**
None

**Returns:**	a boolean, indicating success

<hr>

###update(<i>item_properties=None, data=None, thumbnail=None, metadata=None</i>)

Updates this item’s properties. See http://resources.arcgis.com/en/help/arcgis-rest-api/index.html#//02r3000000ms000000

<div class="alert alert-success">
Only pass in arguments for properties you want to update. All other properties will be left as they are. If you want to update description, then only provide the description argument in item_properties.

That content can be a file (such as a layer package, geoprocessing package, map package) or it can be a URL (to an ArcGIS Server service, WMS service, or an application).

If you are uploading a package or other file, provide a path or URL to the file in the data argument.
</div>

**Arguments:**
<table border="1" class="docutils">
<colgroup>
<col width="22%">
<col width="78%">
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><strong>Argument</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="row-even"><td>item_properties</td>
<td>dictionay containing item properties and their values. Supported item properties are listed <a href="http://resources.arcgis.com/en/help/arcgis-rest-api/index.html#/Common_parameters/02r30000009v000000/">here (see Item parameters)</a></td>
</tr>
<tr class="row-odd"><td>data</td>
<td>optional string, either a path or URL to the data</td>
</tr>
<tr class="row-even"><td>thumbnail</td>
<td>optional string, path or url to a file.  can be PNG, GIF,
JPEG, max size 1 MB</td>
</tr>
<tr class="row-odd"><td>metadata</td>
<td> optional string, either a path or URL to metadata</td>
</tr>
</tbody>
</table>

item_properties dict can have the following keys and values:
<table border="1" class="docutils">
<colgroup>
<col width="22%">
<col width="78%">
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><strong>Key</strong></td>
<td><strong>Value</strong></td>
</tr>
<tr class="row-even"><td>type</td>
<td>optional string, indicates type of item.  See URL below for valid values.</td>
</tr>
<tr class="row-odd"><td>typeKeywords</td>
<td>optinal string list.  Lists all sub-types.  See URL for valid values.</td>
</tr>
<tr class="row-even"><td>description</td>
<td>optional string.  Description of the item.</td>
</tr>
<tr class="row-odd"><td>title</td>
<td>optional string.  Name of the item.</td>
</tr>
<tr class="row-odd"><td>url</td>
<td>optional string.  URL to item that are based on URLs.</td>
</tr>
<tr class="row-odd"><td>tags</td>
<td>optional string of comma-separated values.  Used for searches on items.</td>
</tr>
<tr class="row-odd"><td>snippet</td>
<td>optional string.  Provides a very short summary of the what the item is.</td>
</tr>
<tr class="row-odd"><td>accessInformation</td>
<td>optional string with comma separated values for min x, min y, max x, max y.</td>
</tr>
<tr class="row-odd"><td>spatialReference</td>
<td>optional string.  Coordinate system that the item is in.</td>
</tr>
<tr class="row-odd"><td>accessInformation</td>
<td>optional string.  Information on the source of the content.</td>
</tr>
<tr class="row-odd"><td>licenseInfo</td>
<td>optinal string, any license information or restrictions regarding the content.</td>
</tr>
<tr class="row-odd"><td>culture</td>
<td>optional string.  Locale, country and language information.</td>
</tr>
<tr class="row-odd"><td>access</td>
<td>optional string.  Valid values: private, shared, org, or public.</td>
</tr>
<tr class="row-odd"><td>commentsEnabled</td>
<td>optional boolean.  Default is true.  Controls whether comments are allowed.</td>
</tr>
<tr class="row-odd"><td>culture</td>
<td>optional string.  Language and country information.</td>
</tr>
</tbody>
</table>

URL: http://resources.arcgis.com/en/help/arcgis-rest-api/index.html#//02r3000000ms000000

**Returns:**	a boolean indicating success

<hr>

###download(<i>dir_name</i>)

Downloads this item's data to the specified folder.

**Arguments:**
<table border="1" class="docutils">
<colgroup>
<col width="22%">
<col width="78%">
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><strong>Argument</strong></td>
<td><strong>dir_name</strong></td>
</tr>
<tr class="row-even"><td>reassign_to</td>
<td>filesystem path where the data will be downloaded.</td>
</tr>
</tbody>
</table>

**Returns:**	filename

<hr>

###get_item_data()

Fethces this item's data as an ordered dictionary

**Arguments:**
None

**Returns:**
item's data as an ordered dictionary

<hr>

###get_thumbnail()

Returns the bytes that make up the thumbnail for this item.

**Arguments:**
None.

**Returns:**
bytes that represent the image.

**Example:**
<code>
response = item.get_thumbnail()
f = open(filename, 'wb')
f.write(response)
</code>

<hr>

###get_thumbnail_link()

Returns the URL to the thumbnail image

<hr>

###publish(<i>publish_parameters=None, address_fields=None, output_type=None, overwrite=False</i>)

Publishes a hosted service based on an existing source item (this item). Publishers can create feature services as well as tiled map services. 

Feature services can be created using input files of type csv, shapefile, serviceDefinition, featureCollection, and fileGeodatabase. CSV files that contain location fields, (ie.address fields or X, Y fields) are spatially enabled during the process of publishing. Shapefiles and file geodatabases should be packaged as .zip files. Tiled map services can be created from service definition (.sd) files, tile packages, and existing feature services. 

Service definitions are authored in ArcGIS for Desktop and contain both the cartographic definition for a map as well as its packaged data together with the definition of the geo-service to be created. Use the Analyze operation to generate the default publishing parameters for CSVs. 

**Arguments:**
<table border="1" class="docutils">
<colgroup>
<col width="21%">
<col width="79%">
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><strong>Argument</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="row-even"><td>publish_parameters</td>
<td>A disctionary describing the service to be created as part of the publish operation. The appropriate value for publish parameters depends on the file type being published. Example: publishParameters={"name":"Streets"} . See http://resources.arcgis.com/en/help/arcgis-rest-api/index.html#/Publish_Item/02r300000080000000/
</td>
</tr>
<tr class="row-even"><td>address_fields</td>
<td>used when publishing CSV files.  dict containing mapping of df columns to address fields, eg: { “CountryCode” : “Country”} or { “Address” : “Address” }</td>
</tr>
<tr class="row-even"><td>output_type</td>
<td>Only used when a feature service is published as a tile service Example: outputType=Tiles
</td>
</tr>
<tr class="row-even"><td>overwrite</td>
<td>optional boolen, set to True if overwriting</td>
</tr>

</tbody>
</table>

**Returns:**
	a boolean, indicating success

<hr>

###reassign_to(<i>target_owner, target_folder=None</i>)

Allows the administrator to reassign a single item from one user to another.

<div class="alert alert-success">If you wish to move all of a user’s items (and groups) to another user then use the user.reassign_to() method. This method only moves one item at a time.</div>

**Arguments:**
<table border="1" class="docutils">
<colgroup>
<col width="22%">
<col width="78%">
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><strong>Argument</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="row-even"><td>target_owner</td>
<td>required string, desired owner of the item</td>
</tr>
<tr class="row-even"><td>target_folder</td>
<td>optional string, folder to move the item to</td>
</tr>
</tbody>
</table>

**Returns:**
	a boolean, that indicates success

<hr>

###share(<i>everyone=False, org=False, groups=''</i>)

Shares an item with the specified list of groups


**Arguments:**
<table border="1" class="docutils">
<colgroup>
<col width="22%">
<col width="78%">
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><strong>Argument</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="row-even"><td>everyone</td>
<td>optional boolean, share with everyone</td>
</tr>
<tr class="row-even"><td>org</td>
<td>optional boolean, share with the organization</td>
</tr>
<tr class="row-even"><td>groups</td>
<td>optional string, comma-separated list of group IDs with which the item will be shared</td>
</tr>
</tbody>
</table>

**Returns:**
	dict with key “notSharedWith” containing array of groups with which the item could not be shared.

<hr>

###unshare(<i>groups</i>)

Stops sharing the item with the specified list of groups

**Arguments:**
<table border="1" class="docutils">
<colgroup>
<col width="22%">
<col width="78%">
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><strong>Argument</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="row-even"><td>groups</td>
<td>optional string, comma-separated list of group IDs with which the item will be unshared</td>
</tr>
</tbody>
</table>

**Returns:**
	dict with key “notUnsharedFrom” containing array of groups with which the item could not be shared.

<hr>
