import random 
def password():
 upper_letters = "ASDFGHJKLZXCVBNMQWERTYUIOP"
 lower_letters = upper_letters.lower()
 digits = "1234567890"
 symnols = "#@!%^&*"":\;/?.,-_=+"

 upper , lower , nums , syms = True,True,True,True

 all = ""

 if upper :
    all += upper_letters

 if lower :
    all += lower_letters

 if upper :
    all += digits

 if upper :
    all += symnols
 try:
  lenght_ask = int(input ("What is the length of your password (how many charicters):"))
  amount_ask = int (input("enter how many passwords you want:"))
  lenght = lenght_ask
  amount = amount_ask
 except:
   print ("Something went wrong or your password is to large.")
   
   

 for x in range(amount):
    password ="".join(random.sample(all , lenght))
    print (password)
password()