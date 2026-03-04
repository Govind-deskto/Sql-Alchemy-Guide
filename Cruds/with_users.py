from Databases import SessionLocal
from models import User

db = SessionLocal()

## db is the session object that we will use to interact with the database.


######### Divng  into CRUD operations using SQLAlchemy ORM  #################


# CREATE
def create_user(name, email):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    print("User created:", user.id)


# READ
def get_users():
    users = db.query(User).all()
    for user in users:
        print(f"{user.id} | {user.name} | {user.email}")


# UPDATE
def update_user(user_id, new_name, new_email):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = new_name
        user.email = new_email
        db.commit()
        db.refresh(user)
        print("User updated")
    else:
        print("User not found")


# DELETE
def delete_user(user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        print("User deleted")
    else:
        print("User not found")


def main():

    while True:

        print("\n1. Read Users")
        print("2. Create User")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        match choice:
            case "1":
                get_users()

            case "2":
                create_user(
                    input("Enter name: "),
                    input("Enter email: ")
                )

            case "3":
                get_users()
                update_user(
                    int(input("Enter user id to update: ")),
                    input("Enter new name: ")
                )

            case "4":
                get_users()
                delete_user(
                    int(input("Enter user id to delete: "))
                )

            case "5":
                print("Exiting...")
                db.close()
                break

            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()

"""
Note : Go and revise the python funadatels and OOPs concepts 
if you dont understand the code above, because this code is based on those concepts, 
and also go and revise SQL as well because whole ORM is based on SQL and how it works,
you will understand it better if you have a good understanding of SQL.

"""


"""
"""