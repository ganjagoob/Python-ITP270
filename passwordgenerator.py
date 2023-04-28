#!/bin/python3

def username_generator(first_name, last_name):
    username = ""
    if len(first_name) < 3:
        username += first_name
    else:
        username += first_name[:3]
    if len(last_name) < 4:
        username += last_name
    else:
        username += last_name[:4]
    return username

def password_generator(user_name):
    password = ""
    for i in range(len(user_name)):
        password += user_name[i-1]
    return password

# Test username_generator function
print(username_generator("Justin", "Hua")) # Output: JusHua
print(username_generator("Katelyn", "Bush")) # Output: KatBush
print(username_generator("Abubakarr", "Mansaray")) # Output: AbuMans

# Test password_generator function
print(password_generator("JusHua")) # Output: aJusHu
print(password_generator("KatBush")) # Output: hKatBus
print(password_generator("AbuMans")) # Output: yAbuMan

