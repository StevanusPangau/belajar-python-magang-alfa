# # contoh single line comment
# a = """
# Contoh Multiline
# Hello World
# """

# print(a)
# print("Hello World")

# name = "Packing Box"
# width = 10
# height = 20.5

# print(name)
# print(width)
# print(height)

# x = 10.5
# y = 5
# print(x + y)
# print(int(x) + y)

# a = "Hello"
# b = "World"

# print(a + b)

# nik = "123456"
# query = """SELECT * FROM mahasiswa
#             WHERE nik = """ + nik
# print(query)

# a = "Hello World"
# print(a[-1])

# a = "{} {}".format("Hello", "World")
# print(a)

# x = "Hello"
# y = "World"
# b = f"{x} {y}"
# print(b)

# a = "{:k} {:l}".format({'k': 'Hello', 'l': 'World'})
# print(a)

for index in range(1, 12):
    data = ''
    name = 'user ' + str(index-1)
    email = 'user' + str(index-1) + '@email.com'
    if index == 1:
        data = '{0:3s} {1:10s} {2:15s}\n'.format('No', 'Name', 'Email')
    else:
        data = '{0:3s} {1:10s} {2:15s}\n'.format(str(index-1), name, email)

    print(data)
