import datetime

def showTime():
    time = datetime.datetime.now()
    formatted_now = time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_now
