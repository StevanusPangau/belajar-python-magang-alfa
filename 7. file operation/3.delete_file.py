# import os
# os.remove("demofile.txt")

import os
if os.path.exists("/Users/stevanuspangau/Development/Magang Alfamart/Belajar/Python 2023/7. file operation/demoFile2.txt"):
    os.remove("/Users/stevanuspangau/Development/Magang Alfamart/Belajar/Python 2023/7. file operation/demoFile2.txt")
    print("delete file success")
else:
    print("The file does not exist")
