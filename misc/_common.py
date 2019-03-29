from arcgis.gis import GIS
import datetime

"""accounts to keep from user/groups/items deletion"""
ignore_accounts = ['andrew', 'andrew.chapkowski', 'dvitale', 'david.vitale',
                   'atma.mani', 'john.yaist', 'bill.major', 'YJiang',
                   'rohit.singh', 'rohitgeo', 'gbochenek_python',
                   'system_publisher', 'admin', 'portaladmin',
                   'Demo_User', 'First_User', 'Second_User',
                   'api_data_owner', 'arcgis_python', 'temp_execution']

"""accounts that you want to delete groups and items, but keep user"""
target_accounts = ['arcgis_python']

"""create GIS connection via admin credentials"""
# gis = GIS(profile='your_entp_admin_profile', verify_cert=False)
gis = GIS("https://pythonapi.playground.esri.com/portal","temp_execution", "temp_execution123")


def delete_depending_items(dependent_item):
    """deletes the item's depending items, and then the item"""
    depending_items = dependent_item.dependent_to()
    if depending_items['list']:
        for item in depending_items['list']:
            delete_depending_items(item)
    if dependent_item.protected:
        dependent_item.protect(False)
    try:
        print("=== deleting the item: %s" % dependent_item.homepage)
        dependent_item.delete()
    except:
        print("=== could not delete non-dependent item %s" % dependent_item.homepage)


def delete_items(user):
    """deletes the user items"""
    folders = [None] + user.folders
    for folder in folders:
        print("=== deleting inside folder: %s" % folder)
        for item in user.items(folder=folder, max_items=255):
            delete_depending_items(item)
    print("=== finished deleting items owned by " + user.username)


def delete_groups(user):
    """deletes the user groups, and removes user from groups where user is a member of"""
    groups_for_deletion = gis.groups.get('query=owner:' + user.username)
    if groups_for_deletion is not None:
        for group in groups_for_deletion:
            try:
                print("=== deleting group %s" % group.groupid)
                group.delete()
            except:
                print("=== could not delete group %s" % group.groupid)

    for grp in user.groups:
        print("=== removing from group: %s" % grp.id)
        if grp.owner != user.username:
            try:
                grp.remove_users([user.username])
            except:
                print("=== User cannot be removed from group: %s" % grp.id)
    print("=== finished deleting groups owned by " + user.username)


def delete_for_users():
    """deletes items and groups for users in target_accounts, and ignore others"""
    for user in gis.users.search():
        if user.username not in ignore_accounts and not user.username.startswith("esri_"):
            print("-*-*-*-*-*-*-Delete groups & items & user for %s -*-*-*-*-*-" % user.username)
            delete_items(user)
            delete_groups(user)
            try:
                user.delete()
            except:
                print("could not delete user %s" % user.username)

        elif user.username in target_accounts:
            print("-*-*-*-*-*-*-Delete groups & items for %s -*-*-*-*-*-*-*-*-" % user.username)
            delete_items(user)
            delete_groups(user)

        else:
            print("-*-*-*-*-*-*-*-*-No Delete for %s -*-*-*-*-*-*-*-*-*-*-" % user.username)
