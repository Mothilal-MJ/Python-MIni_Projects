import random

pass_length = int(input("Enter the length of Password : "))
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
password = "".join(random.sample(letters, pass_length))
print(password)