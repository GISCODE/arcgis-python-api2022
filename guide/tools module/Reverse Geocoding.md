
#reverse_geocode() method

The reverse_geocode() method determines the address at a particular x/y location. You pass the coordinates of a point location to the geocoder, and it returns the address that is closest to the location.

<img src="https://developers.arcgis.com/rest/geocode/api-reference/GUID-3A7A77E6-2E26-44E2-A7BA-362DA4EFC0E4-web.png">

# Method Parameters

## location parameter

The point from which to search for the closest address. The point can be represented as a simple list of coordinates ([x, y] or [longitude, latitude]) or as a JSON point object.

The spatial reference of the list of coordinates is always WGS84 (in decimal degress), the same coordinate system as the World Geocoding Service.

Use JSON formatting to specify any other coordinate system for the input location. Specifically, set the spatial reference using its well-known ID (WKID) value. For a list of valid WKID values, see <a href="http://resources.arcgis.com/EN/HELP/REST/APIREF/PCS.HTML">Projected Coordinate Systems</a> and <a href="http://resources.arcgis.com/EN/HELP/REST/APIREF/GCS.HTML">Geographic Coordinate Systems</a>.

Example using simple syntax and the default WGS84 spatial reference:

<code>location=[103.8767227,1.3330736]</code>

Example using JSON and the default WGS84 spatial reference:

<code>location={x: 103.876722, y: 1.3330736}</code>

Example using JSON and specifying a spatial reference (WGS84 Web Mercator Auxiliary Sphere):
<code>
location=
{
    "x": 11563503,
    "y": 148410,
    "spatialReference": {
        "wkid": 3857
    }
}
</code>

### Example: Reverse geocode the location x = 2.2945, y = 48.8583


    from arcgis.gis import GIS
    
    gis = GIS("https://deldev.maps.arcgis.com", "demo_deldev", "P@ssw0rd")
    
    # use the GIS's configured geocoder
    geocoder = gis.tools.geocoder


    results = geocoder.reverse_geocode([2.2945, 48.8583])


    results




    {'address': {'Address': '6 Avenue Gustave Eiffel',
      'City': 'Paris',
      'CountryCode': 'FRA',
      'Loc_name': 'FRA.PointAddress',
      'Match_addr': '6 Avenue Gustave Eiffel, 75007, 7e Arrondissement, Paris, le-de-France',
      'Neighborhood': '7e Arrondissement',
      'Postal': '75007',
      'PostalExt': None,
      'Region': 'le-de-France',
      'Subregion': 'Paris'},
     'location': {'spatialReference': {'latestWkid': 4326, 'wkid': 4326},
      'x': 2.29465293958984,
      'y': 48.85748501186063}}



## distance parameter

The optional distance parameter allows you to specify a radial distance in meters to search for an address from the specified location. If no distance value is specified then the value is assumed to be 100 meters.

Example:

<code>distance=50</code>

## outSR parameter

The spatial reference of the x/y coordinates returned by a geocode request. This is useful for applications using a map with a spatial reference different than that of the geocode service.

The spatial reference can be specified as either a well-known ID (WKID) or as a JSON spatial reference object. If outSR is not specified, the spatial reference of the output locations is the same as that of the service. The World Geocoding Service spatial reference is WGS84 (WKID = 4326).

For a list of valid WKID values, see Projected Coordinate Systems and Geographic Coordinate Systems.

Example (102100 is the WKID for the Web Mercator projection):

<code>outSR=102100</code>

## langCode parameter

Sets the language in which reverse-geocoded addresses are returned. Addresses in many countries are available in more than one language; in these cases the langCode parameter can be used to specify which language should be used for addresses returned by the reverse_geocode() method. This is useful for ensuring that addresses are returned in the expected language by reverse geocoding functionality in an application. For example, a web application could be designed to get the browser language and then pass it as the langCode parameter value in a reverseGeocode request.

