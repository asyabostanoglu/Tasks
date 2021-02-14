#########################
#Title  : Bank Account
#Author : Asya Bostanoğlu
#Date   : 13.02.2021
#########################


#customer class
class Customer:

#constructor or initializer
    def __init__(self, ID, name, surname, birth_year, TCKN, balance):
        self.ID          = ID
        self.name        = name
        self.surname     = surname
        self.birth_year  = birth_year
        self.TCKN        = TCKN
        self.balance     = balance
 
#function to upload money
    def upload_money(self, money_amount):
        self.balance += money_amount
        print("{} TL successfully deposited to the account!\nNew Balance: {}".format(money_amount, self.balance))
    
#function to withdraw money      
    def withdraw_money(self, money_amount):
        if (self.balance >= money_amount):
            self.balance -= money_amount
            print("{} TL successfully withdrawn!\nNew Balance: {}".format(money_amount, self.balance))
        else:
            print("INSUFFICIENT BALANCE! You cannot withdraw {} TL.\nBalance: {}".format(money_amount, self.balance))

#function to take credit
    def take_credit(self, money_amount):
        self.balance += money_amount
        print("\n{} TL credit taken\nNew Balance: {}".format(money_amount, self.balance))

#output structure
    def show_customer(self):
        
        customer_string = """
        ----------------> CUSTOMER {} <----------------
        Name         : {}
        Surname      : {}
        Birth Year   : {}
        TCKN         : {}
        Balance      : {}  
        """.format(self.ID, self.name, self.surname, self.birth_year, self.TCKN, self.balance)

       
        print(customer_string)

#function the data of the customer be saved as txt file
    def save_customer(self):
        
        customer_string = """
        ----------------> CUSTOMER {} <----------------
        Name         : {}
        Surname      : {}
        Birth Year   : {}
        TCKN         : {}
        Balance      : {}  
        """.format(self.ID, self.name, self.surname, self.birth_year, self.TCKN, self.balance)

        customer_file = open("{}_{}.txt".format(self.ID, self.name), "a")
        customer_file.write(customer_string)
        customer_file.close()

#announce the bank
print("        ------------Welcome to Sample Bank------------")


#create customer
customer1 = Customer(1, "Su", "Akıcı", 1976, 77777777777, 700)
customer2 = Customer(2, "Toprak", "Kök", 1986, 8888888888, 800)
customer3 = Customer(3, "Ateş", "Parlak", 1996, 99999999999, 90)

#driver code
customer1.show_customer()
customer1.upload_money (100)

customer2.show_customer()
customer2.withdraw_money(40)

customer3.show_customer()
customer3.withdraw_money(100)
customer3.take_credit(50)


###################################################################

        





 

