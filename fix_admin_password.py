from auth.security import SecurityManager
from database.db import get_db
from database.models import User

security = SecurityManager()

with get_db() as db:
    admin = db.query(User).filter(User.username == "admin").first()

    if admin is None:
        print("Admin user not found.")
    else:
        print("Before:", admin.password)

        admin.password = security.hash_password("admin123")

        print("After :", admin.password)