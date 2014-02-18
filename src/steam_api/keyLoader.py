import dotabearDir

__author__ = 'Russ'


class ApiKeyloader:
    def __init__(self, pathToFile=dotabearDir.getDir()+"/resources/api-key/api-key.txt"):
        #todo add try here, that catches IOError and prints useful error message
        apiKeyFile = open(pathToFile)
        self.__apiKey = apiKeyFile.read()
        apiKeyFile.close()

    def getKey(self):
        return self.__apiKey