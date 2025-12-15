#Collections - single "variable" that holds multiple values
#List = [] ordered and changable, duplicates - ok

#List = [] ordered and changable, duplicates - ok
#fruits = ["apple", "orange", "banana", "coconut"]

#print(fruits)
#print(fruits[1]) #zero indexed
#print(fruits[0:3]) #prints first 3 elements. index[3] not included
#print(fruits[::2]) #prints every second element begining from index 0

#assign value
#fruits[0] = "pineapple"

#add item to the list
#fruits.append("pineapple")

#remove item
#fruits.remove("pineapple")

#insert an item
#fruits.insert(0, "papaya") #(index, item)

#sort
#fruits.sort()

#reverse - base on how items are inserted
#fruits.reverse()

#clear the list
#fruits.clear()

#iterate in the list
#for fruit in fruits:
#    print(fruit)

#display attributes and methods
#print(dir(fruits))

#display modules, classes, functions
#print(help(fruits))

#print lenght/size of the list
#print(len(fruits))

#check an element in the List
#print("apple" in fruits)

#return the index of an item
#print(fruits.index("apple"))


#Set = {} unordered and immutable, add/remove - ok, no duplicates
#fruits = {"apple", "orange", "banana", "coconut"}


#display attributes and methods
#print(dir(fruits))

#print lenght/size of the list
#print(len(fruits))

#check an element in the List
#print("apple" in fruits)

#fruits.remove("orange")
#fruits.add("pineapple")
#fruits.pop()
#friuts.clear()

#print(fruits)

#Tuple = () ordered and unchangeable, duplicate - ok. faster
fruits = ("apple", "orange", "banana", "coconut")
print(dir(fruits))
print(fruits)