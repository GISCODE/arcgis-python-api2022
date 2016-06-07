
#geocode() method

The <code>geocode()</code> method geocodes one location per request; the input address can be either a string containing a single line address, or divided among multiple parameters using a Python dict with keys that are named the same as those in the accepted address fields.

<img src="https://developers.arcgis.com/rest/geocode/api-reference/GUID-F2F78690-5FB5-4BF1-8633-26BF184C45A9-web.png"/>

The geocode() method supports finding the following types of
locations: <ul purpose="ul" id="UL_D677D90485774D6B87807430DC7EDA09"><li purpose="li" id="LI_E7197DD4478C4F0C9BD6E2654CC9F05D"><b>Street addresses</b> <ul purpose="ul" id="UL_2751AF055F8F4155BB2207584178AB67"><li purpose="li" id="LI_AA949A57EC914ABBBA77304DDBEAC802"><code class="usertext">27488 Stanford Ave, Bowden, North Dakota</code></li><li purpose="li" id="LI_1D8A35AF641D4BA7AA70A0F26D4F9092"><code class="usertext">380 New York St, Redlands, CA 92373</code></li></ul></li><li purpose="li" id="LI_D2E856F9AC384E7E8351265ADF25B949"><b>Points of interest (POI)</b> by name and type<ul purpose="ul" id="UL_83358C5FA5DD408BB1B1748481F423EC"><li purpose="li" id="LI_4A56A31BD1CB485E92DE6300EF1BF6B7"><code class="usertext">Disneyland</code></li><li purpose="li" id="LI_AFF58AA0ABD041999ED2F10C0B3A96A4"><code class="usertext">banks in Paris</code></li><li purpose="li" id="LI_2E2F3F5BB97641D586BF2117C345B74C"><code class="usertext">los angeles starbucks</code></li><li purpose="li" id="LI_DCA3B149BB3B49ED912C07D9E9D56BAF"><code class="usertext">mount everest</code></li></ul></li><li purpose="li" id="LI_51BA14AA27124BE3A9EE9F44CC3B6CDD"><b>Administrative place names</b>, such as
city, county, state, province, or country names <ul purpose="ul" id="UL_C6254F5AEB4849369128F768D0877230"><li purpose="li" id="LI_C62D2E56AB374859BD823D0C9533B0CC"><code class="usertext">Seattle, Washington</code></li><li purpose="li" id="LI_8ED527D916E44ADF8957D9CF040A91ED"><code class="usertext">State of Mahārāshtra</code></li><li purpose="li" id="LI_EED027AE03634D07BDF55652DE5358F2"><code class="usertext">Liechtenstein</code></li></ul></li><li purpose="li" id="LI_DBB7D6390DA143ABB017598395DE5075"><b>Postal codes</b> <ul purpose="ul" id="UL_19D4B6B7534541179119E82956AB7D99"><li purpose="li" id="LI_5886C62A652D4F299324F26CBB6A4026"><code class="usertext">92591</code></li><li purpose="li" id="LI_0DBAEE9C46AA41E195BE2D696473C123"><code class="usertext">TW9 1DN</code></li></ul></li><!-- li purpose="li" id="LI_AEFFC2F9878741B7AEF0B1391A16E7D3"><b>X/Y coordinates</b> <ul purpose="ul" id="UL_3A092A7A61084344800FDA80AB00C14E"><li purpose="li" id="LI_FE466B975CC241B68C3720C9D5BEBC56"><code class="usertext">-117.155579,32.703761</code></li --></ul></li></ul>

There are several options for refining or restricting search results. These include:

* Specify output fields to return in the geocoding response with the outFields parameter.
* Specify the spatial reference of candidates with the outSR parameter.
* Limit the number of candidates with the maxLocations parameter.
* Confine the search results to a specified area with the searchExtent parameter.
* Use the location and distance parameters to prefer local candidates, which will then be returned higher in the candidates list.
* Filter search results using the category parameter.

##Method parameters
The <code>geocode()</code> method supports searching for places and addresses in single field format, or in multifield format with the address components separated into mulitple parameters.

###address parameter
#### single line address
The <b>address</b> parameter specifies the location to be geocoded. This can be a string containing the single line address, i.e street address, place name, postal code, or POI.


    from arcgis.gis import GIS
    
    gis = GIS("https://deldev.maps.arcgis.com", "demo_deldev", "P@ssw0rd")
    
    # use the GIS's configured geocoder
    geocoder = gis.tools.geocoder

###Example: plot an address using a single line address


    single_line_address = "380 New York Street, Redlands, CA 92373"


    map = gis.map("Redlands, CA")
    map

    :0: FutureWarning: IPython widgets are experimental and may change in the future.
    

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-3.PNG)


    #geocode the single line address and plot the location of the first geocode result on the map
    
    esrihq = geocoder.geocode(single_line_address)[0]
    popup = { 
        "title" : "Esri Headquarters", 
        "content" : esrihq['address']
        }
    map.draw(esrihq['location'], popup)

