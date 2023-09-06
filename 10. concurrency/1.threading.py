import time
import threading

global running


def perform():
    global running

    counter = 0
    running = True
    while running:
        print('counter : ', str(counter))
        time.sleep(2)
        counter += 1


my_thread = threading.Thread(target=perform)
my_thread.setDaemon(True)
my_thread.start()

# Stop thread
input("Press enter to stop...\n")

print("stop threading...")
running = False
my_thread.join(2)
print("thread has stopping!")
