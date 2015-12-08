print ("************************************************************************")
print ("                  Hello and welcome to RAM Hacks ATM")
print ("                NOTICE: This ATM has a $0.50 surcharge")
print ("************************************************************************")
Balance = input ("Please enter account ballence: $ ")
withdrawalAmount = input ("Please enter withdrawal amount: $ ")
afterWithdrawal = Balance-withdrawalAmount-0.50
if (Balance >= 2000 or withdrawalAmount >= 2000):
  print ("Our banks maximum tranaction is capped at is $2000.00")
else:
  if (withdrawalAmount < 0 or withdrawalAmount % 5 != 0):
    print ("This ATM can only make withdrawals in multiples of five")
  else:
    if (afterWithdrawal > 0):
      print ("\tYour remaining balence is $"), afterWithdrawal
    else:
      print("\tI'm sorry, your balance is too low")
      print ("\t\tYour current ballance is: $"), Balance
print ("************************************************************************")
print("                     Thank you for your bussiness!")
print("                        Please take your receipt")
print ("************************************************************************")
