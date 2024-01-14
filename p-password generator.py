import random
password_len = int(input("Enter the length of password: "))
chara = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

password = "".join(random.sample(chara,password_len))
print(password)