class car:

  def __init__(self, year, speed): 
    self.year = year
    self.speed = speed

  def getSpeed(self):
    print("Speed: ", self.speed) 
  def setSpeed(self, speed):
    self.speed = speed
  def getYear(self):
    print("Year: ", self.year)
  def setYear(self, year):
    self.year = year

Ford = car(2021, 130)
Chevy = car(2019, 110)


Ford.getSpeed() 
Chevy.getSpeed()
Ford.setSpeed(120) 
Ford.getSpeed()

class BankAccount:

  #Class Attributes
  name = ""    
  accountNumber = 0
  balance = 0

  def __init__(self, *args):
    if len(args) <3: 
      self.name = "Unknown" 
      self.accountNumber = 1234
      self.balance = 0
    else:
      self.name = args[0]
      self.accountNumber = args[1]
      self.balance = args[2]

  def getName(self):
    return self.name
  def getAcctNum(self):
    return self.accountNumber
  def getBalance(self):
    return self.balance
  def setName(self, name):
    self.name = name
  def setBalance(self, balance):
    self.balance = balance
  def setAcctNum(self, accountNumber):
    self.accountNumber = accountNumber
  def deposit(self, balance):
    self.balance += balance
  def withdraw(self, balance):
    self.balance -= balance
  def toString(self):
    print("Name: " + self.name + "\nAccount Number: " + str(self.accountNumber) + "\nBalance: $" + str(self.balance))

FirstAccount = BankAccount()
TimAccount = BankAccount("Tim", 10012, 1200)
FirstAccount.toString()
print()
TimAccount.toString()
print()
TimAccount.name