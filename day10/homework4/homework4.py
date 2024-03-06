# მომხმარებელს input-ის გამოყენებით შემოატანინეთ ორი რიცხვითი მნიშვნელობა. შემდეგ if წინადადებით შეამოწმეთ რომელია უდიდესი და გამოიყენეთ for ციკლი: უმცირესიდან უდიდესამდე მოახდინეთ იტერაცია 2-ით და დაპრინტეთ ყველა მნიშვნელობა.

num1=int(input("enter your firsat number: "))
num2=int(input("enter your second number: "))

if num1 > num2:
    for i in range(num2 , num1, 2):
        print(i)
elif num2 > num1:
    for i in range(num1 , num2 , 2):
        print(i)
else:
    print(f"{num1}={num2}")