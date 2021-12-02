from os import name
import re
import sqlite3

class Customers:

    # __email_Id = ""
    # __password = ""
    cursor = ""
    sqlite_connect = ""

    def __init__(self):
        self.sqlite_connect = sqlite3.connect('Users.db')
        self.cursor = self.sqlite_connect.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS customers(SNo INTEGER PRIMARY KEY AUTOINCREMENT, 
                            Name text, EmailId text, Password text, Address text, MobileNo INTEGER)""")
        self.sqlite_connect.commit()

    def addCustomer(self, name, email_Id, password, address, mobileno):
        self.cursor.execute("INSERT INTO customers (Name, EmailId, Password, Address, MobileNo) VALUES (?, ?, ?, ?, ?)",
                             (name, email_Id, password, address, mobileno))
        self.sqlite_connect.commit()

    def signupValidation(self):
        self.cursor.execute("select * from customers")
        result = self.cursor.fetchall()
        emailId_list = []
        for i in result:
            emailId_list.append(i[2])
        return emailId_list
    
    def loginValidation(self):
        self.cursor.execute("select * from customers")
        result = self.cursor.fetchall()
        emailId_list = []
        password_list = [] 
        for i in result:
            emailId_list.append(i[2])
        for j in result:
            password_list.append(j[3])
        data = dict(zip(emailId_list,password_list))
        return data

    def getEmailIdList(self):
        self.cursor.execute("select * from customers")
        result = self.cursor.fetchall()
        emailId_list = [] 
        for i in result:
            emailId_list.append(i[2])
        return emailId_list
    # def setEmailId(self, email_Id):
    #     self.__email_Id = email_Id
    
    # def getEmailId(self):
    #     return self.__email_Id

    # def setPassword(self, password):
    #     self.__password = password
    
    # def getPassword(self):
    #     return self.__password

class Payment(Customers):

    base_bill = 0
    address = ""

    def calculate_base_bill(self):

        self.base_bill = 100

    def validate_base_bill(self):

        if self.base_bill < 100:
            print("Minimum order value not met")

        else:
            pass

    def add_address(self):
        in1 = input()
        self.cursor.execute("INSERT INTO customers (Address) VALUES (?)",
                             (in1))
        self.sqlite_connect.commit()

    def fetch_address(self):
        self.address=self.cursor.fetchone()
        print(self.address)

    def delivery_charge(self):
        pass
    


if __name__ == '__main__':

    customers = Customers()
    payment = Payment()
    flag1 = 1

    while flag1:
        print ("Welcome to ABC Meals")
        print ("1.Sign-Up\n2.Login\n3.Exit")
        in1 = int(input())

        if in1 == 1:
            flag2 = 1
            while flag2:
                print("SIGN-UP PAGE:")
                name = input("Enter your Name: ")
                email_id = input("Enter the Email Id: ")
                pattern = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
                emailId_list = customers.signupValidation()
                if email_id in emailId_list:
                    print("Email-Id already registered")
                else:
                    if re.search(pattern, email_id):
                        password = input("Enter password: ")
                        address = input("Enter your Address: ")
                        mobileno = input("Enter your Contact No: ")
                        customers.addCustomer(name, email_id, password, address, mobileno)
                        print ("Customer Added!!")
                        flag2 = 0
                    else:
                        print("Invalid Email Id")

        if in1 == 2:
            flag3 = 1
            while flag3:
                print("LOGIN PAGE:")
                email_id = input("Email-Id:")
                password = input("Password:")
                data = customers.loginValidation()
                emailId_list = customers.getEmailIdList()
                if email_id in emailId_list:
                    for k,v in data.items():
                        flag4 = 0
                        if k==email_id and v==password:
                            print("Logged In succefully!!")
                            flag3 = 0
                            flag1 = 0
                            flag4 = 1
                            break
                    if flag4==0:
                        print("Incorrect Password!!")
                        flag3 = 0
                else:
                    print("Email-Id not registered")
                    flag3 = 0
        if in1 == 3:
            flag1 = 0 
        
    # payment.add_address()
    
