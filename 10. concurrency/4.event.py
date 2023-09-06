"""Event Thread
Dalam pemrograman multithreading di Python, threading.Event adalah objek yang digunakan untuk mengkoordinasikan aktivitas antara thread. Event memungkinkan satu atau lebih thread untuk menunggu hingga suatu kejadian (event) terjadi sebelum melanjutkan eksekusi mereka. Dengan kata lain, event memungkinkan thread untuk berkomunikasi dan melakukan sinkronisasi dalam eksekusi mereka.

Event memiliki dua keadaan utama: set (atau dikenal sebagai "diatur") dan clear (atau dikenal sebagai "tidak diatur"). Thread-thread dapat menunggu hingga event diatur sebelum melanjutkan eksekusi mereka. Ketika event diatur, thread-thread yang sedang menunggu akan diizinkan untuk melanjutkan eksekusi mereka.
"""

import time
import threading


class Worker(threading.Thread):
    def __init__(self, name, signal):
        threading.Thread.__init__(self)
        self.name = name
        self.signal = signal

    def run(self):
        print(f"Waiting from {self.name}")
        self.signal.wait()
        print(f"Procesing from {self.name}")
        # contoh proses ketika thread mulai saat set event dimulai
        time.sleep(5)
        # saat proses code sudah selesai maka otomatis thread tersebut akan terhenti
        print(f'Done from {self.name}')


signal_event = threading.Event()
my_thread1 = Worker('Thread 1', signal_event)
my_thread1.setDaemon(True)
my_thread2 = Worker('Thread 2', signal_event)
my_thread2.setDaemon(True)
my_thread3 = Worker('Thread 3', signal_event)
my_thread3.setDaemon(True)

my_thread1.start()
my_thread2.start()
my_thread3.start()

# tunggu selama 5 detik sebelum thread yang sudah menuggu di signal.wait mulai
time.sleep(5)

# start proses
print('>>> Sent a signal to start proccesing <<<')
signal_event.set()

input('Press enter to stopping...\n')

print("Done all!!")
