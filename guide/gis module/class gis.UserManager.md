
##The UserManager class

<hr/>

##<b>class gis.UserManager<b>(<i>portal</i>)

Manager class for managing GIS users. This class is not created by users directly. An instance of this class, called ‘users’, is available as a property of the gis object. Users call methods on this ‘users’ object to manipulate (create, get, search...) users. Example of using the 'users' object to search for users:


    from arcgis.gis import GIS
    
    gis = GIS()
    user = gis.users.search('johnsmith')[0]
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
                



 <hr>

###create(<i>username, password, fullname, email</i>)

Signs up a new user with the specified username to an instance of Portal for ArcGIS.

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
<tr class="row-even"><td>username</td>
<td>required string, must be unique in the Portal, >4 characters</td>
</tr>
<tr class="row-odd"><td>password</td>
<td>required string, must be >= 8 characters</td>
</tr>
<tr class="row-even"><td>fullname</td>
<td>required string, name of the user</td>
</tr>
<tr class="row-odd"><td>email</td>
<td>required string, must be an email address</td>
</tr>
</tbody>
</table>


**Returns:**	the user, if created, else None

<hr>

###get(<i>username</i>)

Returns the user object for the user with the specified username.

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
<tr class="row-even"><td>username</td>
<td>required string, the username whose user object you want.</td>
</tr>
</tbody>
</table>

**Returns:**	None if the user is not found and returns a user object if the user is found

<hr>

###list(<i>max_users=1000</i>)

Return the list of users in your organization. This method does not work with ArcGIS Online, only with Portal for ArcGIS.

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
<tr class="row-even"><td>max_users</td>
<td>optional int, the maximum number of users to return</td>
</tr>
</tbody>
</table>

**Returns:**
The list of users in your org

<hr>

###logged_in_user()

Returns the logged in user


<hr>

###search(<i>query, sort_field='username', sort_order='asc', max_users=100, add_org=True</i>)

Searches portal users.

Returns a list of users matching the specified query

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

<tr class="row-even"><td>sort_field</td>
<td>optional string, valid values can be username or created.</td>
</tr>

<tr class="row-even"><td>sort_order</td>
<td>optional string, valid values are asc or desc</td>
</tr>

<tr class="row-even"><td>max_users</td>
<td>optional int, maximum number of users returned</td>
</tr>

<tr class="row-even"><td>add_org</td>
<td>optional boolean, controls whether to search within your org (default is True)</td>
</tr>

</tbody>
</table>

**Returns:**
	a list of users

<hr>