See the <a href="https://developers.arcgis.com/rest/geocode/api-reference/geocode-coverage.htm#GUID-D61FB53E-32DF-4E0E-A1CC-473BA38A23C0">table of supported countries</a> for valid language code values in each country. The Two-Digit Language Codes column provides the valid input values for the langCode parameter. Only the two-digit language codes in this column are accepted as valid input; neither three-digit language codes nor full language names can be used with the langCode parameter.

Note:
The language code "XX" is a convention used to represent transliterated or transcribed versions of a language.

In addition to the supported language codes, the table also includes the Default Language Code column, which lists the default language of addresses returned by the reverseGeocode operation for each country. For countries with multiple supported languages, the default language is the one spoken by the highest percentage of the country's population. Addresses are not always available in the default language for the entirety of a particular country.

Note:
The langCode parameter is not supported for Japan and Hong Kong locations.

Similarly, when there are multiple supported languages for addresses in a country it doesn't mean that every address in the country is available in each of the languages. It may be the case that addresses are available in multiple languages for only one region of the country, or that each language is exclusive to different regions and there is no overlap at all. Examples:

* Both English and French are listed as supported languages for Canada. However there is no overlap between the languages for any addresses - in the province of Quebec only French addresses are available, while English is the only language used for the rest of the country.
* In Belgium, where three languages are supported (Dutch, French, and German), addresses are available in the city of Brussels in both Dutch and French; however, in the rest of the country the addresses are only available in a single language.
* In Greece there is complete address coverage in both Greek and transliterated Greek languages (Greek words translated with Latin characters).

Due to variability of language coverage, the following logic is used to handle the different scenarios which may be encountered.

