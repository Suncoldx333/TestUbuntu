import datetime
import discord


def showTime():
    time = datetime.datetime.now()
    formatted_now = time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_now


def showVersion():
    version = discord.__version__
    #print(version)
    return version

#showVersion()