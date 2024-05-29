# 1. შექმენით ფუნქცია სახელად numbers_product. ფუნქციას გადაეცით სამი არგუმენტი - start, end, step. შემდეგ გამოიყენეთ while ციკლი (for ციკლი არ შეიძლება) და სიაში დაამატეთ რიცხვები - დაიწყეთ start-იდან, იტერაცია მოახდინეთ step-ით და ციკლი ამუშავეთ end-ამდე. განიხილეთ ეს სია და მოახდინეთ მასზე ფილტრაცია, კიდევ ახალ სიაში დაამატეთ მარტო 3-ის ჯერადი რიცხვები. საბოლოოდ დააბრუნეთ 3-ის ჯერადების სიის ყველა რიცხვის ნამრავლი - product.
def numbers_product(start, end, step):
    current = start
    numbers = []
    # შევქმნათ სია while ციკლით
    while current < end:
        numbers.append(current)
        current += step
    
    # ფილტრაცია 3-ის ჯერადებისთვის
    multiples_of_three = [num for num in numbers if num % 3 == 0]
    
    # რიცხვების ნამრავლის გამოთვლა
    product = 1
    for num in multiples_of_three:
        product *= num
    
    return product

# example
print(numbers_product(1, 20, 2))  # უნდა დაბეჭდოს 3-ის ჯერადების ნამრავლი: 3 * 9 * 15 = 405


# 2. პირველ დავალებაში მიღებული შედეგი შეინახეთ ცვლადში. შემდეგ შექმენით ახალი ფუნქცია, სადაც ამ რიცხვზე მოახდენთ მათემატიკურ მოქმედებებს: +, -, *, /. აუცილებელია, რომ მომხმარებელს შემოატანინოთ მეორე რიცხვი და შემდეგ მოახდინოთ მათემატიკური მოქმედებები.

def numbers_product(start, end, step):
    current = start
    numbers = []
    # შევქმნათ სია while ციკლით
    while current < end:
        numbers.append(current)
        current += step
    
    # ფილტრაცია 3-ის ჯერადებისთვის
    multiples_of_three = [num for num in numbers if num % 3 == 0]
    
    # რიცხვების ნამრავლის გამოთვლა
    product = 1
    for num in multiples_of_three:
        product *= num
    
    return product

# example
print(numbers_product(1, 20, 2))  # უნდა დაბეჭდოს 3-ის ჯერადების ნამრავლი: 3 * 9 * 15 = 405
 
def operate_on_number(number):
    # მაგალითისთვის შევქმნათ ცვლადი
    another_number = 10
    
    addition = number + another_number
    subtraction = number - another_number
    multiplication = number * another_number
    division = number / another_number if another_number != 0 else "Error"
    
    return addition, subtraction, multiplication, division

# მაგალითი
product = numbers_product(1, 20, 2)
print(operate_on_number(product))  # უნდა დაბეჭდოს (415, 395, 4050, 40.5) თუ product არის 405

# 3. შექმენით ფუნქცია სახელად hashtag generator. მომხმარებელს შეეკითხეთ წინადადება და ის გადაეცით არგუმენტად ფუნქციას. მუშაობის წესები: საბოლოო ვერსია იწყება #-თი, სიტყვები შეერთებულია, ყველა სიტყვა იწყება დიდი ასოთი. Test case:
# "abc def ghi" -> "#AbcDefGhi"

def hashtag_generator(sentence):
    # შევქმნათ ჰეშთეგი სიტყვების პირველი ასოების დიდებით
    words = sentence.split()
    hashtag = '#' + ''.join(word.capitalize() for word in words)
    return hashtag

# example
print(hashtag_generator("abc def ghi"))  # უნდა დაბეჭდოს "#AbcDefGhi"


# 4. შექმენით ფუნქცია სახელად num_divisors. ამ სიას არგუმენტად გადაეცით მომხმარებლის მიერ შემოტანილი მთელი რიცხვი. თქვენი დავალებაა, რომ დააბრუნოთ სია, სადაც იქნება ამ რიცხვის ყველა გამყოფი. Test case: 20 -> [1, 2, 4, 5, 10, 20]

def num_divisors(number):
    # შევქმნათ სია რიცხვის გამყოფებისთვის
    divisors = []
    
    # გამოვიყენოთ for ციკლი რიცხვის გამყოფების პოვნისთვის
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    
    return divisors

# 5. შექმენით ფუნქცია manual_split. ამ ფუნქციაში უნდა შეიმუშავოთ split-ის მსგავსი ალგორითმი, მაგრამ არ გამოიყენოთ თვითონ split. თქვენ ფუნქციას არგუმენტად გადაეცით მომხმარებლის მიერ შემოტანილი სიტყვა. ასევე მომხმარებელს შეეკითხეთ start, end, step მნიშვნელობები, გადაეცით ფუნქციას და იმუშავეთ სიტყვაზე. Test case: "Hello World!", 2, 6, 2 -> "lo".

def manual_split(string, start, end, step):
    # შექმენით ცარიელი სტრიქონი შედეგისთვის
    result = ""
    
    # გადაამოწმეთ ყველა სიმბოლო სტრიქონში მითითებული დიაპაზონის შიგან
    for i in range(start, min(end, len(string)), step):
        result += string[i]
    
    # დააბრუნეთ შედეგი
    return result
