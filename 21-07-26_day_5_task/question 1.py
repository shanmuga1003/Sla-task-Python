print("PS5 Game Station")
print("Price")
print("1. 70 rps for 1 person, 1 TV, for 1 hour.")
print("2. 60 per person for 2 or 3 people, 1 console, for 1 hour.")
print("3. 50 per person for 4 people, 1 console, for 1 hour.")
print("------------------------------------------")
per = int(input("Enter number of person(1 to 4) : "))
hour = int(input("Enter number of hour : "))

if per == 1:
    print(70 * hour)
elif per == 2 or per == 3:
    print(60 * per * hour)
elif per == 4:
    print(50 * per * hour)
else:
    print("not more than 4 person can book a single console")
