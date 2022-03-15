def get_user_items(user, active_gis):
    """ Given a user object and a gis object, 
        this function returns a tuple with the first
        element the username and the second element
        a dictionary with each item type as the key
        and a list of those item types owned by that user."""
    
    user_inventory = {}
    user_items = active_gis.content.search(query=f"* AND NOT owner:esri*", 
                                           max_items=5000,
                                           outside_org=False)
    for item in user_items:
        if item.type not in user_inventory:
            user_inventory[item.type] = [i 
                                         for i in user_items 
                                         if i.type == item.type]
    user_items = (user.username, user_inventory)
    return user_items
	
def print_user_inventory(inventory):
    """Given the output of the get_user_items()
       function, this returns an onscreen printout
       of the item types and items of each type 
       owned by the user."""
    
    for itype, ilist in inventory.items():
        try:
            print(f"{itype}\n{'-'*50}")
            for i in ilist:
                print(f"{' ':3}{i.title:50}")
            print("\n")
        except Exception as e:
            print(f"\t\tOperation failed on: {i.title}")
            print(f"\t\tException: {sys.exc_info()[1]}")
            continue
					
def get_dash_wm(dash, active_gis):
    """Given an input dashboard and a gis object, 
       returns the webmap used in the dashboard."""
       
    return [active_gis.content.get(widget['itemId']) 
            for widget in dash.get_data()['widgets'] 
            if widget['type'] == "mapWidget"]
            
def list_webmaps(flyr_item, webmap_collection):
    """Given a Feature Layer Collection item and a list of,
       Web Maps, returns a list of all the Web Maps 
       from the collection that consume the Feature Layer Item."""
    from arcgis.mapping import WebMap
    
    flyr_webmaps = {}
    webmap_list = []
    
    for org_webmap in webmap_collection:
        webmap_obj = WebMap(org_webmap)
        for wm_lyr in webmap_obj.layers:
            if wm_lyr.layerType == "ArcGISFeatureLayer":
                if hasattr(wm_lyr, "itemId") and flyr_item.id == wm_lyr.itemId:
                    if not org_webmap in webmap_list:
                        webmap_list.append(org_webmap)
            if wm_lyr.layerType == "GroupLayer":
                for grp_lyr in wm_lyr.layers:
                     if hasattr(grp_lyr, "itemId") and flyr_item.id == grp_lyr.itemId:
                        if not org_webmap in webmap_list:
                            webmap_list.append(org_webmap)                
        else:
            continue
    flyr_webmaps[flyr_item.title] = webmap_list     
    
    return flyr_webmaps

def get_layer_item_ids(wm):
    """Given a Web Map item, returns a list of the 
       unique ItemId values serving as layers in 
       that Web Map."""
       
    from arcgis.features import FeatureLayerCollection
    from arcgis.mapping import WebMap
    
    wmo = WebMap(wm)
    wm_id_list = []
    for layer in wmo.layers:
        try:
            fsvc = FeatureLayerCollection(layer['url'][:-1], active_gis)
            if not fsvc.properties['serviceItemId'] in wm_id_list:
                wm_id_list.append(fsvc.properties['serviceItemId'])
        except Exception as e:   
            continue
    return wm_id_list
    