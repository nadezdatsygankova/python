#Создать лист из 6 любых чисел. 
#Отсортировать его по возрастанию

list_1 = [1,5,8,3,6,7]
sorted(list_1)


#Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно
dictionary = {1:'Name',2:'Age',3:'Education',4:'Job',5:'Telefone'}

dict.items(dictionary)

#Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем

tuple_1 = (0.2,1.3,2.5,0.8,5.6,8.3,6.4,8.3,6.7,10.2)

max1 = max((tuple_1))
min1 = min((tuple_1))
print(max1,min1)

#Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,
#чтобы получилось: 'Earth -> Russia -> Moscow'
list_Earth = ['Earth', 'Russia','Moscow']
result = list_Earth[0]
n = len(list_Earth)

for i in range(1,n):
    result = result + ' ' + list_Earth[i]
    print(result)
        

#Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
stroka = '/bin:/usr/bin:/usr/local/bin'

print(stroka.split(':'))

#Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет

x = range (1,101)

for i in x:
    if i%7 == 0:
        print ('Divide 7 -', i)
    else:
        print('Not divide 7 -',i)

#Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы

a = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

for row in a:
    for elem in row:
        print(elem, end=' ')
    print()


#Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс   
a = ['trick','dog','duck']
idx = 0
for idx,item  in enumerate(a):
    print(idx,item)

#Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'    

listdelete = ['to-delete','dre','fgt','to-delete','to-delete']

while 'to-delete' in listdelete:
    listdelete.remove('to-delete')
    print(listdelete) 


#Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль     

a = [1,2,3,4,5,6,7,8,9,10]

print(list(reversed(a))) 

      