####multi field address
Alternatively, the address can be specified in a multifield format using a dictionary containing the various address fields accepted by the corresponding geocode service. 

In order to provide a way to find addresses in many different countries, which may use different addressing formats, the <code>geocode()</code> method uses standardized field names for submitting address components. 

The Geocoder's 'addressFields' property specifies the various address fields accepted by it when geocoding addresses. The neighborhood, city, subregion, and region parameters represent typical administrative divisions within a country. They may have different contexts for different countries, and not all administrative divisions are used in all countries. For instance, with addresses in the United States, only the city (city) and region(state) parameters are used; for addresses in Mexico, the neighborhood parameter is used for districts (colonias) within a city, city for municipalities (municipios), and the region parameter for states (estados); Spain uses all four administrative divisions.

For example, if the addressFields of a geocode service resource includes fields with the following names: Address, City, Region and Postal, then the address argument is of the form below.

###Example: plot an address using a multiple field address


    multi_field_address = { 
        "Address" : "380 New York Street",
        "City" : "Redlands",
        "Region" : "CA",
        "Postal" : 92373
        }


    map = gis.map("Redlands, CA")
    map

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-3.PNG)


    #geocode the multi field address and plot the location of the first geocode result on the map
    
    esrihq = geocoder.geocode(multi_field_address)[0]
    popup = { 
        "title" : "Esri Headquarters", 
        "content" : esrihq['address']
        }
    map.draw(esrihq['location'], popup)

The geocoder() method retuns an array of potential address matches (also refered to as address candidates). Each address candidate is represented as a Python dictionary with the following keys:


    esrihq.keys()




    dict_keys(['address', 'location', 'attributes', 'extent', 'score'])



The dict keys-values are the following:
* <code>score</code> represents the level of confidence of the geocoder in the match, ranked from 0-100
* <code>location</code> contains the (x, y) location of the match,
* <code>address</code> includes the matched address,
* <code>attributes</code> include several parameters from the 'Candidate Fields' property above, and
* <code>extent</code> specifies an appropriate extent for the matched address.

###searchExtent parameter

A set of bounding box coordinates that limit the search area to a specific region. This is especially useful for applications in which a user will search for places and addresses within the current map extent.

You can specify the spatial reference of the searchExtent coordinates, which is necessary if the map spatial reference is different than that of the geocoding service; otherwise, the spatial reference of the coordinates is assumed to be the same as that of the geocoding service.

The input can either be a comma-separated list of coordinates defining the bounding box or a JSON envelope object. The spatial reference of the bounding box coordinates can be included if an envelope object is used.

###Example: Starbucks around Union Square in San Francisco, CA
The example below finds and plots upto 100 Starbucks locations around Union Square in San Francisco, CA. The extent parameter is obtained from the geocoder's geocoding result for Union Square (<code>unionsquare['extent']</code>) and passed into the next geocode() request for 100 Starbucks locations:


    unionsquare = geocoder.geocode("Union Square, San Francisco, CA")[0]
    map = gis.map("Union Square, San Francisco, CA", 14)
    map

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-9.png)


    # find and plot upto 100 Starbucks(TM) locations around Union Square in San Francisco, CA
    starbucks = geocoder.geocode("Starbucks", unionsquare['extent'], maxLocations=100)
    for starbuck in starbucks:
        map.draw(starbuck['location'])

### location parameter

Defines an origin point location that is used with the distance parameter to sort geocoding candidates based upon their proximity to the location. The distance parameter specifies the radial distance from the location in meters. The priority of candidates within this radius is boosted relative to those outside the radius.

This is useful in mobile applications where a user will want to search for places in the vicinity of their current GPS location; the location and distance parameters can be used in this scenario.

The location parameter can be specified without specifying a distance. If distance is not specified, it defaults to 50000 meters.

The location can be represented with a simple comma-separated syntax (x,y), or as a JSON point object. If the comma-separated syntax is used, the spatial reference of the coordinates must be WGS84. Otherwise, the spatial reference of the point coordinates can be defined in the JSON object.

Example using simple syntax (WGS84):
location=-117.196,34.056
JSON example with a spatial reference:
<code>
location=
{
    "x": -13046165.572,
    "y": 4036389.847,
    "spatialReference": {
        "wkid": 102100
    }
}
</code>

###distance parameter

Specifies the radius of an area around a point location that is used to boost the rank of geocoding candidates so that candidates closest to the location are returned first. The distance value is in meters.

If the distance parameter is specified, then the location parameter must be specified as well.

It is important to note that unlike the searchExtent parameter, the location and distance parameters allow searches to extend beyond the specified search radius. They are not used to filter results, but rather to rank resulting candidates based on their distance from a location. You must pass a searchExtent value in addition to location and distance if you want to confine the search results to a specific area.

