user_name = "shanmuga"
password = "sha@03"
one_time_pwd = 1234

uname = input("Enter username : ")
if user_name == uname:
    pwd = input("Enter password : ")
    if password == pwd:
        otp = int(input("Enter OTP : "))
        if one_time_pwd == otp:
            print("login successful")
        else:
            print("invalid OTP")
    else:
        print("invalid password")
else:
    print("invalid username")