<table class="tablexyz lined-rows lined-columns bordered"><colgroup width="*"></colgroup><colgroup width="*"></colgroup><colgroup width="1.50*"></colgroup><thead><tr><th colspan="1">Scenario</th><th colspan="1">Result</th><th colspan="1">Example</th></tr></thead><tbody class="align-middle">                <tr class="align-middle">                  <td purpose="entry" rowspan="1" colspan="1">                    <p id="GUID-EB71E5B8-877B-42A9-B9F1-ED0166A2B0F3">No langCode value is specified and only one language is supported at the input location </p>                  </td>                  <td purpose="entry" rowspan="1" colspan="1">                    <p id="GUID-82D25E27-FE8C-4E40-A336-50CD1CEF85D6">Address is returned in the supported language</p>                  </td>                  <td purpose="entry" rowspan="1" colspan="1">                    <p id="GUID-714A5B57-7EC6-4A9A-8712-9CB5D66EDB16">Location in Geneva, Switzerland (only French addresses are supported)</p>                    <p id="GUID-6FBCA5AE-5BA3-45EA-B0BE-6C9420EB630B">French address returned</p>                  </td>                </tr>                <tr class="align-middle">                  <td purpose="entry" rowspan="1" colspan="1">                    <p id="GUID-F9803273-DD4A-4FEC-A937-965853370458">No langCode value is specified and multiple  languages are supported at the input location </p>                  </td>                  <td purpose="entry" rowspan="1" colspan="1">                    <p id="GUID-C54F9C90-C96D-4084-A798-CB8A55B863EE">Address is returned in the country's default language</p>                  </td>                  <td purpose="entry" rowspan="1" colspan="1">                    <p id="GUID-838C527A-22CB-4A44-8D3E-A8276C0AA7DE">Location in Brussels, Belgium (Dutch and French addresses are supported; Dutch is the default language)</p>                    <p id="GUID-1DEC47D4-A5D6-4B74-81D5-8FA29C22106C">Dutch address returned</p>                  </td>                </tr>                <tr class="align-middle">                  <td purpose="entry" rowspan="1" colspan="1">                    <p id="GUID-8D83C913-DA2F-4F12-B606-FC055FA92FE4">An invalid langCode value is specified and only one language is supported at the input location</p>                  </td>                  <td purpose="entry" rowspan="1" colspan="1">                    <p id="GUID-63CAF295-911E-472E-9450-4B50DCB5FDF8">Address is returned in the supported language</p>                  </td>                  <td purpose="entry" rowspan="1" colspan="1">                    <p id="GUID-6F5BB01B-A35C-4AB5-9FB3-91A3DFB1FEBA">Location in Geneva, Switzerland (only French addresses are supported) and langCode=zh</p>                    <p id="GUID-28603318-F027-4F98-888C-A2B5392404C7">French address returned</p>                  </td>                </tr>                <tr class="align-middle">                  <td purpose="entry" rowspan="1" colspan="1">                    <p id="GUID-1DF791D3-263B-4EAE-B127-9AC7F77720E2">An invalid langCode is specified and multiple languages are supported at the input location; the input langCode is a Latin-based script and a transliterated address exists at the location</p>                  </td>                  <td purpose="entry" rowspan="1" colspan="1">                    <p id="GUID-4E2867AF-B9F1-4843-B11A-C0E789CDCBF3">Address is returned in transliterated format</p>                  </td>                  <td purpose="entry" rowspan="1" colspan="1">                    <p id="GUID-851C22C5-AA8E-4025-8A67-3BCFBE332541">Location in Athens, Greece (Greek and transliterated Greek are supported) and langCode=fr</p>                    <p id="GUID-2C304741-0888-4160-A6CF-AD383601C321">Transliterated Greek address returned</p>                  </td>                </tr>                <tr class="align-middle">                  <td purpose="entry" rowspan="1" colspan="1">                    <p id="GUID-B614E962-972E-4788-A385-A0B52383A2DF">An invalid langCode is specified and multiple languages are supported at the input location; the  input langCode is not a Latin-based script</p>                  </td>                  <td purpose="entry" rowspan="1" colspan="1">                    <p id="GUID-E82D7CC0-4941-4EC9-A2C7-918788EAFEEC">Address is returned in the country's default language</p>                  </td>                  <td purpose="entry" rowspan="1" colspan="1">                    <p id="GUID-E9B1E9A8-7A8D-40FB-9AEF-0062CEA29D35">Location in Athens, Greece (Greek and transliterated Greek are supported; Greek is the default language) and langCode=ru</p>                    <p id="GUID-B01175B5-8721-4315-9DF4-AFE9E2017EB3">Greek address returned</p>                  </td>                </tr>              </tbody></table>

Example:

<code>langCode="fr"</code>

## returnIntersection parameter

A Boolean which specifies whether the service should return the nearest street intersection or the nearest address to the input location. If true, then the closest intersection to the input location is returned; if false, then the closest address to the input location is returned. The default value is false.

Example:

<code>returnIntersection=True</code>

## forStorage parameter

Specifies whether the results of the operation will be persisted. The default value is false, which indicates the results of the operation can't be stored, but they can be temporarily displayed on a map for instance. If you store the results, in a database for example, you need to set this parameter to true.

Applications are contractually prohibited from storing the results of reverse-geocoding transactions unless they make the request by passing the forStorage parameter with a value of True 

### Example: Reverse geocode a location in Brussels with langCode=fr (location = 4.366281,50.851994)


    result = geocoder.reverse_geocode([4.366281,50.851994], langCode="fr")


    result




    {'address': {'Address': 'Rue de la Sablonnire 15',
      'City': 'Bruxelles',
      'CountryCode': 'BEL',
      'Loc_name': 'BEL.PointAddress',
      'Match_addr': 'Rue de la Sablonnire 15, 1000, Bruxelles',
      'Neighborhood': 'Bruxelles',
      'Postal': '1000',
      'PostalExt': None,
      'Region': 'Bruxelles',
      'Subregion': 'Bruxelles'},
     'location': {'spatialReference': {'latestWkid': 4326, 'wkid': 4326},
      'x': 4.366265813154625,
      'y': 50.85196404988331}}


