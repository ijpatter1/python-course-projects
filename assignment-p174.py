

class User:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def displayUser(self):
        print(f"\nName: {self.fname} {self.lname}\nEmail: {self.email}")

class Customer(User):
    def __init__(self, fname, lname, email, address, mailing_list):
        super().__init__(fname, lname, email)
        self.address = address
        self.mailing_list = mailing_list
    def mailingList(self):
        if self.mailing_list:
            print(f"{self.fname} has subscribed to the mailing list!")
        else:
            print(f"{self.fname} has not subscribed to the mailing list.")

class Employee(User):
    def __init__(self, fname, lname, email, salary, department):
        super().__init__(fname, lname, email)
        self.salary = salary
        self.department = department
    def getSalary(self):
        print(f"{self.fname} makes ${self.salary}. You go, {self.fname}!")

user1 = User("Ian", "Patterson", "ian@email.com")
user1.displayUser()

customer1 = Customer("Jeff", "Bridges", "jbridges@email.com", "Walker Ave", True)
customer1.displayUser()
customer1.mailingList()

employee1 = Employee("Bob","Jones","bejones@email.com", 50000, "Sales")
employee1.displayUser()
employee1.getSalary()

