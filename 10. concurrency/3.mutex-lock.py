"""Mutex Lock
Mutex (Mutual Exclusion) lock adalah mekanisme dalam pemrograman multithreading yang digunakan untuk mengontrol 
akses ke sumber daya bersama atau bagian kode yang kritis secara bersamaan oleh beberapa thread. 
Tujuan utama dari mutex adalah untuk mencegah beberapa thread mengakses sumber daya yang sama pada saat yang bersamaan, 
yang dapat mengakibatkan kondisi balapan (race condition) atau ketidakpastian dalam aplikasi multithread.

Dalam konteks Python, Anda dapat menggunakan modul threading untuk mengimplementasikan mutex lock. Anda dapat membuat objek threading.Lock() 
yang akan bertindak sebagai mutex dan memastikan bahwa hanya satu thread yang dapat mengakses bagian kode yang dikunci oleh mutex tersebut pada 
satu waktu. 
"""

import time
import threading


class MyThread(threading.Thread):
    def __init__(self, name, o_lock):
        threading.Thread.__init__(self)
        self.name = name
        self.running = False
        self.value_lock = o_lock

    def run(self):
        global value
        self.running = True
        while self.running:
            self.value_lock.acquire()
            value += 1
            print(f'value : {str(value)} from {self.name}')
            self.value_lock.release()
            time.sleep(2)

    def stop(self):
        print(f"Stopping {self.name}")
        self.running = False
        self.join(2)


global value
value = 0
value_lock = threading.Lock()

myThread1 = MyThread('Thread 1', value_lock)
myThread1.setDaemon(True)

myThread2 = MyThread('Thread 2', value_lock)
myThread2.setDaemon(True)

myThread1.start()
myThread2.start()

input("Press enter to stop...\n")

myThread1.stop()
myThread2.stop()

# myThread1.join()
# myThread2.join()
