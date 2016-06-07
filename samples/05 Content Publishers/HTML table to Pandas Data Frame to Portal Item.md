
# HTML table to Pandas Data Frame to Portal Item

This notebooks shows how Pandas can be used to extract data from a table within a web page (in this case, a Wikipedia article) and how it can be then brought into the GIS for further analysis and visualization.


    import pandas as pd


    df = pd.read_html("https://en.wikipedia.org/wiki/Number_of_guns_per_capita_by_country")[2]


    df.columns = df.iloc[0]
    df = df.reindex(df.index.drop(0))


    df.head()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Guns per 100 Residents</th>
      <th>Rank</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>United States</td>
      <td>112.6[6]</td>
      <td>1</td>
      <td>According to the Congressional Research Servic...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Serbia</td>
      <td>75.6</td>
      <td>2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Yemen</td>
      <td>54.8</td>
      <td>3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Switzerland</td>
      <td>45.7[note 1]</td>
      <td>4</td>
      <td>Including the personal weapons of the militia....</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Cyprus</td>
      <td>36.4[9]</td>
      <td>5</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




    df.iloc[0,1] = 112.6


    import matplotlib.pyplot as plt


    df.dtypes




    0
    Country                   object
    Guns per 100 Residents    object
    Rank                      object
    Notes                     object
    dtype: object




    df = df.convert_objects(convert_numeric=True)


    df.head(15)




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Guns per 100 Residents</th>
      <th>Rank</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>United States</td>
      <td>112.6</td>
      <td>1</td>
      <td>According to the Congressional Research Servic...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Serbia</td>
      <td>75.6</td>
      <td>2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Yemen</td>
      <td>54.8</td>
      <td>3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Switzerland</td>
      <td>NaN</td>
      <td>4</td>
      <td>Including the personal weapons of the militia....</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Cyprus</td>
      <td>NaN</td>
      <td>5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Saudi Arabia</td>
      <td>35.0</td>
      <td>6</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Iraq</td>
      <td>34.2</td>
      <td>7</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Uruguay</td>
      <td>31.8</td>
      <td>8</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Sweden</td>
      <td>31.6</td>
      <td>9</td>
      <td>According to the Swedish National Police Agenc...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Norway</td>
      <td>31.3</td>
      <td>10</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>France</td>
      <td>31.2</td>
      <td>11</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Canada</td>
      <td>30.8</td>
      <td>12</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Austria</td>
      <td>30.4</td>
      <td>13</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Iceland</td>
      <td>30.3</td>
      <td>14</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Germany</td>
      <td>30.3</td>
      <td>15</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




    from arcgis.gis import GIS
    from arcgis.lyr import FeatureCollection
    from arcgis.viz import MapView
    import json
    
    gis = GIS("https://deldev.maps.arcgis.com", "demo_deldev", "P@ssw0rd")

    :0: FutureWarning: IPython widgets are experimental and may change in the future.
    


    path = "content/features/analyze"
    postdata = {
        "f": "pjson",
        "text" : df.to_csv(),
        "filetype" : "csv",
        "analyzeParameters" : {
            "enableGlobalGeocoding": "true",
            "sourceLocale":"en-us",
            "locationType":"address",
            "sourceCountry":"",
            "sourceCountryHint":""
        }
    }
    
    
    res = gis._portal.con.post(path, postdata)
    #import json
    #json.dumps(res)
    res['publishParameters'].update({"addressFields":{"CountryCode":"Country"}})
    
    path = "content/features/generate"
    postdata = {
        "f": "pjson",
        "text" : df.to_csv(),
        "filetype" : "csv",
        "publishParameters" : json.dumps(res['publishParameters'])
    }
    
    res2014 = gis._portal.con.post(path, postdata,  use_ordered_dict=True)
    #print(json.dumps(res2014))
    fc2014 = FeatureCollection(res2014['featureCollection']['layers'][0])


    map = gis.map('USA', 2)


    map

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/wikidata.png"/>


    map.add_layer(fc2014)


    item_properties = {
        "title": "Worldwide gun ownership",
        "tags" : "guns,violence",
        "snippet": " GSR Worldwide gun ownership",
        "description": "test description",
        "text": json.dumps({"featureCollection": {"layers": [ fc2014 ]}}),
        "type": "Feature Collection",
        "typeKeywords": "Data, Feature Collection, Singlelayer",
        "extent" : "-102.5272,-41.7886,172.5967,64.984"
    }
    item = gis.content.add(item_properties)
    


    item




<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='https://deldev.maps.arcgis.com/home/item.html?id=019ab56a1e7a45eead96270ba27c3949' target='_blank'>
                        <img src='http://static.arcgis.com/images/desktopapp.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='https://deldev.maps.arcgis.com/home/item.html?id=019ab56a1e7a45eead96270ba27c3949' target='_blank'><b>Worldwide gun ownership</b>
                        </a>
                        <br> GSR Worldwide gun ownership<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/features16.png' style="vertical-align:middle;">Feature Collection by demo_deldev
                        <br>Last Modified: June 05, 2016
                        <br>0 comments, 0 views
                    </div>
                </div>
                


