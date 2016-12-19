# Publisher persona
# Script to publish content for each user.

from arcgis.gis import *
import csv
import json

# Read the csv containing user accounts and their territory info
csv_path = "users.csv"

# Read template web map
template_webmap_dict = dict()
with open('.\\user_content\\web_map.json', 'r') as webmap_file:
            template_webmap_dict = json.load(webmap_file)

# Connect to the GIS
gis = GIS("https://dev003327.esri.com/portal", "admin", "esri.agp")

# Loop through each user and publish the content
with open(csv_path, 'r') as csv_handle:
    reader = csv.DictReader(csv_handle)
    for row in reader:
        try:
            data_to_publish = '.\\user_content\\' + row['assigned_state'] + ".csv"

            print("Publishing ", data_to_publish, end = " # ")
            added_item = gis.content.add({}, data = data_to_publish)
            published_item = added_item.publish()

            if published_item is not None:
                # publish web map
                print('webmaps', end= " ## ")
                user_webmap_dict = template_webmap_dict
                user_webmap_dict['operationalLayers'][0].update({'itemId': published_item.itemid,
                                                                 'layerType': "ArcGISFeatureLayer",
                                                                 'title': published_item.title,
                                                                 'url': published_item.url + r"/0"})

                web_map_properties = {'title': '{0} {1} response locations'.format(row['Firstname'], row['Lastname']),
                                      'type': 'Web Map',
                                      'snippet': 'Areas affected by Hurricane Matthew under the supervision of' +\
                                                 '{0} {1}'.format(row['Firstname'], row['Lastname']),
                                      'tags': 'ArcGIS Python API',
                                      'typeKeywords' : "Collector, Explorer Web Map, Web Map, Map, Online Map",
                                      'text': json.dumps(user_webmap_dict)}

                web_map_item = gis.content.add(web_map_properties)

                print("success. Assigning to: ", end="  #  ")
                result1 = published_item.reassign_to(row['username'])
                result2 = web_map_item.reassign_to(row['username'])
                if (result1 and result2) is not None:
                    print(row['username'])
                else:
                    print("error")
            else:
                print(" error publishing csv")

        except Exception as pub_ex:
            print("Error : ", str(pub_ex))
