import queue

def mru(pages, frames):
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
            
    return page_faults

li = [1, 2, 1, 3, 1, 4 ]
print(mru(li, 3))
