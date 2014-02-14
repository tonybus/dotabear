# See https://steamcommunity.com/dev for info on url structure
# http://api.steampowered.com/<interface name>/<method name>/v<version>/?key=<api key>&format=<format>.
BASE_URL = "https://api.steampowered.com"

__author__ = 'Russ'

import urllib


class SteamApiRequest(object):

    def __init__(self, interface, methodName, version, key, responseFormat="json"):
        self.interface = interface
        self.methodName = methodName
        self.version = version
        self.key = key
        self.format = responseFormat

    def __buildPath(self):
        return BASE_URL + "/" + self.interface + "/" + self.methodName + "/V" + str(self.version) + "/"

    def __buildParamString(self, paramMap):
        extendedParamMap = {}
        if paramMap:
            extendedParamMap.update(paramMap)
        else:
            print("are you sure you want to make a query without parameters?")

        extendedParamMap['key'] = self.key
        extendedParamMap['format'] = self.format
        return urllib.urlencode(extendedParamMap)

    def _makeRequest(self, paramMap):
        path = self.__buildPath()
        params = self.__buildParamString(paramMap)

        #TODO might need try catch here
        pathAndParams = path + "?" + params
        print(pathAndParams)
        f = urllib.urlopen(pathAndParams)
        ret = f.read()
        f.close()
        return ret