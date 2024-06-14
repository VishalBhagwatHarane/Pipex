# text="Vishal Harane"
# print(text.capitalize())

# s = 'Credence For Credence'
# print(s.isupper())
# # First character in first
# # word is lowercase
# s = 'credence For Credence'
# print(s.isupper())
# # Third word has uppercase
# # characters at middle
# s = 'Credence For CREDENCE'
# print(s.isupper())
# # Ignore the digit 6041, hence returns True
# s = '6041 Is My Number'
# print(s.isupper())
# # word has uppercase
# # characters at middle
# s = 'CREDENCE'
# print(s.isupper())

# s = 'credence For Credence'
# print(s.lower())
# # Third word has uppercase
# # characters at middle
# s = 'Credence For CREDENCE'
# print(s.lower())
# # Ignore the digit 6041, hence returns True
# s = '6041 Is My Number'
# print(s.lower())
# # word has uppercase
# # characters at middle
# s = 'CREDENCE'
# print(s.lower())

# s = 'Credence For Credence'
# print(len(s))
# s = 'credence For Credence'
# print(len(s))
# s = 'Credence For CREDENCE'
# print(len(s))
# s = '6041 Is My Number'
# print(len(s))
# s = 'CREDENCE'
# print(len(s))

# String = "Credence"
# print("$".join(String))
# print(",".join(String))
# s1 = 'abc'
# s2 = '123'
# # each element of s2 is separated by s1
# # '1'+ 'abc'+ '2'+ 'abc'+ '3'
# print('s1.join(s2):', s1.join(s2))
# # each element of s1 is separated by s2
# # 'a'+ '123'+ 'b'+ '123'+ 'b'
# print('s2.join(s1):', s2.join(s1))

# listt=[1,2,3,4,5]
# l=listt*2
# print(l)

# list1 = [12, 14, 16, 18, 20]
# list2 = [9, 10, 32, 54, 86]
# liar3=list1+list2
# print(liar3)

# list1 = [12, 14, 16, 18, 20, 23, 27, 39, 40]
# print(len(list1))

# list1 = [12, 14, 16, 18, 20, 23, 27, 39, 40]
# for i in list1:
#     print(i)
# print(12 in list1)

# a = [ 1, 2, "Ram", 3.50, "Rahul", 5, 6 ]
# b= [ 1, 2, "Ram", 3.50, "Rahul", 5, 6 ]
# print(a==b)

# a = [ 1, 2, "Ram", 3.50, "Rahul", 5, 6 ]
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])

# my_list = [1, 2, 3, 4, 5]
# # # print(my_list[:])
# # print(my_list[2:])
# print(my_list[2:4])
# print(my_list[::2])
# print(my_list[1:4:2])

# my_list = [1, 2, 3, 4, 5]
# print(my_list[0:6])
# print(my_list[1:6:2])
# listt=[1,2,3,4,5]
# print(listt[-1])
# print(listt[-3:])
# print(listt[-3:-1])

# Lst = [50, 70, 30, 20, 90, 10, 50]
# print(Lst[::])
# print(Lst[-7::1])
# print(Lst[1:5])
# List=[1,2,3,4,5,6,7,8,9]
# print('/nOriginal list: ',List)
# print(List[3:9:2])
# print(List[::2])
# print(List[::])

# print(List[::-1])
# print(List[::-3])
# print(List[:1:-2])
# print(List[10::2])
# print(List[-1:-1:-1])
# print(List[:0:])

# List = [-999, 'G4G', 1706256, 3.1496, '^_^']
# print('n/Original List:\n',List)
# List[2:4]=['Geeks','For','Geeks']
# print(List)
# List[:6]=[]
# print(List)

# List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print("/nOriginal List:\n",List)
# # new_List=List[::2]+List[7:]
# # print(new_List)
# # list=List[::2]+List[1::2]
# # print(list)
# newList = List[:3]+List[7:]
# print(newList)

# list = [1, 2, 3, 4, 5, 6]
# print(list)
# list[2]=10
# print(list)
# list[1:3]=[89,78]
# print(list)
# list[-1]=26
# print(list)

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# animals = ['cat', 'dog', 'rabbit']
# animals.append('Tiger')
# print('Updated animals list:',animals)

# animals list
# animals = ['cat', 'dog', 'rabbit']
# # list of wild animals
# wild_animals = ['tiger', 'fox']
# animals.append(wild_animals)
# print('Updated animals list',animals)

