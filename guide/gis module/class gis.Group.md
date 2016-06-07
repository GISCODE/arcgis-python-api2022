
##The Group class

<hr/>

##<b>class gis.Group<b>(<i>portal, groupid, groupdict=None)</i>)

Bases: builtins.dict

Represents a group (for example, San Bernardino Fires) within the GIS (ArcGIS Online or Portal for ArcGIS)

An instance of this class is not created directly by users. It is returned from the gis.groups GroupManager object as a result of an create() or search() operation.


    from arcgis.gis import GIS
    
    gis = GIS()
    group = gis.groups.search('Python')[0]

The group object has a rich representation in the IPython notebook environment:


    group




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
                



The Group object is a Python dict. User properties can be accessed using subscript notation:


    group['title']




    'Aggregated Live Feed Community'



The group properties can also be accessed using the dot(.) notation, as properties of the class:


    group.snippet




    'A collection of tools, scripts, and methodologies that help ArcGIS users better leverage available data. (expand for more detail)'



 <hr>

###add_users(<i>usernames</i>)

Adds users to this group.

<div class="alert alert-success">
This method will only work if the user for the Portal object is either an administrator for the entire
Portal or the owner of the group.
</div>

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
<tr class="row-even"><td>usernames</td>
<td>required string, comma-separated users</td>
</tr>
</tbody>
</table>

**Returns:**	A dictionary with a key of “not_added” which contains the users that were not added to the group.

<hr>

###invite_users(<i>usernames, role='group_member', expiration=10080</i>)

Invites users to this group.

<div class="alert alert-success">
A user who is invited to this group will see a list of invitations in the “Groups” tab of portal listing invitations. The user can either accept or reject the invitation.

The user executing the command must be group owner

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
<tr class="row-even"><td>usernames:</td>
<td>a required string list of users to invite</td>
</tr>
<tr class="row-odd"><td>role:</td>
<td>an optional string, either group_member or group_admin</td>
</tr>
<tr class="row-even"><td>expiration:</td>
<td>an optional int, specifies how long the invitation is
valid for in minutes.</td>
</tr>
</tbody>
</table>

**Returns:**
a boolean that indicates whether the call succeeded.

<hr>

###remove_users(<i>usernames</i>)

<div class="alert alert-success">
This method will only work if the user for the Portal object is either an administrator for the entire
Portal or the owner of the group.
</div>

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
<tr class="row-even"><td>usernames</td>
<td>required string, comma-separated list of users</td>
</tr>
</tbody>
</table>

**Returns:**
    A dictionary with a key of “notRemoved” which contains the users that were not removed from the group.

<hr>

###reassign_to(<i>target_owner</i>)

Reassigns this group to another owner.

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
<td>required string, username of new group owner</td>
</tr>
</tbody>
</table>

**Returns:**
a boolean, indicating success

<hr>

###leave()

Removes the logged in user from the specified group.

**Requires:**
User must be logged in.

**Arguments:**
None.

**Returns:**
    a boolean indicating whether the operation was successful.

<hr>

###update(<i>(title=None, tags=None, description=None, snippet=None, access=None, is_invitation_only=None, sort_field=None, sort_order=None, is_view_only=None, thumbnail=None)</i>)

Updates this group’s properties.

<div class="alert alert-success">
Only pass in values for the arguments you want to update. All other properties will be left as they are. If you want to update description, then only provide the description argument.
</div>

**Arguments:**
<table border="1" class="docutils">
<colgroup>
<col width="24%">
<col width="76%">
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><strong>Argument</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="row-even"><td>title</td>
<td>optional string, name of the group</td>
</tr>
<tr class="row-odd"><td>tags</td>
<td>optional string, comma-delimited list of tags</td>
</tr>
<tr class="row-even"><td>description</td>
<td>optional string, describes group in detail</td>
</tr>
<tr class="row-odd"><td>snippet</td>
<td>optional string, &lt;250 characters summarizes group</td>
</tr>
<tr class="row-even"><td>access</td>
<td>optional string, can be private, public, or org</td>
</tr>
<tr class="row-odd"><td>thumbnail</td>
<td>optional string, URL or file location to group image</td>
</tr>
<tr class="row-even"><td>is_invitation_only</td>
<td>optional boolean, defines whether users can join by
request.</td>
</tr>
<tr class="row-odd"><td>sort_field</td>
<td>optional string, specifies how shared items with the
group are sorted.</td>
</tr>
<tr class="row-even"><td>sort_order</td>
<td>optional string, asc or desc for ascending or descending.</td>
</tr>
<tr class="row-odd"><td>is_view_only</td>
<td>optional boolean, defines whether the group is searchable</td>
</tr>
</tbody>
</table>


**Returns:**	a boolean indicating success

<hr>

###delete()

Deletes this group.

**Arguments:**
None

**Returns:**	a boolean indicating whether the operation succeeded or failed.

<hr>

###get_thumbnail()

Returns the bytes that make up the thumbnail for this group.

**Arguments:**
None.

**Returns:**
bytes that represent the image.

**Example:**
<code>
response = group.get_thumbnail()
f = open(filename, 'wb')
f.write(response)
</code>

<hr>

###get_thumbnail_link()

Returns the URL to the thumbnail image

<hr>

###get_members()

Returns members of this group.

<div class="alert alert-success">This method must be executed as an administrator. This method also can not be undone. The changes are immediately made and permanent.</div>

**Arguments:**
None.

**Returns:**
    a dictionary with keys: owner, admins, and users.
<table border="1" class="last docutils">
<colgroup>
<col width="22%">
<col width="78%">
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><strong>Key</strong></td>
<td><strong>Value</strong></td>
</tr>
<tr class="row-even"><td>owner</td>
<td>string value, the group’s owner</td>
</tr>
<tr class="row-odd"><td>admins</td>
<td>list of strings, typically this is the same as the owner</td>
</tr>
<tr class="row-even"><td>users</td>
<td>list of strings, the members of the group</td>
</tr>
</tbody>
</table>