Example of searching within two miles of the current extent:
<code>distance=3218.69</code>

###category parameter

A place or address type which can be used to filter geocoding results. The parameter supports input of single category values or multiple comma-separated values. The category parameter can be passed in a request with or without a single line address input. 

Example of category filtering with a single category:

<code>category="Address"</code>

Example of category filtering with multiple categories:

<code>category="Address,Postal"</code>

Note:
The category parameter is only functional when used with single line address input. It does not work with multi field addresses; specifically the address, neighborhood, city, region, subregion, countryCode, and postal parameters.

###Example: Indian Food around Union Square in San Francisco, CA


    unionsquare = geocoder.geocode("Union Square, San Francisco, CA")[0]
    
    map = gis.map("Union Square, San Francisco, CA", 14)
    map

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-11.png)


    # find and plot upto 100 Indian restaurants around Union Square in San Francisco, CA
    
    dhaabas = geocoder.geocode(None, unionsquare['extent'], category="Indian Food", maxLocations=100)
    for dhaaba in dhaabas:
        popup = { 
        "title" : dhaaba['address'], 
        "content" : "Phone: " + dhaaba['attributes']['Phone']
        }
        map.draw(dhaaba['location'], popup)

###Example: Searching for multiple categories and plotting them with different smbols
In the example below, we search for Indian food as well as Thai Food in San Francisco and plot their locations using different symbols based on the 'Type' attribute:


    categories = "Indian Food, Thai Food"


    unionsquare = geocoder.geocode("San Francisco, CA")[0]
    
    map = gis.map("San Francisco, CA")
    map

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-14.png)


    # find and plot upto 100 Indian and Thai restaurants in San Francisco, CA
    
    thaisymbol = {
    "type": "esriSMS",
     "style": "esriSMSSquare",
     "color": [76,115,0,255],
     "size": 8,
     "angle": 0,
     "xoffset": 0,
     "yoffset": 0,
     "outline": 
      {
      "color": [152,230,0,255],
       "width": 1
      }
    }
    
    restaurants = geocoder.geocode(None, unionsquare['extent'], category=categories, maxLocations=100)
    for restaurant in restaurants:
        popup = { 
        "title" : restaurant['address'], 
        "content" : "Phone: " + restaurant['attributes']['Phone']
            }
        if restaurant['attributes']['Type'] == 'Thai Food':
            map.draw(restaurant['location'], popup, thaisymbol) # use a green square symbol for Thai food
        else:
            map.draw(restaurant['location'], popup)

### outSR parameter

The spatial reference of the x/y coordinates returned by the geocode method. This is useful for applications using a map with a spatial reference different than that of the geocoder.

The spatial reference can be specified as either a well-known ID (WKID) or as a <a href="http://resources.arcgis.com/EN/HELP/REST/APIREF/GEOMETRY.HTML#SR">JSON spatial reference object</a>. If outSR is not specified, the spatial reference of the output locations is the same as that of the geocoder. The World Geocoding Service spatial reference is WGS84 (WKID = 4326).

For a list of valid WKID values, see <a href="http://resources.arcgis.com/EN/HELP/REST/APIREF/PCS.HTML">Projected Coordinate Systems</a> and <a href="http://resources.arcgis.com/EN/HELP/REST/APIREF/GCS.HTML">Geographic Coordinate Systems</a>.

Example (102100 is the WKID for the Web Mercator projection):

<code>outSR=102100</code>

### outFields parameter

The list of fields to be returned in the response. Descriptions for each of these fields are available in the <a href="https://developers.arcgis.com/rest/geocode/api-reference/geocoding-service-output.htm#ESRI_SECTION1_42D7D3D0231241E9B656C01438209440">Output fields section of this document</a>.

The returned address, x/y coordinates of the match location, match score, spatial reference, extent of the output feature, and the addr_type (match level) are returned by default.

Example that returns all output fields:

<code>outFields=*</code>

Example that returns the specified fields only:

<code>outFields=AddrNum,StName,City</code>

### maxLocations parameter

The maximum number of locations to be returned by a search, up to the maximum number allowed by the geocoder. If not specified, then all matching candidates up to the maximum are returned.

The World Geocoding Service allows up to 20 candidates to be returned for a single request. Note that up to 50 POI candidates can be returned.

Example:

<code>maxLocations=10</code>

### forStorage parameter

Specifies whether the results of the operation will be persisted. The default value is false, which indicates the results of the operation can't be stored, but they can be temporarily displayed on a map for instance. If you store the results, in a database for example, you need to set this parameter to true.

Applications are contractually prohibited from storing the results of geocoding transactions unless they make the request by passing the forStorage parameter with a value of true.

ArcGIS Online service credits are deducted from the organization account for each geocode transaction that includes the forStorage parameter with a value of true. Refer to the <a href="http://www.esri.com/SOFTWARE/ARCGIS/ARCGISONLINE/CREDITS">ArcGIS Online service credits overview page<a/> for more information on how credits are charged.

