__author__ = 'lordobius'

from threading import Thread
from time import sleep

list = ["Bob", "aime", "Les", "Chat"]

def threaded_function(arg):
    for i in range(arg):
        print "\n"
        sleep(1)

def threaded_function2():
    for g in range(10):
        for i in list:
            print i
        print "\n"
    sleep(1)

def threaded_function3(arg):
    for i in arg:
        print(i)
        sleep(1)

if __name__ == "__main__":
    thread = Thread(target = threaded_function, args = (10, ))
    thread2 = Thread(target = threaded_function2)
    thread3 = Thread(target = threaded_function3, args = (["Beaucoup", "Trop", "Car", "Il", "En", "a", "15"], ))
    thread.start()
    thread2.start()
    thread3.start()
    thread.join()
    thread2.join()
    thread3.join()
    print "thread finished...exiting"