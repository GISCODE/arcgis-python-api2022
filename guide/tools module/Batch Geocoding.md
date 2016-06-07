
#batch_geocode() method

The batch_geocode() method geocodes an entire list of addresses. Geocoding many addresses at once is also known as bulk geocoding.

<img src="https://developers.arcgis.com/rest/geocode/api-reference/GUID-FD609701-B9B5-49DB-BFD9-A936280A09C6-web.png">

This method can be used to find the following types of locations:

* Street addresses:
 * 27488 Stanford Ave, Bowden, North Dakota
 * 380 New York St, Redlands, CA 92373
* Administrative place names, such as city, county, state, province, or country names:
 * Seattle, Washington
 * State of Mahārāshtra
 * Liechtenstein
* Postal codes:
 * 92591
 * TW9 1DN

Note:
Points of interest (POI) can only be batch geocoded by using the category parameter to specify the place types to geocode.

The addresses in your table can be stored in a single field or in multiple fields — one for each address component. Batch geocoding performance is better when the address parts are stored in separate fields.

Tip:
You can also batch geocode address tables using the gis.content.import_data() and Item.publish() methods. These are higher-level APIs that simplify the batch geocoding process.

# Maximum addresses

There is a limit to the maximum number of addresses that can be geocoded in a single batch request with the geocoder. The MaxBatchSize property defines this limit. For instance, if MaxBatchSize=2000, and 3000 addresses are sent as input, only the first 2000 will be geocoded. The SuggestedBatchSize property is also useful as it specifies the optimal number of addresses to include in a single batch request.

Both of these properties can be determined by querying the geocoder: 


    from arcgis.gis import GIS
    
    gis = GIS("https://deldev.maps.arcgis.com", "demo_deldev", "P@ssw0rd")
    
    # use the GIS's configured geocoder
    geocoder = gis.tools.geocoder


    print("MaxBatchSize : " + str(geocoder['locatorProperties']['MaxBatchSize']))
    print("SuggestedBatchSize : " + str(geocoder['locatorProperties']['SuggestedBatchSize']))

    MaxBatchSize : 1000
    SuggestedBatchSize : 150
    

The client application must account for the limit by dividing the input address table into lists of MaxBatchSize or fewer addresses, and send each list to the service as a separate request. Note that the gis.content.import_data() and Item.publish() methods take care of this for you.

For batch geocode operations, the geocoder returns a response when each address in the input recordset has been geocoded. If an unhandled error such as a timeout occurs during the process, the geocoder will not return the results for that call, even if most of the addresses in the input have already been geocoded. For this reason, the client application should implement logic to detect and handle such errors.

#Batch geocode access

An ArcGIS Online organizational account is required to use the batch geocoding functionality provided by the World Geocoding Service. Successfully geocoded addresses, which return a status of Matched or Tied, cause ArcGIS Online service credits to be consumed for batch geocoding operations.

# Method Parameters

The batch_geocode() method supports searching for lists of places and addresses. Each address in the list can be specified as a single line of text (single field format), or in multifield format with the address components separated into mulitple parameters.

## addresses parameter

A list of addresses to be geocoded. 

For passing in the location name as a single line of text — single field batch geocoding — use a string.

For passing in the location name as multiple lines of text — multifield batch geocoding — use the address fields described in the Geocoder documentation.

The Geocoder provides localized versions of the input field names in all locales supported by it. See the topic Localized input field names in the Geocoder documentation for more information.

### Example: batch geocode using single line addresses


    addresses = ["380 New York St, Redlands, CA", 
                 "1 World Way, Los Angeles, CA",
                 "1200 Getty Center Drive, Los Angeles, CA", 
                 "5905 Wilshire Boulevard, Los Angeles, CA",
                 "100 Universal City Plaza, Universal City, CA 91608",
                 "4800 Oak Grove Dr, Pasadena, CA 91109"]


    results = geocoder.batch_geocode(addresses)


    map = gis.map("Los Angeles", 9)
    map

    :0: FutureWarning: IPython widgets are experimental and may change in the future.
    


    for address in results:
        map.draw(address['location'])

Each match has keys for score, location, attributes and address:


    results[0].keys()




    dict_keys(['score', 'location', 'attributes', 'address'])



##category parameter

A place or address type which can be used to filter batch geocoding results. The parameter supports input of single category values or multiple comma-separated values. See the help topic <a href="https://developers.arcgis.com/rest/geocode/api-reference/geocoding-category-filtering.htm">Category filtering</a> for complete details about the category parameter.

Example of category filtering with a single category:

<code>category="Address"</code>

Example of category filtering with multiple categories:

<code>category="Address,Postal"</code>


## sourceCountry parameter

