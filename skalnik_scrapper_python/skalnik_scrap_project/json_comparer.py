import sys
from deepdiff import DeepDiff

def comparer():
    # pass two files as args, todo: automatic pick two previous json files and compare them
    json_today = sys.argv[0]
    json_yesterday = sys.argv[1]
    #figure out this function 
    difference = DeepDiff(open(json_today, 'r'), open(json_yesterday, 'r'))

    print(difference)
comparer()