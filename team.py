from ArgumentReader import ArgumentReader
import json
import sys
import os
import random

# Can be run from both Python 2.x and 3.x, should produce the same results.
# Needs a "config.json" in the same directory as the python file.
#
# Example config.json
# {
#     "developers": ["Developer 1", "Developer 2", "Developer 3"],
#     "dynamic" : {
#         "s" : "Stephanie",
#         "n" : "Norbert",
#         "a" : "Adam",
#         "d" : "Developer 3"
#     }
# }
# Developer 3 is in the dynamic list. If they are specified in args, then they will be listed in the outside category.
# Any team members listed in the "outside" category will not be listed in the developer category.
# Otherwise, they will be listed in the team

def readConfig():
    configPath = os.path.join(sys.path[0], "config.json")
    config = json.load(open(configPath))
    return config

def removeDevs(devs, others):
    copy = devs[:]
    for other in others:
        if other in copy:
            copy.remove(other)
    return copy

def randomizeMembers(members):
    team = []
    while len(members) > 0:
        member = random.choice(members)
        members.remove(member)
        team.append(str(member))   #Removes preceeding unicode u' in python 2.x, does not affect python 3.x 

    return (team)


def main(argv):
    random.seed()
    config = readConfig()
    devs = config["developers"]
    others = config["dynamic"]

    argReader = ArgumentReader(others)
    others = argReader.readArguments(argv)
    devs = removeDevs(devs, others)

    print(randomizeMembers(devs))
    print('+')
    print(randomizeMembers(others))
    # print(randomizeMembers(devs) + '\n' + randomizeMembers(others) ) 

if __name__ == "__main__":
    main(sys.argv[1:])