from database import create_db

from user_db import (

    add_user,

    get_all_users,

    find_user_by_email,

    update_user,

    delete_user

)
 
 
def show_users():

    users = get_all_users()
 
    if not users:

        print("❌ No users found")

        return
 
    print("\n--- USER LIST ---")

    for u in users:

        print(f"ID:{u[0]} | Name:{u[1]} | Email:{u[2]} | Age:{u[3]}")
 
 
def main():

    create_db()
 
    while True:

        print("\n===== USER DATABASE MENU =====")

        print("1. Add User")

        print("2. View All Users")

        print("3. Find User by Email")

        print("4. Update User")

        print("5. Delete User")

        print("6. Exit")
 
        choice = input("Enter choice: ")
 
        if choice == "1":

            name = input("Enter name: ")

            email = input("Enter email: ")

            age = int(input("Enter age: "))

            add_user(name, email, age)
 
        elif choice == "2":

            show_users()
 
        elif choice == "3":

            email = input("Enter email: ")

            user = find_user_by_email(email)

            if user:

                print(f"Found → ID:{user[0]}, Name:{user[1]}, Age:{user[3]}")

            else:

                print("❌ User not found")
 
        elif choice == "4":

            email = input("Enter email to update: ")

            new_name = input("Enter new name: ")

            new_age = int(input("Enter new age: "))

            update_user(email, new_name, new_age)
 
        elif choice == "5":

            email = input("Enter email to delete: ")

            delete_user(email)
 
        elif choice == "6":

            print("Exiting program...")

            break
 
        else:

            print("❌ Invalid choice")
 
 
if __name__ == "__main__":

    main()

 
