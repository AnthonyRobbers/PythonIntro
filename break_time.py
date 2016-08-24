import time
import webbrowser


tot_breaks = 3
breaks = 0

print("This program started at "+time.ctime())
while(breaks < tot_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=nFdBQaxNxd0&list=PLUdbhaF8EyP0ZPe06UwnAAANAWRlZZUMF&index=175")
    breaks=breaks+1
    print("It is now "+time.ctime())

    