# fruits = ['apple', 'banana', 'cherry', 'orange']
# fruits.clear()
# print(fruits)

# list = [{1, 2}, ('a'), ['1.1', '2.2']]
# list.clear()
# print("List",list)

# list = [{1, 2}, ('a'), ['1.1', '2.2']]
# del list[:2]
# print("List",list)

# mixed list
# my_list = ['cat', 0, 6.7]
# # copying a list
# new_list = my_list.copy()
# print('Copied list',new_list)

# old_list = [1, 2, 3]
# new_list=old_list
# print(new_list)
# new_list.append('a')
# print("New List:",new_list)
# print("Old list:",old_list)

# list = ['cat', 0, 6.7]
# new_list=list[:]
# new_list.append('dog')
# print("Old list:",list)
# print("New List:",new_list)

# numbers = [2, 3, 5, 2, 11, 2, 7]
# cout=numbers.count(2)
# print(cout)

# vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# count=vowels.count('i')
# print('The count of i is',count)
# count=vowels.count('p')
# print('The count p is',count)

# old_number=[1,3,5]
# number=[1,4]
# number.extend(old_number)
# print(number)

# languages list
# languages = ['French', 'English']
# # another list of language
# languages1 = ['Spanish', 'Portuguese']
# languages.extend(languages1)
# print('Language list',languages)

# languages = ['French']
# # languages tuple
# languages_tuple = ('Spanish', 'Portuguese')
# languages_set = {'Chinese', 'Japanese'}
# # appending language_tuple elements to language
# languages.extend(languages_tuple)
# print('New Language List:', languages)
# # appending language_set elements to language
# languages.extend(languages_set)
# print('Newer Languages List:', languages)

# a1 = [1, 2]
# a2 = [1, 2]
# b = (3, 4)
# # a1.extend(b)
# print(a1)
#
# a2.extend(b)
# print(a2)
# a1.append(b)
# print(a1)
# a2.append(b)
# print(a2)

# animals = ['cat', 'dog', 'rabbit', 'horse']
# index=animals.index('dog')
# print(index)

# vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# index=vowels.index('e')
# print("The index of e",index)
# print(vowels.index('p'))

# alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']
# # index=alphabets.index('e')
# # print("The index e:",index)
# index=alphabets.index('i',4)
# print(index)

# vowel = ['a', 'e', 'i', 'u']
# vowel.insert(3,'o')
# print('LSt',vowel)

# vowel = ['a', 'e', 'i', 'u']
# vowel.insert(1,'v')
# print(vowel)

# prime_numbers = [2, 3, 5, 7]
# prime_numbers.insert(4,23)
# print(prime_numbers)

# mixed_list = [{1, 2}, [5, 6, 7]]
# number_tuple=(3,4)
# mixed_list.insert(1,number_tuple)
# print(mixed_list)

# prime_numbers = [2, 3, 5, 7]
# removed_element=prime_numbers.pop(2)
# print("Removed Element:",removed_element)
# print("Updated List:",prime_numbers)

# languages = ['Python', 'Java', 'C++', 'French', 'C']
# return_value=languages.pop(3)
# print('Return value:',return_value)
# print('updated list:',languages)

# languages = ['Python', 'Java', 'C++', 'Ruby', 'C']
# print('Return value',languages.pop())
# print("Updated list",languages)
# print('return value',languages.pop(-1))
# print('Updated list:',languages)
# print(languages.pop(-3))

# prime_numbers = [2, 3, 5, 7, 9, 11]
# prime_numbers.remove(9)
# print('Updated List:',prime_numbers)

# animals = ['cat', 'dog', 'rabbit', 'guinea pig']
# animals.remove('rabbit')
# print("Updated animals list",animals)

# animals = ['cat', 'dog', 'rabbit', 'guinea pig']
# animals.remove('dog')
# print("Updated animals list:",animals)

# prime_numbers = [11, 3, 7, 5, 2]
# prime_numbers.sort()
# print(prime_numbers)

# vowels = ['e', 'a', 'u', 'o', 'i']
# vowels.sort()
# print("Sorted list",vowels)

# vowels = ['e', 'a', 'u', 'o', 'i']
# vowels.sort(reverse=True)
# print("Sorted list descendingL=",vowels)

