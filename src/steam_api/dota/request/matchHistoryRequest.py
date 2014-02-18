from steam_api.dota.request.dotaApiRequest import DotaApiRequest

PARAM_NUM_RESULTS = "matches_requested"
PARAM_TOURNAMENT_ONLY = "tournament_games_only"
PARAM_START_AT_MATCH_ID = "start_at_match_id"
PARAM_LEAGUE_ID = "league_id"
PARAM_ACCOUNT_ID = "account_id"
PARAM_MAX_DATE = "date_max"
PARAM_MIN_DATE = "date_min"
PARAM_SKILL = "skill"
PARAM_HERO_ID = "hero_id"
PARAM_GAME_MODE = "game_mode"
PARAM_PLAYER_NAME = "player_name"
METHOD_NAME = "GetMatchHistory"
__author__ = 'Russ'


class GameMode:
    _None, All_Pick, Captains_Mode, Random_Draft, Single_Draft, All_Random, Intro, Diretide, Reverse_Captains_Mode, The_Greeviling, Tutorial, Mid_Only, Least_Played, New_Player_Pool, Compendium_Matchmaking, Captains_Draft = range(16)


class Skill:
    Any, Normal, High, VeryHigh = range(4)


class MatchHistoryRequest(DotaApiRequest):
    def __init__(self, key, responseFormat="json"):
        super(MatchHistoryRequest, self).__init__(methodName=METHOD_NAME, key=key, responseFormat=responseFormat)
        self.criteriaDict = {}

    def getMatchHistoryAndClearConfig(self):
        ret = self._makeRequest(self.criteriaDict)
        self.criteriaDict.clear()
        return ret

    def withPlayerName(self, playerName):
        return self.__addIfNotNullOrEmpty(PARAM_PLAYER_NAME, playerName)

    def withHeroId(self, heroId):
        return self.__addIfNotNullOrEmpty(PARAM_HERO_ID, heroId)

    def withGameMode(self, gameMode):
        return self.__addIfNotNullOrEmpty(PARAM_GAME_MODE, gameMode)

    def withSkill(self, skill):
        return self.__addIfNotNullOrEmpty(PARAM_SKILL, skill)

    # unix timestamp rounded to nearest day (int)
    def withMinDate(self, minDate):
        return self.__addIfNotNullOrEmpty(PARAM_MIN_DATE, minDate)

    # unix timestamp rounded to nearest day (int)
    def withMaxDate(self, maxDate):
        return self.__addIfNotNullOrEmpty(PARAM_MAX_DATE, maxDate)

    # 32-bit account ID. (string)
    def withAccountId(self, accountId):
        return self.__addIfNotNullOrEmpty(PARAM_ACCOUNT_ID, accountId)

    #Only return matches from this league.
    def withLeagueId(self, leagueId):
        return self.__addIfNotNullOrEmpty(PARAM_LEAGUE_ID, leagueId)

    #Start searching for matches equal to or older than this match ID.
    def startAtMatchId(self, matchId):
        return self.__addIfNotNullOrEmpty(PARAM_START_AT_MATCH_ID, matchId)

    def onlyTournamentGames(self):
        return self.__addIfNotNullOrEmpty(PARAM_TOURNAMENT_ONLY, "true")

    def numResults(self, numResults):
        return self.__addIfNotNullOrEmpty(PARAM_NUM_RESULTS, numResults)

    def __addIfNotNullOrEmpty(self, paramName, value):
        if value or isinstance(value, int):
            self.criteriaDict[paramName] = value
        return self