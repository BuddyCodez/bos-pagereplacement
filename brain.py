from queue import Queue
import queue
from quickchart import QuickChart
class Algorithm:

    def  LIFO(self, pages,  frames):
        pages, frames = self.convertThings(pages, frames)
        q = queue.LifoQueue()
        page_faults = 0
        for  page in pages:
            if  page not in q.queue:
                if  len(q.queue) == frames:
                    q.get()
                q.put(page)
                page_faults += 1
        print("Lifo Page Faults: ", page_faults)
        return  page_faults, self.chart(page_faults, pages, name="LIFO")
    def LRU(self, capacity, pageList):
        pageList, capacity = self.convertThings(pageList, capacity)
        s = []
        faults = []
        pageFaults = 0
        for i in pageList:
            #  ? If i is not present in currentPages list
            if i not in s:
                # ! Check if the list can hold equal pages
                if(len(s) == capacity):
                    s.remove(s[0])
                    s.append(i)
                else:
                    s.append(i)
                # ! Increment Page faults
                pageFaults +=1
                faults.append(i)
            # ! If page is already there in 
            # ! currentPages i.e in Main
            else:
                # ? Remove previous index of current page
                s.remove(i)
            # ? Now append it, at last index
                s.append(i)
        return pageFaults, self.chart(pageFaults, pageList, name="LRU")
    def FIFO(self,capacity, pageList):
        pageList, capacity = self.convertThings(pageList, capacity)
        s = set()
        indexes = Queue()
        pageFaults = 0
        for i in range(len(pageList)):
            if (len(s) < capacity):
                if (pageList[i] not in s):
                    s.add(pageList[i])
                    pageFaults += 1
                    indexes.put(pageList[i])
            else:
                if (pageList[i] not in s):
                    val = indexes.queue[0]
                    indexes.get()
                    s.remove(val)
                    s.add(pageList[i])
                    indexes.put(pageList[i])
                    pageFaults += 1
        return pageFaults, self.chart(pageFaults, pageList)
    
    def chart(self, pageFaults, faults, name="FIFO"):
        qc = QuickChart()
        qc.width = 500
        qc.height = 300
        qc.device_pixel_ratio = 2.0
        qc.config = {
            "type": "bar",
            "data": {
                
                "labels": ["Page Faults", "Page Hits"],

                "datasets": [
                    {
                        "label": name,
                        "data": [pageFaults, len(faults)-pageFaults],
                        "backgroundColor": '#6419E6',
                    }
                ]
            }
        }
        return qc.get_url()
    def convertThings(self, List, Capacity):
        li = []
        for i in List:
            li.append(int(i))
        return li, int(Capacity)

