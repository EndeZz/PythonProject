from db.DB import DB

db = DB()

users = db.getAllUsers()

print(users)
