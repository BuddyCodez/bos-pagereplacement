import eel
import brain as Brain
# ! imported eel module for the gui.

# ? eel.init('web') is used to initialize the GUI folder.
eel.init('pagereplacement')
@eel.expose 
def Algorithm(type, capacity,pageList):
    print(type,capacity,pageList)
    if type == "fifo":
        return Brain.Algorithm().FIFO(capacity=capacity, pageList=pageList)   
    elif type == "lifo":
        return Brain.Algorithm().LIFO(frames=capacity, pages=pageList)
    elif type == "mru":
        return Brain.Algorithm().MRU(frames=capacity, pages=pageList)
    else:
        return Brain.Algorithm().LRU(capacity=capacity, pageList=pageList)


    

# ! eel.start('index.html') is used to start the GUI.
eel.start('index.html', mode='firefox')
