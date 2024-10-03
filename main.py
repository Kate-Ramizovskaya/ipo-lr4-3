num=int(input("Введите число для поиска факториала: ")) #ввод числа с клавиатуры
i=1
factorial=1
while i<=num:
    factorial*=i
    i+=1
print ("Факториал числа ", num, "равен: ", factorial)