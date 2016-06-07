
##The User class

<hr/>

##<b>class gis.User<b>(<i>portal, username, userdict=None</i>)

Bases: builtins.dict

Represents a registered user of the GIS (ArcGIS Online, or Portal for ArcGIS).

An instance of this class is not created directly by users. It is returned from the gis.users UserManager object as a result of an create() or search() operation.


    gis = GIS()
    user = gis.users.search('johnsmith')[0]

The user object has a rich representation in the IPython notebook environment:


    user




<div class="item_container">
                    <div class="item_left">
                       <a href='http://www.arcgis.com/home/user.html?user=jes0070' target='_blank'>
                        <img src='http://www.arcgis.com/home/js/arcgisonline/css/images/no-user-thumb.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right">
                        <a href='http://www.arcgis.com/home/user.html?user=jes0070' target='_blank'><b>JOHN SMITH</b>
                        </a>
                        <br><br><b>Bio</b>: Real Estate Services @ Reconassist and 4deeds.com SALESFORCE.COM (SFDC), GPS, GIS, VA. Beach, VA.   @1JohnSmith
                        <br><b>First Name</b>: JOHN
                        <br><b>Last Name</b>: SMITH
                        <br><b>Username</b>: jes0070
                        <br><b>Joined</b>: November 04, 2011
                        
                    </div>
                </div>
                



The User object is a Python dict. User properties can be accessed using subscript notation:


    user['firstName']




    'JOHN'



The User properties can also be accessed using the dot(.) notation, as properties of the class:


    user.lastName




    'SMITH'



 <hr>

###reset(<i>password, new_password=None, new_security_question=None, new_security_answer=None</i>)

Resets a user’s password, security question, and/or security answer.

<div class="alert alert-success">
This function does not apply to those using enterprise accounts that come from an enterprise such as ActiveDirectory, LDAP, or SAML. It only has an effect on built-in users.

If a new security question is specified, a new security answer should be provided.
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
<tr class="row-even"><td>password</td>
<td>required string, current password</td>
</tr>
<tr class="row-odd"><td>new_password</td>
<td>optional string, new password if resetting password</td>
</tr>
<tr class="row-even"><td>new_security_question</td>
<td>optional int, new security question if desired</td>
</tr>
<tr class="row-odd"><td>new_security_answer</td>
<td>optional string, new security question answer if desired</td>
</tr>
</tbody>
</table>

**Returns:**	a boolean, indicating success

<hr>

###update(<i>access=None, preferred_view=None, description=None, tags=None, thumbnail=None, fullname=None, email=None, culture=None, region=None</i>)

Updates this user’s properties.

<div class="alert alert-success">
Only pass in arguments for properties you want to update. All other properties will be left as they are. If you want to update description, then only provide the description argument.
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
<tr class="row-even"><td>access</td>
<td>optional string, values: private, org, public</td>
</tr>
<tr class="row-odd"><td>preferred_view</td>
<td>optional string, values: Web, GIS, null</td>
</tr>
<tr class="row-even"><td>description</td>
<td>optional string, a description of the user.</td>
</tr>
<tr class="row-odd"><td>tags</td>
<td>optional string, comma-separated tags for searching</td>
</tr>
<tr class="row-even"><td>thumbnail</td>
<td>optional string, path or url to a file.  can be PNG, GIF,
JPEG, max size 1 MB</td>
</tr>
<tr class="row-odd"><td>fullname</td>
<td>optional string, name of the user, only for built-in users</td>
</tr>
<tr class="row-even"><td>email</td>
<td>optional string, email address, only for built-in users</td>
</tr>
<tr class="row-odd"><td>culture</td>
<td>optional string, two-letter language code, fr for example</td>
</tr>
<tr class="row-even"><td>region</td>
<td>optional string, two-letter country code, FR for example</td>
</tr>
</tbody>
</table>


**Returns:**	a boolean indicating success

The resource manager for GIS users

<hr>

###delete(<i>reassign_to=None</i>)

The resource manager for groups in the GIS

Deletes this user from the portal, optionally deleting or reassigning groups and items.

<div class="alert alert-success">You can not delete a user in Portal if that user owns groups or items. If you specify someone in the reassign_to argument then items and groups will be transferred to that user. If that argument is not set then the method will fail if the user has items or groups that need to be reassigned.</div>

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
<tr class="row-even"><td>reassign_to</td>
<td>optional string, new owner of items and groups</td>
</tr>
</tbody>
</table>

**Returns:**	a boolean indicating whether the operation succeeded or failed.

<hr>

###get_thumbnail()

Returns the bytes that make up the thumbnail for this user.

**Arguments:**
None.

**Returns:**
bytes that represent the image.

**Example:**
<code>
response = user.get_thumbnail()
f = open(filename, 'wb')
f.write(response)
</code>

<hr>

###get_thumbnail_link()

Returns the URL to the thumbnail image

<hr>

###reassign_to(<i>target_owner, target_folder=None</i>)

Reassigns all of this user’s items and groups to another user.

Items are transferred to the target user into a folder named &lt;user&gt;_&lt;folder&gt; where user corresponds to the user whose items were moved and folder corresponds to the folder that was moved.

<div class="alert alert-success">This method must be executed as an administrator. This method also can not be undone. The changes are immediately made and permanent.</div>

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
<tr class="row-even"><td>target_username</td>
<td>required string, user who will own items/groups after this.</td>
</tr>
</tbody>
</table>

**Returns:**
	a boolean, indicating success

<hr>

###update_role(<i>role</i>)

Updates this user’s role to org_user, org_publisher, org_admin

<div class="alert alert-success">There are three types of roles in Portal - user, publisher, and administrator. A user can share items, create maps, create groups, etc. A publisher can do everything a user can do and create hosted services. An administrator can do everything that is possible in Portal.</div>

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
<tr class="row-even"><td>role</td>
<td>required string, one of these values org_user,
org_publisher, org_admin</td>
</tr>
</tbody>
</table>

**Returns:**
	a boolean, that indicates success
