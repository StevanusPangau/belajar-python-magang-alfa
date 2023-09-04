import time

# ambil waktu sekarang
now = time.time()
print(now)

# menunjukan waktu saat ini yang dapat dibaca dengan format
print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(now)))
print(time.timezone)
