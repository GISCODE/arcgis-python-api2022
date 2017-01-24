# Script to read account list from a csv file and create appropriate users in the portal.
import csv
from arcgis.gis import *

print("CREATING USER ACCOUNTS")

# Connect to the GIS
gis = GIS("https://dev003327.esri.com/portal", "admin", "esri.agp")

# loop through and create users
with open("users.csv", 'r') as users_csv:
    users = csv.DictReader(users_csv)
    for user in users:
        try:
            print("Creating user: ", user['username'], end=" ## ")
            result = gis.users.create(username=user['username'],
                                      password=user['password'],
                                      firstname=user['Firstname'],
                                      lastname=user['Lastname'],
                                      email=user['email'],
                                      role =user['role'])
            if result:
                print("success  ##")

                print("\t Adding to groups: ", end=" # ")
                groups = user['groups']
                group_list = groups.split(",")

                # Search for the group
                for g in group_list:
                    group_search = gis.groups.search(g)
                    if len(group_search) > 0:
                        try:
                            group = group_search[0]
                            groups_result = group.add_users([user['username']])
                            if len(groups_result['notAdded']) == 0:
                                print(g, end =" # ")

                        except Exception as groups_ex:
                            print("\n \t Cannot add user to group ", g, str(groups_ex))
                print("\n")

        except Exception as add_ex:
            print("Cannot create user: " + user['username'])
            print(str(add_ex))
