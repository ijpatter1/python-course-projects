class Master:
    def __init__(self):
        self._protected_name = "Ian Patterson"
        self.__private_password = "1234abcd"
    def getPassword(self):
        print(self.__private_password)
    def setPassword(self,password):
        self.__private_password = password

if __name__ == "__main__":
    a = Master()
    a.getPassword()
    a.setPassword("blueberry")
    a.getPassword()