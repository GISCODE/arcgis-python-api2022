
##The FeatureCollection class

<hr/>

<code><b>class lyr.FeatureCollection<b>(<i>dictdata</i>)</code>

Bases: collections.OrderedDict

Represents a feature collection. A feature collection is a type of feature layer.  A feature collection consists of a layer definition and feature set. 

A feature set contains the geometry and attributes of features in a layer. See http://resources.arcgis.com/en/help/arcgis-rest-api%20%20/index.html#/featureSet/02r300000047000000/

The layerDefinition object defines the attribute schema and drawing information for a layer drawn using client-side graphics. See http://resources.arcgis.com/en/help/arcgis-rest-api%20%20/index.html#/layerDefinition/02r30000004v000000/

The feature collection is represented as a Python dictionary.

<hr>

##to_df()

Represents the data in the feature collection as a Pandas data frame.

<hr>
