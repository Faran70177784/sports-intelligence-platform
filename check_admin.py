from database.db import get_db
from database.models import User

with get_db() as db:
    user = db.query(User).filter(User.username == "admin").first()

    if user is None:
        print("Admin user NOT found.")
    else:
        print("Username:", user.username)
        print("Role:", user.role)
        print("Password:", user.password)