A value representing the country. When a value is passed for this parameter, all of the addresses in the input table are sent to the specified country locator to be geocoded. For example, if sourceCountry="USA" is passed in a batch_geocode() call, it is assumed that all of the addresses are in the United States, and so all of the addresses are sent to the USA country locator. Using this parameter can increase batch geocoding performance when all addresses are within a single country.

Acceptable values include the full country name, the ISO 3166-1 2-digit country code, or the ISO 3166-1 3-digit country code.

A list of supported countries and codes is available <a href="https://developers.arcgis.com/rest/geocode/api-reference/geocode-coverage.htm">here</a>.

Example:

<code>sourceCountry="USA"</code>

## outSR parameter

The spatial reference of the x/y coordinates returned by the geocode method. This is useful for applications using a map with a spatial reference different than that of the geocoder.

The spatial reference can be specified as either a well-known ID (WKID) or as a <a href="http://resources.arcgis.com/EN/HELP/REST/APIREF/GEOMETRY.HTML#SR">JSON spatial reference object</a>. If outSR is not specified, the spatial reference of the output locations is the same as that of the geocoder. The World Geocoding Service spatial reference is WGS84 (WKID = 4326).

For a list of valid WKID values, see <a href="http://resources.arcgis.com/EN/HELP/REST/APIREF/PCS.HTML">Projected Coordinate Systems</a> and <a href="http://resources.arcgis.com/EN/HELP/REST/APIREF/GCS.HTML">Geographic Coordinate Systems</a>.

Example (102100 is the WKID for the Web Mercator projection):

<code>outSR=102100</code>

## Batch geocoding output fields

When you geocode a list of addresses, the output fields are returned as part of the attributes in the response. See the example JSON response below which shows all of the output fields that are returned for each record from a batch geocode process. The output fields are described <a href="https://developers.arcgis.com/rest/geocode/api-reference/geocoding-service-output.htm#ESRI_SECTION1_42D7D3D0231241E9B656C01438209440">here</a>.


# Batch geocoding examples

The earlier example showed how to call batch_geocode() with single line addresses. The following example illustrates how to call batch_geocode() with a list of multi-field addresses. 

### Example: Batch geocode using multiple field addresses


    addresses= [{
                    "Address": "380 New York St.",
                    "City": "Redlands",
                    "Region": "CA",
                    "Postal": "92373"
                },{
                    "Address": "1 World Way",
                    "City": "Los Angeles",
                    "Region": "CA",
                    "Postal": "90045"
                }]


    results = geocoder.batch_geocode(addresses)


    map = gis.map("Los Angeles", 9)
    map


    for address in results:
        map.draw(address['location'])

# Category filtering

The batch_geocode() method supports batch geocode filtering by category values, which represent address and place types. By including the category parameter in a batch_geocode() call you can avoid false positive matches to unexpected place and address types due to ambiguous input.

For example, a user has a table of three-letter airport codes that they want to geocode. There may be city or business names that are the same as an airport code, causing false positive matches to other places. However the user can ensure that only airport matches are returned by specifying category=airport in the request.

### Example: Batch geocode airport codes with category


    airports = geocoder.batch_geocode(["LAX", "SFO", "ONT", "FAT", "LGB"],
                                      category="airport")


    map = gis.map("CA", 6)
    map


    for airport in airports:
        popup = { 
        "title" : airport['attributes']['PlaceName'], 
        "content" : airport['address']
        }
        map.draw(airport['location'], popup)

You can also use category filtering to avoid "low resolution" fallback matches. By default if the World Geocoding Service cannot find a match for an input address it will automatically search for a lower match level, such as a street name, city, or postal code. For batch geocoding a user may prefer that no match is returned in such cases so that they are not charged for the geocode. If a user passes category="Point Address,Street Address" in a batch_geocode() call, no fallback will occur if address matches cannot be found; the user will only be charged for the actual address matches.

### Example: Batch geocode with fallback allowed (no category)

In the example below, the second address is not matched to a point address, but is matched to the city instead, due to fallback: 


    results = geocoder.batch_geocode(["380 New York St Redlands CA 92373",
                                      "27488 Stanford Dr Escondido CA"])


    for result in results:
        print("Score " + str(result['score']) + " : " + result['address'])

    Score 100 : 380 New York St, Redlands, California, 92373
    Score 100 : Escondido, California
    

### Example: Batch geocode with no fallback allowed (category="Point Address")
In the example below, as a point address match is not found for the second address, there is no low resolution fallback as the category has been set to Point Address, and no match is returned for the second address:


    results = geocoder.batch_geocode(["380 New York St Redlands CA 92373",
                                      "27488 Stanford Dr Escondido CA"],
                                      category="Point Address")


    for result in results:
        print("Score " + str(result['score']) + " : " + result['address'])

    Score 0 : 
    Score 0 : 
    
