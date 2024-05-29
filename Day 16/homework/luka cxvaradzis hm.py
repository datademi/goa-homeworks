#  შექმენით სია სადაც შეინახავთ თქვენთვის საყვარელ ფილბეს და დაბეჭდეთ მთლიანი სია/ კონკრეტული ფილმი

films = ["pianist" , "deadpul","spiderman"]
print(films)
print(films[2])

#  შექმენით 2 სია და გააერთიანეთ ისინი
list1 = ["games", "films","cars"]
list2 = ["books", "names"]
print(list1 + list2)
#  შექმენით სტრინგი მაგ. თქვენი სახელი, და გამოიტანეთ სახელის პირველი და ბოლო სიმბოლო
name = "data"
print(name[0] + name[3])
#  შექმენით სია და სტრინგი ხოლო შემდეგ დაბეჭდეთ len ფუნქციის გამოყენებით მათი ზომა
list = ["books", "audi", "porshe"]
child = "data"
print(len(list))
print(len(child))
#  შეცვალეთ სიიდან რომელიმე მნიშვნელობა (ჯერ გაიარეთ სოლოლეარნი)
list = ["marvel", "disney", "georgia"]
list[2] = "aladin"
print(list)
#  შექმენით რიცხვების სია სადაც 10 რიცხვს შეიტანთ, გამოიტანეთ პირელ ინდექსა და ბოლო ინდექსზე მყოფი ელემენტების ჯამი
numbers = [1 , 2 , 3 , 4 , 5 , 6 ,7 ,8 ,9 , 10]
print(numbers[0] + numbers [9])