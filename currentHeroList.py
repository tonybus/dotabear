#!/usr/bin/python

import dotalib
import urllib
import xml.dom.minidom as minidom
import pickle

hFile = urllib.request.urlopen("http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?language=en_us&key=%s&format=xml" % dotalib.apiKey)
hData = hFile.read()
hFile.close()

hDom = minidom.parseString(hData)

heroes = hDom.getElementsByTagName("hero")

herolist = [str()] * int(heroes[-1].getElementsByTagName("id")[0].firstChild.data)

print( str(len(heroes)) + " heroes processed")

for hero in heroes:

	herolist[int(hero.getElementsByTagName("id")[0].firstChild.data) - 1] = hero.getElementsByTagName("localized_name")[0].firstChild.data



heroListFile = open("heroList", "wb")
pickle.dump(herolist, heroListFile)
