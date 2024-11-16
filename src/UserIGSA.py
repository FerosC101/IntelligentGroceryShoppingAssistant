class UserIGSA:
    def __init_(self):
        pass


    def menu(self):
        while True:
            print("Welcome to Intelligent Grocery Shopping Assistant!")
            print("1. How to use.")
            print("2. Login.")
            print("3. Register.")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.introduction()
            elif choice == 2:
                self.login()
            elif choice == 3:
                self.register()
            elif choice == 4:
                exit()
            else:
                return "Invalid choice"

    def introduction(self):
        pass

    def login(self):
        pass

    def register(self):
        pass