# my_tuple = (1, 2, 3)
# print(my_tuple)

# my_tuple = (1, "Hello", 3.4)
# print(my_tuple)
# my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# print(my_tuple)

# var1 = ("Hello") # string
# var2 = ("Hello",) # tuple
# print(type(var1))
# print(type(var2))

# tuple1 = (101, 102, 103) + (104, 105, 106)
# # print(tuple1)
#
# T = ('red', 'green', 'blue') + (1, 2, 3)
# print(T)
# tuple2=tuple1+T
# print(tuple2)

# T=('red',)*3
# print(T)

# T=('red','green')*3
# # print(T)
# print('red' in T)

# for i in T:
    # print(i)

# tuple1 = (12, 14, 16, 18, 20, 23, 27, 39, 40)
# print(len(tuple1))

# T = ('red', 'green', 'blue')
# T[0]='black'
# print(T)

# tuple1 = (0, 1, 2, 3)
# tuple1[0]=4
# print(tuple1)

# T = ('red', 'green', 'blue', 'yellow', 'black')
# print(T[0])
# print(T[1])
# print(T[-1])

# tup1 = ('physics', 'chemistry', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5, 6, 7 )
# print('tup1[0]:',tup1[0])
# print('tup2[1:5]',tup2[1:5])

# T = ('a', 'b', 'c', 'd', 'e', 'f')
# print(T[2:5])
# print(T[0:2])
# print(T[3:-1])

# tuple1 = (0 ,1, 2, 3)
# print(tuple1[1:])
# print(tuple1[::-1])
# print(tuple1[2:4])

# T = ('red', 'green', 'blue')
# del T
#

# t = ('red', 'green', 'blue')
# del t[0]
# print(t)

# T = ('red', 'green', 'blue', 'cyan')
# print(T)

# T = ('red', 'green', 'blue', 'cyan')
# (a,b,c,d)=T
# print(a)
# print(b)
# print(c)

# a = (1,2,1,3,1,3,1,2,1,4,1,5,1,5)
# print(a.count(1))
# print(a.index(5))

# abc=("Yusuf","Amit","Pooja","raj", "Pritesh","Priya","Yusuf")
# print(abc.count('Yusuf'))
# print(abc.index('Yusuf'))
# print(abc.index("Yusuf",1,7))
# print(abc.index(-7,-1))
# print(abc.index('Yusuf',-1,-7))

# tup = (22, 3, 45, 4, 2.4, 2, 56, 890, 1)
# print(max(tup))
# print(min(tup))
# print(sum(tup))

# tup2 = ("Yusuf","yusuf")
# print(max(tup2))
# print(min(tup2))

# tuple_ = (5, 2, 24, 3, 1, 6, 7)
# sorted_ = tuple(sorted(tuple_))
# print(type(sorted_))
# print('Sorted tuple:',sorted_)

# tuple_ = (5, 2, 24, 3, 1, 6, 7)
# sorted_=tuple(sorted(tuple_,reverse=True))
# print(sorted_)

# a = (1,2,3,4,5)
# print(len(a))

# a_list = [1,2,3,4,5]
# print(a_list)
# print(type(a_list))
# b_tuple=tuple(a_list)
# print(b_tuple)
# print(type(b_tuple))

# a="Yusuf"
# a=tuple(a)
# print(type(a))

# x = ("apple", "banana", "cherry")
# y=list(x)
# y[1]='kiwi'
# print(x)
# print(y)
# x=tuple(y)
# print(x)

thistuple = ("apple", "banana", "cherry")
# y=list(thistuple)
# y.append('Orange')
# thistuple=tuple(y)
# print(thistuple)

# y = ("orange",)
# thistuple+=y
# print(thistuple)

# tuple1 = (5, 3, 2, 8, 4, 4, 6, 2)
# list1=list(tuple1)
# list1[2]=63
# tuple1=tuple(list1)
# print(tuple1)

# tuple1 = (5, 3, 2, 8, 4, 4, 6, 2)
# list1=list(tuple1)
# list1.remove(2)
# tuple1=tuple(list1)
# print(tuple1)

# y={'y', 'n', 't', 'p', 'h', 'o'}
# print("Curely brackets",y)

# student_id = {112, 114, 116, 118, 115}
# print("Student ID:",student_id)

# vowel_letters = {'a', 'e', 'i', 'o', 'u'}
# print('Vowel Letters:', vowel_letters)

