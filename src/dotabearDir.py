__author__ = 'Russ'

import os
import re


def getDir():
    full_path = os.path.realpath(__file__)

    dotabearPattern = re.compile("(.*\\\\dotabear\\\\).*")
    matcher = dotabearPattern.match(full_path)
    if matcher:
        return matcher.group(1)
    else:
        raise Exception("didn't find dotabear directory in path='" + full_path + "'")