VERSION = 1
INTERFACE = "IDOTA2Match_570"
__author__ = 'Russ'

import raw_downloader.steamApiRequest


class DotaApiRequest(raw_downloader.steamApiRequest.SteamApiRequest):

    def __init__(self, methodName, key, responseFormat="json"):
        super(DotaApiRequest, self).__init__(interface=INTERFACE, version=VERSION, methodName=methodName, key=key,
                                             responseFormat=responseFormat)


