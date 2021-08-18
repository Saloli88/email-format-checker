import re
class Checker:
    def __init__(self,check_email):
        self.check_list = check_email
    def checking(check_email):
        return re.match(r"^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$",check_email)
while True:
    email = input("Email Adress (@ and .com required, cant contain symbols (!#$%&...)):")
    check = Checker.checking(email)
    if check:
        print(f"{email} is correct")
        break
    else:
        print("Email is not valid, please try again.")
        continue