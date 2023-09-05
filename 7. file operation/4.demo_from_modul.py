#####################################
print('creating files...')
# create a file.
# Jika file sudah ada, maka file tersebut akan di hapus dan dibuatkan yang baru (w)
f1 = open('mydoc1', 'w')

# create a file.
# Jika file sudah ada, maka file tersebut tidak akan di ganti tapi di tambahkan di dalam filenya (a)
f2 = open('mydoc2', 'a')

# binary files
bf1 = open('mydoc3', 'wb')
bf2 = open('mydoc4', 'ab')

#######################################
# writing data

print('writing data into file')
for index in range(1, 12):
    data = ''
    name = 'user ' + str(index-1)
    email = 'user ' + str(index-1) + '@gmail.com'

    if index == 1:
        data = '{0:3s} {1:10s} {2:15s}\n'.format('No', 'Name', 'Email')
    else:
        data = '{0:3s} {1:10s} {2:15s}\n'.format(str(index-1), name, email)

    f1.write(data)
    f2.write(data)
    bf1.write(data.encode())
    bf2.write(data.encode())

#######################################
# close all file
print("close file")

f1.close()
f2.close()
bf1.close()
bf2.close()
