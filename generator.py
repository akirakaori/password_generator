import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

let= int(input("How may letters would you like to have in your password?\n"))
symb=int(input("Hoy many symbols you like to use in your password?\n"))
num =int(input("How many numbers would you like to have in your password?\n"))

password_list=[]

for char in range(1,let+1):
    password_list.append(random.choice(letters))
for char in range(1,symb+1):
    password_list.append(random.choice(symbols))
for char in range(1,num+1):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)

password=" "
for char in password_list:
    password+=char
print(f"Your password is{password}")