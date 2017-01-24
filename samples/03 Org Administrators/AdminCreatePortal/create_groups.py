# Script to read list of groups from a csv and create them on the portal.
from arcgis.gis import *
import csv

print("CREATING GROUPS")

# connect to gis
gis = GIS("https://dev003327.esri.com/portal", "admin", "esri.agp")

with open("groups.csv", 'r') as groups_csv:
    groups = csv.DictReader(groups_csv)
    for group in groups:
        try:
            print(" Creating group: ", group['title'], end="  ##  ")
            result = gis.groups.create_from_dict(group)
            if result:
                print("success")

        except Exception as create_ex:
            print("Error... ", str(create_ex))
