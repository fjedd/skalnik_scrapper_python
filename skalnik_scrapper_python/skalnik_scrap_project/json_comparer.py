from importlib.resources import path
import glob
from itertools import product
import os, glob

def comparer():
    # get list of files in json_store dir - change path
    json_list = glob.glob(#/YOUR PATH/json_store)
    # get 2 latest json files to compare products 
    json_latest = sorted(json_list, key = os.path.getctime)[-1]
    json_2nd_latest = sorted(json_list, key = os.path.getctime)[-2]
    
    # check which products changed since last crawl
    with open(json_latest ,'r') as json1, open(json_2nd_latest, 'r') as json2:
        difference = set(json2) - set(json1) 

    # print products that changed
    print(f'Products that changed since yesterday ({len(difference)}):')
    print('\n'.join(product for product in difference))
comparer()