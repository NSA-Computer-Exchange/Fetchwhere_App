##################################### Fetchwhere call function ########################################
#
#  Author: Rob Thayer
#  Date: March 31 2022
#  Updated: 
#  Description: This script prompts a user for a folder and path to save a fetchwhere request 
#  defined in the payloads folder.
#
#######################################################################################################

import requests
from lib.GetTokenClass import ParseConfig,GetAuthToken
import json
import sys

cp = ParseConfig(r'./config/config.ini', 'URL', 'conoFetchUrl')
searchSigItemUrl = cp.configfileparam

# Fetchwhere decorator function
def apireq_decorator(func):
    def apireqdecorator_fn(*args,**kwargs):
        token,request = func(*args,**kwargs)
        searchHeaders = {
                        'accept': 'application/json; charset=utf-8', 
                        'Content-Type': 'application/json;charset=utf-8', 
                        'Authorization': 'Bearer ' + token
                        }
        idm_search_response = requests.post(searchSigItemUrl, 
                                        headers=searchHeaders, 
                                        data=request, 
                                        verify=False)
        fetchWhereResponse = json.loads(idm_search_response.content)
        prettyfetchWhereResponse = json.dumps(fetchWhereResponse, indent=4, sort_keys=True)
        
        print("Enter a path and folder to save the file: ")
        folderinput = input()
        print("Enter a filename: ")
        print("Note: File names will be saved with the .json extension")
        fileinput  = input()
        with open(folderinput+fileinput+".json", "w", encoding="utf-8") as jsonresponse:
            jsonresponse.write(prettyfetchWhereResponse)
                             
    return apireqdecorator_fn   

@apireq_decorator
def fetchRequest(tkn,payload):
    return tkn,payload 

def run(call):
    fetch = GetAuthToken()
    run = fetchRequest(fetch.auth_token,fetch.processPayload(call))
    return run    

def main():
    inputarg = sys.argv[1]
    run(inputarg)    

if __name__ == main():
    main()     