# mixed_set = {'Hello', 101, -2, 'Bye'}
# print('Set of mixed data types:', mixed_set)


# student_id = set[112, 114, 116, 118, 115]
# print('Student ID:', student_id)

# vowel_letters = set['a', 'e', 'i', 'o', 'u']
# print('Vowel Letters:', vowel_letters)

# Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
# print(Days)
# print(type(Days))

# x = set("python")
# print("by set()",x)

# y={'y', 'n', 't', 'p', 'h', 'o'}
# print('curly {}brackets: ', y)
# print(type(y))

# empty_set = set()
# empty_dictionary = {}
# # check data type of empt
# # check data type of empty_set
# print('Data type of empty_set:', type(empty_set))
# # check data type of dictionary_set
# print('Data type of empty_dictionary', type(empty_dictionary))

# x={'p','h','t','n','o'}
# for y in x:
#     print(y)

# fruits = {"Apple", "Peach", "Mango"}
# for x in fruits:
#     print(x)

# numbers = {2, 4, 6, 6, 2, 8}
# print(numbers)

# numbers = {21, 34, 54, 12}
# print("Initial set:",numbers)
# numbers.add(22)
# print("Updated set:",numbers)

# companies = {'Lacoste', 'Ralph Lauren'}
# tech_companies = ['apple', 'google', 'apple']
# companies.update(tech_companies)
# print(companies)

# y={2,3,4,5}
# x=set()
# print('Set y:',y)
# x.update(y)
# print(x)
# print(y)

# x={'Python','Java','PHP','Angular'}
# print('Set x: ', x)
# # x.remove('Java')
# # print('Set x after remove:',x)
# # x.discard('PHP')
# # print(x)
#
# # x={1,2,"py"}
# # z=x.pop()
# # print(z)
# x.clear()
# print(x)

# anguages = {'Python', 'Java', 'English'}
# anguages.remove('English')
# print(anguages)

# numbers = {2, 3, 4, 5}
# numbers.discard(3)
# print(numbers)

# A = {'a', 'b', 'c', 'd'}
# remove_item=A.pop()
# print(remove_item)


# primeNumbers = {2, 3, 5, 7}
# primeNumbers.clear()
# print(primeNumbers)

# first set
A = {1, 3, 5,2}
# second set
B = {0, 2, 4,1}
# print('Union using|',A|B)
# print('Union using usion()',A.union(B))
# print("Intersection using &",A&B)
# print('Intersection using intersection():',A.intersection(B))
# print("Differnce using &",A-B)
# print('Differnce using differnce():',A.difference(B))
# print("Differnce using &",B-A)
# print('Differnce using differnce():',B.difference(A))
# print('Using^',A^B)
# print("using symmetric differnce()",A.symmetric_difference(B))

# x={1,2}
# y={1,2,3,4}
# z=x.issubset(y)
# print(z)

# Initialization set x and y
# x={1,2}
# y={3,4}
# z=x.isdisjoint(y)
# print(z)


# x = {'a','b','c'}
# y = {'a','b','c'}
# # print('Set x: ', x)
# # print('Set y: ', y)
# print('Set x==y',x==y)
# print(x!=y)
# print(x<y)
# print(x>y)

# x = {1,2}
# y = {1,2,3,4}
# print('Set x: ', x)
# print('Set y: ', y)
# print('Set x <= y: ', x <= y)
# print('Set x < y: ', x < y)

# x = {1,2,3,4}
# y = {1,2,3}
# print('Set x superset y:', x >= y)
# print('Set x proper superset y:', x > y)
# print('Intersection x & y:', x & y)
# print('Union of x & y:', x | y)
# print('Difference of x & y:', x - y)
# print('Symmetric Difference of x & y:', x ^ y)

# Initialization of set x
# x={20,1,2,3,4,10}
# # copy set x to set z
# z=x.copy()
# print('Copy set x to set z: ', z)
# print('Print length of set z: ',len(z) )
# print('Print min of set z: ',min(z))
# print('Print max of set z: ',max(z))
# print('Print Sum of set z: ',sum(z))
# # Sort set z
# print(sorted(z))
# print(sorted(z, reverse=True))
# print(all(x))
# print(any(x))
# print(5 in x)
# print(5 not in x)

