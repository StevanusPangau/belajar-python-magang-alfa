# def fungsi(*args, **kwargs):
#     return args, kwargs


# a = (3, 2, 1)

# hasil, resultD = fungsi(*a, b=3, d=6)
# print(hasil)
# print(resultD)

def suatufungsiE(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)
    # print(kwargs["angka1"])
    # print(kwargs["angka2"])
    # print(kwargs["angka3"])

    # for key, val in kwargs.items():
    #     print(key, " = ", val)


c = {"angka1": 1, "angka2": 2, "angka3": 3}

suatufungsiE("hallo", b=5, **c)
