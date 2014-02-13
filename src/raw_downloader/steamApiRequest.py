# See https://steamcommunity.com/dev for info on url structure
# http://api.steampowered.com/<interface name>/<method name>/v<version>/?key=<api key>&format=<format>.
BASE_URL = "https://api.steampowered.com/"

__author__ = 'Russ'

import urllib


class SteamApiRequest:

    def __init__(self, interface, methodName, version, key, responseFormat="json"):
        self.interface = interface
        self.methodName = methodName
        self.version = version
        self.key = key
        self.format = responseFormat

    def __buildPath(self):
        return BASE_URL + "/" + self.interface + "/" + self.methodName + "/v" + self.version + "/"

    def __buildParamString(self, paramMap):
        if paramMap.len() == 0:
            return ""
        else:
            extendedParamMap = paramMap.copy()
            extendedParamMap['key'] = self.key
            extendedParamMap['format'] = self.format
            return urllib.urlencode(extendedParamMap)

    def _makeRequest(self, paramMap):
        path = self.__buildPath()
        params = self.__buildParamString(paramMap)

        #TODO might need try catch here
        f = urllib.urlopen(path, params)
        ret = f.read()
        f.close()
        return ret