x={20,1,2,3,4,10}
# z=x.copy()
# print("copy set x to set z",z)
# print("Print lenth of set z",len(z))
# print('Min value of set:',min(z))
# print('max value of set z',max(z))
# print('sum value of set z ',sum(z))
# print(sorted(z))
# print(sorted(z,reverse=True))
# print(all(z))
# print(any(z))
# print(5 in z)
# print(5 not in z)
# print(2 in z)
# print(2 not in z)

# b=False
# print(type(b))
# a=10
# b=20
# # print(a>b)
# # print(type(a>b))
# print(a<b)
# print(type(a<b))

# tuple of vowels
# vowels = ('a', 'e', 'i', 'o', 'u')
# fSet=frozenset(vowels)
# print('The frozen set is',fSet)
# print('Empty frozen set is',frozenset())
# fSet.add('v')
# print(fSet)

# random dictionary
# person = {"name": "John", "age": 23, "sex": "male"}
# fSet=frozenset(person)
# print("The frozen set is",fSet)

# A=frozenset([1,2,3,4])
# B=frozenset([3,4,5,6])
# # C=A.copy()
# # print(C)
# print(A.union(B))
# print(A.intersection(B))
# print(A.difference(B))
# print(B.difference(A))
# print(A.symmetric_difference(B))

# A=frozenset([1,2,3,4])
# B=frozenset([3,4,5,6])
# C=frozenset([5,6])
# print(A.isdisjoint(C))
# print(C.issubset(B))
# print(B.issuperset(C))

# D1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
#
# L = [('name', 'Bob'),
#  ('age', 25),
#  ('job', 'Dev')]
# D=dict(L)
# print(D)
# print(D1)

# T = (['name', 'Bob'],
#  ['age', 25],
#  ['job', 'Dev'])
#
# D=dict(T)
# print(D)

# D = dict(name = 'Bob',
#  age = 25,
#  job = 'Dev')

# keys = ['name', 'age', 'job']
# values = ['Bob', 25, 'Dev']
#
# D=dict(zip(keys,values))
# print(D)

# keys = ['a', 'b', 'c']
# defaultValue = 0
# D=dict.fromkeys(keys,defaultValue)
# print(D)

# D = {'name': 'Bob',
#  'age': 25,
#  'name': 'Jane'}
# print(D)

# D = {(2,2): 25,
#  True: 'a',
#  'name': 'Bob'}
# print(D)

# D = {[2,2]: 25,
#  'name': 'Bob'}
# print(D)

# D = {'a':[1,2,3],
#  'b':{1,2,3}}
# print(D)

# D = {'a':[1,2],
#  'b':[1,2],
#  'c':[1,2]}
# print(D)

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# print(D['name'])
# print(D['salary'])
# print(D.get('name'))
# print(D.get("age"))

# Dict = {'Dict1': {1: 'Geeks'},
#  'Dict2': {'Name': 'For'}}
# # print(Dict['Dict2'])
# print(Dict['Dict1'])
# print(Dict['Dict1'][1])
# print(Dict['Dict2']['Name'])

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# D['name']='Vishal'
# print(D)
# D['age']=23
# print(D)
# D['job']='Software Test Enginner'
# print(D)

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# D['City']='Washim'
# print(D)

Dict={}
# # print("Empty Dictionary",Dict)
#
# Dict[0] = 'Geeks'
# Dict[2] = 'For'
# Dict[3] = 1
# print('Dictionary after adding 3 elements',Dict)

# Dict['Value_set'] = 2, 3, 4
# # print(Dict)
# Dict[2] = 'Welcome'
# print(Dict)
#
# Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
# print(Dict)

# D1 = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# # D2 = {'age': 30,
# #  'city': 'New York',
# #  'email': 'bob@web.com'}
# x=D1.pop('age')
# print(x)
# print(D1)
# # D1.update(D2)
# print(D1)

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# del D['age']
# print(D)

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# x=D.popitem()
# print(D)
# print(x)

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
#
# D.clear()
# print(D)

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# print(list(D.keys()))
# print(list(D.values()))
# print(list(D.items()))

# D={'name':'Vishal',
#    'age':22,
#    'Job':"Dev"
# }
# for x in D.items():
#  print(x)

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
#
# for x in D:
#  print(D[x])

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# # print('name' in D)
# # print('salary' in D)
# print('Bob' in D.values())
# print('Sam' in D.values())

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# print(len(D))

dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
# dict2=dict1.copy()
# print(dict2)
# dict1.clear()
# print(dict1)
# print(dict1.get(1))
# print(dict1.items())
# print(dict1.keys())
# print(dict1.pop(4))
# dict1.popitem()
# print(dict1)
# dict1.update({3:"vvv"})
# print(dict1)
# print(dict1.values())

# dict = {1: "Ayan", 2: "Bunny", 3: "Ram", 4: "Bheem"}
# # print(len(dict))
# # print(any({'':'','':'',3:''}))
#
# dict = {7: "Ayan", 5: "Bunny", 8: "Ram", 1: "Bheem"}
# print(sorted(dict))

# dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}
# dict_demo=dict.copy()
# print(dict_demo)

# dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}
# demo_dict=dict.copy()
# print(demo_dict.pop(1))
# print(demo_dict)

# dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}
# # dict.popitem()
# # print(dict)
# # print(dict.keys())
# # print(dict.items())
# # print(dict.get(3))
# dict.update({3:"TCS"})
# print(dict)

kitchen='apple'
# if kitchen=='apple':
#     print('Hai hai apple')
# print("Thik hai")

# if kitchen=='Mango':
#     print("Hai hai apple")
# print('thik hai')

# if (kitchen=='Mango'):
    # print('Hai hia apple')

# num=5
# if num<10:
    # print("Num is smaller than 10")

# a=7
# b=0
# if a>b:
    # print('a is greater than b')

# a=0
# b=7
# if b>a:
#     print('b is greater than a')
#
# a = 7
# b = 0
# if (a):
#     print('True')

# i=10
# if i>15:
#     print("10 is less than 15")
# print("i ma not in if")

# if 'Python' in ['java','Python','C++']:
#     print("True")

# passing_score=40
# my_score=67
# if my_score>=passing_score:
#     print("Congratulation! you have passed your exam")

# passing_Score = 60
# my_Score = 67
# if my_Score>=passing_Score:
#     print('You passed the exam')
# print('Congratulations')

# num=5
# if num>10:
#     print("Number is greater than 10")
# else:
#     print('Number is less than 10')
# print("The statement will always be executed")

# a=7
# b=0
# if a>b:
#     print("a is greater than b")
# else:
#     print("b is greater than a")

# a=7
# b=0
# if a<b:
#     print('a is smaller than b')
# else:
#     print('b is smaller than a')

# passing_Score = 60
# my_Score = 67
# if my_Score>=passing_Score:
#     print("Congratulations You passed the exam")
#     print("You are passed in the exam")
# else:
#     print("sorry you failed the exam better luck next time")
#
# passing_Score = 60
# my_Score = 47
# if my_Score>=passing_Score:
#     print('Congratulations you passed the exam')
#     print("You are passed in the exam")
# else:
#     print("Sorry you failed the exam better luck next time")


# i=20
# if i<15:
#     print('i is smaller than 15')
#     print('i m in if block')
# else:
#     print('i is greater than 15')
#     print(' i m in else block')
# print(' i m not in if and not in else block')

# num = 10
# if num==0:
#     print('Number is zero')
# elif num>5:
#     print("Number is grater than 5")
# else:
#     print("Number is smaller than 5")

# num = -7
# if num>0:
#     print('Number is postive')
# elif num<0:
#     print('Number is nagative')
# else:
#     print('Number is zero')

# num = 7
# if num!=0:
#     if num>0:
#         print('Number is greater than zero')

# i=10
# if i==10:
#     if i<20:
#         print(i,'is smaller than 20')
#     if i<20:
#         print(i,'is smaller than 21')

# i=10
# if i==10:
#     if i<15:
#         print(i,'is smaller than 15')

# num = -7
# if num!=0:
#     if num>0:
#         print('Number is positive')
#     else:
#         print('Number is nagative')
# else:
#     print("Number is zero")

# i=10
# if i==10:
#     if i<15:
#         print('i is smaller than 15')
#     if i<12:
#         print("is smaller than 12 too")
#     else:
#         print('is greater 15')

# i=20
# if i==10:
#     print('i is 10')
# elif i==15:
#     print('i is 15')
# elif i==20:
#     print('i is 20')
# else:
#     print('i is not present')

# my_marks = 90
# if my_marks<35:
#     print('Sorry you failed the exam')
# elif my_marks>60 and my_marks>100:
#     print('Passed in first class')
# else:
#     print("Passed in first class with distinction")

