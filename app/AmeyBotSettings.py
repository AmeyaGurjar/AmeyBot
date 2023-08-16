from os.path import exists
from colorama import Fore
from json import load, dump
from urllib.request import urlopen
def printGood(text):
    print(Fore.GREEN, text, Fore.RESET)
def printError(text):
    print(Fore.RED, text, Fore.RESET)
AmeyBotConfigUrl = "https://gitlab.com/AmeyaGurjar/ameybotassets/-/raw/main/AmeyBotConfig.json"
def jsonFetch():
    global configBotFunction, optionBotConfig, inputBotString
    internalAmeyBotConfigFile = urlopen("https://gitlab.com/AmeyaGurjar/ameybotassets/-/raw/main/config/internalAmeyBotSetting.json")
    internalAmeyBotConfig = load(internalAmeyBotConfigFile)
    configBotFunction = internalAmeyBotConfig["AmeyConfigFile"]["configFunction"]
    optionBotConfig = internalAmeyBotConfig["AmeyConfigFile"]["optionConfig"]
    inputBotString = internalAmeyBotConfig["AmeyConfigFile"]["inputString"]
def configValidator(ameyBotConfig, configFunction ,optionConfig, inputString):
    if configFunction == "botName" or configFunction == "botUrl":
        if ameyBotConfig["AmeyBotConfig"][configFunction] == "":
            print("\n")
            readingBot = str(input(Fore.BLUE+inputString+Fore.RESET)).lower()
            if configFunction == "botUrl": 
                readingBot = readingBot.replace("https://www.youtube.com/channel/", "")
            ameyBotConfig["AmeyBotConfig"][configFunction] = ameyBotConfig["AmeyBotConfig"][configFunction].replace(ameyBotConfig["AmeyBotConfig"][configFunction], str(readingBot))
            printGood("Settings Saved Successfully")
        else:
            pass
    elif configFunction == "emojiLimit" or configFunction == "wordLimit" or configFunction == "sayDelay" or configFunction == "timeOutTimeNormal" or configFunction == "timeOutTimeMod":
        if ameyBotConfig["AmeyBotConfig"][configFunction] == "":
            print("\n")
            try:
                readingBot = int(input(Fore.BLUE+inputString+Fore.RESET))
                ameyBotConfig["AmeyBotConfig"][configFunction] = ameyBotConfig["AmeyBotConfig"][configFunction].replace(ameyBotConfig["AmeyBotConfig"][configFunction], str(readingBot))
                printGood("Settings Saved Successfully")
            except: 
                printError("Invalid Option Entered!")
                configValidator(ameyBotConfig=ameyBotConfig, configFunction=configFunction, optionConfig=optionConfig, inputString=inputString)
        else:
            pass
    else:
        optionConfigList = optionConfig.split(", ")
        if ameyBotConfig["AmeyBotConfig"][configFunction] not in optionConfigList:
            print("\n")
            readingBot = str(input(Fore.BLUE+inputString+Fore.RESET)).lower()
            if readingBot in optionConfigList:
                ameyBotConfig["AmeyBotConfig"][configFunction] = ameyBotConfig["AmeyBotConfig"][configFunction].replace(ameyBotConfig["AmeyBotConfig"][configFunction], str(readingBot))
                printGood("Settings Saved Successfully")
            else:
                printError("Invalid Option Entered!")
                configValidator(ameyBotConfig=ameyBotConfig, configFunction=configFunction, optionConfig=optionConfig, inputString=inputString)
    ameyBotConfigFile = open("config/AmeyBotConfig.json", "w")
    dump(ameyBotConfig, ameyBotConfigFile)
        
def configCheck(ameyBotConfig):
    jsonFetch()
    for i in range(len(configBotFunction)):
        configValidator(ameyBotConfig=ameyBotConfig, configFunction=configBotFunction[i], optionConfig=optionBotConfig[i], inputString=inputBotString[i])
    
def configRun():
    if exists("AmeyBotConfig.json"):
        ameyBotConfigFile = open("config/AmeyBotConfig.json", "r")
        try:
            ameyBotConfig = load(ameyBotConfigFile)
            configCheck(ameyBotConfig=ameyBotConfig)
        except:
            AmeyBotConfigDefault = urlopen(AmeyBotConfigUrl)
            open("config/AmeyBotConfig.json", "wb").write(AmeyBotConfigDefault)
            configRun()
    else:
        AmeyBotConfigDefault = urlopen(AmeyBotConfigUrl)
        open("config/AmeyBotConfig.json", "wb").write(AmeyBotConfigDefault)
        configRun()
