import model

user = model.UserModel()

insertResult = user.insertUser({"name": "Stevanus Pangau", "age": 21})
print(insertResult)
