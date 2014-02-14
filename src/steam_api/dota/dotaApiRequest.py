from steam_api.steamApiRequest import SteamApiRequest

VERSION = 1
INTERFACE = "IDOTA2Match_570"
__author__ = 'Russ'


class DotaApiRequest(SteamApiRequest):

    def __init__(self, methodName, key, responseFormat="json"):
        super(DotaApiRequest, self).__init__(interface=INTERFACE, version=VERSION, methodName=methodName, key=key,
                                             responseFormat=responseFormat)


