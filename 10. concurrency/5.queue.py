"""Queue
Di Python, queue adalah struktur data yang digunakan untuk menyimpan dan mengelola sekumpulan elemen dengan prinsip "first-in, first-out" (FIFO), yang berarti elemen pertama yang dimasukkan ke dalam antrian adalah elemen pertama yang keluar. Antrian sangat berguna dalam pemrograman untuk situasi di mana Anda perlu mengkoordinasikan antara beberapa proses atau thread, membagi pekerjaan, atau melakukan tugas lain yang melibatkan antrean eksekusi.

Python memiliki beberapa modul yang mendukung penggunaan antrian, salah satunya adalah modul queue yang menyediakan beberapa jenis antrian, termasuk:

queue.Queue: Ini adalah jenis antrian umum yang mengimplementasikan FIFO. Anda dapat menggunakannya untuk menyimpan elemen-elemen dalam urutan mereka tiba dan mengeluarkannya dalam urutan yang sama.

queue.LifoQueue: Ini adalah jenis antrian yang mengimplementasikan LIFO (Last-In, First-Out), yang mirip dengan tumpukan. Elemen yang terakhir dimasukkan adalah yang pertama kali diambil.

queue.PriorityQueue: Ini adalah jenis antrian yang mengimplementasikan prioritas. Setiap elemen dalam antrian memiliki nilai prioritas, dan elemen dengan prioritas tertinggi akan diambil terlebih dahulu.

Contoh penggunaan antrian bisa melibatkan mengirimkan pesan antar thread, mengelola tugas dalam program berbasis multithreading, atau mengimplementasikan algoritma seperti BFS (Breadth-First Search) dalam graf atau pohon.

Anda dapat menggunakan modul queue ini untuk memudahkan pengelolaan dan koordinasi data antara thread atau proses dalam program Python Anda.
"""

import time
import threading
import queue


class Worker(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        while True:
            if self.q.empty():
                print("Thread stop!")
                break
            job = self.q.get()
            print(f'run job {str(job)} from {self.name}')
            time.sleep(3)
            self.q.task_done()


q = queue.Queue()

# generate job
print('populate job')
for i in range(15):
    q.put(i)

my_thread1 = Worker('Thread 1', q)
my_thread1.setDaemon(True)
my_thread2 = Worker('Thread 2', q)
my_thread2.setDaemon(True)
my_thread3 = Worker('Thread 3', q)
my_thread3.setDaemon(True)

my_thread1.start()
my_thread2.start()
my_thread3.start()

my_thread1.join()
my_thread2.join()
my_thread3.join()

input('Press enter to stop...\n')
print("Done all")