To learn more about free and paid geocoding operations, see <a href="https://developers.arcgis.com/rest/geocode/api-reference/geocoding-free-vs-paid.htm">this help topic</a>.

Example:

<code>forStorage=true</code>

# Search for street addresses
You can search for a street address, street name, or street intersection using the geocode() method. For best results, you should include as much location information as possible in the search in addition to the street address. See the section entitled <a href="https://developers.arcgis.com/rest/geocode/api-reference/geocoding-service-output.htm#GUID-AF8BB306-55A7-4808-B816-6E2F8D4E2486">Match accuracy</a> for more information about obtaining optimal results for address searches.

You can pass the address components as a single address string or separated into multiple parameters using a dict. Examples of each are shown. Note that in each case the response is the same for both the single and multiple parameter addresses.

### Example: Find a street address (380 New York Street, Redlands, CA 92373)

Single line address:


    single_line_address = "380 New York Street, Redlands, CA 92373"


    map = gis.map("Redlands, CA")
    map

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-3.PNG)


    #geocode the single line address and plot the location of the first geocode result on the map
    
    esrihq = geocoder.geocode(single_line_address)[0]
    popup = { 
        "title" : "Esri Headquarters", 
        "content" : esrihq['address']
        }
    map.draw(esrihq['location'], popup)

###Example: plot an address using a multiple field address

In this example, the street address component (380 New York St) is passed as the value for the address parameter; the city component (Redlands) as the value for the city parameter; the state component (CA) as the region parameter; and the zip code (92373) as the value for the postal parameter.


    multi_field_address = { 
        "Address" : "380 New York Street",
        "City" : "Redlands",
        "Region" : "CA",
        "Postal" : 92373
        }


    map = gis.map("Redlands, CA")
    map

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-3.PNG)


    #geocode the multiple field address and plot the location of the first geocode result on the map
    
    esrihq = geocoder.geocode(multi_field_address)[0]
    popup = { 
        "title" : "Esri Headquarters", 
        "content" : esrihq['address']
        }
    map.draw(esrihq['location'], popup)

###Example: Search for a street intersection
The following example illustrates how to search for a street intersection. An intersection is where two streets cross each other, and hence an intersection search consists of the intersecting street names plus the containing administrative division or postal code. For example, <code>redlands blvd and new york st 92373</code> is a valid intersection search, as is <code>redlands blvd & new york st redlands ca</code>.


    intersection = "redlands blvd and new york st 92373"


    multi_field_intersection = { 
        "Address" : "redlands blvd & new york st",
        "City" : "Redlands",
        "Region" : "CA"
        }


    map = gis.map("Esri, Redlands, CA", 15)
    map

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-23.png)


    # geocode the intersection address and plot the location of the first geocode result on the map
    
    # either of the two intersection address formats can be used, they give itentical results:
    # intersection_result = geocoder.geocode(intersection)[0]
    intersection_result = geocoder.geocode(multi_field_intersection)[0]
    
    popup = { 
        "title" : "redlands blvd and new york st", 
        "content" : intersection_result['address']
            }
    map.draw(intersection_result['location'], popup)

# Search for Points of Interests (POIs)

A POI is a point location that can represent a cultural or geographic landmark, business, or administrative division. For example, you can find amusement parks, museums, schools restaurants, hotels, gas stations, or other types of businesses or landmarks; geographic features, such as mountains, lakes, rivers, or deserts; or administrative places, such as neighborhoods, cities, states, counties, or countries. The geocode method supports geocoding POIs by name or by type.

The supported types are listed in this <a href="https://developers.arcgis.com/rest/geocode/api-reference/geocoding-category-filtering.htm#GUID-20D9858C-C27C-4C9C-BE4C-1EDB36E04D62">table</a>.

As with street addresses, you can search for POIs with findAddressCandidates using the single field or multifield approach.

## Single field POI search

To search for POIs with a single field search, use the singleLine parameter. In general, valid singleLine POI search strings can be formatted in variations of two basic structures:

1. &lt;name or type&gt; &lt;optional connector&gt; &lt;optional zone&gt;
2. &lt;optional zone&gt; &lt;name or type&gt;
Where:

* &lt;name or type&gt; = A place name, such as "Disneyland", "Starbucks", "Niagra Falls", or "Paris"; or a type, such as "amusement parks", "waterfalls", or "coffee shops"
* &lt;optional zone&gt; = A zone—which can be a city, state or region, country, or any combination thereof—provides a spatial boundary to the search; it can be included to limit matching candidates but is not required
* &lt;optional connector&gt; = "in", "at", or "near"; this is not required for the search

Examples of valid single line address search strings include:

Business name searches:

* Starbucks San Diego
* Starbucks San Diego CA
* Starbucks San Diego USA
* Starbucks in San Diego
* San Diego Starbucks
* San Diego CA Starbucks
* San Diego USA Starbucks

