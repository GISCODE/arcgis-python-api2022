
##The GroupManager class

<hr/>

##<b>class gis.GroupManager<b>(<i>portal</i>)

Manager class for manipulating GIS groups. This class is not created by users directly. An instance of this class, called ‘groups’, is available as a property of the Gis object. Users call methods on this ‘groups’ object to manipulate (create, get, search...) users.

 <hr>

###create(<i>title, tags, description=None, snippet=None, access='public', thumbnail=None, is_invitation_only=False, sort_field='avgRating', sort_order='desc', is_view_only=False</i>)

Creates a group and returns it if successful.

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
<tr class="row-even"><td>title</td>
<td>required string, name of the group</td>
</tr>
<tr class="row-odd"><td>tags</td>
<td>required string, comma-delimited list of tags</td>
</tr>
<tr class="row-even"><td>description</td>
<td>optional string, describes group in detail</td>
</tr>
<tr class="row-odd"><td>snippet</td>
<td>optional string, <250 characters summarizes group</td>
</tr>
<tr class="row-odd"><td>access</td>
<td>optional string, can be private, public, or org</td>
</tr>
<tr class="row-odd"><td>thumbnail</td>
<td>optional string, URL to group image</td>
</tr>
<tr class="row-odd"><td>is_invitation_only</td>
<td>optional boolean, defines whether users can join by request</td>
</tr>
<tr class="row-odd"><td>sort_field</td>
<td>optional string, specifies how shared items with the group are sorted</td>
</tr>
<tr class="row-odd"><td>sort_order</td>
<td>optional string, asc or desc for ascending or descending</td>
</tr>
<tr class="row-odd"><td>is_view_only</td>
<td>optional boolean, defines whether the group is searchable</td>
</tr>
</tbody>
</table>


**Returns:**	the group, if created, else None

<hr>

###get(<i>username</i>)

Returns the group object having the specified groupid.

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
<tr class="row-even"><td>groupid</td>
<td>required string, the group identifier</td>
</tr>
</tbody>
</table>

**Returns:**	None if the group is not found and returns a group object if the group is found

<hr>

###search(<i>query='', sort_field='title', sort_order='asc', max_groups=1000, add_org=True<i>)

Searches for portal groups.

Returns a list of groups matching the specified query

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

<tr class="row-even"><td>max_groups</td>
<td>optional int, maximum number of groups returned</td>
</tr>

<tr class="row-even"><td>add_org</td>
<td>optional boolean, controls whether to search within your org (default is True)</td>
</tr>

</tbody>
</table>

**Returns:**
	Returns a list of groups matching the specified query

<hr>
