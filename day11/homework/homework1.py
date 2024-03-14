# Timer: დაწერეთ პროგრამა, რომელიც ითვლის 10-დან 1-მდე, დაბეჭდავს თითოეულ რიცხვს და შემდეგ დაბეჭდავს "დრო ამოიწურა".

i = 1+1
sum = 10

while i <= 10:
    print(sum)
    i = i + 1
    sum = sum - 1
    
print("Time out: ")

# რიცხვების ჯამი: დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვებს განუწყვეტლივ, სანამ ისინი არ შეიყვანენ 0-ს. შემდეგ დაბეჭდეთ ყველა შეყვანილი რიცხვის ჯამი.

i = 500
sum = 0


while i >= 0:
    print(sum)
    i = i - 1
    sum = sum + 1

# რიცხვების ჯამი: დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვებს განუწყვეტლივ, სანამ ისინი არ შეიყვანენ 0-ს. შემდეგ დაბეჭდეთ ყველა შეყვანილი რიცხვის ჯამი.

num = 1
num_3 = 0

while num != 0:
    num = int(input("type a number: "))
    num_3 += num
    

print(num_3)

# პაროლის შემოწმება: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. განაგრძეთ კითხვა, სანამ სწორი პაროლი არ იქნება შეყვანილი. დავუშვათ, რომ სწორი პაროლი არის "12345678".

password = (input("please enter the password: "))

while password == "12345678":
    print("passrowd was correct")
    password = (input("please enter the password: "))
else:
    print(f"u have typed the wrong password")
    password = (input("please enter the password: "))

# ლუწი რიცხვები: დაწერეთ პროგრამა, რომელიც ბეჭდავს ყველა ლუწ რიცხვს 0-დან 20-მდე while ციკლის გამოყენებით.

i = 11
sum = 0

while i >= 1:
    print(sum)
    i = i - 1
    sum = sum + 2

# დადებითი რიცხვები: შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს უწყვეტად შეიყვანოს დადებითი რიცხვები, სანამ ისინი უარყოფით რიცხვს არ შეიყვანენ. შემდეგ დაბეჭდეთ ყველა შეყვანილი დადებითი რიცხვის ჯამი. (edited)

num = int(input("please type a number: "))



while num % 2 == 0:
        print(num, "is even: ")
        num = int(input("please type a number: "))
else:
    print(num, "is odd: ")
   

# ტემპერატურის კლასიფიკაცია: შექმენით პროგრამა, რომელიც მომხმარებელს სთხოვს ტემპერატურას ცელსიუსში. შემდეგ დაბეჭდეთ ცხელი (> 30°C), თბილი (20-30°C) ან ცივი (<20°C).

num = int(input("tell us tempeture in Celsius: "))

while num == 30:
    print("the tempeture is hot")
    num = int(input("tell us tempeture in Celsius: "))
if num <= 30:
    print("the tempeture is warm")
    num = int(input("tell us tempeture in Celsius: "))
elif num <=20:
    print("the tempeture is cold")
    num = int(input("tell us tempeture in Celsius: "))


# ასოების შეფასება: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს გამოცდის ქულას. შემდეგ დაბეჭდეთ მათი ასოების შეფასება შემდეგი სკალის მიხედვით: A (90-100), B (80-89), C (70-79), D (60-69), F (< 60).

score = int(input("enter your score: "))


while score >= 90 or score >= 100 :
    print("u got a A")
    score = int(input("enter your score: "))

if score >= 80 or score >= 89:
    print("u got a B")
    score = int(input("enter your score: "))
elif score >= 70 or score >= 79:
    print("u got a D")
    score = int(input("enter your score: "))
else:
    print(f"{60 <=60}u got a F")
    score = int(input("enter your score: "))

# შეამოწმეთ გაყოფა: შექმენით პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვს. შემდეგ დაბეჭდეთ, იყოფა თუ არა 2-ზე, 3-ზე ან ორივეზე.



num = int(input("type a number: "))

while num % 2 == 0:
    print(num, "it divides on two: ")
    num = int(input("type a number: "))

if num % 3  == 0:
    print(num, "it divides on three")
    num = int(input("type a number: "))

elif num % 2 == 0 and num % 3 == 0:
    print("it divides on two and three")
    num = int(input("type a number: "))

# რიცხვების შედარება: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს ორ რიცხვს და შეადარებს მათ.

num1 = int(input("type a frist number: "))

num2 = int(input("type a second number: "))

while num1 <= num2:
    print("num2 is bigger than num1: ")
    num1 = int(input("type a frist number: "))
    num2 = int(input("type a second number: "))
if num1 >= num2:
    print("num1 is bigger than num2: ")
    num1 = int(input("type a frist number: "))
    num2 = int(input("type a second number: "))
elif num1 == num2:
    print("num1 and num2 are equal: ")
    num1 = int(input("type a frist number: "))
    num2 = int(input("type a second number: "))

# რიცხვის გამოცნობა: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი (მაგ., 5, ეს რიცხვი თქვენ აირჩიეთ). განაგრძეთ კითხვა, სანამ არ გამოიცნობენ სწორად.
 
num = int(input("type a number thought 1 to 10"))

sum = ("u have guessed the number")

while num >= 0:
    print(num)
    num = int(input("type a number thought 1 to 10"))
    if num == 5:
        print(sum)
        break

# რიცხვების შემოწმება: შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს რიცხვს. სანამ ეს რიცხვი არ იქნება ლუწი, შეეკითხეთ მომხმარებელს თავიდან.

num = int(input("type a number: "))

while num % 3 == 0:
    print(num, "it is odd try again: ")
    num = int(input("type a number: "))
    if num % 2 == 0:
        print(num, "it is even u got it right")
        num = int(input("type a number: "))
        break

# რიცხვების კლასიფიკაცია: შექმენით პროგრამა, სადაც 50-იდან 100-ის ჩათვლით გამოიტანთ კენტ რიცხვებს. ციკლის გარეთ შექმენით ჯამის ცვლადი, სადაც დაემატება ციკლის ის რიცხვები, რომლებიც მეტია 75-ზე. ბოლოს დაპრინტეთ ამ ცვლადის მნიშვნელობა

def Odd_num(start,end):

    for i in range(start, end+1):
        if(i%2==1):
            print(i)
Odd_num(50,100)
Odd_num=(50,100)
num=50
for i in range(50,101):
    if(i%2==1):
        print(i)

# რიცხვების შედარება: მომხმარებელს შეეკითხეთ რიცხვი. სანამ ის ნაკლები იქნება მასზე 20-ით დიდ რიცხვზე, დაპრინტეთ ის და მასზე მოახდინეთ იტერაცია 1-ით.
        
num = int(input("enter your number: "))
while num < num + 20:
    print(num)
    num1=int(input("enter your number: "))
    if num1 > num + 20:
        break

# სახელის გამოცნობა. შექმენით ცვლადი სადაც იქნება შენახული თქვენი სახელი. მომხმარებელს შეეკითხეთ სახელი და სანამ თქვენსას არ შემოიტანს თავიდან შეეკითხეთ.
    
name = "data"
name1 = input("Enter Name: ")
while name1 != name:
    print("Error")
    name1=input("Enter Name: ")
    if name1 == name:
        print("You are right")

    break






