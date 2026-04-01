import threading
import time

def cleaning_the_house():
    print("started cleaning the house")
    time.sleep(2)
    print("Finish cleaning the house")

def cooking():
    print("started cooking")
    time.sleep(2)
    print("Finshed cooking")

task1 = threading.Thread(target=cleaning_the_house)
task2 = threading.Thread(target=cooking)

task1.start()
task2.start()

task1.join()
task2.join()
print("finsihed doing everything")
