class Authentication:
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def login (self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

    def authenticate_account(self, users):
        if self.username in users:
            print("Username already exists!")
            return False
        if len(self.username) < 4:
            print("Username must be at least 4 characters!")
            return False



