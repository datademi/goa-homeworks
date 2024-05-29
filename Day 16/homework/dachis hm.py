# # 1) შექმენით ლისტი სადაც ჩამოწერილიქნება თამაშის სახელები და შემდგომ თამაშებს ვანაცვლებთ სოლოლერნით , w3 , codewars - ებით და ასეშემდეგ.
games = ["pubg","cs go","resident evil"]
games[0] = "codewars"
games[1] = "w3"
games[2] = "sololearn"

print(games)

# 2)შექმენით 5 ინფუთი და ამ ინფუთებით შეადგინეთ სია, შემდეგ გამოიტანეთ ამ სიიდან ლუწი რიცხვები, ისე რომ ლოგიკამ ყველა შემთხვევაში იმუშაოს
num1 = float(input("enter your firts number"))
num2 = float(input("enter your second number"))
num3 = float(input("enter your third number"))
num4 = float(input("enter your forth number"))
num5 = float(input("enter your fifth number"))
numbers = [num1 , num2 , num3 , num4 , num5]
for i in range(len(numbers)):
   if numbers [i] % 2 == 0:
       print(numbers[i])

