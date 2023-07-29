class Account:
    def __init__ (self, cust_num, u_name):
        self.cust_num = cust_num
        self.u_name = u_name

class Order(Account):
    def __init__ (self, cust_num, u_name, midterm, password, meal_cost, balance):
        super().__init__(cust_num, u_name)
        self.__midterm = midterm
        self.__password = password
        self.meal_cost = meal_cost
        self.balance = balance
    
