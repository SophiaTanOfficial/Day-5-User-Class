class User:
    def __init__(self, thisUsername, thisEmail, thisPassword, thisAge = "Unknown"):
        self.username = thisUsername
        self.email = thisEmail
        self.password = thisPassword
        self.age = thisAge
        self.mood = "Unknown"
    def status_update(self, mood):
        print(f"I'm feeling {self.mood} today.")
    def change_password(self, oldpass, newpass):
        if oldpass == self.password:
            self.password = newpass
            print("Password change succesful.")
        else:
            print("Incorrect password.")
                