Type searches:

* coffee shops San Diego
* coffee shops San Diego CA
* coffee shops San Diego USA
* coffee shops in San Diego CA
* San Diego coffee shops
* San Diego CA coffee shops
* San Diego USA coffee shops

## Multifield POI search

When searching for POIs using multifield input, the name or type of the POI must be passed as the value for the address parameter. The zone information can be passed in the neighborhood, city, subregion, region, and countryCode parameters.

Note:
The postal and postalExt parameters are not valid input for POI searches.

### General information

It is important to note that instead of providing a zone, you can limit searches to a specific area by using the searchExtent parameter. You can also influence the sorting of match candidates according to their proximity to a location with the location and distance parameters.

As with address searches, the quality of POI search results is dependent on the amount and quality of information in the search string. If you just search for hotels without qualifying information such as zone, search extent, or location, then your results will not be meaningful. Adding supplemental information to the search string—the more specific the better—will result in more accurate and relevant matches.

Note:
There may be instances when searches yield unexpected results. For example, a search for New York pizza, where the expected results are pizzerias in New York City, may instead return a match to a restaurant named New York Pizza in Sacramento, California. This is because exact place name matches are given higher priority to increase performance. If this occurs, you can obtain the desired results by modifying the search string—in this case, a search for pizza in NYC should yield the expected results.

Note:
The address, phone number, and website URL of a POI can be returned by including <code>outFields=Place_addr,Phone,URL</code> in the request. But not all POIs have address, phone, and URL values associated with them. 


### Example: Find a business name (Starbucks Sydney AUS)



    starbucks_sydney = "starbucks sydney AUS"

We can use either the single line address above, or the multiple field address below to search.


    starbucks_sydney = {
        "Address": "starbucks",
        "City": "Sydney",
        "CountryCode": "AUS"
        }


    map = gis.map("Sydney, AUS", 13)
    map

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-30.png)


    starbucks = geocoder.geocode(starbucks_sydney)
    for starbuck in starbucks:
        map.draw(starbuck['location'])

###Example: Find a business type (hotels Miami, FL)


    address = "hotels miami FL"

We can use either the single line address above, or the multiple field address below to search.


    address = {
        "Address": "hotels",
        "City": "miami",
        "Region": "FL"
        }


    map = gis.map("Miami, Florida", 10)
    map

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-31.png)


    miamihotels = geocoder.geocode(address)
    for hotel in miamihotels:
        map.draw(hotel['location'])

#Search for administrative place names
The geocode method supports single field and multifield searches for administrative place names. This includes searches for neighborhoods, cities, counties, states, provinces, or countries. If a search for a city name results in multiple matches with the same name, the World Geocoding Service will sort the candidates in order of their relative importance to each other (as indicated by the value of the Rank output field), with priority generally based on population and capital status. For example, there are many cities in the world named London, so a search for "London" results in several equivalent matches; London, UK will always be the top candidate since it has the greatest population.

### Example: Find a city name (London)


    address = "London"


    map = gis.map("United Kingdon", 5)
    map

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-35.png)


    london = geocoder.geocode(address)[0]


    map.draw(london['location'])

However, rank alone is not always enough to distinguish between administrative places. Also, you may not necessarily want to find the highest-ranked feature for a particular search. It may be necessary to remove ambiguity by refining searches with additional information. For example, a search for "Oxford" returns Oxford, UK as the top candidate based on rank. If you instead want to find the town of Oxford, Alabama, it is necessary to add the state information to the search.

###Example: Search for city, state (Oxford, AL)


    address = "Oxford AL"

Either the single line address above or the multiple foeld address below can be used to search for Oxford, AL.


    address = {
        "Address" : "Oxford",
        "Region" : "AL"
    }


    map = gis.map("United States", 4)
    map

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-40.png)


    oxford = geocoder.geocode(address)[0]
    map.draw(oxford['location'])

#Search for postal codes

The geocode method supports searches for postal codes and postal code extensions. When searching for postal codes it is important to note that the same code can be valid in more than one country; for best results it may be necessary to include additional information with the postal code, such as city or country.

###Example: Find a postal code (110085 India)


    address = {
        "Postal" : 110001,
        "CountryCode" : "India"
    }


    map = gis.map("New Delhi, India")
    map

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-43.png)


    pincode = geocoder.geocode(address)[0]
    map.draw(pincode['location'])

