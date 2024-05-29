# ნამრავლის გამოთვლა: დაწერეთ ალგორითმი, რომელიც დაბეჭდავს სიის ყველა ელემენტის ნამრავლს.
list = [10,10,15,15,15,15,15,15]

Multiplied_numbers =  1

for i in list:
  Multiplied_numbers *= i


print(Multiplied_numbers)

    
# უარყოფითი რიცხვების ამოღება: დაწერეთ ალგორითმი, რომელიც მიიღებს მთელ რიცხვთა სიას და ამოიღებს ყველა უარყოფით რიცხვს, დაბეჭდავს ახალ სიას ამ ელემენტების გარეშე.

def remove_negatives(numbers):
    non_negatives = []
    for number in numbers:
        if number >= 0:
            non_negatives.append(number)
    return non_negatives


# საშუალოს პოვნა: დაწერეთ ალგორითმი, რომელიც მიიღებს სიას და დააბრუნებს მის საშუალო არითმეტიკულს.
def average_of_list(list):
    if not list:  # თუ სია ცარიელია
        return 0
    
    total = sum(list)  # სიაში რიცხვების ჯამი
    count = len(list)  # სიის სიგრძე (რიცხვების რაოდენობა)
    
    return total / count  # საშუალო არითმეტიკული



numbers = [3, 6, 9, 12, 15]
print( numbers)
print( average_of_list(numbers))

   
# სიების შეერთება: დაწერეთ ალგორითმი, რომელიც მიიღებს ორ რიცხვთა სიას, გააერთიანებს მათ ერთ სიაში და ამ სახით დაბეჭდავს.
num1 = [1 ,2,3,4]
num2 = [5,6,7,8]
numbers = num1 + num2
print(numbers)
# დუბლიკატების სია: დაწერეთ ალგორითმი, რომელიც მიიღებს სიას. თქვენ შემდეგ ამ სიის დუბლიკატებს გადაიტანთ ახალ სიაში და დაბეჭდავთ მას.
def remove_duplicates(input_list):
    unique_items = []  # ახალი სია უნიკალურ ელემენტებზე
    for item in input_list:
        if item not in unique_items:  # თუ ელემენტი უნიკალურია
            unique_items.append(item)  # დაემატე ახალ სიაში
    return unique_items


my_list = [1, 2, 2, 3, 4, 4, 5]
print( remove_duplicates(my_list))