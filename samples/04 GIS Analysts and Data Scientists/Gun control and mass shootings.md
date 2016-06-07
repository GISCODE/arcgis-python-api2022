
# Gun control and mass shootings

This notebooks attempts to find if there is a correlation between gun ownership and mass shootings in the US.


    from arcgis.gis import GIS
    from arcgis.lyr import FeatureService
    
    gis = GIS("https://deldev.maps.arcgis.com", "demo_deldev", "P@ssw0rd")


    massshootings = gis.content.search("US Mass Shootings 2013-2015", "Feature Service", max_items=1)[0]


    massshootings




<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='https://deldev.maps.arcgis.com/home/item.html?id=5fe857d4fb534a78aa232c642d126d00' target='_blank'>
                        <img src='data:image/png;base64,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' width='200' height='133' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='https://deldev.maps.arcgis.com/home/item.html?id=5fe857d4fb534a78aa232c642d126d00' target='_blank'><b>US Mass Shootings 2013-2015</b>
                        </a>
                        <br>Analysis Feature Service generated from Merge Layers<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/featureshosted16.png' style="vertical-align:middle;">Feature Service by deldev
                        <br>Last Modified: December 04, 2015
                        <br>0 comments, 73 views
                    </div>
                </div>
                




    usstates = gis.content.search("USA States (Generalized)", "Feature Service", max_items=1)[0]


    usstates




<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='https://deldev.maps.arcgis.com/home/item.html?id=99fd67933e754a1181cc755146be21ca' target='_blank'>
                        <img src='data:image/png;base64,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' width='200' height='133' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='https://deldev.maps.arcgis.com/home/item.html?id=99fd67933e754a1181cc755146be21ca' target='_blank'><b>USA States (Generalized)</b>
                        </a>
                        <br>This layer presents the 50 states and the District of Columbia of the United States.    This layer is available at no cost to users with an ArcGIS Online subscription.<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/featureshosted16.png' style="vertical-align:middle;">Feature Service by esri
                        <br>Last Modified: September 03, 2013
                        <br>0 comments, 1,479,951 views
                    </div>
                </div>
                



For our analysis, we aggregate the mass shootings into the US states, using the Spatial Analysis aggregate_points() tool:


    aggr_incidents = gis.tools.analysis.aggregate_points(massshootings, usstates)


    map = gis.map('USA', 4)

    :0: FutureWarning: IPython widgets are experimental and may change in the future.
    


    map

<img src="http://esri.github.io/arcgis-python-api/notebooks/nbimages/guncontrol.png"/>

The code below queries ArcGIS Online for gun ownership by state, and displays machinegun ownership using Classed Color renderer on the map. The states shaded the darkest have the highest machine gun ownership, and the lightest states have the lowest.


    gunownership = gis.content.search("GunOwnership", "Feature Service", max_items=1)[0]


    gunownership




<div class="item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='https://deldev.maps.arcgis.com/home/item.html?id=bbc39cbee9284c6283e5f9a60fc7b920' target='_blank'>
                        <img src='data:image/png;base64,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' width='200' height='133' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right"     style="float: none; width: auto; overflow: hidden;">
                        <a href='https://deldev.maps.arcgis.com/home/item.html?id=bbc39cbee9284c6283e5f9a60fc7b920' target='_blank'><b>GunOwnership</b>
                        </a>
                        <br>Gun Ownership by State<img src='http://www.arcgis.com/home/js/jsapi/esri/css/images/item_type_icons/featureshosted16.png' style="vertical-align:middle;">Feature Service by mass_shootings_project
                        <br>Last Modified: August 29, 2014
                        <br>0 comments, 1,376 views
                    </div>
                </div>
                




    gunownership_lyr = FeatureService(gunownership).layers[0]


    map.add_layer({
            "type": "FeatureLayer",
            "url" : gunownership_lyr['url'],
            "renderer" : "ClassedColorRenderer",
            "field_name" : "Machinegun"
        })

To compare the gun ownership with the aggregates mass shootings, the code below overlays the results of the aggregates mass shootings per state using the pink circles (default) renderer. States with larger circles have witnessed larger number of mass shootings.


    map.add_layer(aggr_incidents['aggregated_layer'])