The matched address contains several attributes, that provide values for the various output fields supported by the geocoder.


    pincode['attributes']




    {'AddBldg': '',
     'AddNum': '',
     'AddNumFrom': '',
     'AddNumTo': '',
     'Addr_type': 'Postal',
     'City': '',
     'Country': 'IND',
     'DisplayX': 77.226595,
     'DisplayY': 28.622481,
     'Distance': 0,
     'LangCode': '',
     'Loc_name': 'IND.Postal',
     'Match_addr': '110001',
     'Nbrhd': '',
     'Phone': '',
     'PlaceName': '',
     'Place_addr': '',
     'Postal': '110001',
     'PostalExt': '',
     'Rank': '',
     'Region': '',
     'Score': 100,
     'Side': '',
     'StAddr': '',
     'StDir': '',
     'StName': '',
     'StPreDir': '',
     'StPreType': '',
     'StType': '',
     'Subregion': '',
     'Type': '',
     'URL': '',
     'X': 77.226595,
     'Xmax': 77.25453,
     'Xmin': 77.19862,
     'Y': 28.622481,
     'Ymax': 28.641,
     'Ymin': 28.60405}



#Specify output fields

The geocode method allows you to specify individual output fields or return all output fields. The outFields parameter is used for this. If you want to return all supported output fields, use the default i.e. outFields=*; If you want to return specific fields, pass the desired field names as comma separated values, such as outFields=PlaceName,Type,City,Country, which returns the name, feature type, city, and country for a POI search.

See the topic <a href="https://developers.arcgis.com/rest/geocode/api-reference/geocoding-service-output.htm#ESRI_SECTION1_42D7D3D0231241E9B656C01438209440">Service output</a> for detailed information about the attribute fields returned by the geocode method.

###Example: Specify individual outfields for a POI search (PlaceName,Type,City,Country)


    matches = geocoder.geocode("coffee shops austin", outFields="PlaceName,Type,City,Country")

The returned attributes only contain the key-value pairs for the specified output fields:


    matches[0]['attributes']




    {'City': 'Austin',
     'Country': 'USA',
     'PlaceName': 'Starbucks',
     'Type': 'Coffee Shop'}



#Specify the output spatial reference

By default the World Geocoding Service returns candidate geometry in WGS84 coordinates (decimal degrees). You can specify a different spatial reference for output coordinates by using the outSR parameter. This is necessary if you have a mapping application in which you display geocoding candidates and the map spatial reference is not WGS84. For example, the ArcGIS.com basemaps use a Web Mercator spatial reference, with coordinates in meters. In order to display geocoding candidates correctly in such a map you would need to set outSR=102100, which is the well-known ID (WKID) of the Web Mercator spatial reference.

For a list of valid WKID values, see <a href="http://resources.arcgis.com/EN/HELP/REST/APIREF/PCS.HTML">Projected Coordinate Systems</a> and <a href="http://resources.arcgis.com/EN/HELP/REST/APIREF/GCS.HTML">Geographic Coordinate Systems</a>.

###Example: Specify output coordinates in Web Mercator spatial reference (380 new york st redlands ca)


    esrihq = geocoder.geocode("380 New York St, Redlands, CA")[0]


    esrihq['location']




    {'x': -117.1956658832732, 'y': 34.05649020076322}



The location above is in the default spatial reference of the geocoder (4326). We can set the output spatial reference to 102100 using the outSR parameter to obtain the location in the Web Mercator spatial reference(102100):


    esrihq2 = geocoder.geocode("380 New York St, Redlands, CA", outSR=102100)[0]


    esrihq2['location']




    {'x': -13046161.849304594, 'y': 4036389.80445789}



#Specify the maximum number of candidates

The maxLocations parameter allows you to specify the maximum number of candidates to be returned by a search, up to the maximum number of candidates allowed by the World Geocoding Service. By default the service allows up to 20 candidates to be returned for address searches, and 50 for POI searches. As an example, if you set maxLocations=10, then geocode() will return the top 10 candidates for the search, regardless of whether the search matches to an address or a POI. If no value is specified for maxLocations, then geocode() returns upto a maximum default of 20 matches.

###Example: Specify the maximum number of candidates for a POI search (Starbucks in Paris)


    matches = geocoder.geocode("coffee shops austin", outFields="PlaceName,City,Country", maxLocations=3)

We get back 3 matches as we've specified maxLocations=3:


    len(matches)




    3




    matches




    [{'address': 'Starbucks',
      'attributes': {'City': 'Austin', 'Country': 'USA', 'PlaceName': 'Starbucks'},
      'extent': {'xmax': -97.963419,
       'xmin': -97.973419,
       'ymax': 30.346169,
       'ymin': 30.336169},
      'location': {'x': -97.96841805299965, 'y': 30.34116889100045},
      'score': 100},
     {'address': 'Starbucks',
      'attributes': {'City': 'Austin', 'Country': 'USA', 'PlaceName': 'Starbucks'},
      'extent': {'xmax': -97.92906,
       'xmin': -97.93906,
       'ymax': 30.308998,
       'ymin': 30.298998},
      'location': {'x': -97.93405910199965, 'y': 30.303997689000482},
      'score': 100},
     {'address': 'Starbucks',
      'attributes': {'City': 'Austin', 'Country': 'USA', 'PlaceName': 'Starbucks'},
      'extent': {'xmax': -97.873198,
       'xmin': -97.883198,
       'ymax': 30.207829,
       'ymin': 30.197829},
      'location': {'x': -97.87819655899966, 'y': 30.20282866700046},
      'score': 100}]



