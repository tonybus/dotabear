__author__ = 'Russ'


class MatchHistoryDownloader:
    MATCH_BASE_URL = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/"
    #http://api.steampowered.com/IDOTA2Match_<ID>/GetMatchHistory/v1

    def getMatchHistory(self, **searchCriteriaMap):
        url=self.MATCH_BASE_URL

    # if "playerID" in args:
    #     argString = argString + "&account_ID=" + str(args['playerID'])
    #
    # if "skill" in args:
    #     argString = argString + "&skill=" + str(args['skill'])
    #
    # if "hero" in args:
    #     argString = argString + "&hero_id=" + str(args['hero'])
    #
    # if "dateMin" in args:
    #     argString = argString + "&date_min=" + str(args['dateMin'])
    #
    # if "dateMax" in args:
    #     argString = argString + "&date_max=" + str(args['dateMax'])
    #
    # if "league" in args:
    #     argString = argString + "&league_id=" + str(args['league'])
    #
    # if "startID" in args:
    #     argString = argString + "&start_at_match_id=" + str(args['startID'])
    #
    # if "numReq" in args:
    #     argString = argString + "&matches_requested=" + str(args['numReq'])