from src.models.UserProfile import UserProfile
from src.database.Db_manager import createConnection

class Main:
    def __init__(self, db: createConnection):
        self.db = db
        self.user_profile = UserProfile(self.db)

    def menu(self) -> None:
        while True:
            try:
                print("[1] Register")
                print("[2] Manual")
                print("[3] Exit")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    pass
                elif choice == 2:
                    pass
                elif choice == 3:
                    exit(0)
                else:
                    print("Invalid Input")
            except  ValueError as e:
                print(e)

    def register(self):
        while True:
            try:
                print("Input details to continue")
                print("Enter name: ")
                name = input()
                print("budget: ")
                budget = float(input())
                print("Dietary Preference: ")
                preference = input()

                user_id = self.user_profile.create_user(name, budget, preference)
                if user_id:
                    print(f"User created successfully. User ID: {user_id}")
                    break
                else:
                    print("Registration failed")

            except ValueError as e:
                print(e)


