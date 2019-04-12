import threading
import time

exitFlag = 0

class myThread (threading.Thread):#
   def __init__(self, threadID, name, delay):  # inheritance from class thread
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.delay = delay

   def run(self):    # over riding (run function exists in thread
      print ("Starting " + self.name)
      print_time(self.name, self.delay, 5)    #function calling
      print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")