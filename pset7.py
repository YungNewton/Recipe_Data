import math


class Account:
    def __init__ (self, cust_num, u_name):
        self.cust_num = cust_num
        self.u_name = u_name

#your code here
import math


class Order(Account):
    """Subclass of Account representing a student's order."""

    def __init__(self, cust_num, u_name, midterm , meal_cost, password , balance = 0):
        """
        Initialize an Order instance.

        Args:
        cust_num (int): a 4 digit number to store student id. Example: 1000, 1001, 1002
        u_name (str): a string to store student's university name.
                       Only 3 names are allowed: HARVARD, MIT, and OTHERS (all case sensitive).
        midterm (int): the midterm score of a student for CS101.
        meal_cost (float): the cost of the meal purchased.
        password (str): the student's password. If forgotten, set to "0".
        balance (int): the total frequent dining points. Defaults to 0.


        Returns:
        None
        """
        super().__init__(cust_num, u_name)  # Initializing attributes of the parent class
        self.__midterm = midterm
        self.__password = password
        self.meal_cost = meal_cost
        self.balance = balance

    def get_balance(self):
        """Return the frequent dining balance for a student."""
        return self.balance

    def get_midterm(self):
        """Return the midterm score for the student."""
        return self.__midterm

    def get_password(self):
        """Return the password of the student."""
        return self.__password

    def set_midterm(self, score):
        """Set/update the midterm score for the student."""
        self.__midterm = score

    def update_balance(self):
        """Update the frequent dining points for a student after each meal."""
        if self.__password == "0":
            # If student forgot the password, reset the points
            self.balance = 0
        else:
            # Calculating the points based on meal cost
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

# Creating an instance of Order class
order1 = Order(1000, "HARVARD", 50 ,45.0,"password")

# Updating balance
order1.update_balance()

# Printing attributes of order1
print("Balance: ", order1.get_balance())  # Expected Output: 20.0

account = Account(1002, "OTHERS")
print(f"Customer number is: {account.cust_num} \nUniversity: {account.u_name}\n")

# Test Case 2 - Testing frequent dining points for HARVARD student with cust_num =1003,
# u_name = "HARVARD", midterm = 82, meal_cost = 30, password = 'efgh'
harvard_student_order = Order(1003, "HARVARD", 82 , 30 , 'efgh')
harvard_student_order.update_balance()
print(f"The HARVARD student's frequent dining balance = {harvard_student_order.get_balance()}\n")

# Test Case 3 - Testing frequent dining points for OTHER student with cust_num =1004,
# u_name = "OTHERS", midterm = 70, meal_cost = 40, password = 'ijkl'
other_student_order = Order(1004, "OTHERS", 70, 40, 'ijkl')
other_student_order.update_balance()
print(f"The OTHER student's frequent dining balance = {other_student_order.get_balance()}\n")

# Test Case 4 - Testing updating of midterm score
print(f"Before updating: HARVARD student's midterm score = {harvard_student_order.get_midterm()}")
harvard_student_order.set_midterm(90)
print(f"After updating: HARVARD student's midterm score = {harvard_student_order.get_midterm()}\n")

# Test Case 5 - Testing points reset when student forgets password
print(f"Before forgetting password: HARVARD student's balance = {harvard_student_order.get_balance()}")
harvard_student_order = Order(1003, "HARVARD", 90, 30 ,'0',harvard_student_order.get_balance())  # student forgot password
harvard_student_order.update_balance()
print(f"After forgetting password: HARVARD student's balance = {harvard_student_order.get_balance()}\n")