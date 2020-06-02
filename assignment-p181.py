

class User:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def displayInfo(self):
        print(f"\nName: {self.fname} {self.lname}\nEmail: {self.email}")

class Customer(User):
    def __init__(self, fname, lname, email, address, mailing_list):
        super().__init__(fname, lname, email)
        self.address = address
        self.mailing_list = mailing_list
    def displayInfo(self):
        print(f"\nName: {self.fname} {self.lname}\nEmail: {self.email}\nAdress: {self.address}")
        if self.mailing_list:
            print(f"{self.fname} is subscribed to the mailing list!")
        else:
            print(f"{self.fname} is not subscribed to the mailing list.")

class Employee(User):
    def __init__(self, fname, lname, email, salary, pin):
        super().__init__(fname, lname, email)
        self.salary = salary
        self.pin = pin
    def displayInfo(self):
        entry_pin = input("\nEnter pin to access employee information: \n>>>")
        if entry_pin == self.pin:
            print(f"\nName: {self.fname} {self.lname}\nEmail: {self.email}\nSalary: {self.salary}")
        else:
            print("Incorrect Pin")

user1 = User("Ian", "Patterson", "ian@email.com")
user1.displayInfo()

customer1 = Customer("Jeff", "Bridges", "jbridges@email.com", "Walker Ave", True)
customer1.displayInfo()

employee1 = Employee("Bob","Jones","bejones@email.com", 50000, "1234")
employee1.displayInfo()