# num = 7
# if num>0:
#     print('Number is greater tham zero')

# a=10
# if a:
#     print('The given value of a:')
#     print(a)

# num=7
# if num>0:
#     print('Number is greater than zero')
# else:
#     print('Number is smaller than  zero')

# if ('a' in 'fruits'): print('Apple'); print('Orange')

# if ('a' in 'fruits'): print('Apple'); print('Orange')
# elif ('e' in 'fruits'): print('Mango'); print('Grapes')
# else: print('No fruits available')

# num1 = 10
# num2 = 20
# num3 = 30
# if num1==10 and num2==20 and num3==30:
#     print('All the conditions are true')

# fruitName = 'Apple'
# if fruitName=='Mango' or fruitName=='Apple' or fruitName=='Grapes':
#     print("It's a fruit")

# currentYear=int(input('Enter the year: '))
# month=int(input("Enter the month: "))
# if currentYear%4==0:
#     print('Leap Year')
#     if month==1 or month==3 or month==5 or month==7 or month==9 or month==11:
#         print("There are 31 days in this month")
#     elif month==4 or month==6 or month==8 or month==10 or month==12:
#         print('There are 30 days in this month')
#     elif month==2:
#         print("There are 30 days in this month")
#     else:
#         print("Invalid month")
# elif currentYear %4 !=0:
#     print("Non Leap Year")
#     if month==1 or month==3 or month==5 or month==7 or month==8 or month==11:
#         print("There are 31 days")
#     elif month==4 or month==6 or month==9 or month==12 or month==10:
#         print("There are 30 days")
#     elif month==2:
#         print("There are 28 days")
#     else:
#         print("Invalid Year")

# kitchen= "Apple"
# while 'Apple' in kitchen:
#     print('Apple')

# count=0
# while count<3:
#     print("Apple")

# count=0
# while count<3:
#     print('Apple')
#     count=count+1
# else:
#     print('Not found')

# count=0
# while count<3:
#     count+=1
#     print('Apple')

# kitchen = "Apple"
# count=0
# while count<3:
#     count+=1
#     print('Apple')

# i=0
# while i<6:
#     print(i)
#     i+=1

# i=1
# while i <6:
#     print(i)
#     i+=1

# i=2
# while i<6:
#     print(i)
#     i+=1

# count=0
# while count<5:
#     count+=1
#     print("hello geeks enter ",count,"Thtimes")

# count=0
# while count<3:
#     count+=1
#     print("hello geeks")

# count=0
# while count<3:
#     count+=1
#     print("hello geek")
# else:
#     print("In else block")


# count=0
# while count==0:
#
# age=32
# while age>=18:
#     print('You can vote')

# i = 1
# n = 5
# while i<=n:
#     print(n)
#     i+=1

# total = 0
# number=int(input("Enter a number: "))
# while number!=0:
#     total+=number
#     number=int(input("Enter a number: "))
# print('Total number',total)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)

# for x in 'banana':
#     print(x)


# value=range(5)
# for i in value:
#     print(i)

# for x in range(6):
#     print(x)

# number=range(2,5)
# print(list(number))

# number=range(-2,2)
# print(list(number))

# numbers = range(2, 10, 3)
# print(list(numbers)) # [2, 5, 8]
# # numbers from 4 to -1 with increment of -1
# numbers = range(4, -1, -1)
# print(list(numbers)) #

# numbers = range(0, 5, 1)
# print(list(numbers))

# for x in range(2, 30, 3):
#  print(x)

# digits = [0, 1, 5]
# for i in digits:
#  print(i)
# else:
#  print("No items left.")

# for x in range(6):
#  print(x)
# else:
#  print("Finally finished!")

# fruits = ['banana', 'apple', 'mango']
# for index in range(len(fruits)):
#  print ('Current fruit :', fruits[index])
# print ("Good bye!")

# nums = (1, 2, 3, 4)
# sum_nums = 0
# for num in nums:
#  sum_nums = sum_nums + num
# print(f'Sum of numbers is {sum_nums}')
# for i in range(3):
#     print(i)

# list1 =[1,2,3,4,5]
# item=1
# while item in list1:
#     print("While loop")
#     item+=1

# for i in range(11):
#  print (i)

# i = 0
# while i <= 10:
#     print(i)
#     i+=1






