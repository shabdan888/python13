
# print()
# len()
# sum()
# max()
# min()
# pow()
# divmod()
# dir()
# abs()
# input()
# str()
# list()
# dict()
# set()
# int()
# float()
# tuple()
# globals()
# locals()

# map(function, iterable) --> Она применяет функцию к каждрму элементу в iterable

# nums = [1,2,3,4,5]
# def square(number):
#     return number * number
# map_function = map(square, nums)
# result = list(map_function)
# print(result)

# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# for value in a_dict:
#     print(value)

# *********************************************





# dict_ = {1:2, 3:4, 5:6}

# def convert(value):
#     return str(value)
# result = list(map(convert, dict_.values()))
# for new_dict in dict_: 
# # new_dict = dict.fromkeys(dict_.keys(), result)
# print(new_dict)



# Анонимная функция -- lambda. Та же самая функция , только без имени.
# def square(a,b):
#     return a**b 
# print(square(5,5))


# Pythonic way
# square = lambda a,b: a**b
# result = square(5,5)
# print(result)

# ********************************
# filter(function, iterable) --> Фильтрует если функция возврашает True

# nums = [1,2,3,4,5,6,7,8,9,10]

# def filter_nums(number):
#     if number % 2 == 0:
#         return True
# result = list(filter(filter_nums, nums))
# print(result)



# result = list(filter(lambda
# num: (num % 2 == 0), nums))
# print(result)

# ************************************

# letters = ['a','b','c','d','f','h','o','i']
# def filter_vowels(letter):
#     vowels = ['a','e','i','o','u']
    
#     return True if letter in vowels else False
# res = list(filter(filter_vowels, letters))
# print(res)





# letters = ['a','b','c','d','f','h','o','i']
# vowels = ['a','e','i','o','u']
# result = list(filter(lambda letter: (letter in vowels), letters))
# print(result)


# *******************************************
# arr = [0, False, 1, 'Hello', '0', [1,2,3]]
# # 0(False), false , 1(True), 'Hello'(True), '0'(True),[1,2,3](True)
# res = list(filter(None, arr ))
# print(res)



# ******************************************
# zip(iterable, irterable --> *iterables --> Сопостваляет каждый элемент из iterable со следующим.
# Возвращает множество из кортежей.
# [1,2,3,4,5]
# [6,7,8,9,10]
# zip(a,b) --> {(1,6),(2,7),(3,8),(4,9),(5,10)}

# number = [1,2,3,4,5]
# list_letters = ['one','two','three','four','five']
# dict_ = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5'}
# result = set(zip(number,list_letters, dict_.values()))

# print(result)

# *******************************************
# enumerate(iterable, [start])--> Возвращает кортеж из индекса и его значения. 
# Возвращает количество итераций 
# [1,2,3,4,5]
# enumerate(a) --> [(0,1),(1,2),(2,3),...]



# list_ = ['one','two','three']
# res = list(enumerate(list_,1))
# print(res)

# set_ = {1,2,3,4,5}
# for count, elem in enumerate(set_):
#     print(count,elem)
#     if count == 3:
#         break


# ********************************
# reduce(function,iterable) --> Выводит одно значение.
# [1,2,3,4,5]
# 1*2*3*4*5 --> n
# reduce(lambda n, y: n*y, a) --> n

# from functools import reduce 
# numbers = [1,2,3,4,5]
# res = reduce(lambda x, y: x*y, numbers)
# print(res)
    
# *********************************

# all(iterable)--> True если все значения в iterable являются True, иначе False
# list_ = [0,1,2,3, True, '0',[1,2,3],3.14,None]
# res = all(list_)
# print(res)



# ************************* 
# any(iterable) --> Возвращает True если хотя бы один элемент является True, иначе False

# list_ = [0,1,2,3, True, '0',[1,2,3],3.14,None, False]
# list_2 = False, False
# res = any(list_)
# print(res)


# ********************************
# next(iterable)--> Возвращает следующее значение в iterable
# list_ = [1,2,3,4,5]

# list_iterable = iter(list_)

# v_1 = next(list_iterable)
# v_2 = next(list_iterable)
# print(v_1,)


# list_ = [-1, 2, 3, 0, 5, -3, 7,]
# res = list(map(lambda a: (a >= 0),list_))
# print(res)

# from functools import reduce
# list_ = ['qwe','asdf','qwertyui','zxcvb']
# max_ = reduce(lambda a,b: a if (a > b) else b, list_)
 
# print (max_)



