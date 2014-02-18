from steam_api.dota.response.matchHistoryResponse import MatchHistoryResponse
from steam_api.dota.request.matchHistoryRequest import MatchHistoryRequest, GameMode, Skill
from steam_api.keyLoader import ApiKeyloader

__author__ = 'Russ'

#todo probably augment the code to allow a list of game modes/skills/etc..

key = ApiKeyloader().getKey()
request = MatchHistoryRequest(key)\
    .withGameMode(GameMode.All_Pick)\
    .withSkill(Skill.Any)\
    .numResults(2)

matchHistoryResponse = request.getMatchHistoryAndClearConfig()

print matchHistoryResponse

response = MatchHistoryResponse(matchHistoryResponse)
print response

