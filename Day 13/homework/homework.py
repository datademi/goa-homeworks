# 1) დაწერეთ პროგრამა, რომელიც ეკითხება მომხმარებლის ასაკს და შემდეგ დაბეჭდავს შეტყობინებას ასაკის მიხედვით: using(if-elif-else)
# If the age is less than 18, print "You are a minor."
# If the age is between 18 and 65, print "You are an adult."
# If the age is 65 or older, print "You are a senior citizen."

age = int(input("please enter your age"))
if age < 18:
    print("You are a minor")
elif age >= 18 and age <= 65:
    print("You are adult")
else:
    age >= 65 
    print("You are a senior citinez")

# 2) შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ დაბეჭდოს რიცხვი ლუწია თუ კენტი. გამოიყენეთ ფორ ციკლი, რომ სთხოვოთ მომხმარებელს 5 რიცხვი და შეამოწმეთ ხუთივე რიცხვი.

num = int(input("please enter the first number: "))

while num % 2 == 0:
        print(num, "is even: ")
        sum = int(input("please enter the second number: "))
else:
    print(num, "is odd: ")

# 3) დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს ქულები ასოებით (A, B, C, D ან F) და შემდეგ დაბეჭდოს შეტყობინება ასოების მიხედვით: using(if-elif-else)
# If the grade is A, print "Excellent!"
# If the grade is B, print "Good job!"
# If the grade is C, print "You passed."
# If the grade is D, print "You can do better."
# If the grade is F, print "You failed."

grade = input("please enter your grade : ")

if grade == "A":
   print("Excellent")
elif grade == "B":
   print("good job") 
elif grade == "C":
   print("you passed")
elif grade == "D":
    print("you can do better")
elif grade == "F":
   print("you failed") 
else:
   print("try again")
    
# 4) დაწერეთ პროგრამა, რომელიც ბეჭდავს რიცხვებს 1-დან 10-მდე while ციკლის გამოყენებით
sum=0
while sum != 10:
    sum += 1
    print(sum)

     

# 5) შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი 1-დან 10-მდე. გამოიყენეთ while loop, რათა გააგრძელოთ კითხვა, სანამ მომხმარებელი სწორად არ გამოიცნობს
import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    print("Sorry, that's not the correct number. Try again.")

# 6) დაწერეთ პროგრამა, რომელიც დაბეჭდავს მოცემული რიცხვის (მაგ 5) პირველ 10 ჯერადს for loop-ის გამოყენებით.
number = 6
for i in range(1,11):
    result = number * i
    print(result)

# 7) შექმენით პროგრამა, რომელიც ბეჭდავს უკუთვლას 10-დან 1-მდე for loop-ის გამოყენებით.
for i in range(10 , 0, -1):
    print(i)
