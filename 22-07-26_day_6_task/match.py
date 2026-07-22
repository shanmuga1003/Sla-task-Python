print("Fresh juice shop")
juice = input("Enter the flavour to check the price: ")

match juice:
    case "apple":
        print("apple juice price is 50rps")
    case "orange":
        print("orange juice price is 40rps")
    case "rosemilk":
        print("rosemilk price is 20rps")
    case "grape":
        print("grape juice price is 30rps")
    case "lemon":
        print("lemon juice price is 10rps")
    case _:
        print("This flavour is not available")