The code below looks at the data behind the layers, as well as the data behind the results of our analysis, and brings them into a Pandas data frame for further analysis, quering and display:


    incident_df = aggr_incidents['aggregated_layer'].to_df()


    incident_df.columns




    Index(['AGE_10_14', 'AGE_15_19', 'AGE_20_24', 'AGE_25_34', 'AGE_35_44',
           'AGE_45_54', 'AGE_55_64', 'AGE_5_9', 'AGE_65_74', 'AGE_75_84',
           'AGE_85_UP', 'AGE_UNDER5', 'AMERI_ES', 'ASIAN', 'AVE_FAM_SZ',
           'AVE_HH_SZ', 'AVG_SALE07', 'AVG_SIZE07', 'AnalysisArea', 'BLACK',
           'CROP_ACR07', 'FAMILIES', 'FEMALES', 'FHH_CHILD', 'HAWN_PI', 'HISPANIC',
           'HOUSEHOLDS', 'HSEHLD_1_F', 'HSEHLD_1_M', 'HSE_UNITS', 'MALES',
           'MARHH_CHD', 'MARHH_NO_C', 'MED_AGE', 'MED_AGE_F', 'MED_AGE_M',
           'MHH_CHILD', 'MULT_RACE', 'NO_FARMS07', 'OBJECTID', 'OTHER',
           'OWNER_OCC', 'POP10_SQMI', 'POP12_SQMI', 'POP2010', 'POP2012',
           'Point_Count', 'RENTER_OCC', 'SQMI', 'STATE_ABBR', 'STATE_NAME',
           'SUB_REGION', 'Shape_Area', 'Shape_Length', 'VACANT', 'WHITE',
           'geometry.rings'],
          dtype='object')




    gun_df = gunownership_lyr.query()


    incident_df




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AGE_10_14</th>
      <th>AGE_15_19</th>
      <th>AGE_20_24</th>
      <th>AGE_25_34</th>
      <th>AGE_35_44</th>
      <th>AGE_45_54</th>
      <th>AGE_55_64</th>
      <th>AGE_5_9</th>
      <th>AGE_65_74</th>
      <th>AGE_75_84</th>
      <th>...</th>
      <th>RENTER_OCC</th>
      <th>SQMI</th>
      <th>STATE_ABBR</th>
      <th>STATE_NAME</th>
      <th>SUB_REGION</th>
      <th>Shape_Area</th>
      <th>Shape_Length</th>
      <th>VACANT</th>
      <th>WHITE</th>
      <th>geometry.rings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>81539</td>
      <td>85994</td>
      <td>95829</td>
      <td>185333</td>
      <td>176373</td>
      <td>193765</td>
      <td>175562</td>
      <td>83361</td>
      <td>100523</td>
      <td>64377</td>
      <td>...</td>
      <td>192656</td>
      <td>6429.38</td>
      <td>HI</td>
      <td>Hawaii</td>
      <td>Pacific</td>
      <td>None</td>
      <td>None</td>
      <td>64170</td>
      <td>336599</td>
      <td>[[[-17328681.259800002, 2145729.6799000017], [...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>438233</td>
      <td>462128</td>
      <td>461512</td>
      <td>933781</td>
      <td>908305</td>
      <td>988205</td>
      <td>835165</td>
      <td>429877</td>
      <td>457220</td>
      <td>253186</td>
      <td>...</td>
      <td>946156</td>
      <td>67620.68</td>
      <td>WA</td>
      <td>Washington</td>
      <td>Pacific</td>
      <td>None</td>
      <td>None</td>
      <td>265601</td>
      <td>5196362</td>
      <td>[[[-13662595.938099999, 6153003.099299997], [-...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>61124</td>
      <td>66724</td>
      <td>67138</td>
      <td>122864</td>
      <td>112945</td>
      <td>149832</td>
      <td>138858</td>
      <td>60765</td>
      <td>80742</td>
      <td>45979</td>
      <td>...</td>
      <td>131189</td>
      <td>147042.71</td>
      <td>MT</td>
      <td>Montana</td>
      <td>Mountain</td>
      <td>None</td>
      <td>None</td>
      <td>73218</td>
      <td>884961</td>
      <td>[[[-12409387.5594, 5574754.270499997], [-12409...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>79013</td>
      <td>88310</td>
      <td>79646</td>
      <td>144624</td>
      <td>171376</td>
      <td>218575</td>
      <td>192101</td>
      <td>74116</td>
      <td>112651</td>
      <td>69293</td>
      <td>...</td>
      <td>159802</td>
      <td>32489.12</td>
      <td>ME</td>
      <td>Maine</td>
      <td>New England</td>
      <td>None</td>
      <td>None</td>
      <td>164611</td>
      <td>1264971</td>
      <td>[[[-7612908.5415, 5524009.787600003], [-760871...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>39790</td>
      <td>47474</td>
      <td>58956</td>
      <td>90485</td>
      <td>75262</td>
      <td>96657</td>
      <td>81819</td>
      <td>40076</td>
      <td>46873</td>
      <td>33916</td>
      <td>...</td>
      <td>97249</td>
      <td>70700.02</td>
      <td>ND</td>
      <td>North Dakota</td>
      <td>West North Central</td>
      <td>None</td>
      <td>None</td>
      <td>36306</td>
      <td>605449</td>
      <td>[[[-10990621.962, 5770462.616400003], [-110213...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>53960</td>
      <td>57628</td>
      <td>57596</td>
      <td>105429</td>
      <td>93112</td>
      <td>116918</td>
      <td>97804</td>
      <td>55531</td>
      <td>57627</td>
      <td>39728</td>
      <td>...</td>
      <td>102724</td>
      <td>77116.22</td>
      <td>SD</td>
      <td>South Dakota</td>
      <td>West North Central</td>
      <td>None</td>
      <td>None</td>
      <td>41156</td>
      <td>699392</td>
      <td>[[[-11442350.6328, 5311257.036700003], [-11466...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>35955</td>
      <td>38142</td>
      <td>40318</td>
      <td>77649</td>
      <td>66966</td>
      <td>83577</td>
      <td>73513</td>
      <td>37213</td>
      <td>39568</td>
      <td>21920</td>
      <td>...</td>
      <td>69802</td>
      <td>97813.89</td>
      <td>WY</td>
      <td>Wyoming</td>
      <td>Mountain</td>
      <td>None</td>
      <td>None</td>
      <td>34989</td>
      <td>511279</td>
      <td>[[[-11583195.4614, 5115880.6532000005], [-1158...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>375927</td>
      <td>399209</td>
      <td>386552</td>
      <td>721694</td>
      <td>725666</td>
      <td>873753</td>
      <td>699811</td>
      <td>368617</td>
      <td>400496</td>
      <td>258313</td>
      <td>...</td>
      <td>728210</td>
      <td>56103.98</td>
      <td>WI</td>
      <td>Wisconsin</td>
      <td>East North Central</td>
      <td>None</td>
      <td>None</td>
      <td>344590</td>
      <td>4902067</td>
      <td>[[[-9688638.9349, 5667356.3715], [-9683265.465...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>116955</td>
      <td>115359</td>
      <td>108209</td>
      <td>208965</td>
      <td>191609</td>
      <td>208537</td>
      <td>180313</td>
      <td>121195</td>
      <td>109534</td>
      <td>59892</td>
      <td>...</td>
      <td>174505</td>
      <td>83570.14</td>
      <td>ID</td>
      <td>Idaho</td>
      <td>Mountain</td>
      <td>None</td>
      <td>None</td>
      <td>88388</td>
      <td>1396487</td>
      <td>[[[-13027307.5891, 5415905.134800002], [-13027...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>37637</td>
      <td>46012</td>
      <td>43851</td>
      <td>69622</td>
      <td>78359</td>
      <td>102603</td>
      <td>89973</td>
      <td>34654</td>
      <td>49538</td>
      <td>28743</td>
      <td>...</td>
      <td>75035</td>
      <td>9614.43</td>
      <td>VT</td>
      <td>Vermont</td>
      <td>New England</td>
      <td>None</td>
      <td>None</td>
      <td>66097</td>
      <td>596292</td>
      <td>[[[-8155049.916300001, 5273398.919699997], [-8...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>352342</td>
      <td>367829</td>
      <td>355651</td>
      <td>715586</td>
      <td>681094</td>
      <td>807898</td>
      <td>629364</td>
      <td>355536</td>
      <td>354427</td>
      <td>222030</td>
      <td>...</td>
      <td>563368</td>
      <td>84376.21</td>
      <td>MN</td>
      <td>Minnesota</td>
      <td>West North Central</td>
      <td>None</td>
      <td>None</td>
      <td>259974</td>
      <td>4524062</td>
      <td>[[[-10211377.6539, 5388323.559799999], [-10250...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>242553</td>
      <td>254860</td>
      <td>253048</td>
      <td>524144</td>
      <td>499525</td>
      <td>539075</td>
      <td>509566</td>
      <td>237214</td>
      <td>290041</td>
      <td>165620</td>
      <td>...</td>
      <td>574453</td>
      <td>97076.81</td>
      <td>OR</td>
      <td>Oregon</td>
      <td>Pacific</td>
      <td>None</td>
      <td>None</td>
      <td>156624</td>
      <td>3204614</td>
      <td>[[[-13518806.9335, 5160130.819799997], [-13612...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>84620</td>
      <td>93620</td>
      <td>84546</td>
      <td>144472</td>
      <td>179178</td>
      <td>225961</td>
      <td>178243</td>
      <td>77756</td>
      <td>96762</td>
      <td>56745</td>
      <td>...</td>
      <td>150657</td>
      <td>9266.56</td>
      <td>NH</td>
      <td>New Hampshire</td>
      <td>New England</td>
      <td>None</td>
      <td>None</td>
      <td>95781</td>
      <td>1236050</td>
      <td>[[[-8046163.5418, 5269520.4111], [-8065739.420...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>200904</td>
      <td>216837</td>
      <td>213350</td>
      <td>382583</td>
      <td>364548</td>
      <td>439726</td>
      <td>372750</td>
      <td>200646</td>
      <td>224656</td>
      <td>153574</td>
      <td>...</td>
      <td>340941</td>
      <td>56272.82</td>
      <td>IA</td>
      <td>Iowa</td>
      <td>West North Central</td>
      <td>None</td>
      <td>None</td>
      <td>114841</td>
      <td>2781561</td>
      <td>[[[-10143446.742, 4968991.195600003], [-101444...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>405613</td>
      <td>462756</td>
      <td>475668</td>
      <td>845141</td>
      <td>887149</td>
      <td>1012435</td>
      <td>803369</td>
      <td>385687</td>
      <td>456460</td>
      <td>301065</td>
      <td>...</td>
      <td>959917</td>
      <td>8103.95</td>
      <td>MA</td>
      <td>Massachusetts</td>
      <td>New England</td>
      <td>None</td>
      <td>None</td>
      <td>261179</td>
      <td>5265236</td>
      <td>[[[-7795895.011399999, 5058460.8904], [-779308...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>122706</td>
      <td>128930</td>
      <td>129276</td>
      <td>245176</td>
      <td>220838</td>
      <td>258726</td>
      <td>213176</td>
      <td>128928</td>
      <td>123126</td>
      <td>84243</td>
      <td>...</td>
      <td>236400</td>
      <td>77353.01</td>
      <td>NE</td>
      <td>Nebraska</td>
      <td>West North Central</td>
      <td>None</td>
      <td>None</td>
      <td>75663</td>
      <td>1572838</td>
      <td>[[[-11288619.3952, 4866088.137599997], [-11360...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1211456</td>
      <td>1366278</td>
      <td>1410935</td>
      <td>2659337</td>
      <td>2610017</td>
      <td>2878691</td>
      <td>2303668</td>
      <td>1163955</td>
      <td>1360602</td>
      <td>866467</td>
      <td>...</td>
      <td>3419918</td>
      <td>48578.82</td>
      <td>NY</td>
      <td>New York</td>
      <td>Middle Atlantic</td>
      <td>None</td>
      <td>None</td>
      <td>790348</td>
      <td>12740974</td>
      <td>[[[-8264018.3235, 4939748.0704], [-8264018.346...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>791151</td>
      <td>905066</td>
      <td>874146</td>
      <td>1511119</td>
      <td>1615669</td>
      <td>1940404</td>
      <td>1622344</td>
      <td>753635</td>
      <td>979538</td>
      <td>674093</td>
      <td>...</td>
      <td>1527182</td>
      <td>45292.96</td>
      <td>PA</td>
      <td>Pennsylvania</td>
      <td>Middle Atlantic</td>
      <td>None</td>
      <td>None</td>
      <td>548411</td>
      <td>10406288</td>
      <td>[[[-8624565.87, 4825281.943899997], [-8693601....</td>
    </tr>
    <tr>
      <th>18</th>
      <td>240265</td>
      <td>250834</td>
      <td>227898</td>
      <td>420377</td>
      <td>484438</td>
      <td>575597</td>
      <td>443452</td>
      <td>222571</td>
      <td>254944</td>
      <td>166717</td>
      <td>...</td>
      <td>445801</td>
      <td>4962.77</td>
      <td>CT</td>
      <td>Connecticut</td>
      <td>New England</td>
      <td>None</td>
      <td>None</td>
      <td>116804</td>
      <td>2772410</td>
      <td>[[[-8185365.8072, 5089754.9750000015], [-81838...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>63824</td>
      <td>80046</td>
      <td>82167</td>
      <td>126962</td>
      <td>136860</td>
      <td>162350</td>
      <td>130589</td>
      <td>60440</td>
      <td>73879</td>
      <td>51252</td>
      <td>...</td>
      <td>162648</td>
      <td>1086.87</td>
      <td>RI</td>
      <td>Rhode Island</td>
      <td>New England</td>
      <td>None</td>
      <td>None</td>
      <td>49788</td>
      <td>856869</td>
      <td>[[[-7933647.647600001, 5104415.023100004], [-7...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>587335</td>
      <td>598099</td>
      <td>541238</td>
      <td>1109801</td>
      <td>1238297</td>
      <td>1379196</td>
      <td>1046165</td>
      <td>564750</td>
      <td>611434</td>
      <td>394948</td>
      <td>...</td>
      <td>1111895</td>
      <td>7553.07</td>
      <td>NJ</td>
      <td>New Jersey</td>
      <td>Middle Atlantic</td>
      <td>None</td>
      <td>None</td>
      <td>339202</td>
      <td>6029248</td>
      <td>[[[-8403428.2859, 4824592.3561], [-8401947.025...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>452171</td>
      <td>475515</td>
      <td>452026</td>
      <td>827345</td>
      <td>840830</td>
      <td>946768</td>
      <td>769143</td>
      <td>444821</td>
      <td>452335</td>
      <td>273501</td>
      <td>...</td>
      <td>754179</td>
      <td>36183.72</td>
      <td>IN</td>
      <td>Indiana</td>
      <td>East North Central</td>
      <td>None</td>
      <td>None</td>
      <td>293387</td>
      <td>5467906</td>
      <td>[[[-9611503.6058, 4604501.0363000035], [-96140...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>183173</td>
      <td>182600</td>
      <td>177509</td>
      <td>387286</td>
      <td>383043</td>
      <td>376527</td>
      <td>315499</td>
      <td>183077</td>
      <td>197781</td>
      <td>96391</td>
      <td>...</td>
      <td>414770</td>
      <td>110561.37</td>
      <td>NV</td>
      <td>Nevada</td>
      <td>Mountain</td>
      <td>None</td>
      <td>None</td>
      <td>167564</td>
      <td>1786688</td>
      <td>[[[-13263990.1055, 4637763.931900002], [-13282...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>227951</td>
      <td>221090</td>
      <td>226519</td>
      <td>445687</td>
      <td>332475</td>
      <td>306964</td>
      <td>240241</td>
      <td>249572</td>
      <td>138224</td>
      <td>80247</td>
      <td>...</td>
      <td>259555</td>
      <td>84898.13</td>
      <td>UT</td>
      <td>Utah</td>
      <td>Mountain</td>
      <td>None</td>
      <td>None</td>
      <td>102017</td>
      <td>2379560</td>
      <td>[[[-12695684.3587, 4598889.773000002], [-12695...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2590930</td>
      <td>2823940</td>
      <td>2765949</td>
      <td>5317877</td>
      <td>5182710</td>
      <td>5252371</td>
      <td>4036493</td>
      <td>2505839</td>
      <td>2275336</td>
      <td>1370210</td>
      <td>...</td>
      <td>5542127</td>
      <td>158144.83</td>
      <td>CA</td>
      <td>California</td>
      <td>Pacific</td>
      <td>None</td>
      <td>None</td>
      <td>1102583</td>
      <td>21453934</td>
      <td>[[[-13174768.4013, 3871329.6675999984], [-1318...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>774699</td>
      <td>823682</td>
      <td>763116</td>
      <td>1409959</td>
      <td>1479831</td>
      <td>1742191</td>
      <td>1452266</td>
      <td>747889</td>
      <td>850234</td>
      <td>541352</td>
      <td>...</td>
      <td>1492381</td>
      <td>41256.24</td>
      <td>OH</td>
      <td>Ohio</td>
      <td>East North Central</td>
      <td>None</td>
      <td>None</td>
      <td>524073</td>
      <td>9539437</td>
      <td>[[[-9269880.6704, 4665854.5288999975], [-92718...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>879448</td>
      <td>922092</td>
      <td>878964</td>
      <td>1775957</td>
      <td>1725890</td>
      <td>1870879</td>
      <td>1473207</td>
      <td>859405</td>
      <td>849535</td>
      <td>524766</td>
      <td>...</td>
      <td>1573333</td>
      <td>56341.77</td>
      <td>IL</td>
      <td>Illinois</td>
      <td>East North Central</td>
      <td>None</td>
      <td>None</td>
      <td>459743</td>
      <td>9177877</td>
      <td>[[[-9804084.7206, 4510580.393200003], [-980590...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>25041</td>
      <td>39919</td>
      <td>64110</td>
      <td>124745</td>
      <td>80659</td>
      <td>75703</td>
      <td>63977</td>
      <td>26147</td>
      <td>36969</td>
      <td>21525</td>
      <td>...</td>
      <td>154652</td>
      <td>62.19</td>
      <td>DC</td>
      <td>District of Columbia</td>
      <td>South Atlantic</td>
      <td>None</td>
      <td>None</td>
      <td>30012</td>
      <td>231471</td>
      <td>[[[-8572483.6335, 4716898.046899997], [-856168...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>56848</td>
      <td>64583</td>
      <td>62867</td>
      <td>111417</td>
      <td>116087</td>
      <td>133554</td>
      <td>110929</td>
      <td>56486</td>
      <td>72453</td>
      <td>41080</td>
      <td>...</td>
      <td>95573</td>
      <td>1975.78</td>
      <td>DE</td>
      <td>Delaware</td>
      <td>South Atlantic</td>
      <td>None</td>
      <td>None</td>
      <td>63588</td>
      <td>618617</td>
      <td>[[[-8427672.8732, 4658497.009999998], [-842807...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>109045</td>
      <td>120092</td>
      <td>117204</td>
      <td>220698</td>
      <td>237494</td>
      <td>276156</td>
      <td>264825</td>
      <td>106016</td>
      <td>163520</td>
      <td>97963</td>
      <td>...</td>
      <td>202818</td>
      <td>24229.88</td>
      <td>WV</td>
      <td>West Virginia</td>
      <td>South Atlantic</td>
      <td>None</td>
      <td>None</td>
      <td>118086</td>
      <td>1739988</td>
      <td>[[[-8820028.3662, 4647527.9595], [-8824558.625...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>379029</td>
      <td>406241</td>
      <td>393698</td>
      <td>762042</td>
      <td>795572</td>
      <td>902204</td>
      <td>695768</td>
      <td>366868</td>
      <td>386357</td>
      <td>223159</td>
      <td>...</td>
      <td>700636</td>
      <td>9899.54</td>
      <td>MD</td>
      <td>Maryland</td>
      <td>South Atlantic</td>
      <td>None</td>
      <td>None</td>
      <td>222403</td>
      <td>3359284</td>
      <td>[[[-8379057.8901, 4583340.935099997], [-837613...</td>
    </tr>
    <tr>
      <th>31</th>
      <td>332654</td>
      <td>339475</td>
      <td>348615</td>
      <td>726278</td>
      <td>699644</td>
      <td>742698</td>
      <td>597644</td>
      <td>348603</td>
      <td>309960</td>
      <td>170052</td>
      <td>...</td>
      <td>679768</td>
      <td>104093.95</td>
      <td>CO</td>
      <td>Colorado</td>
      <td>Mountain</td>
      <td>None</td>
      <td>None</td>
      <td>240030</td>
      <td>4089202</td>
      <td>[[[-11359536.8691, 4528901.215599999], [-11359...</td>
    </tr>
    <tr>
      <th>32</th>
      <td>284154</td>
      <td>296795</td>
      <td>289968</td>
      <td>566216</td>
      <td>576662</td>
      <td>643097</td>
      <td>538993</td>
      <td>282888</td>
      <td>325314</td>
      <td>183705</td>
      <td>...</td>
      <td>538694</td>
      <td>40409.65</td>
      <td>KY</td>
      <td>Kentucky</td>
      <td>East South Central</td>
      <td>None</td>
      <td>None</td>
      <td>207199</td>
      <td>3809537</td>
      <td>[[[-9966798.2786, 4369387.117600001], [-997055...</td>
    </tr>
    <tr>
      <th>33</th>
      <td>198884</td>
      <td>203821</td>
      <td>204454</td>
      <td>377720</td>
      <td>346673</td>
      <td>406264</td>
      <td>331247</td>
      <td>202447</td>
      <td>190389</td>
      <td>126409</td>
      <td>...</td>
      <td>358564</td>
      <td>82277.97</td>
      <td>KS</td>
      <td>Kansas</td>
      <td>West North Central</td>
      <td>None</td>
      <td>None</td>
      <td>121119</td>
      <td>2391044</td>
      <td>[[[-10583358.9584, 4439312.814599998], [-10620...</td>
    </tr>
    <tr>
      <th>34</th>
      <td>511246</td>
      <td>550965</td>
      <td>572091</td>
      <td>1090419</td>
      <td>1108928</td>
      <td>1214000</td>
      <td>954964</td>
      <td>511849</td>
      <td>549804</td>
      <td>304730</td>
      <td>...</td>
      <td>1000872</td>
      <td>39995.61</td>
      <td>VA</td>
      <td>Virginia</td>
      <td>South Atlantic</td>
      <td>None</td>
      <td>None</td>
      <td>308881</td>
      <td>5486852</td>
      <td>[[[-8445478.5581, 4516374.472400002], [-845368...</td>
    </tr>
    <tr>
      <th>35</th>
      <td>396925</td>
      <td>423786</td>
      <td>413289</td>
      <td>775467</td>
      <td>748616</td>
      <td>888572</td>
      <td>723278</td>
      <td>390463</td>
      <td>450490</td>
      <td>274025</td>
      <td>...</td>
      <td>742001</td>
      <td>69702.89</td>
      <td>MO</td>
      <td>Missouri</td>
      <td>West North Central</td>
      <td>None</td>
      <td>None</td>
      <td>337118</td>
      <td>4958770</td>
      <td>[[[-9919126.9919, 4432686.063500002], [-992186...</td>
    </tr>
    <tr>
      <th>36</th>
      <td>448664</td>
      <td>461582</td>
      <td>442584</td>
      <td>856693</td>
      <td>822494</td>
      <td>842546</td>
      <td>726228</td>
      <td>453680</td>
      <td>497892</td>
      <td>280539</td>
      <td>...</td>
      <td>809303</td>
      <td>113997.77</td>
      <td>AZ</td>
      <td>Arizona</td>
      <td>Mountain</td>
      <td>None</td>
      <td>None</td>
      <td>463536</td>
      <td>4667121</td>
      <td>[[[-12748377.9624, 3898982.2342000008], [-1275...</td>
    </tr>
    <tr>
      <th>37</th>
      <td>253664</td>
      <td>264484</td>
      <td>269242</td>
      <td>506755</td>
      <td>460937</td>
      <td>525611</td>
      <td>440482</td>
      <td>259336</td>
      <td>280467</td>
      <td>164335</td>
      <td>...</td>
      <td>478690</td>
      <td>69900.14</td>
      <td>OK</td>
      <td>Oklahoma</td>
      <td>West South Central</td>
      <td>None</td>
      <td>None</td>
      <td>203928</td>
      <td>2706845</td>
      <td>[[[-10512937.2448, 4154257.195600003], [-10513...</td>
    </tr>
    <tr>
      <th>38</th>
      <td>631104</td>
      <td>659591</td>
      <td>661573</td>
      <td>1246593</td>
      <td>1327151</td>
      <td>1368646</td>
      <td>1138761</td>
      <td>635945</td>
      <td>697567</td>
      <td>389051</td>
      <td>...</td>
      <td>1247255</td>
      <td>49339.57</td>
      <td>NC</td>
      <td>North Carolina</td>
      <td>South Atlantic</td>
      <td>None</td>
      <td>None</td>
      <td>582373</td>
      <td>6528950</td>
      <td>[[[-8520830.0777, 4108031.220700003], [-852204...</td>
    </tr>
    <tr>
      <th>39</th>
      <td>418941</td>
      <td>437186</td>
      <td>426244</td>
      <td>823997</td>
      <td>854130</td>
      <td>926436</td>
      <td>785715</td>
      <td>412181</td>
      <td>487074</td>
      <td>266471</td>
      <td>...</td>
      <td>792960</td>
      <td>42142.36</td>
      <td>TN</td>
      <td>Tennessee</td>
      <td>East South Central</td>
      <td>None</td>
      <td>None</td>
      <td>318581</td>
      <td>4921948</td>
      <td>[[[-9345784.1996, 4225961.418799996], [-935223...</td>
    </tr>
    <tr>
      <th>40</th>
      <td>1881883</td>
      <td>1883124</td>
      <td>1817079</td>
      <td>3613473</td>
      <td>3458382</td>
      <td>3435336</td>
      <td>2597691</td>
      <td>1928234</td>
      <td>1472256</td>
      <td>824451</td>
      <td>...</td>
      <td>3237580</td>
      <td>264778.77</td>
      <td>TX</td>
      <td>Texas</td>
      <td>West South Central</td>
      <td>None</td>
      <td>None</td>
      <td>1054503</td>
      <td>17701552</td>
      <td>[[[-10831540.8994, 3073755.2841], [-10837874.4...</td>
    </tr>
    <tr>
      <th>41</th>
      <td>141691</td>
      <td>149861</td>
      <td>142370</td>
      <td>267245</td>
      <td>248523</td>
      <td>292009</td>
      <td>256936</td>
      <td>143308</td>
      <td>153794</td>
      <td>86468</td>
      <td>...</td>
      <td>249273</td>
      <td>121588.62</td>
      <td>NM</td>
      <td>New Mexico</td>
      <td>Mountain</td>
      <td>None</td>
      <td>None</td>
      <td>109993</td>
      <td>1407876</td>
      <td>[[[-12139334.2882, 3821476.7344999984], [-1213...</td>
    </tr>
    <tr>
      <th>42</th>
      <td>319655</td>
      <td>343471</td>
      <td>335322</td>
      <td>608922</td>
      <td>619501</td>
      <td>693854</td>
      <td>588033</td>
      <td>308229</td>
      <td>370501</td>
      <td>211607</td>
      <td>...</td>
      <td>571202</td>
      <td>51649.05</td>
      <td>AL</td>
      <td>Alabama</td>
      <td>East South Central</td>
      <td>None</td>
      <td>None</td>
      <td>288062</td>
      <td>3275394</td>
      <td>[[[-9469956.554, 3760777.875699997], [-9474975...</td>
    </tr>
    <tr>
      <th>43</th>
      <td>208248</td>
      <td>224619</td>
      <td>210894</td>
      <td>387253</td>
      <td>374947</td>
      <td>416976</td>
      <td>347325</td>
      <td>205672</td>
      <td>214469</td>
      <td>121579</td>
      <td>...</td>
      <td>338695</td>
      <td>47675.31</td>
      <td>MS</td>
      <td>Mississippi</td>
      <td>East South Central</td>
      <td>None</td>
      <td>None</td>
      <td>158951</td>
      <td>1754684</td>
      <td>[[[-9846298.3604, 3689452.557099998], [-984449...</td>
    </tr>
    <tr>
      <th>44</th>
      <td>689684</td>
      <td>709999</td>
      <td>680080</td>
      <td>1335560</td>
      <td>1397540</td>
      <td>1391252</td>
      <td>1069557</td>
      <td>695161</td>
      <td>606429</td>
      <td>311783</td>
      <td>...</td>
      <td>1231182</td>
      <td>58808.69</td>
      <td>GA</td>
      <td>Georgia</td>
      <td>South Atlantic</td>
      <td>None</td>
      <td>None</td>
      <td>503217</td>
      <td>5787440</td>
      <td>[[[-9070874.8971, 3620272.8149000034], [-90632...</td>
    </tr>
    <tr>
      <th>45</th>
      <td>297286</td>
      <td>328989</td>
      <td>332494</td>
      <td>592056</td>
      <td>601292</td>
      <td>659428</td>
      <td>583795</td>
      <td>295853</td>
      <td>369043</td>
      <td>192114</td>
      <td>...</td>
      <td>552376</td>
      <td>30941.68</td>
      <td>SC</td>
      <td>South Carolina</td>
      <td>South Atlantic</td>
      <td>None</td>
      <td>None</td>
      <td>336502</td>
      <td>3060000</td>
      <td>[[[-8991030.9254, 3797310.3136000037], [-89856...</td>
    </tr>
    <tr>
      <th>46</th>
      <td>197559</td>
      <td>203805</td>
      <td>199650</td>
      <td>375892</td>
      <td>366208</td>
      <td>407266</td>
      <td>350991</td>
      <td>196877</td>
      <td>234602</td>
      <td>133977</td>
      <td>...</td>
      <td>378928</td>
      <td>53178.77</td>
      <td>AR</td>
      <td>Arkansas</td>
      <td>West South Central</td>
      <td>None</td>
      <td>None</td>
      <td>169215</td>
      <td>2245229</td>
      <td>[[[-10515427.3833, 4055253.4870000035], [-1051...</td>
    </tr>
    <tr>
      <th>47</th>
      <td>306836</td>
      <td>326779</td>
      <td>338309</td>
      <td>628433</td>
      <td>564599</td>
      <td>654375</td>
      <td>535562</td>
      <td>306362</td>
      <td>311994</td>
      <td>180177</td>
      <td>...</td>
      <td>566061</td>
      <td>46776.06</td>
      <td>LA</td>
      <td>Louisiana</td>
      <td>West South Central</td>
      <td>None</td>
      <td>None</td>
      <td>236621</td>
      <td>2836192</td>
      <td>[[[-10122790.5283, 3408664.435999997], [-10126...</td>
    </tr>
    <tr>
      <th>48</th>
      <td>1130847</td>
      <td>1228382</td>
      <td>1228758</td>
      <td>2289545</td>
      <td>2431254</td>
      <td>2741493</td>
      <td>2337668</td>
      <td>1080255</td>
      <td>1727940</td>
      <td>1097537</td>
      <td>...</td>
      <td>2421823</td>
      <td>56695.03</td>
      <td>FL</td>
      <td>Florida</td>
      <td>South Atlantic</td>
      <td>None</td>
      <td>None</td>
      <td>1568778</td>
      <td>14109162</td>
      <td>[[[-8933328.3201, 2919404.0801], [-8945151.740...</td>
    </tr>
    <tr>
      <th>49</th>
      <td>675216</td>
      <td>739599</td>
      <td>669072</td>
      <td>1164149</td>
      <td>1277974</td>
      <td>1510033</td>
      <td>1251997</td>
      <td>637784</td>
      <td>724709</td>
      <td>444940</td>
      <td>...</td>
      <td>1079166</td>
      <td>58128.82</td>
      <td>MI</td>
      <td>Michigan</td>
      <td>East North Central</td>
      <td>None</td>
      <td>None</td>
      <td>659725</td>
      <td>7803120</td>
      <td>[[[-9666409.0135, 5125917.6630000025], [-96422...</td>
    </tr>
    <tr>
      <th>50</th>
      <td>50816</td>
      <td>52141</td>
      <td>54419</td>
      <td>103125</td>
      <td>92974</td>
      <td>111026</td>
      <td>85909</td>
      <td>50887</td>
      <td>35350</td>
      <td>14877</td>
      <td>...</td>
      <td>95293</td>
      <td>581369.17</td>
      <td>AK</td>
      <td>Alaska</td>
      <td>Pacific</td>
      <td>None</td>
      <td>None</td>
      <td>48909</td>
      <td>473576</td>
      <td>[[[-19804885.652, 6726414.172700003], [-198263...</td>
    </tr>
  </tbody>
</table>
<p>51 rows × 57 columns</p>
</div>




    gun_df




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AGE_10_14</th>
      <th>AGE_15_19</th>
      <th>AGE_20_24</th>
      <th>AGE_25_34</th>
      <th>AGE_35_44</th>
      <th>AGE_45_54</th>
      <th>AGE_55_64</th>
      <th>AGE_5_9</th>
      <th>AGE_65_74</th>
      <th>AGE_75_84</th>
      <th>...</th>
      <th>STATE_NA_1</th>
      <th>SUB_REGION</th>
      <th>ShBarRifle</th>
      <th>ShBarShtgn</th>
      <th>Silencer</th>
      <th>Total</th>
      <th>VACANT</th>
      <th>WHITE</th>
      <th>Weapons</th>
      <th>geometry.rings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>81539</td>
      <td>85994</td>
      <td>95829</td>
      <td>185333</td>
      <td>176373</td>
      <td>193765</td>
      <td>175562</td>
      <td>83361</td>
      <td>100523</td>
      <td>64377</td>
      <td>...</td>
      <td>Hawaii</td>
      <td>Pacific</td>
      <td>55</td>
      <td>61</td>
      <td>117</td>
      <td>7105</td>
      <td>64170</td>
      <td>336599</td>
      <td>7105</td>
      <td>[[[-6305917.17596083, 419246.123156209], [-630...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>438233</td>
      <td>462128</td>
      <td>461512</td>
      <td>933781</td>
      <td>908305</td>
      <td>988205</td>
      <td>835165</td>
      <td>429877</td>
      <td>457220</td>
      <td>253186</td>
      <td>...</td>
      <td>Washington</td>
      <td>Pacific</td>
      <td>1437</td>
      <td>776</td>
      <td>14018</td>
      <td>60009</td>
      <td>265601</td>
      <td>5196362</td>
      <td>60009</td>
      <td>[[[-1949473.67265324, 1309020.69706041], [-195...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>61124</td>
      <td>66724</td>
      <td>67138</td>
      <td>122864</td>
      <td>112945</td>
      <td>149832</td>
      <td>138858</td>
      <td>60765</td>
      <td>80742</td>
      <td>45979</td>
      <td>...</td>
      <td>Montana</td>
      <td>Mountain</td>
      <td>744</td>
      <td>386</td>
      <td>4571</td>
      <td>11461</td>
      <td>73218</td>
      <td>884961</td>
      <td>11461</td>
      <td>[[[-1219906.91078047, 735020.492304123], [-122...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>79013</td>
      <td>88310</td>
      <td>79646</td>
      <td>144624</td>
      <td>171376</td>
      <td>218575</td>
      <td>192101</td>
      <td>74116</td>
      <td>112651</td>
      <td>69293</td>
      <td>...</td>
      <td>Maine</td>
      <td>New England</td>
      <td>1528</td>
      <td>430</td>
      <td>1728</td>
      <td>11509</td>
      <td>164611</td>
      <td>1264971</td>
      <td>11509</td>
      <td>[[[2068257.97132597, 861684.791519502], [20642...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>39790</td>
      <td>47474</td>
      <td>58956</td>
      <td>90485</td>
      <td>75262</td>
      <td>96657</td>
      <td>81819</td>
      <td>40076</td>
      <td>46873</td>
      <td>33916</td>
      <td>...</td>
      <td>North Dakota</td>
      <td>West North Central</td>
      <td>356</td>
      <td>244</td>
      <td>2834</td>
      <td>6863</td>
      <td>36306</td>
      <td>605449</td>
      <td>6863</td>
      <td>[[[-212118.215811846, 771550.516870331], [-233...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>53960</td>
      <td>57628</td>
      <td>57596</td>
      <td>105429</td>
      <td>93112</td>
      <td>116918</td>
      <td>97804</td>
      <td>55531</td>
      <td>57627</td>
      <td>39728</td>
      <td>...</td>
      <td>South Dakota</td>
      <td>West North Central</td>
      <td>361</td>
      <td>183</td>
      <td>3651</td>
      <td>9677</td>
      <td>41156</td>
      <td>699392</td>
      <td>9677</td>
      <td>[[[-551341.213212869, 462212.672788204], [-568...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>35955</td>
      <td>38142</td>
      <td>40318</td>
      <td>77649</td>
      <td>66966</td>
      <td>83577</td>
      <td>73513</td>
      <td>37213</td>
      <td>39568</td>
      <td>21920</td>
      <td>...</td>
      <td>Wyoming</td>
      <td>Mountain</td>
      <td>454</td>
      <td>384</td>
      <td>2040</td>
      <td>114052</td>
      <td>34989</td>
      <td>511279</td>
      <td>114052</td>
      <td>[[[-666556.864149306, 327634.144378249], [-668...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>375927</td>
      <td>399209</td>
      <td>386552</td>
      <td>721694</td>
      <td>725666</td>
      <td>873753</td>
      <td>699811</td>
      <td>368617</td>
      <td>400496</td>
      <td>258313</td>
      <td>...</td>
      <td>Wisconsin</td>
      <td>East North Central</td>
      <td>1969</td>
      <td>1156</td>
      <td>6347</td>
      <td>44705</td>
      <td>344590</td>
      <td>4902067</td>
      <td>44705</td>
      <td>[[[650093.461815352, 689255.20830435], [643250...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>116955</td>
      <td>115359</td>
      <td>108209</td>
      <td>208965</td>
      <td>191609</td>
      <td>208537</td>
      <td>180313</td>
      <td>121195</td>
      <td>109534</td>
      <td>59892</td>
      <td>...</td>
      <td>Idaho</td>
      <td>Mountain</td>
      <td>1778</td>
      <td>428</td>
      <td>14539</td>
      <td>39019</td>
      <td>88388</td>
      <td>1396487</td>
      <td>39019</td>
      <td>[[[-1676725.83434016, 712218.608704149], [-167...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>37637</td>
      <td>46012</td>
      <td>43851</td>
      <td>69622</td>
      <td>78359</td>
      <td>102603</td>
      <td>89973</td>
      <td>34654</td>
      <td>49538</td>
      <td>28743</td>
      <td>...</td>
      <td>Vermont</td>
      <td>New England</td>
      <td>182</td>
      <td>106</td>
      <td>70</td>
      <td>4032</td>
      <td>66097</td>
      <td>596292</td>
      <td>4032</td>
      <td>[[[1836378.57236287, 645002.388264762], [18354...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>352342</td>
      <td>367829</td>
      <td>355651</td>
      <td>715586</td>
      <td>681094</td>
      <td>807898</td>
      <td>629364</td>
      <td>355536</td>
      <td>354427</td>
      <td>222030</td>
      <td>...</td>
      <td>Minnesota</td>
      <td>West North Central</td>
      <td>1464</td>
      <td>1051</td>
      <td>719</td>
      <td>51658</td>
      <td>259974</td>
      <td>4524062</td>
      <td>51658</td>
      <td>[[[344343.64169679, 505568.008881014], [316365...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>242553</td>
      <td>254860</td>
      <td>253048</td>
      <td>524144</td>
      <td>499525</td>
      <td>539075</td>
      <td>509566</td>
      <td>237214</td>
      <td>290041</td>
      <td>165620</td>
      <td>...</td>
      <td>Oregon</td>
      <td>Pacific</td>
      <td>2984</td>
      <td>1365</td>
      <td>13304</td>
      <td>44811</td>
      <td>156624</td>
      <td>3204614</td>
      <td>44811</td>
      <td>[[[-2071939.0754562, 622770.79776274], [-21385...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>84620</td>
      <td>93620</td>
      <td>84546</td>
      <td>144472</td>
      <td>179178</td>
      <td>225961</td>
      <td>178243</td>
      <td>77756</td>
      <td>96762</td>
      <td>56745</td>
      <td>...</td>
      <td>New Hampshire</td>
      <td>New England</td>
      <td>2669</td>
      <td>407</td>
      <td>4568</td>
      <td>19284</td>
      <td>95781</td>
      <td>1236050</td>
      <td>19284</td>
      <td>[[[1914329.66627553, 662447.192620517], [19003...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>200904</td>
      <td>216837</td>
      <td>213350</td>
      <td>382583</td>
      <td>364548</td>
      <td>439726</td>
      <td>372750</td>
      <td>200646</td>
      <td>224656</td>
      <td>153574</td>
      <td>...</td>
      <td>Iowa</td>
      <td>West North Central</td>
      <td>442</td>
      <td>949</td>
      <td>414</td>
      <td>18880</td>
      <td>114841</td>
      <td>2781561</td>
      <td>18880</td>
      <td>[[[410106.309602416, 199362.159780982], [40947...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>405613</td>
      <td>462756</td>
      <td>475668</td>
      <td>845141</td>
      <td>887149</td>
      <td>1012435</td>
      <td>803369</td>
      <td>385687</td>
      <td>456460</td>
      <td>301065</td>
      <td>...</td>
      <td>Massachusetts</td>
      <td>New England</td>
      <td>1680</td>
      <td>935</td>
      <td>8486</td>
      <td>32682</td>
      <td>261179</td>
      <td>5265236</td>
      <td>32682</td>
      <td>[[[2018123.26880244, 582008.956230312], [20161...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>122706</td>
      <td>128930</td>
      <td>129276</td>
      <td>245176</td>
      <td>220838</td>
      <td>258726</td>
      <td>213176</td>
      <td>128928</td>
      <td>123126</td>
      <td>84243</td>
      <td>...</td>
      <td>Nebraska</td>
      <td>West North Central</td>
      <td>895</td>
      <td>781</td>
      <td>3483</td>
      <td>13864</td>
      <td>75663</td>
      <td>1572838</td>
      <td>13864</td>
      <td>[[[-459017.593853539, 124194.708378807], [-513...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1211456</td>
      <td>1366278</td>
      <td>1410935</td>
      <td>2659337</td>
      <td>2610017</td>
      <td>2878691</td>
      <td>2303668</td>
      <td>1163955</td>
      <td>1360602</td>
      <td>866467</td>
      <td>...</td>
      <td>New York</td>
      <td>Middle Atlantic</td>
      <td>3771</td>
      <td>7698</td>
      <td>3010</td>
      <td>64353</td>
      <td>790348</td>
      <td>12740974</td>
      <td>64353</td>
      <td>[[[1327259.77622246, 479916.612240614], [13500...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>791151</td>
      <td>905066</td>
      <td>874146</td>
      <td>1511119</td>
      <td>1615669</td>
      <td>1940404</td>
      <td>1622344</td>
      <td>753635</td>
      <td>979538</td>
      <td>674093</td>
      <td>...</td>
      <td>Pennsylvania</td>
      <td>Middle Atlantic</td>
      <td>5181</td>
      <td>12511</td>
      <td>20629</td>
      <td>191189</td>
      <td>548411</td>
      <td>10406288</td>
      <td>191189</td>
      <td>[[[1568810.07651078, 239912.258624651], [15168...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>240265</td>
      <td>250834</td>
      <td>227898</td>
      <td>420377</td>
      <td>484438</td>
      <td>575597</td>
      <td>443452</td>
      <td>222571</td>
      <td>254944</td>
      <td>166717</td>
      <td>...</td>
      <td>Connecticut</td>
      <td>New England</td>
      <td>1463</td>
      <td>966</td>
      <td>6375</td>
      <td>40740</td>
      <td>116804</td>
      <td>2772410</td>
      <td>40740</td>
      <td>[[[1847964.01042134, 508312.523737108], [18451...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>63824</td>
      <td>80046</td>
      <td>82167</td>
      <td>126962</td>
      <td>136860</td>
      <td>162350</td>
      <td>130589</td>
      <td>60440</td>
      <td>73879</td>
      <td>51252</td>
      <td>...</td>
      <td>Rhode Island</td>
      <td>New England</td>
      <td>104</td>
      <td>112</td>
      <td>30</td>
      <td>3973</td>
      <td>49788</td>
      <td>856869</td>
      <td>3973</td>
      <td>[[[1985520.04923583, 553419.795121632], [19841...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>587335</td>
      <td>598099</td>
      <td>541238</td>
      <td>1109801</td>
      <td>1238297</td>
      <td>1379196</td>
      <td>1046165</td>
      <td>564750</td>
      <td>611434</td>
      <td>394948</td>
      <td>...</td>
      <td>New Jersey</td>
      <td>Middle Atlantic</td>
      <td>802</td>
      <td>2504</td>
      <td>1016</td>
      <td>51670</td>
      <td>339202</td>
      <td>6029248</td>
      <td>51670</td>
      <td>[[[1734440.31204607, 275504.175241996], [17354...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>452171</td>
      <td>475515</td>
      <td>452026</td>
      <td>827345</td>
      <td>840830</td>
      <td>946768</td>
      <td>769143</td>
      <td>444821</td>
      <td>452335</td>
      <td>273501</td>
      <td>...</td>
      <td>Indiana</td>
      <td>East North Central</td>
      <td>3129</td>
      <td>8637</td>
      <td>22223</td>
      <td>92700</td>
      <td>293387</td>
      <td>5467906</td>
      <td>92700</td>
      <td>[[[840174.504173944, -46142.504728484], [83801...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>183173</td>
      <td>182600</td>
      <td>177509</td>
      <td>387286</td>
      <td>383043</td>
      <td>376527</td>
      <td>315499</td>
      <td>183077</td>
      <td>197781</td>
      <td>96391</td>
      <td>...</td>
      <td>Nevada</td>
      <td>Mountain</td>
      <td>3411</td>
      <td>850</td>
      <td>9104</td>
      <td>54436</td>
      <td>167564</td>
      <td>1786688</td>
      <td>54436</td>
      <td>[[[-1989522.26504359, 189879.078754569], [-200...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>227951</td>
      <td>221090</td>
      <td>226519</td>
      <td>445687</td>
      <td>332475</td>
      <td>306964</td>
      <td>240241</td>
      <td>249572</td>
      <td>138224</td>
      <td>80247</td>
      <td>...</td>
      <td>Utah</td>
      <td>Mountain</td>
      <td>2484</td>
      <td>1227</td>
      <td>12229</td>
      <td>37490</td>
      <td>102017</td>
      <td>2379560</td>
      <td>37490</td>
      <td>[[[-1563419.22674578, 60548.1092402786], [-155...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2590930</td>
      <td>2823940</td>
      <td>2765949</td>
      <td>5317877</td>
      <td>5182710</td>
      <td>5252371</td>
      <td>4036493</td>
      <td>2505839</td>
      <td>2275336</td>
      <td>1370210</td>
      <td>...</td>
      <td>California</td>
      <td>Pacific</td>
      <td>8069</td>
      <td>12863</td>
      <td>8907</td>
      <td>292877</td>
      <td>1102583</td>
      <td>21453934</td>
      <td>292877</td>
      <td>[[[-2207430.23510085, 222090.261331047], [-222...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>774699</td>
      <td>823682</td>
      <td>763116</td>
      <td>1409959</td>
      <td>1479831</td>
      <td>1742191</td>
      <td>1452266</td>
      <td>747889</td>
      <td>850234</td>
      <td>541352</td>
      <td>...</td>
      <td>Ohio</td>
      <td>East North Central</td>
      <td>4630</td>
      <td>5284</td>
      <td>26566</td>
      <td>131990</td>
      <td>524073</td>
      <td>9539437</td>
      <td>131990</td>
      <td>[[[1098937.78013447, 33940.3079409422], [10976...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>879448</td>
      <td>922092</td>
      <td>878964</td>
      <td>1775957</td>
      <td>1725890</td>
      <td>1870879</td>
      <td>1473207</td>
      <td>859405</td>
      <td>849535</td>
      <td>524766</td>
      <td>...</td>
      <td>Illinois</td>
      <td>East North Central</td>
      <td>1512</td>
      <td>1675</td>
      <td>1348</td>
      <td>118295</td>
      <td>459743</td>
      <td>9177877</td>
      <td>118295</td>
      <td>[[[696518.552287092, -133992.400470367], [6954...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>25041</td>
      <td>39919</td>
      <td>64110</td>
      <td>124745</td>
      <td>80659</td>
      <td>75703</td>
      <td>63977</td>
      <td>26147</td>
      <td>36969</td>
      <td>21525</td>
      <td>...</td>
      <td>District of Columbia</td>
      <td>South Atlantic</td>
      <td>760</td>
      <td>1048</td>
      <td>212</td>
      <td>42897</td>
      <td>30012</td>
      <td>231471</td>
      <td>42897</td>
      <td>[[[1625111.35193147, 166759.183198092], [16350...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>56848</td>
      <td>64583</td>
      <td>62867</td>
      <td>111417</td>
      <td>116087</td>
      <td>133554</td>
      <td>110929</td>
      <td>56486</td>
      <td>72453</td>
      <td>41080</td>
      <td>...</td>
      <td>Delaware</td>
      <td>South Atlantic</td>
      <td>166</td>
      <td>507</td>
      <td>293</td>
      <td>3907</td>
      <td>63588</td>
      <td>618617</td>
      <td>3907</td>
      <td>[[[1744629.38236586, 146763.518470691], [17420...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>109045</td>
      <td>120092</td>
      <td>117204</td>
      <td>220698</td>
      <td>237494</td>
      <td>276156</td>
      <td>264825</td>
      <td>106016</td>
      <td>163520</td>
      <td>97963</td>
      <td>...</td>
      <td>West Virginia</td>
      <td>South Atlantic</td>
      <td>962</td>
      <td>589</td>
      <td>3357</td>
      <td>17429</td>
      <td>118086</td>
      <td>1739988</td>
      <td>17429</td>
      <td>[[[1446990.33157261, 76524.6633184003], [14443...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>379029</td>
      <td>406241</td>
      <td>393698</td>
      <td>762042</td>
      <td>795572</td>
      <td>902204</td>
      <td>695768</td>
      <td>366868</td>
      <td>386357</td>
      <td>223159</td>
      <td>...</td>
      <td>Maryland</td>
      <td>South Atlantic</td>
      <td>2448</td>
      <td>3898</td>
      <td>9103</td>
      <td>88732</td>
      <td>222403</td>
      <td>3359284</td>
      <td>88732</td>
      <td>[[[1742070.89845562, 156606.881501351], [17446...</td>
    </tr>
    <tr>
      <th>31</th>
      <td>332654</td>
      <td>339475</td>
      <td>348615</td>
      <td>726278</td>
      <td>699644</td>
      <td>742698</td>
      <td>597644</td>
      <td>348603</td>
      <td>309960</td>
      <td>170052</td>
      <td>...</td>
      <td>Colorado</td>
      <td>Mountain</td>
      <td>3024</td>
      <td>1472</td>
      <td>10535</td>
      <td>63178</td>
      <td>240030</td>
      <td>4089202</td>
      <td>63178</td>
      <td>[[[-530336.46552419, -132349.12551744], [-5319...</td>
    </tr>
    <tr>
      <th>32</th>
      <td>284154</td>
      <td>296795</td>
      <td>289968</td>
      <td>566216</td>
      <td>576662</td>
      <td>643097</td>
      <td>538993</td>
      <td>282888</td>
      <td>325314</td>
      <td>183705</td>
      <td>...</td>
      <td>Kentucky</td>
      <td>East South Central</td>
      <td>1813</td>
      <td>1701</td>
      <td>18481</td>
      <td>59240</td>
      <td>207199</td>
      <td>3809537</td>
      <td>59240</td>
      <td>[[[843043.146359638, -214872.846221842], [8200...</td>
    </tr>
    <tr>
      <th>33</th>
      <td>198884</td>
      <td>203821</td>
      <td>204454</td>
      <td>377720</td>
      <td>346673</td>
      <td>406264</td>
      <td>331247</td>
      <td>202447</td>
      <td>190389</td>
      <td>126409</td>
      <td>...</td>
      <td>Kansas</td>
      <td>West North Central</td>
      <td>1506</td>
      <td>864</td>
      <td>4493</td>
      <td>31926</td>
      <td>121119</td>
      <td>2391044</td>
      <td>31926</td>
      <td>[[[82208.560465072, -220248.170430365], [52562...</td>
    </tr>
    <tr>
      <th>34</th>
      <td>511246</td>
      <td>550965</td>
      <td>572091</td>
      <td>1090419</td>
      <td>1108928</td>
      <td>1214000</td>
      <td>954964</td>
      <td>511849</td>
      <td>549804</td>
      <td>304730</td>
      <td>...</td>
      <td>Virginia</td>
      <td>South Atlantic</td>
      <td>9069</td>
      <td>6474</td>
      <td>21718</td>
      <td>248939</td>
      <td>308881</td>
      <td>5486852</td>
      <td>248939</td>
      <td>[[[1493856.06171441, -132012.696481957], [1487...</td>
    </tr>
    <tr>
      <th>35</th>
      <td>396925</td>
      <td>423786</td>
      <td>413289</td>
      <td>775467</td>
      <td>748616</td>
      <td>888572</td>
      <td>723278</td>
      <td>390463</td>
      <td>450490</td>
      <td>274025</td>
      <td>...</td>
      <td>Missouri</td>
      <td>West North Central</td>
      <td>2615</td>
      <td>2384</td>
      <td>9199</td>
      <td>51550</td>
      <td>337118</td>
      <td>4958770</td>
      <td>51550</td>
      <td>[[[610580.618020856, -202745.619268663], [6091...</td>
    </tr>
    <tr>
      <th>36</th>
      <td>448664</td>
      <td>461582</td>
      <td>442584</td>
      <td>856693</td>
      <td>822494</td>
      <td>842546</td>
      <td>726228</td>
      <td>453680</td>
      <td>497892</td>
      <td>280539</td>
      <td>...</td>
      <td>Arizona</td>
      <td>Mountain</td>
      <td>7162</td>
      <td>1951</td>
      <td>21382</td>
      <td>123130</td>
      <td>463536</td>
      <td>4667121</td>
      <td>62527</td>
      <td>[[[-1718233.11656762, -484581.84187505], [-172...</td>
    </tr>
    <tr>
      <th>37</th>
      <td>253664</td>
      <td>264484</td>
      <td>269242</td>
      <td>506755</td>
      <td>460937</td>
      <td>525611</td>
      <td>440482</td>
      <td>259336</td>
      <td>280467</td>
      <td>164335</td>
      <td>...</td>
      <td>Oklahoma</td>
      <td>West South Central</td>
      <td>2516</td>
      <td>1558</td>
      <td>19317</td>
      <td>47419</td>
      <td>203928</td>
      <td>2706845</td>
      <td>47419</td>
      <td>[[[142174.039999942, -448479.075167963], [1419...</td>
    </tr>
    <tr>
      <th>38</th>
      <td>631104</td>
      <td>659591</td>
      <td>661573</td>
      <td>1246593</td>
      <td>1327151</td>
      <td>1368646</td>
      <td>1138761</td>
      <td>635945</td>
      <td>697567</td>
      <td>389051</td>
      <td>...</td>
      <td>North Carolina</td>
      <td>South Atlantic</td>
      <td>4080</td>
      <td>2713</td>
      <td>13461</td>
      <td>109388</td>
      <td>582373</td>
      <td>6528950</td>
      <td>109388</td>
      <td>[[[1090218.71745379, -370906.508602684], [1078...</td>
    </tr>
    <tr>
      <th>39</th>
      <td>418941</td>
      <td>437186</td>
      <td>426244</td>
      <td>823997</td>
      <td>854130</td>
      <td>926436</td>
      <td>785715</td>
      <td>412181</td>
      <td>487074</td>
      <td>266471</td>
      <td>...</td>
      <td>Tennessee</td>
      <td>East South Central</td>
      <td>3598</td>
      <td>5787</td>
      <td>13349</td>
      <td>73320</td>
      <td>318581</td>
      <td>4921948</td>
      <td>73320</td>
      <td>[[[1086456.34361785, -319376.248393211], [1081...</td>
    </tr>
    <tr>
      <th>40</th>
      <td>1881883</td>
      <td>1883124</td>
      <td>1817079</td>
      <td>3613473</td>
      <td>3458382</td>
      <td>3435336</td>
      <td>2597691</td>
      <td>1928234</td>
      <td>1472256</td>
      <td>824451</td>
      <td>...</td>
      <td>Texas</td>
      <td>West South Central</td>
      <td>15533</td>
      <td>7104</td>
      <td>86579</td>
      <td>337309</td>
      <td>1054503</td>
      <td>17701552</td>
      <td>337309</td>
      <td>[[[-952130.577330002, -789294.007505148], [-97...</td>
    </tr>
    <tr>
      <th>41</th>
      <td>141691</td>
      <td>149861</td>
      <td>142370</td>
      <td>267245</td>
      <td>248523</td>
      <td>292009</td>
      <td>256936</td>
      <td>143308</td>
      <td>153794</td>
      <td>86468</td>
      <td>...</td>
      <td>New Mexico</td>
      <td>Mountain</td>
      <td>1400</td>
      <td>639</td>
      <td>4124</td>
      <td>84471</td>
      <td>109993</td>
      <td>1407876</td>
      <td>84471</td>
      <td>[[[-1224189.88934714, -637216.377299837], [-12...</td>
    </tr>
    <tr>
      <th>42</th>
      <td>319655</td>
      <td>343471</td>
      <td>335322</td>
      <td>608922</td>
      <td>619501</td>
      <td>693854</td>
      <td>588033</td>
      <td>308229</td>
      <td>370501</td>
      <td>211607</td>
      <td>...</td>
      <td>Alabama</td>
      <td>East South Central</td>
      <td>1915</td>
      <td>2139</td>
      <td>11967</td>
      <td>96744</td>
      <td>288062</td>
      <td>3275394</td>
      <td>96744</td>
      <td>[[[1032552.02416212, -714328.851320478], [1029...</td>
    </tr>
    <tr>
      <th>43</th>
      <td>208248</td>
      <td>224619</td>
      <td>210894</td>
      <td>387253</td>
      <td>374947</td>
      <td>416976</td>
      <td>347325</td>
      <td>205672</td>
      <td>214469</td>
      <td>121579</td>
      <td>...</td>
      <td>Mississippi</td>
      <td>East South Central</td>
      <td>1002</td>
      <td>727</td>
      <td>6072</td>
      <td>20389</td>
      <td>158951</td>
      <td>1754684</td>
      <td>20389</td>
      <td>[[[719101.817956658, -807206.46372158], [72355...</td>
    </tr>
    <tr>
      <th>44</th>
      <td>689684</td>
      <td>709999</td>
      <td>680080</td>
      <td>1335560</td>
      <td>1397540</td>
      <td>1391252</td>
      <td>1069557</td>
      <td>695161</td>
      <td>606429</td>
      <td>311783</td>
      <td>...</td>
      <td>Georgia</td>
      <td>South Atlantic</td>
      <td>5321</td>
      <td>10707</td>
      <td>43958</td>
      <td>145412</td>
      <td>503217</td>
      <td>5787440</td>
      <td>145512</td>
      <td>[[[1029578.38791626, -737280.191573997], [1029...</td>
    </tr>
    <tr>
      <th>45</th>
      <td>297286</td>
      <td>328989</td>
      <td>332494</td>
      <td>592056</td>
      <td>601292</td>
      <td>659428</td>
      <td>583795</td>
      <td>295853</td>
      <td>369043</td>
      <td>192114</td>
      <td>...</td>
      <td>South Carolina</td>
      <td>South Atlantic</td>
      <td>2095</td>
      <td>3761</td>
      <td>13952</td>
      <td>55286</td>
      <td>336502</td>
      <td>3060000</td>
      <td>55286</td>
      <td>[[[1321990.62656223, -537896.9311659], [132072...</td>
    </tr>
    <tr>
      <th>46</th>
      <td>197559</td>
      <td>203805</td>
      <td>199650</td>
      <td>375892</td>
      <td>366208</td>
      <td>407266</td>
      <td>350991</td>
      <td>196877</td>
      <td>234602</td>
      <td>133977</td>
      <td>...</td>
      <td>Arkansas</td>
      <td>West South Central</td>
      <td>1712</td>
      <td>1037</td>
      <td>9609</td>
      <td>62527</td>
      <td>169215</td>
      <td>2245229</td>
      <td>123130</td>
      <td>[[[141508.364322876, -529550.803637548], [1417...</td>
    </tr>
    <tr>
      <th>47</th>
      <td>306836</td>
      <td>326779</td>
      <td>338309</td>
      <td>628433</td>
      <td>564599</td>
      <td>654375</td>
      <td>535562</td>
      <td>306362</td>
      <td>311994</td>
      <td>180177</td>
      <td>...</td>
      <td>Louisiana</td>
      <td>West South Central</td>
      <td>2258</td>
      <td>1613</td>
      <td>10088</td>
      <td>69668</td>
      <td>236621</td>
      <td>2836192</td>
      <td>69668</td>
      <td>[[[221958.824506369, -967494.392578407], [2225...</td>
    </tr>
    <tr>
      <th>48</th>
      <td>1130847</td>
      <td>1228382</td>
      <td>1228758</td>
      <td>2289545</td>
      <td>2431254</td>
      <td>2741493</td>
      <td>2337668</td>
      <td>1080255</td>
      <td>1727940</td>
      <td>1097537</td>
      <td>...</td>
      <td>Florida</td>
      <td>South Atlantic</td>
      <td>10958</td>
      <td>6924</td>
      <td>39613</td>
      <td>199828</td>
      <td>1568778</td>
      <td>14109162</td>
      <td>199828</td>
      <td>[[[1493412.92849889, -1007484.19569054], [1496...</td>
    </tr>
    <tr>
      <th>49</th>
      <td>675216</td>
      <td>739599</td>
      <td>669072</td>
      <td>1164149</td>
      <td>1277974</td>
      <td>1510033</td>
      <td>1251997</td>
      <td>637784</td>
      <td>724709</td>
      <td>444940</td>
      <td>...</td>
      <td>Michigan</td>
      <td>East North Central</td>
      <td>804</td>
      <td>1134</td>
      <td>5627</td>
      <td>42855</td>
      <td>659725</td>
      <td>7803120</td>
      <td>42855</td>
      <td>[[[561676.052448916, 1041253.90261263], [55340...</td>
    </tr>
    <tr>
      <th>50</th>
      <td>50816</td>
      <td>52141</td>
      <td>54419</td>
      <td>103125</td>
      <td>92974</td>
      <td>111026</td>
      <td>85909</td>
      <td>50887</td>
      <td>35350</td>
      <td>14877</td>
      <td>...</td>
      <td>Alaska</td>
      <td>Pacific</td>
      <td>919</td>
      <td>1204</td>
      <td>2919</td>
      <td>11167</td>
      <td>48909</td>
      <td>473576</td>
      <td>11167</td>
      <td>[[[-3687433.93347983, 3615917.14634088], [-369...</td>
    </tr>
    <tr>
      <th>51</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td></td>
      <td></td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>[[[131851.19254655, -324473.775350928], [13322...</td>
    </tr>
    <tr>
      <th>52</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td></td>
      <td></td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>53 rows × 67 columns</p>
</div>




    gun_df.columns




    Index(['AGE_10_14', 'AGE_15_19', 'AGE_20_24', 'AGE_25_34', 'AGE_35_44',
           'AGE_45_54', 'AGE_55_64', 'AGE_5_9', 'AGE_65_74', 'AGE_75_84',
           'AGE_85_UP', 'AGE_UNDER5', 'AMERI_ES', 'ASIAN', 'AVE_FAM_SZ',
           'AVE_HH_SZ', 'AVG_SALE07', 'AVG_SIZE07', 'BLACK', 'CROP_ACR07',
           'DestDev', 'FAMILIES', 'FEMALES', 'FHH_CHILD', 'FID_', 'GlobalID',
           'GunsPerCapita', 'HAWN_PI', 'HISPANIC', 'HOUSEHOLDS', 'HSEHLD_1_F',
           'HSEHLD_1_M', 'HSE_UNITS', 'MALES', 'MARHH_CHD', 'MARHH_NO_C',
           'MED_AGE', 'MED_AGE_F', 'MED_AGE_M', 'MHH_CHILD', 'MULT_RACE',
           'Machinegun', 'NO_FARMS07', 'OBJECTID_1', 'OTHER', 'OWNER_OCC',
           'ObjectID', 'Other_1', 'POP10_SQMI', 'POP12_SQMI', 'POP2010', 'POP2012',
           'RENTER_OCC', 'SQMI', 'STATE_ABBR', 'STATE_FIPS', 'STATE_NAME',
           'STATE_NA_1', 'SUB_REGION', 'ShBarRifle', 'ShBarShtgn', 'Silencer',
           'Total', 'VACANT', 'WHITE', 'Weapons', 'geometry.rings'],
          dtype='object')




    incident_df.columns




    Index(['AGE_10_14', 'AGE_15_19', 'AGE_20_24', 'AGE_25_34', 'AGE_35_44',
           'AGE_45_54', 'AGE_55_64', 'AGE_5_9', 'AGE_65_74', 'AGE_75_84',
           'AGE_85_UP', 'AGE_UNDER5', 'AMERI_ES', 'ASIAN', 'AVE_FAM_SZ',
           'AVE_HH_SZ', 'AVG_SALE07', 'AVG_SIZE07', 'AnalysisArea', 'BLACK',
           'CROP_ACR07', 'FAMILIES', 'FEMALES', 'FHH_CHILD', 'HAWN_PI', 'HISPANIC',
           'HOUSEHOLDS', 'HSEHLD_1_F', 'HSEHLD_1_M', 'HSE_UNITS', 'MALES',
           'MARHH_CHD', 'MARHH_NO_C', 'MED_AGE', 'MED_AGE_F', 'MED_AGE_M',
           'MHH_CHILD', 'MULT_RACE', 'NO_FARMS07', 'OBJECTID', 'OTHER',
           'OWNER_OCC', 'POP10_SQMI', 'POP12_SQMI', 'POP2010', 'POP2012',
           'Point_Count', 'RENTER_OCC', 'SQMI', 'STATE_ABBR', 'STATE_NAME',
           'SUB_REGION', 'Shape_Area', 'Shape_Length', 'VACANT', 'WHITE',
           'geometry.rings'],
          dtype='object')




    from scipy.stats import pearsonr

# Is there a statistical correlation?

scipy.stats.pearsonr

Calculates a Pearson correlation coefficient and the p-value for testing non-correlation.

The Pearson correlation coefficient measures the linear relationship between two datasets. Strictly speaking, Pearson’s correlation requires that each dataset be normally distributed. Like other correlation coefficients, this one varies between -1 and +1 with 0 implying no correlation. Correlations of -1 or +1 imply an exact linear relationship. Positive correlations imply that as x increases, so does y. Negative correlations imply that as x increases, y decreases.


    from IPython.display import IFrame
    IFrame('https://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient',  width=900, height=700)





        <iframe
            width="900"
            height="700"
            src="https://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient"
            frameborder="0"
            allowfullscreen
        ></iframe>
        



Using sophisticated statistical analysis from scipy.stats module, we can check if there is a positive correlation between gun ownership and mass shootings. 1 is total positive correlation, 0 is no correlation, and −1 is total negative correlation. 


    pearsonr(gun_df['Machinegun'][:51], incident_df['Point_Count'])




    (0.75510559076163486, 1.5339951955373912e-10)




    pearsonr(gun_df['Weapons'][:51], incident_df['Point_Count'])




    (0.74426820024491702, 3.8595097934175797e-10)


