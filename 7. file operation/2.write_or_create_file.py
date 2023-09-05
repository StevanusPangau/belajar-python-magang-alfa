file = open('/Users/stevanuspangau/Development/Magang Alfamart/Belajar/Python 2023/7. file operation/demoFile.txt', 'a')
file.write("\n\nNow the file has more content!")
file.close()

file = open('/Users/stevanuspangau/Development/Magang Alfamart/Belajar/Python 2023/7. file operation/demoFile.txt', 'r')
print(file.read())
