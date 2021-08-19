import sys
import os
import json

def readConfig():
    configPath = os.path.join(sys.path[0], "config.json")
    with open(configPath, "r") as configFile:
        config = json.load(configFile)
    return config

def saveConfig(config):
    configPath = os.path.join(sys.path[0], "config.json")
    with open(configPath, "w") as configFile:
        json.dump(config, configFile)
    
def getDevelopers(config):
    return config["developers"]

def removeDeveloper(config, member):
    devs = getDevelopers(config) 
    devs.remove(member)   

def addDeveloper(config, member):
    devs = getDevelopers(config) 
    devs.append(member)

def main(argv):
    config = readConfig()
    modified = False
    if argv[0].lower() == "add":
        for name in argv[1:]:
            addDeveloper(config, name)
            modified = True
    elif argv[0].lower() == "remove":
        for name in argv[1:]:
            removeDeveloper(config, name)
            modified = True
    if modified:
        saveConfig(config)

if __name__ == "__main__":
    main(sys.argv[1:])