import random

lower = "abcdefghijklmnopqrstuvwxyz"

upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

NUMBER = "0123456789"

Symbol = "[]{}#()*;-_-"

all=lower + upper + NUMBER + Symbol

length = int(input("Enter length of password:"))

password = "".join(random. sample (all  ,length)) 
print(" The Password You Generated is :",password)
