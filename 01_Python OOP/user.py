class User:
    def __init__(self, username, email, password):
        self.username = username
        # self.__email = email
        self._email = email
        self.password = password

    def say_hi_to_user(self, user):
        print(
            f"Sending message to {user.username}: Hi {user.username}, its {self.username}."
        )

    # Accessing and Modifying Data
    # 1. The traditional way: make data private and use getters and setters:
    # prefix data field (email) with '__' name mangling
    #def get_email(self):
    #    return self.__email

    #def set_email(self, new_email):
    #    self.__email = new_email


    # 2. Use of Properties
    @property
    def email(self):
        print("Email accessed")
        return self._email

user1 = User("Batman", "batman@gotham.com", "imB@tman")
user2 = User("Robin", "robin@gotham.com", "r0bin")

# user1.say_hi_to_user(user2)

#print(user1.get_email())
#user2.set_email("sample@email.com")
#print(user2.get_email())

print(user1.email)