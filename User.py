# your User class goes here

PEOPLE_NAMES = ["Sky", "Jack", "Casper", "Mike", "Raph"]
PEOPLE_MAILS = ["sky@email.com", "Jack@email.com", "Casper@email.com", "Mike@email.com", "Raph@email.com"]
PEOPLE_DRIVER = ["s12345", "j67890", "c12345", "m67890", "r12345"]

class User():
    # We create a class that uses simple params to emulate a registration
    
    def __init__(self, user_name, user_email_address, user_driver_lic):
        self.name = user_name
        self.email_address = user_email_address
        self.driver_lic = user_driver_lic
    
    def __str__(self):
        return f"NAME: {self.name}, EM: {self.email_address}  DR: {self.driver_lic}"

for x in range(0, 5):
    person = User(PEOPLE_NAMES[x], PEOPLE_MAILS[x], PEOPLE_DRIVER[x])
    print(person)