#Search within an extent

The geocode method allows spatial filtering of search results by using the searchExtent parameter. If you want to confine a search to a localized area, something that is especially useful in a mobile application, you can define a bounding rectangle to search within. No candidates outside of the rectangle are returned. Bounding rectangle coordinates can be entered as a simple comma-separated string in the format &lt;lower left corner&gt;,&lt;upper right corner&gt;. If the simple format is used, the coordinates must be in the default spatial reference of the geocoder, which is WGS84. The searchExtent parameter can be used with all supported search types (street address, POI, admin place, postal code).

The example URL below illustrates how to find McDonald's in downtown San Diego using the simple searchExtent format.

###Example: Find POIs using searchExtent with default spatial reference (McDonald's)
The example below finds and plots upto 100 Mc Donalds' locations in San Diego, CA. The extent parameter is obtained from the geocoder's geocoding result for San Diego (sandiego['extent']) and passed into the next geocode() request for 100 Mc Donalds' locations:


    sandiego = geocoder.geocode("San Diego, CA")[0]
    map = gis.map("San Diego, CA")
    map

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-55.png)


    # find and plot upto 100 Mc Donalds' locations in San Diego, CA
    
    mcds = geocoder.geocode("McDonalds", sandiego['extent'],  maxLocations=100)
    for mcd in mcds:
        map.draw(mcd['location'])

###Example: Find POIs using searchExtent and zone (Starbucks garland)

Requests that include searchExtent can also include zone information (that is, city, state, and country). If the extent defined for searchExtent is large enough to encompass multiple cities, it may be necessary to include the city name in the search to achieve optimal results. For example, if the searchExtent covers the entire state of Texas, and you search for Starbucks, there could be matches returned in any city in Texas. If you specifically want to find Starbucks in Garland for example, then this needs to be specified in the search.


    texas = geocoder.geocode("TX")[0]
    map = gis.map("Dallas Fort Worth", 10)
    map

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-57.png)


    starbucks = geocoder.geocode("Starbucks Garland", texas['extent'], maxLocations=20)
    for starbuck in starbucks:
        map.draw(starbuck['location'])

###Example: Find a street address using searchExtent (380 New York St)

You can also search for street addresses within an extent. When the searchExtent parameter is defined for an address search, city and postal code can be omitted from the search and valid matches can still be found. However, if the searchExtent is large, it is possible for a street address to occur multiple times within the extent, and it may be necessary to refine the search by including city, state, postal code, or other distinguishing information. Additionally, if the search includes a city or postal code that is outside the searchExtent, no matches will be returned. See the following example which illustrates finding a street address using searchExtent.




    map = gis.map("Redlands, CA")
    map

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-3.PNG)


    redlands = geocoder.geocode("Redlands, CA")[0]
    
    # search for "380 New Yort St" within the extent of Redlands
    esrihq = geocoder.geocode("380 New York St", redlands['extent'])[0]
    map.draw(esrihq['location'])


    redlands['extent']




    {'xmax': -117.108538,
     'xmin': -117.256538,
     'ymax': 34.129567,
     'ymin': 33.981567}



#Proximity searches

Geocoding results are typically sorted according to their relevance to the search and their relative importance. However, with some applications, especially mobile apps, users are more concerned with finding features closest to their current location. For this reason, the geocode method supports prioritization of candidates based on their distance from a specified point. By passing in the location and distance parameters, you can define a circular area of influence for your searches. The location parameter represents the center point of the area, and the distance parameter defines the radius in meters. The purpose of this area is to boost the rank of results closest to the specified location so that they show up higher in the list of candidates. Results that are within the area receive a greater boost than those outside the area.


###Example: Find a place name using proximity search (Golden Nugget)

It is important to note that proximity search does not filter results that are outside of the location and distance area—it is intended to influence the sort order of results so that the most locationally relevant candidates are returned first. For instance, if your location is in Las Vegas, distance=3000, and you search for "Golden Nugget", the first candidate is Golden Nugget in Las Vegas. The second is Golden Nugget in Biloxi, Mississippi. So even though Golden Nugget in Biloxi, Mississippi is much farther away than the 3000 meter search distance, it is still returned because it is the second most relevant (closest) candidate. In general, the number of candidates returned by a proximity search is only limited by the maxLocations parameter.


    map = gis.map("Las Vegas")
    map

