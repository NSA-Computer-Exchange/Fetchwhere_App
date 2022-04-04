##################################### Read IONAPI file, get access token ##############################
#
#  Author: Rob Thayer
#  Date: March 31 2022
#  Updated: 
#  Description: This class file reads the IONAPI file defined in the config.ini 
#  file to request a bearer tokem from the auth url.
#
#######################################################################################################

import configparser
import json
import requests
import urllib3

class ParseConfig(object):
    def __init__(self, configfile,section,sectionval):
        self.configParserObj = configparser.RawConfigParser()
        __configParser = self.configParserObj
        __configParser.read(configfile)
        self.configfileparam = __configParser.get(section,sectionval)
        
class GetAuthUrl(ParseConfig):
    def __init__(self):
        super().__init__(r'./config/config.ini', 'Params', 'ionapi_file')

    def processPayload(self,payloadfile):
        with open("./payloads/"+payloadfile+".json", "r")as payload:
            payloadrequest = payload.read()
        return payloadrequest        

    def parseionapi(tokenurl,_tokenurl):
        with open(GetAuthUrl().configfileparam, "r") as readionapi:
            __authkeys = json.load(readionapi)

        def getcredentials(user,password,client_id,client_secret):
            urllib3.disable_warnings()
            data = {
                    'grant_type': 'password',
                    'username': __authkeys[user], 
                    'password': __authkeys[password]
                    }
            authrequest = requests.post(__authkeys[tokenurl]+__authkeys[_tokenurl],
                          data=data, verify=False, allow_redirects=False, 
                          auth=(__authkeys[client_id],__authkeys[client_secret]))
            authtoken = json.loads(authrequest.content)
            return authtoken['access_token']
        return getcredentials('saak','sask','ci','cs')

class GetAuthToken(GetAuthUrl):
    def __init__(self):
        self.auth_token = GetAuthToken.parseionapi('pu','ot')



