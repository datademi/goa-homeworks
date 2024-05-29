enter_age=int(input("please enter your age: "))

if enter_age >= 0 and enter_age < 18:
    print("you are child")
elif enter_age >= 18 and enter_age < 50:
    print("you are adult")
else:
    print("you are old")


    number = float(input("Please enter number: "))

if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is 0")