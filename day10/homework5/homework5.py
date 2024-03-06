num5=int(input("enter your first number: "))
num6=int(input("enter your second number: "))
sum = 0
if num5 > num6:
    for i in range(num6 , num5 + 1):
        sum += i
elif num6 > num5:
    for i in range(num5 , num6 + 1):
        sum += i 
else:
    print(f"{num5}={num6}")
print(sum)