import json

__author__ = 'Russ'

#TODO all these classes should be enums, need to figure out how to import enums into this or just upgrade to 3.3


class Status:
    OK = 1
    ERROR = 15


class LobbyType:
    INVALID = -1
    PUBLIC_MATCHMAKING = 0
    PRACTISE = 1
    TOURNAMENT = 2
    TUTORIAL = 3
    CO_OP_WITH_BOTS = 4
    TEAM_MATCH = 5
    SOLO_QUEUE = 6


class Team:
    RADIANT = 0
    DIRE = 1


class Match:
    def __init__(self, matchJson):
        self.matchId = matchJson["match_id"]
        self.matchSequenceNum = matchJson["match_seq_num"]
        self.startTime = matchJson["start_time"]
        self.lobby_type = matchJson["lobby_type"]
        self.extractPlayers(matchJson["players"])

    def extractPlayers(self, playersJson):
        self.players = []
        for playerJson in playersJson:
            player = Player(playerJson)
            self.players.append(player)


class Player:
    def __init__(self, playerJson):
        #print(str(playerJson) + "\n")
        self.accountId = playerJson["account_id"]

        playerSlotRaw = playerJson["player_slot"]
        self.team = self.__getTeam(playerSlotRaw)
        self.position = self.__getPlayerPosition(playerSlotRaw)

        self.heroId = playerJson["hero_id"]

    def __getTeam(self, playerSlotRaw):
        return self.__getFirstBit(playerSlotRaw)

    def __getPlayerPosition(self, playerSlotRaw):
        return self.__getLastThreeBitsAsInt(playerSlotRaw)

    def __getFirstBit(self, unsignedInt):
        if unsignedInt & 128 == 0:
            return 0
        else:
            return 1

    def __getLastThreeBitsAsInt(self, playerSlotRaw):
        return playerSlotRaw & 7


class MatchHistoryResponse:
    def __init__(self, rawResponseJsonString):
        self.json = json.loads(rawResponseJsonString)
        self.result = self.json["result"]
        self.status = self.result["status"]
        if self.status == Status.OK:
            self.extractFieldsOnSuccess()
        else:
            self.extractFieldsOnFailure()

    def extractFieldsOnFailure(self):
        self.errorMessage = self.result["statusDetail"]

    def extractFieldsOnSuccess(self):
        self.extractQueryResultCounts()
        self.extractMatches()

    def extractQueryResultCounts(self):
        self.numResults = self.result["num_results"]
        self.totalResults = self.result["total_results"]
        self.resultsRemaining = self.result["results_remaining"]

    def extractMatches(self):
        self.matches = []
        matchesJson = self.result["matches"]
        for matchJson in matchesJson:
            match = Match(matchJson)
            self.matches.append(match)