![sample output](http://esri.github.io/arcgis-python-api/notebooks/nbimages/geocoding-62.png)


    lasvegas = geocoder.geocode("Las Vegas, NV")[0]
    lasvegas['location']




    {'x': -115.1372160299997, 'y': 36.174968712000464}



We search for Golden Nugget near Las Vegas, NV and plot it on the map:


    goldennuggets = geocoder.geocode("Golden Nugget", location=lasvegas['location'], distance=3000)


    map.draw(goldennuggets[0]['location'])


    # print the matched addresses - note that the address in Las Vegas is the first result
    for nugget in goldennuggets:
        print(nugget['attributes']['Place_addr'])

    129 Fremont St, Las Vegas, Nevada
    151 Beach Blvd, Biloxi, Mississippi
    Mudalige Mawatha, Colombo, Western
    2406 W Diversey Ave, Chicago, Illinois
    Huron Ave, Atlantic City, New Jersey
    20 Marine Parade, Great Yarmouth, Norfolk
    Marco-Polo-Strae 3, Satteldorf, Baden-Wrttemberg
    Brixner Strae 4, Innsbruck, Tirol
    Rainerstrae 19, Linz, Obersterreich
    117 Lonsdale St, Melbourne, Victoria
    29 Bannister Rd, Boddington, Western Australia
    R348, Ballinasloe, County Galway
    22 Shaftesbury Avenue, London
    Mallikatta Road, Mangalore, Karnataka
    Dr Ramaswamy Salai, Chennai, Tamil Nadu
    

Contrast the results with a search for Golden Nugget without the location and distance parameters influencing the search results:


    goldennuggets = geocoder.geocode("Golden Nugget")
    for nugget in goldennuggets:
        print(nugget['attributes']['Place_addr'])

    151 Beach Blvd, Biloxi, Mississippi
    Mudalige Mawatha, Colombo, Western
    129 Fremont St, Las Vegas, Nevada
    2406 W Diversey Ave, Chicago, Illinois
    Huron Ave, Atlantic City, New Jersey
    20 Marine Parade, Great Yarmouth, Norfolk
    Marco-Polo-Strae 3, Satteldorf, Baden-Wrttemberg
    Brixner Strae 4, Innsbruck, Tirol
    Rainerstrae 19, Linz, Obersterreich
    29 Bannister Rd, Boddington, Western Australia
    117 Lonsdale St, Melbourne, Victoria
    22 Shaftesbury Avenue, London
    Mallikatta Road, Mangalore, Karnataka
    Dr Ramaswamy Salai, Chennai, Tamil Nadu
    R348, Ballinasloe, County Galway
    

###Example: Find a place name using both proximity and searchExtent (Golden Nugget)

If you only want to return candidates within a specific area, and sort the candidates according to their proximity to a location, then you need to define a search extent by passing the searchExtent parameter in the request along with the location and distance parameters. Consider the Golden Nugget example again. If your location is in Las Vegas and you want to confine your search results to places named Golden Nugget that are within the map extent, then you would need to construct a request with the following parameters:


    address = "Golden Nugget"
    location = lasvegas['location']
    distance =  4000
    searchExtent = lasvegas['extent']


    goldennuggets = geocoder.geocode(address, searchExtent, location, distance)
    for nugget in goldennuggets:
        print(nugget['attributes']['Place_addr'])

    129 Fremont St, Las Vegas, Nevada
    

#Category filtering

The geocode method supports filtering searches by category values, which represent address and place types. By including the category parameter in a geocode() call you can avoid false positive matches to unexpected place and address types due to ambiguous searches.

Note:
The category parameter is only functional when used with single line addresses. It does not work with the multifield parameters; specifically the address, neighborhood, city, region, subregion, countryCode, and postal parameters.

For example, a user may search for "Mammoth", expecting the service to match to Mammoth Mountain ski resort. However there are many places in the world named "Mammoth", and so the search returns several cities named "Mammoth".

###Example: Search for "Mammoth" without category


    mammoths = geocoder.geocode("Mammoth")
    for mammoth in mammoths:
        print(mammoth['address'])

    Mammoth, Arizona, United States
    Mammoth, California, United States
    Mammoth, Utah, United States
    Mammoth, Montana, United States
    Mammoth, Missouri, United States
    Mammoth, West Virginia, United States
    Mammoth, Pennsylvania, United States
    Mammoth, Wyoming, United States
    Mammoth, New Zealand
    Mammoth
    Mammoth
    Mammoth
    Mammoth
    Mammoth
    Mammoth
    Mammoth
    Mammoth
    Mammoth
    Mammoth
    Mammoth
    

The solution for this case is to pass the category parameter in the method call. By including category=Ski Resort, all places that are not ski resorts are bypassed by the search, and only ski resorts whose names begin with "Mammoth" are returned.

###Example: Search for "Mammoth" with category=Ski Resort


    mammoths = geocoder.geocode("Mammoth", category="Ski Resort")
    for mammoth in mammoths:
        print(mammoth['address'])

    Mammoth Mountain
    Takamagahara Mammoth
    Mammoth Ski Resort
    

See the topic <a href="https://developers.arcgis.com/rest/geocode/api-reference/geocoding-category-filtering.htm">Category filtering</a> for complete details.
