#! /Library/Frameworks/Python.framework/Versions/3.12/bin/python3
"""
Menu driven program
"""


from user_service import add_user, delete_user_by_index, print_users, user_count
import subprocess


def menu():
    print("""
    === Main Menu ===
    0. Exit
    1. Add new user
    2. Search
    3. Edit
    4. Delete
    5. View all
          """)
    
    choice = input("Enter your choice (0-5): ")
    try:
        choice = int(choice)
    except:
        choice = -1

    return choice


def main():
    while True:
        subprocess.run("clear")
        choice = menu()
        if choice == 0:
            print("Thanks for using our app.")
            break

        if choice <0 or choice > 5:
            print("Enter a valid value between 0 and 5.")

        if choice == 1:
            username = input("Enter a user's name: ")
            username = username.strip()
            if len(username) > 0:
                add_user(username)
            else:
                print("Name was not added, since it was empty!")

        if choice == 2:
            print("Search user feature not ready yet")

        if choice == 3:
            print("Edit user feature not ready yet")

        if choice == 4:
            index = int(input("Enter index of the username to delete: "))
            # TODO: handle exception for the above statement
            username = delete_user_by_index(index)
            # TODO: handle exception for the above statement
            print(f'"{username}" deleted from index {index}')

            
        if choice == 5:
            if user_count() == 0:
                print("No users found. Add few users first.")
            else:
                print("Here are the users:")
                print_users()

        input("Hit ENTER/RETURN key to proceed")


if __name__ == '__main__':
    main()
