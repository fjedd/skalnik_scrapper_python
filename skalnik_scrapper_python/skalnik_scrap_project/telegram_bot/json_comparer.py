import os, glob

def comparer():
    # get list of files in json_store dir - change path
    json_list = glob.glob('/home/fjed/Documents/vscode/skalnik_scrapper_python/skalnik_scrap_project/json_store/*.json') # chcange path of json_store dir
    # get 2 latest json files to compare products 
    json_latest = sorted(json_list, key = os.path.getctime)[-1]
    json_2nd_latest = sorted(json_list, key = os.path.getctime)[-2]
    
    # check which products changed since last crawl
    with open(json_latest ,'r') as json1, open(json_2nd_latest, 'r') as json2:
        difference = set(json2) - set(json1) 
    different_items = '\n'.join(product for product in difference)
    # print products that changed
    return f'Products that changed since yesterday ({len(difference)}):\n\n {different_items}' 
comparer()