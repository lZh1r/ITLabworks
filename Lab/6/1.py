class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_pswd):
        self.__password = new_pswd

    def check_password(self, pswd):
        return self.__password == pswd

a = UserAccount('jeff', 'google@gmail.com', 9999)

print(a.check_password(123456789))

a.set_password(123456789)

print(a.check_password(123456789))