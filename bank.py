# create a parent class
#create a method or function to hold our user details
#create our first user and print it's details
#create a child class which will inherit from the parent class
#create a method/function on user's withdrawal and deposit
#create our second user 
#print number of users

# parent class 
class User:
    no_of_user = 0
    acc_num = 110023


    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.cus_acc_number = User.acc_num 

        User.no_of_user = User.no_of_user +1 
        User.acc_num = User.acc_num + 1 

# method/function to hold user detals
    def user_details(self):
        print(f'user: {self.name}\t age: {self.age}\t accunt number: {self.acc_num}\t gender:{self.gender}')
        

user1 = User('tim', 23, 'female')
user1.user_details()

# child class
class Bank(User):
    def __init__(self, name,age ,gender):
        super().__init__(name, age, gender)
        self.account_balance = 0
        


# details about the current amount and deposit
    def deposit(self):
        amount = int(input('How much do you ant to deposit? : '))
        print()
        self.account_balance = self.account_balance + amount 
        if amount > 0:
            print('Your current account balance is  $', self.account_balance)
        else:
            print('invalid transaction.....')
# withdrawals 
    def withdrawal(self):
        amount = int(input('How much do yu want to withdraw?: '))
        print()
        if amount <= self.account_balance:
            self.account_balance = self.account_balance - amount
            print(f'transaction successful. Current amount is  ', self.account_balance )
        else:
            print('insufficient funds. curent amount is ', self.account_balance  )
            


user2 = Bank('muna', 53, 'male', )
print(user2.user_details())
print()
print('Number of user/users, is/are:', User.no_of_user)
print(" ")
print(user2.deposit ())
print(user2.withdrawal ())
#print('Number of user/users, is/are', BankUser.no_of_user)


