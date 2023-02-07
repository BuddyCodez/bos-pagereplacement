from queue import Queue
import queue
from quickchart import QuickChart
class Algorithm:
    def MRU(self,pages, frames):
        pages, frames = self.convertThings(pages, frames)
        q = queue.Queue()
        page_faults = 0
        recent = 0
        for page in pages:
            if page in q.queue:
                recent = q.queue.index(page)
            if page not in q.queue:
                if q.qsize() == frames:
                    if recent == 0:
                        q.queue.pop()
                    else:
                        q.queue.remove(q.queue[recent])
                q.put(page)
                page_faults += 1
                
        return page_faults, self.chart(page_faults, pages, name="MRU")

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
        # To represent set of current pages. We use
        # an unordered_set so that we quickly check
        # if a page is present in set or not
        s = set()
        # To store least recently used indexes
        # of pages.
        indexes = {}
        # Start from initial page
        page_faults = 0
        # list na traverse karav use thase
        for i in range(len(pageList)):
            # Check if the set can hold more pages
            if len(s) < capacity:
                # Insert it into set if not present
                # already which represents page fault
                if pageList[i] not in s:
                    s.add(pageList[i])
                    # increment page fault
                    page_faults += 1
                # Store the recently used index of
                # each page
                indexes[pageList[i]] = i
            # If the set is full then need to perform lru
            # i.e. remove the least recently used page
            # and insert the current page
            else:
                # Check if current page is not already
                # present in the set
                if pageList[i] not in s:
                    # Find the least recently used pageList
                    # that is present in the set
                    lru = float('inf')
                    for page in s:
                        if indexes[page] < lru:
                            lru = indexes[page]
                            val = page
                    # Remove the indexes page
                    s.remove(val)
                    # insert the current page
                    s.add(pageList[i])
                    # increment page fault
                    page_faults += 1
                # Update the current page index
                indexes[pageList[i]] = i
        return page_faults, self.chart(page_faults, pageList, name="LRU")
 

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

