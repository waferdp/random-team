import sys
import os
import json

def readConfig():
    configPath = os.path.join(sys.path[0], "config.json")
    try:
        with open(configPath, "r") as configFile:
            config = json.load(configFile)
    except:
        config = {
            "developers" : [],
            "dynamics" : []
        }
    return config

def saveConfig(config):
    configPath = os.path.join(sys.path[0], "config.json")
    with open(configPath, "w") as configFile:
        json.dump(config, configFile, indent=4)
    
def getDevelopers(config):
    return config["developers"]

def getDynamics(config):
    return config["dynamic"]

def removeDeveloper(config, member):
    devs = getDevelopers(config) 
    devs.remove(member)   

def addDeveloper(config, member):
    devs = getDevelopers(config) 
    devs.append(member)

def removeDynamic(config, acronym):
    dynamics = getDynamics(config)
    del dynamics[acronym]

def addDynamic(config, acronym, member):
    dynamics = getDynamics(config)
    if acronym in dynamics:
        raise Exception('Acronym "' + acronym + '" already in use')
    dynamics[acronym] = member

def dictify(keys, values):
    dictionary = {}
    for key in keys:
        for value in values:
            dictionary[key] = value
            values.remove(value)
            break
    return dictionary

def matchCommand(command, *matches):
    if command.lower() in matches:
        return True
    else:
        return False
    
def main(argv):
    config = readConfig()

    if len(argv) == 0:
        print('Usage: python[3] changeMember.py <command> [member]')
        print('Commands:')
        print('add-developer:    Adds a developer with name - ''add-developer John''')
        print('remove-developer: Removes a developer with name - ''remove-developer John''')
        print('add-dynamic: Adds non-developer speaker with acronym''add-dynamic j Jane''')
        print('remove-dynamic: Removes non-developer speaker (using acronym)''remove-dynamic j''')
    command = argv[0]

    if matchCommand(command, "add-developer", "addev"):
        for name in argv[1:]:
            addDeveloper(config, name)
    elif matchCommand(command, "add-dynamic", "addyn"):
        newDynamics = dictify(argv[1:][::2], argv[1:][1::2])
        for acronym in newDynamics:
            addDynamic(config, acronym, newDynamics[acronym])
    elif matchCommand(command, "remove-developer", "rmdev"):
        for name in argv[1:]:
            removeDeveloper(config, name)
    elif matchCommand(command, "remove-dynamic", "rmdyn"):
        for acronym in argv[1:]:
            removeDynamic(config, acronym)
    saveConfig(config)

if __name__ == "__main__":
    main(sys.argv[1:])