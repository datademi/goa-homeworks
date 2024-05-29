# დაწერეთ ალგორითმი რომელიც დაბეჭდავს დადებითია, უარყოფითი თუ ნულის ტოლი მომხმარებლის მიერ შემოტანილი რიცხვი.

print("if u type number 0 u will get out for program")

while True:
    num = int(input("type a number: "))
    if num >=1:
        print("u have chosen positive number: ")
        num = int(input("type a number: "))
    if num <= -1:
        print("u have chosen negative number: ")
        num = int(input("type a number: "))
    if num == 0:
        print("u have chosen zero: ")
        break


# დაწერეთ ალგორითმი რომელიც მომხმარებელს შეთავაზებს ორ ოპერაციას: კილომეტრი - მილი, მილი - კილომეტრი. მომხმარებელმა უნდა აირჩიოს ერთ-ერთი მათგანი, ხოლო შემდეგ შეეკითხეთ რიცხვითი მნიშვნელობა, რომელზეც მოახდენთ მუშაობას და საბოლოოდ დაუბეჭდეთ უკვე გადაყვანილი მნიშვნელობა. თუ მომხმარებელი სწორად არ აირჩევს ოპერაციას, დაბეჭდეთ "Wrong decision".

ask = input("which operation do u want m or km: ")

number = int(input("enter some number"))

if ask == "m":
    print(int(number * 1.6))

elif ask == "km":
    print(int(number * 0.62))

# შექმენით რეგისტრაციის ალგორითმი. მომხმარებელს შეეკითხეთ სახელი, გვარი, ასაკი და მეილი, საბოლოოდ კი ერთ წინადადებაში გამოიტანეთ მიღებული ინფორმაცია.

print("registration")

#person name
name = input("type your first name? : ")
#person last_name
last_name = input("type your last name? : ")
#person age
age = input("choose your age? : ")
#preson email
email = input("type your email: ")
print(" Your name is " + name + " your last_name is " + last_name, " your age is " + age + " your email is " + email,)

# მომხმარებელს სამჯერ შეეკითხეთ რიცხვითი მნიშვნელობა და დაბეჭდეთ მათი საშუალო არითმეტიკული.

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

print((num1 + num2 + num3)/ 3)

# მომხმარებელს შეეკითხეთ 1-იდან 9-ის ჩათვლით რომელიმე რიცხვი. შემდეგ გამოიყენეთ for ციკლი და გამოიტანეთ ამ რიცხვის ჯერადები 1-იდან 50-მდე დიაპაზონში.

num = int(input("enter number from 1 to 10: "))
for i in range(1, 51):
    if i % num==0:
        print(i)

# მომხმარებელს შემოატანინეთ ორი რიცხვი. შემდეგ მათ შორის უმცირესი for ციკლში საწყის, ხოლო უდიდესი საბოლოო მნიშვნელობად გამოიყენეთ. ციკლში იტერაცია მოახდინეთ ერთით და გამოიტანეთ საიტერაციო ცვლადის მესამე ხარისხი (კუბი).

num1 = int(input("type small number: "))

num2 = int(input("type big number: "))

for i in range(num1, num2 + 1):
    print(i ** 3)

# მომხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ მისი ციფრთა ჯამი.
    
number = input("Enter a number: ")

digit_sum = sum(int(digit) for digit in number if digit.isdigit())

print("The sum of digits in the number is:", digit_sum)

# დაწერეთ პროგრამა, რომელიც იღებს მომხმარებლისგან მთელ რიცხვს და დაბეჭდავს მის გამრავლების ცხრილს 10-ის ჩათვლით. მაგ: x, x2, x3 ... x*10.

number = int(input("enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# second way

# num = (input("Enter a number: "))

# length = len(num)

# numbers_sum = 0
# for i in range(length):
#     numbers_sum = numbers_sum + int(num[i])

# print(numbers_sum)

# შექმენით კალკულატორი, სადაც გექნებათ ოთხი ოპერაცია: + - / და გამრავლება (ფიფქი არ იწერება). მომხმარებელს შეეკითხებით ორ რიცხვს, შემდეგ სასურველ ოპერაციას და დაუბეჭდავთ გამოთვლილ მნიშვნელობას.
    

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


operation = input("Choose operation (+, -, *, /): ")


if operation in ['+', '-', '*', '/']:
    result = eval(f"{num1} {operation} {num2}")
    if operation == '/' and num2 == 0:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"

print("Result:", result)

# დაწერეთ პროგრამა, რომელიც იღებს სთრინგს, შემდეგ მომხმარებელს ეკითხება თუ რამდენჯერ განმეორდეს და for ციკლის გამოყენებით დაბეჭდეთ ის.

string = input("Enter a string: ")
count = int(input("How many times to repeat? "))

for _ in range(count):
    print(string)

# დაწერეთ პროგრამა, რომელიც გამოთვლის სხეულის მასის ინდექსს (BMI), მომხმარებლისგან მიღებული წონის (კილოგრამებში) და სიმაღლის (მეტრებში) გათვალისწინებით.

weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

bmi = weight_kg / (height_m ** 2)

print("Your Body Mass Index (BMI) is:", bmi)

# მომხმარებელს შემოატანინეთ წელი და შეამოწმეთ ის ნაკიანი არის თუ არა.

user_year = int(input("Enter a year: "))


if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
    print("Leap year!")
else:
    print("Not a leap year.")

# მომხმარებელს შეეკითხეთ სამი რიცხვი და შეამოწმეთ არიან თუ არა პითაგორას რიცხვები.

a, b, c = map(float, input("Enter three numbers separated by spaces: ").split())

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("The numbers form a Pythagorean triplet.")
else:
    print("The numbers do not form a Pythagorean triplet.")

# დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი 1-დან 5-ის ჩათვლით. თუ რიცხვი არის 1-ზე ნაკლები ან 5-ზე მეტი, დაბეჭდეთ "Invalid input". თუ რიცხვი 1-დან 5-ის ჩათვლითაა, დაბეჭდეთ "Valid input".

number = int(input("Enter a number from 1 to 5: "))

if 1 <= number <= 5:
    print("Valid input")
else:
    print("Invalid input")