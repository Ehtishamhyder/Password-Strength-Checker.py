# password strength checker
# input password

from unittest import skip


print("              Welcome to the Password Strength Checker!              ")

password = input("Enter your password: ")
# check password strength

# function to check for sequential patterns in numeric passwords
def is_sequential(password):
    if not password.isdigit():
        return False
    increasing = True
    decreasing = True

    for i in range(len(password) - 1):
        if int(password[i]) + 1 != int(password[i + 1]):
            increasing = False
        if int(password[i]) - 1 != int(password[i + 1]):
            decreasing = False
    return increasing or decreasing        
if is_sequential(password):
  print("Password is very weak (sequential pattern)")
  print("Password strength is 10%")


# function to check length based strength instead of sequential patterns
else:

  if len(password) <= 6:
        print("Password is weak")
        print("Password strength is 30%")
  elif len(password) <= 10:
        print("Password is medium")
        print("Password strength is 60%")
  elif len(password) <= 12:
     print("Password is above average")
     print("Password strength is 70%")
  elif len(password) >= 13 and password.isdigit():
     print("Password is strong")
     print("Password strength is 80%")
  elif len(password) >= 12 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for c in password):
     print("Excellent! Password is extremely strong")
     print("Password strength is 100%")

