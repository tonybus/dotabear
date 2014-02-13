#!/usr/bin/python


import dotalib
import sys

#match results for tonybus most current game
matchResults = dotalib.parseMatch(dotalib.getMatchDetails(dotalib.getMatches(playerID=76561198002507434)[0]))


def padString(string, length):
    if len(string) > (length - 1):
        string = string[0:length - 1]
    return string + (" " * (length - len(string)))


class dummyPlayer:
    playerName = "Player Name"
    playerName = "Player Name"
    level = "LVL"
    kills = "K"
    deaths = "D"
    assists = "A"
    gpm = "GPM"
    endingGold = "Gold"
    xpm = "XPM"
    heroName = "Hero"
    team = False


def fancyDisplay(matchResults):
    matchIDstring = padString(str(matchResults.matchID), 12)

    if matchResults.winner:
        winnerString = "\033[1;32mRadiant\033[0m  "
    else:
        winnerString = "\033[1;31mDire\033[0m     "

    #skillLevel = dotalib.findMatchSkillLevel(matchResults.matchID)

    #if skillLevel == 1:
    #	skillString = "Normal"
    #elif skillLevel == 2:
    #	skillString = "High"
    #elif skillLevel == 3:
    #	skillString = "Very High"
    #else:
    #	skillString = "Unknown"
    skillString = "Unknown"
    skillString = padString(skillString, 10)

    titleString = "Match ID: " + matchIDstring + "Winner: " + winnerString + "MMR: " + skillString

    print(titleString)

    headerPlayer = dummyPlayer()
    headerList = list()
    headerList.append(headerPlayer)

    playerList = headerList + matchResults.players

    for player in playerList:
        try:
            player.playerName
            colorCode = "\033[0m"
        except:
            if player.team:
                colorCode = "\033[1;32m"
            else:
                colorCode = "\033[1;31m"
            player.playerName = "Unknown"

        nameString = colorCode + padString(player.playerName, 15) + "\033[0m"
        heroString = padString(player.heroName, 20)

        levelString = padString(str(player.level), 4)
        killString = padString(str(player.kills), 3)
        deathString = padString(str(player.deaths), 3)
        assistString = padString(str(player.assists), 3)

        gpmString = padString(str(player.gpm), 5)
        xpmString = padString(str(player.xpm), 5)
        goldString = padString(str(player.endingGold), 6)

        playerString = nameString + heroString + levelString + killString + deathString + assistString + "  " + gpmString + xpmString + goldString

        print(playerString)


if __name__ == "__main__":
    fancyDisplay(dotalib.parseMatch(dotalib.getMatchDetails(dotalib.getMatches(playerID=76561198002507434)[0])))
