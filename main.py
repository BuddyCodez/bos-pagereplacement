import eel
import pyttsx3
import brain as Brain
# ! imported eel module for the gui.

# ? eel.init('web') is used to initialize the GUI folder.
eel.init('pagereplacement')
@eel.expose 
def Algorithm(type, capacity,pageList):
    print(type,capacity,pageList)
    if type == "fifo":
        return Brain.Algorithm().FIFO(capacity=capacity, pageList=pageList)   
    else:
        return Brain.Algorithm().LRU(capacity=capacity, pageList=pageList)

@eel.expose
def takeCommand():
    cmd = Brain.VoiceRecognize().takeCommand()
    return cmd
    

# ! eel.start('index.html') is used to start the GUI.
eel.start('index.html', mode='firefox')
