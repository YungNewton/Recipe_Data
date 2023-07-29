class Account:
    def __init__ (self, cust_num, u_name):
        self.cust_num = cust_num
        self.u_name = u_name

class Order(Account):
    def __init__ (self, midterm, password, meal_cost)