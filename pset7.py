import math


class Account:
    def __init__ (self, cust_num, u_name):
        self.cust_num = cust_num
        self.u_name = u_name

class Order(Account):
    def __init__ (self, cust_num, u_name, midterm , meal_cost, password , balance = 0):
        super().__init__(cust_num, u_name)
        self.__midterm = midterm
        self.__password = password
        self.meal_cost = meal_cost
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    def get_midterm(self):
        return self.__midterm
    def get_password(self):
        return self.__password
    def set_midterm(self, score):
        self.__midterm = score
    def update_balance(self):
        if self.__password == '0':
            self.balance = 0
        else:
            points = 0
            extraPoints = 5 * (math.floor((self.meal_cost - 15) / 15))
            if self.meal_cost >= 15:
                points += 10
                points += extraPoints
                if self.u_name == "HARVARD":
                    points += 5
                    if self.__midterm >= 80:
                        points += 3
                elif self.u_name == "MIT":
                    points += 3
                self.balance += points


import numpy as np
test3 = (1002, 'MIT', 89, 0, "9879")
meal_costs = np.arange(0, 300, 100) 

order = Order(test3[0],test3[1],test3[2],test3[3],test3[4])
order.update_balance()

for meal_cost in meal_costs:
    order.meal_cost = meal_cost
    order.update_balance()
    print(f"Balance with meal cost {order.meal_cost} is: {order.get_balance()}")