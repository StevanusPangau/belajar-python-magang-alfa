import pymongo
import globalVar


class UserModel:
    def __init__(self):
        self.client = pymongo.MongoClient(globalVar.URI_MONGODB)
        self.db = self.client[globalVar.MONGODB_DATABASE_TEST]
        self.users_collection = self.db[globalVar.MONGODB_COLLECTION_USERS]

    def insertUser(self, userData):
        results = {'status': False, 'data': None, 'msg': ''}
        try:
            self.users_collection.insert_one(userData)
            results['status'] = True
        except Exception as error:
            # Biasa saat sudah dalam project perusaahan ini di isi dengan logging
            print(f"usermodel | Error Insert | {error}")
            results['msg'] = "Gagal insert data"

        return results
