#მომხმარებელს შემოატანინეთ ხუთი რიცხვი და ყველა შეიტანეთ სიაში. თქვენი დავალებაა, რომ დაბეჭდოთ ამ სიის ჯამი, არ გამოიყენოთ sum მეთოდი.
num1 = float(input("enter your firts number"))
num2 = float(input("enter your second number"))
num3 = float(input("enter your third number"))
num4 = float(input("enter your forth number"))
num5 = float(input("enter your fifth number"))
numbers = [num1 , num2 , num3 , num4 , num5]

sum_of_numbers = [num1 + num2 + num3 + num4 + num5]
print(sum_of_numbers)


#სიაში შეიტანეთ თქვენთვის სასურველი 10 რიცხვი. დაბეჭდეთ ამ სიაში არსებული ყველაზე დიდი რიცხვი, მინიშნება: გამოიყენეთ for ციკლი. არ გამოიყენოთ max მეთოდი.
numbers = [6 , 7, 3 , 13 , 7 , 9 , 78 , 9 , 56 , 59]

 
for num in numbers:
    if num >= 78:
        print(num)
    
    
# სიაში შეიტანეთ 30-იდან 50-ის ჩათვლით არსებული ყველა რიცხვი. შემდეგ დაითვალეთ ამ სიაში არსებული კენტი რიცხვები და დაბეჭდეთ მათი რაოდენობა.
numbers = []
even_numbers = []
for i in range(30 , 50+1):
 if i % 2 == 1:
     even_numbers.append(i)
 
print(len(even_numbers))

#სიაში შეიტანეთ 10-იდან 50-ის ჩათვლით არსებული 4-ის ჯერადი რიცხვები. შემდეგ შეაბრუნეთ ეს სია და დაბეჭდეთ ის, test case: [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]
numbers = [12,16,20,24,28,32,36,40,44,48]
numbers.reverse()
print(numbers)
#თქვენი დავალებაა, რომ სიაში შეიტანოთ 50-იდან 100-მდე არსებული ყველა რიცხვი. შემდეგ გამოიყენეთ for ციკლი და დაბეჭდეთ ყველა ლუწი რიცხვი  მათი ინდექსებით. test case: ["50 - 0", "52 - 3", "54 - 5", "56 - 7"]

numbers = []


for i in range(50,100+1):
    numbers.append(i)

even_numbers = []

for index in range(0, len(numbers)):
    if numbers[index] % 2 == 0:
        even_numbers.append(str(numbers[index]) + "-" + str(index))

print(numbers)
print(even_numbers)