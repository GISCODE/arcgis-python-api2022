
##The ContentManager class

<hr/>

##<b>class gis.ContentManager<b>(<i>portal</i>)

Manager class for manipulating GIS content. This class is not created by users directly. An instance of this class, called ‘content’, is available as a property of the Gis object. Users call methods on this ‘content’ object to manipulate (create, get, search...) items.

 <hr>

###add(<i>item_properties, data=None, thumbnail=None, metadata=None, owner=None, folder=None</i>)

Adds content to a Portal by creating an item.

<div class="alert alert-success">
That content can be a file (such as a service definition, shapefile, CSV, layer package, geoprocessing package, map package) or it can be a URL (to an ArcGIS Server service, WMS service, or an application).
<p>
If you are uploading a package or other file, provide a path or URL to the file in the data argument.
<p>
From a technical perspective, none of the item properties below are required. However, it is strongly recommended that title, type, typeKeywords, tags, snippet, and description be provided.

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
<td>required dictionary, see below for the keys and values</td>
</tr>

<tr class="row-odd"><td>data</td>
<td>optional string, either a path or URL to the data</td>
</tr>

<tr class="row-even"><td>thumbnail</td>
<td>optional string, either a path or URL to an image</td>
</tr>

<tr class="row-odd"><td>metadata</td>
<td>optional string, either a path or URL to metadata</td>
</tr>

<tr class="row-even"><td>owner</td>
<td>optional string, defaults to logged in user</td>
</tr>

<tr class="row-odd"><td>folder</td>
<td>optional string, content folder where placing item</td>
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


**Returns:**	The item if successfully added, None if unsuccessful.

<hr>

###create_folder(<i>owner, title</i>)

Creates a folder for the given user with the given title.

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
<tr class="row-even"><td>owner</td>
<td>required string, the name of the user</td>
</tr>
<tr class="row-even"><td>title</td>
<td>required string, the name of the folder to create for the owner</td>
</tr>
</tbody>
</table>

**Returns:**	a python dict like the following: {“username” : “portaladmin”,”id” : “bff13218991c4485a62c81db3512396f”,”title” : “testcreate”}

<hr>

###create_service(<i>name, service_description='', has_static_data=False, max_record_count=1000, supported_query_formats='JSON', capabilities='Image, Catalog, Metadata, Download, Pixels, Edit, Mensuration, Uploads', description='', copyright_text='', wkid=102100, service_type='imageService', owner=None, folder=None</i>)

Creates a service in the Portal

<b>Returns</b>:
The item for the service, if successfully added, None if unsuccessful. 

<hr>

###get(<i>itemid</i>)

Returns the item object for the specified itemid.

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
<tr class="row-even"><td>itemid</td>
<td> required string, the item identifier</td>
</tr>
</tbody>
</table>

**Returns:**	None if the item is not found and returns an item object if the item is found

<hr>

###get_folder_id(<i>owner, folder_name</i>)

Finds the folder for a particular owner and returns its id.

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
<tr class="row-even"><td>owner</td>
<td>required string, the name of the user</td>
</tr>
<tr class="row-even"><td>folder_name</td>
<td>required string, the name of the folder to search for</td>
</tr>
</tbody>
</table>

**Returns:**
the folder id, if the folder is found

<hr>

###import_data(<i>df, address_fields=None</i>)

Imports a Pandas data frame, that has an address column, as a feature collection

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
<tr class="row-even"><td>df</td>
<td>pandas dataframe </td>
</tr>
<tr class="row-even"><td>address_fields</td>
<td>dict containing mapping of df columns to address fields, eg: { “CountryCode” : “Country”} or { “Address” : “Address” }</td>
</tr>
</tbody>
</table>

**Returns:**
Returns feature collection, that can be used for analysis, visualization or published to the GIS as an item

<hr>

###search(<i>query, item_type=None, sort_field='numViews', sort_order='desc', max_items=6, add_org=False</i>)

Searches for portal items.

Returns a list of items matching the specified query

<div class="alert alert-success">
A few things that will be helpful to know.
<p>
1.The query syntax has quite a few features that can’t be adequately described here. The query syntax is available in ArcGIS help. A short version of that URL is http://bitly.com/1fJ8q31.
<p>
2.Most of the time when searching groups you want to search within your organization in ArcGIS Online or within your Portal. As a convenience, the method automatically appends your organization id to the query by default. If you don’t want the API to append to your query set add_org to false. If you use this feature with an OR clause such as field=x or field=y you should put this into parenthesis when using add_org.

</div>

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

<tr class="row-even"><td>query</td>
<td>required string, query string. See notes.</td>
</tr>


<tr class="row-even"><td>item_type</td>
<td>Optional string, set type of item to search</td>
</tr>

<tr class="row-even"><td>sort_field</td>
<td>optional string, valid values can be title, uploaded, type, owner, modified, avgRating, numRatings, numComments, and numViews.</td>
</tr>

<tr class="row-even"><td>sort_order</td>
<td>optional string, valid values are asc or desc</td>
</tr>

<tr class="row-even"><td>max_users</td>
<td>optional int, maximum number of items returned<, default is 6/td>
</tr>

<tr class="row-even"><td>add_org</td>
<td>optional boolean, controls whether to search within your org (default is False)</td>
</tr>

</tbody>
</table>

**Returns:**
	Returns a list of items matching the specified query

<hr>
