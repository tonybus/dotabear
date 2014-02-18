from steam_api.dota.request import dotaApiRequest

MATCH_ID = "match_id"
METHOD_NAME = "GetMatchDetails"
__author__ = 'Russ'


class MatchDetailsRequest(dotaApiRequest.DotaApiRequest):
    def __init__(self, key, responseFormat="json"):
        super(MatchDetailsRequest, self).__init__(methodName=METHOD_NAME, key=key, responseFormat=responseFormat)

    def getMatchDataById(self, matchId):
        return self._makeRequest({MATCH_ID: matchId})