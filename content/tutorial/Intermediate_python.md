---
title: "Intermediate Python Codeblocks 🐍"
keywords: ["python", "cheatsheet"]
categories: [cheatsheet]
date: 2023-26-05T21:30:03+05:30
draft: false
defaultTheme: auto
tags: ["python", "cheatsheet"]
showToc: true
comments: true
cover:
  image: posts/intermediate-py(1).png
  alt: python intermediate level
---

# Intermediate Python

## 1. List

Oredered, mutable, allows duplicate items & different data types

### Creating

```python
print("1.1 using [] - list constructor")
a1=["banana","cherry","apple"]
a2=["banana",2,True,'a']
a3=["a","a"*2,"a"*3]    # output: ['a', 'aa', 'aaa']

a20=[20]*10
a21=[1]*10
a22=a20+a21

print(a1,a2,a3,a20,a21,a22,"\n")

print('''1.2 using "list()"''')
a4=list(a1)
a5=list(range(1,6))
a6=list("janav makkar") # output: ['j', 'a', 'n', 'a', 'v', ' ', 'm', 'a', 'k', 'k', 'a', 'r']
a7=list()
a8=list(["ab","bc","cd"])

print(a4,a5,a6,a7,a8,"\n")

print("1.3 using list comprehensions")
a9=[1,2,3,4,5,6,7,8,9,10]

a10=[i for i in a9 if i%2==0]
a11=[i**2 for i in a9]
a12=[i*12 for i in range(11,20)]

print(a10, a11, a12,"\n")

### Accessing
print("2.1 Index values")
print(a9[0])
print(a9[1])
print(a9[-10])
print(a9[9])
print(a9[-1],"\n")

print("2.2 Slicing")
print(a10[1:6])
print(a10[5:])
print(a10[:5])
print(a10[1:-2])
print(a10[:],"\n")

print("2.3 Step Slicing")
print(a10[0:6:2])
print(a10[:6:2])
print(a10[3::2])
print(a10[10:2:-1], "\n")

print("2.4 for loop")
for i in a10:
    print(i)

### Methods
print("3.1 ADD METHODS")    # .insert(), .extend(), .append()
a13=list(range(1,6))
a14=list(range(6,11))
print(a13,a14,"\n")

a13.insert(0,120) # .insert(index,value) - inserts value at given index
print(a13)

a13.extend(a14) # .extend(list) - joins list at the back
print(a13)

a13.append(11) # .append(value) - adds the value at the back
print(a13,"\n")

print("3.2 DELETE METHODS")       # .pop(), .remove(), .clear()
a15=list(range(1,11))
print(a15)

a15.pop() # .pop() - removes last value
print(a15)

a15.pop(1) # .pop(index) - removes value at given index
print(a15)

a15.remove(4) # .remove(value) - removes first occurence of the value
print(a15)

a15.clear() # .clear() - clears whole list
print(a15,"\n")

print("3.3 OTHER METHODS") # .sort(), .reverse(), .index(), .count()
a16=[11,44,23,9,1,87,56,31,10,27,64,11,11,11]
print(a16)

a16.sort() # .sort() - modifies original list
print(a16)

a16.reverse() # .reverse() - modifies original list
print(a16)

a17=a16.index(87) # .index() - returns index of first occurence of the given value
print(a17)

a18=a16.count(11) # .count() - returns number of times value in the list
print(a18,"\n")

print("4. Functions - len(), min(), max(), sum(), sorted()")
print(len(a9), min(a9), max(a9), sum(a9)) # len(*) - returns length of list, min(*), max(*), sum(*) - only works for numeric lists
a19=sorted(a16) # sorted(*) - does not modify original list
print(a19,"\n")

### Etc

print('5.1 "in" operator')
a=2 in a9
b="gold" in a1
print(a,b,"\n")

print("5.2 COPY METHODS") # =, .copy(), [:], list()
a23=[1,2,3,4,5,6,7,8,9,10]
a24=a23
a24.append(11)
print(a23,a24,"\n")  # this happens because a24 is just a reference to a23, actual copy does'nt takes place

print("5.3 Actual copy methods")
a25=a23.copy() # .copy()
a25.append(12)
print(a23,a25,"\n")

a26=a23[:] # [:]
a26.append(13)
print(a23,a26,"\n")

a27=list(a23) # list()
a27.append(14)
print(a23,a27,"\n")
```

    1.1 using [] - list constructor
    ['banana', 'cherry', 'apple'] ['banana', 2, True, 'a'] ['a', 'aa', 'aaa'] [20, 20, 20, 20, 20, 20, 20, 20, 20, 20] [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    1.2 using "list()"
    ['banana', 'cherry', 'apple'] [1, 2, 3, 4, 5] ['j', 'a', 'n', 'a', 'v', ' ', 'm', 'a', 'k', 'k', 'a', 'r'] [] ['ab', 'bc', 'cd']

    1.3 using list comprehensions
    [2, 4, 6, 8, 10] [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] [132, 144, 156, 168, 180, 192, 204, 216, 228]

    2.1 Index values
    1
    2
    1
    10
    10

    2.2 Slicing
    [4, 6, 8, 10]
    []
    [2, 4, 6, 8, 10]
    [4, 6]
    [2, 4, 6, 8, 10]

    2.3 Step Slicing
    [2, 6, 10]
    [2, 6, 10]
    [8]
    [10, 8]

    2.4 for loop
    2
    4
    6
    8
    10
    3.1 ADD METHODS
    [1, 2, 3, 4, 5] [6, 7, 8, 9, 10]

    [120, 1, 2, 3, 4, 5]
    [120, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [120, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    3.2 DELETE METHODS
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [1, 3, 4, 5, 6, 7, 8, 9]
    [1, 3, 5, 6, 7, 8, 9]
    []

    3.3 OTHER METHODS
    [11, 44, 23, 9, 1, 87, 56, 31, 10, 27, 64, 11, 11, 11]
    [1, 9, 10, 11, 11, 11, 11, 23, 27, 31, 44, 56, 64, 87]
    [87, 64, 56, 44, 31, 27, 23, 11, 11, 11, 11, 10, 9, 1]
    0
    4

    4. Functions - len(), min(), max(), sum(), sorted()
    10 1 10 55
    [1, 9, 10, 11, 11, 11, 11, 23, 27, 31, 44, 56, 64, 87]

    5.1 "in" operator
    True False

    5.2 COPY METHODS
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    5.3 Actual copy methods
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14]

---

## 2. Tuples

Ordered, Immutable, allows duplicates & multi data type

```python
    b1=("max",1,"janav",2,"makkar",3,True)
    b2="max",1,"janav",2,"makkar",3,True # still a tuple without ()
    print(type(b1),type(b2),"\n")

    print(" 0. COMMA IS IMPORTANT ")
    b3=("janav") # not a tuple , just a string
    print(type(b3))
    b4=("janav",) # tuple, comma is important
    print(type(b4),"\n" )

    print(" 1. TUPLE CONSTRUCTOR")
    b5=tuple(["janav",1,"makkar",2,True]) # tuple() is a constructor
    print(b5,"\n")

    print(" 2. TUPLE UNPACKING " )
    b6=("janav",1,"makkar",2,True)
    name,rollno,surname,age,married=b6
    print(name)
    print(rollno)
    print(surname,"\n")

    b9=(0,1,2,3,4,5,6,7,8,9,10)
    a,*b,c=b9
    print(a) # 0
    print(b) # [1,2,3,4,5,6,7,8,9]
    print(c,"\n") # 10

    print(" 3. ACCESSING & SLICING")
    print(b6[0])
    print(b6[1])
    print(b6[-1],"\n")
    # Slicing
    print(b6[0:3])
    print(b6[3:])
    print(b6[:3])
    print(b6[1:-2])
    print(b6[:])
    print(b6[::2]) # step slicing
    print(b6[::-1])
    print(b6[-1:1:-1],"\n")

    print(" 4. MEMEBERSHIP OPERATOR ")
    for i in b6:
        print(i)

    print(1 in b6,"\n")

    print(" 5. BUILT-IN FUNCTIONS/METHODS ") # .count(), .index()
    b7=(tuple("apple")) # b7=("a","p","p","l","e")
    count=b7.count('p') # .count() - returns number of times value in the tuple
    index=b7.index('p') # .index() - returns index of first occurence of the given value
    print(b7)
    print(count)
    print(index,"\n")

    print(" 6. CONVERTING TUPLE TO LIST ")
    b8=list(b6)
    print(b8)
    print(type(b8),type(b6),"\n")

    print("7. TUPLE MORE EFFICIENT THAN LIST")
    import sys
    a28=["janav",1,"makkar",2,True]
    a29=("janav",1,"makkar",2,True)
    print(sys.getsizeof(a28),"bytes","List") # getsizeof(*) - returns size of the object in bytes
    print(sys.getsizeof(a29),"bytes", "Tuple", "\n")

    import timeit
    print(timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=1000000),"List")
    # timeit.timeit(stmt="*",number=*) - returns time taken to execute the statement
    print(timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)",number=1000000),"Tuple","\n")
```


    <class 'tuple'> <class 'tuple'>

     0. COMMA IS IMPORTANT
    <class 'str'>
    <class 'tuple'>

     1. TUPLE CONSTRUCTOR
    ('janav', 1, 'makkar', 2, True)

     2. TUPLE UNPACKING
    janav
    1
    makkar

    0
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    10

     3. ACCESSING & SLICING
    janav
    1
    True

    ('janav', 1, 'makkar')
    (2, True)
    ('janav', 1, 'makkar')
    (1, 'makkar')
    ('janav', 1, 'makkar', 2, True)
    ('janav', 'makkar', True)
    (True, 2, 'makkar', 1, 'janav')
    (True, 2, 'makkar')

     4. MEMEBERSHIP OPERATOR
    janav
    1
    makkar
    2
    True
    True

     5. BUILT-IN FUNCTIONS/METHODS
    ('a', 'p', 'p', 'l', 'e')
    2
    1

     6. CONVERTING TUPLE TO LIST
    ['janav', 1, 'makkar', 2, True]
    <class 'list'> <class 'tuple'>

    7. TUPLE MORE EFFICIENT THAN LIST
    96 bytes List
    80 bytes Tuple

    0.21319740000001275 List
    0.013402999999982512 Tuple

---

## 3. Dictionary

Key-Value pairs, Unordered, Mutable

```python
c1={"name":"janav","rollno":42,"surname":"makkar","age":21,"married":False}
print(c1,"\n")

print("1. DICITIONARY CONSTRUCTOR")
c2=dict(name="janav",surname="makkar",age=21,married=False)
print(c2,"\n")                      # {"name":"janav","surname":"makkar","age":21,"married":False}

print("2. ACCESSING VALUES")
print(c1["name"],"\n")

print("3. ADDING KEY-VALUE PAIRS")
c1["email"]="jm.rocks@mail.com"
print(c1,"\n")

print("4. UPDATING KEY-VALUE PAIRS")
c1["email"]="jm.cool@mail.com"
print(c1,"\n")

print("5. DELETING KEY-VALUE PAIRS") # del, .pop(), .popitem()
del c2["married"]
print(c2,"\n")

c2.pop("age")
print(c2,"\n")

c2.popitem() # removes last key-value pair
print(c2,"\n")

print("6. MEMBERSHIP OPERATOR")

if "name" in c1:
    print(c1["name"])

try:
    print(c1["name"],"\n")
except:
    print("Error","\n")

print("7. LOOPING THROUGH DICTIONARY")
for i in c1: # prints only keys
    print(i)

for i in c1.keys(): # prints only keys
    print(i)

for i in c1.values(): # prints only values
    print(i)

for k,v in c1.items(): # prints key-value pairs
    print(k," - ",v)

print("8. COPYING DICTIONARY") # .copy(), dict(),
c3=c1
c3["surname"]="lakkar"
print("c1- ",c1,"c3- ",c3,"\n") # this happens because c3 is just a reference to c1, actual copy does'nt takes place

c4=c2.copy() # Now this is a copy
c4["surname"]="takkar"
print("c2- ",c2,"c4- ",c4,"\n")

c5=dict(c2) # Now this is a copy
c5["surname"]="jhakkar"
print("c2- ",c2,"c5- ",c5,"\n")


print("9. UPDATING DICTIONARY USING ANOTHER DICTIONARY")

c6={"name":"Max","age":28,"email":"max@wyz.com"}
c7=dict(name="Janav",age=22,email="jm.cool@email.com")
c6.update(c7)
print("c6- ",c6,"\n")


print("10. NESTED DICTIONARIES")

c8={"name":"janav","rollno":42,"surname":"makkar","age":21,"married":False,"address":{"street":"abc","city":"xyz","state":"pqr"}}
print(c8,"\n")


print("11. CONVERTING DICTIONARY TO LIST")

c9=list(c8)
print(c9,"\n")


print("12. CONVERTING DICTIONARY TO TUPLE")

c10=tuple(c8)
print(c10,"\n")


print("13. CONVERTING DICTIONARY TO STRING")

c11=str(c8)
print(c11,"\n")


print("14. DIFFERENT KEY TYPES")

c12=(1,3) # tuple
c13={c12:"Jello"} # tuple as key and string as value
print(c13,"\n") # Only immutable objects can be used as keys, so a list cannot be used as key


```

    {'name': 'janav', 'rollno': 42, 'surname': 'makkar', 'age': 21, 'married': False}

    1. DICITIONARY CONSTRUCTOR
    {'name': 'janav', 'surname': 'makkar', 'age': 21, 'married': False}

    2. ACCESSING VALUES
    janav

    3. ADDING KEY-VALUE PAIRS
    {'name': 'janav', 'rollno': 42, 'surname': 'makkar', 'age': 21, 'married': False, 'email': 'jm.rocks@mail.com'}

    4. UPDATING KEY-VALUE PAIRS
    {'name': 'janav', 'rollno': 42, 'surname': 'makkar', 'age': 21, 'married': False, 'email': 'jm.cool@mail.com'}

    5. DELETING KEY-VALUE PAIRS
    {'name': 'janav', 'surname': 'makkar', 'age': 21}

    {'name': 'janav', 'surname': 'makkar'}

    {'name': 'janav'}

    6. MEMBERSHIP OPERATOR
    janav
    janav

    7. LOOPING THROUGH DICTIONARY
    name
    rollno
    surname
    age
    married
    email
    name
    rollno
    surname
    age
    married
    email
    janav
    42
    makkar
    21
    False
    jm.cool@mail.com
    name  -  janav
    rollno  -  42
    surname  -  makkar
    age  -  21
    married  -  False
    email  -  jm.cool@mail.com
    8. COPYING DICTIONARY
    c1-  {'name': 'janav', 'rollno': 42, 'surname': 'lakkar', 'age': 21, 'married': False, 'email': 'jm.cool@mail.com'} c3-  {'name': 'janav', 'rollno': 42, 'surname': 'lakkar', 'age': 21, 'married': False, 'email': 'jm.cool@mail.com'}

    c2-  {'name': 'janav'} c4-  {'name': 'janav', 'surname': 'takkar'}

    c2-  {'name': 'janav'} c5-  {'name': 'janav', 'surname': 'jhakkar'}

    9. UPDATING DICTIONARY USING ANOTHER DICTIONARY
    c6-  {'name': 'Janav', 'age': 22, 'email': 'jm.cool@email.com'}

    10. NESTED DICTIONARIES
    {'name': 'janav', 'rollno': 42, 'surname': 'makkar', 'age': 21, 'married': False, 'address': {'street': 'abc', 'city': 'xyz', 'state': 'pqr'}}

    11. CONVERTING DICTIONARY TO LIST
    ['name', 'rollno', 'surname', 'age', 'married', 'address']

    12. CONVERTING DICTIONARY TO TUPLE
    ('name', 'rollno', 'surname', 'age', 'married', 'address')

    13. CONVERTING DICTIONARY TO STRING
    {'name': 'janav', 'rollno': 42, 'surname': 'makkar', 'age': 21, 'married': False, 'address': {'street': 'abc', 'city': 'xyz', 'state': 'pqr'}}

    14. DIFFERENT KEY TYPES
    {(1, 3): 'Jello'}

---

## 4. Sets

Unordered, Mutable, No Duplicates, Multi Data types supported

```python
d1={1,3,9,4,33,3,3,1,2}
print(d1,"\n") # output: {1, 2, 3, 4, 33, 9}

d2=set([1,3,9,4,33,3,3,1,2])
print(d2,"\n")

d3=set("janav makkar")
print(d3,"\n") # output: {'a', 'k', 'n', 'j', 'v', 'r', 'm', ' ', 'a'}

print("1. CREATE EMPTY SET")
d4=set() # empty set
d5={} # empty dictionary
print(type(d4),type(d5),"\n")  # output: <class 'set'> <class 'dict'>

print("2. ADD & DELETE ELEMENTS") # add(), remove(), discard(), pop(), clear()
d4.add(1) # add() method
d4.add(2)
d4.add(3)
d4.add(4)
d4.add(5)
print(d4,"\n")

d4.remove(2)    # remove() - removes element if present
print(d4,"\n")

d4.discard(3)   # discard() - removes element if present
print(d4,"\n")

d4.pop()        # pop() - removes random element
print(d4,"\n")

d4.clear()      # clear() - clears whole set
print(d4,"\n")

print("3. ITERATING THROUGH SET")
for i  in d2:
    print(i)

print("4. MEMBERSHIP OPERATOR")
if 33 in d2:
    print("Yes","\n")

print("5. SET OPERATIONS") # union(), intersection(), difference(), symetric_difference()
odds={1,3,5,7,9}
evens={0,2,4,6,8}
primes={2,3,5,7}
union=odds.union(evens) # union: aUb, output:
intersection=odds.intersection(primes) # intersection: a^b

print("Union - ",union,"\n","Intersection - ",intersection,"\n")
print(odds|evens,"\n") # union: aUb

c6={1,2,3,4,5,6,7,8,9,10}
c7={1,2,3,10,11,12}

diff=c6.difference(c7) # difference: a-b
print("Difference - ",diff,"\n")

symetric_diff=c6.symmetric_difference(c7) # symetric difference: aUb-a^b
print("Symetric Difference - ",symetric_diff,"\n")

print("6. UPDATE SET") # update(), intersection_update(), difference_update(), symetric_difference_update()
c6.update(c7) # update() method, adds all elements of c7 to c6
print("Update - ",c6,"\n") # output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

c6.intersection_update(c7) # intersection_update() method, removes all elements from c6 that are not present in c7
print("Intersection - ",c6,"\n") # output: {1, 2, 3, 10}

c6.difference_update(c7) # difference_update() method, removes all elements from c6 that are present in c7
print("Difference - ",c6,"\n")

primes.symmetric_difference_update(odds) # symetric_difference_update() method, removes all elements from c6 that are present in c7 and adds all elements from c7 that are not present in c6
print("Symmetric Difference - ",primes,"\n")

print("7. SUBSET & SUPERSET") # issubset(), issuperset()
c8={1,2,3,4,5,6,7,8,9,10}
c9={1,2,3,10}
print(c9.issubset(c8)) # issubset() method - true
print(c8.issubset(c9)) # issubset() method - false

print(c9.issuperset(c8)) # issuperset() method - false
print(c8.issuperset(c9)) # issuperset() method - true

print("8. DISJOINT")
print(c9.isdisjoint(c8)) # isdisjoint() method - false, true if no common elements

print("9. COPY SET")
c10=c9.copy() # copy() method, creates a copy of the set
print(c10,"\n")

c11=set(c9) # set() constructor
print(c11,"\n")

print("10. FROZEN SET")
# immutable set, but can contain mutable objects and
# union,intersection,difference,symetric_difference can be performed on it
c12=frozenset([1,2,3,4,5,6,7,8,9,10]) # frozen set

print("11. SET COMPREHENSIONS")
c13={i for i in range(1,11)}
print(c13,"\n")

c14={i**2 for i in range(1,11)}
print(c14,"\n")

c15={i for i in range(1,11) if i%2==0}
print(c15,"\n")

```

    {1, 33, 3, 4, 2, 9}

    {1, 33, 3, 4, 2, 9}

    {'r', 'n', 'm', 'a', ' ', 'v', 'k', 'j'}

    1. CREATE EMPTY SET
    <class 'set'> <class 'dict'>

    2. ADD & DELETE ELEMENTS
    {1, 2, 3, 4, 5}

    {1, 3, 4, 5}

    {1, 4, 5}

    {4, 5}

    set()

    3. ITERATING THROUGH SET
    1
    33
    3
    4
    2
    9
    4. MEMBERSHIP OPERATOR
    Yes

    5. SET OPERATIONS
    Union -  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
     Intersection -  {3, 5, 7}

    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    Difference -  {4, 5, 6, 7, 8, 9}

    Symetric Difference -  {4, 5, 6, 7, 8, 9, 11, 12}

    6. UPDATE SET
    Update -  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    Intersection -  {1, 2, 3, 10, 11, 12}

    Difference -  set()

    Symmetric Difference -  {1, 2, 9}

    7. SUBSET & SUPERSET
    True
    False
    False
    True
    8. DISJOINT
    False
    9. COPY SET
    {10, 1, 2, 3}

    {10, 1, 2, 3}

    10. FROZEN SET
    11. SET COMPREHENSIONS
    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}

    {2, 4, 6, 8, 10}

---

## 5. Strings

Ordered, Immutable, Text Representation

```python
print("1. Quotes")
e1="Hello World" # Double quotes
e2='Janav Makkar' # Single quotes
e3="""Hello
    World""" # Triple quotes, used for multiline strings
e6='''Janav\
 Makkar''' # Triple quotes,\ -> escape character, used to ignore the next character, here it ignores the newline character
# \ -> outputs character in same line: Janav Makkar
# \n -> newline character
print(e1,"\n",e2,"\n",e3,"\n",e6)

e4="I'm Janav Makkar" # Single quotes inside double quotes
e5='I\'m Janav Makkar' # Escape character to use single quotes inside single quotes
print(e4,"\n",e5)

print("2. ACCESSING CHARACTERS")
print(e1[0]) # Accessing characters like a list
print(e1[-1],"\n")

# Strings are immutable, so this will give an error
# e1[0]="j"

print("3. SLICING")
print(e1[0:5]) # Slicing
print(e1[6:])
print(e1[:5])
print(e1[1:-1])

print(e1[0:10:2]) # Step Slicing
print(e1[::-1],"\n") # Reverse String

print("4. CONCATINATION")
e7="Hello"
e8="World"
e9=e7+" "+e8 # Concatination
print(e9,"\n")

print("6. ITERATING THROUGH STRING (CHARACTER BY CHARACTER)")
for i in e7:
    print(i)

print("7. CHECK SUBSTRING")
if "el" in e7:
    print("Yes","\n")
else:
    print("No","\n")

print("8. REMOVE WHITESPACES")
e10="       janu          "
print("With spaces - ",e10)

e11=e10.strip()             # strip() method, it does not change the OG string
print("Without spaces - ",e11,"\n")

print("9. CONVERTING TO LOWERCASE & UPPERCASE")
e12="Janav Makkar"
print(e12.lower()) # lower() method, it does not change the OG string due to immutability
print(e12.upper(),"\n") # upper() method, it does not change the OG string (dncos), returns new string (rns)

print("10. STARTS WITH & ENDS WITH")
print(e12.startswith("J")) # startswith() method, (dncos) (rns) (case sensitive)
print(e12.endswith("r"),"\n") # endswith() method, (dncos) (rns) (case sensitive)

print("11. FIND & REPLACE")
print(e12.find("Makkar")) # find() method, (dncos) (rns), returns index of first occurence of the substring
print(e12.find("makkar")) # find() method, (dncos) (rns), returns -1 if substring not found

print(e12.replace("Makkar","Lakkar")) # replace() method, (dncos) (rns), replaces all occurences of the substring
print(e12,"\n")

print("12. COUNT")
print(e12.count("a")) # count() method, (dncos), returns number of times substring occurs in the string
print(e12.count("a",0,5),"\n") # count() method, (dncos), returns number of times substring occurs in the string in the given range

print("13. CONVERTING STRING TO LIST") # split()
e13="How are you doing?"
e14=e13.split() # split() method, (dncos), returns a list of words in the string, space is the default delimiter
print(e14,"\n") # output: ['How', 'are', 'you', 'doing?']

e15="How,are,you,doing?"
e16=e15.split(",") # split() method, (dncos), returns a list of words in the string, comma is the delimiter chosen
print(e16,"\n")

print("14. CONVERTING LIST TO STRING ***") # join()
e17="".join(e14) # join() method, (dncos), returns a string of words in the list, no-space is the delimiter chosen
print(e17,"\n") # output: Howareyoudoing?

e18=" ".join(e14) # join() method, (dncos), returns a string of words in the list, space is the delimiter chosen
print(e18,"\n") # output: How are you doing?

print("15. COMPARING LIST TO STRING OPERATIONS")
from timeit import default_timer as timer
e19=['a']*10000

# bad
start=timer()
e20=""
for i in e19:
    e20+=i
stop=timer()
print("loop method - ",stop-start,"\n")

# good
start=timer()
e21="".join(e19)
stop=timer()
print("join method - ",stop-start,"\n")

print("16. FORMATTING STRINGS")
# % operator - old way
e22_str = "tom"
e22_int=22
e22_float=3.14159265359

e23_str="My var is %s" %e22_str
e23_int="My var is %d" %e22_int
e23_float="My var is %.3f" %e22_float
print(e23_str, e23_int, e23_float,"\n") # output: My var is tom | My var is 22 | My var is 3.142

# format() method - new way
e24_str="My var is {}".format(e22_str)
e24_int="My var is {}".format(e22_int)
e24_float="My var is {:.2f} & {}".format(e22_float,e22_str)
print(e24_str, e24_int, e24_float,"\n") # output: My var is tom | My var is 22 | My var is 3.14 & tom

# f-strings - newest way
e24_str= f"My var is {e22_str}"
e24_int= f"My var is {e22_int}"
e24_float= f"My var is {e22_float} & {e22_int*3}" # expressions can be used inside {}
print(e24_str, e24_int, e24_float,"\n") # output: My var is tom | My var is 22 | My var is 3.14159265359 & 66
```

    1. Quotes
    Hello World
     Janav Makkar
     Hello
        World
     Janav Makkar
    I'm Janav Makkar
     I'm Janav Makkar
    2. ACCESSING CHARACTERS
    H
    d

    3. SLICING
    Hello
    World
    Hello
    ello Worl
    HloWr
    dlroW olleH

    4. CONCATINATION
    Hello World

    6. ITERATING THROUGH STRING (CHARACTER BY CHARACTER)
    H
    e
    l
    l
    o
    7. CHECK SUBSTRING
    Yes

    8. REMOVE WHITESPACES
    With spaces -         janu
    Without spaces -  janu

    9. CONVERTING TO LOWERCASE & UPPERCASE
    janav makkar
    JANAV MAKKAR

    10. STARTS WITH & ENDS WITH
    True
    True

    11. FIND & REPLACE
    6
    -1
    Janav Lakkar
    Janav Makkar

    12. COUNT
    4
    2

    13. CONVERTING STRING TO LIST
    ['How', 'are', 'you', 'doing?']

    ['How', 'are', 'you', 'doing?']

    14. CONVERTING LIST TO STRING ***
    Howareyoudoing?

    How are you doing?

    15. COMPARING LIST TO STRING OPERATIONS
    loop method -  0.007538199999999051

    join method -  0.0002733999999975367

    16. FORMATTING STRINGS
    My var is tom My var is 22 My var is 3.142

    My var is tom My var is 22 My var is 3.14 & tom

    My var is tom My var is 22 My var is 3.14159265359 & 66

---

## 6. Collections

### 6.1 Counter

Dict subclass for counting hashable objects \
Counter('abracadabra') - Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

### 6.2 NamedTuple

Tuple with names for each position  
namedtuple('Name', 'age')

### 6.3 OrderedDict

Dict subclass that remembers the order entries were added \
OrderedDict([('a', 1), ('b', 2), ('c', 3)])

### 6.4 DefaultDict

Dict subclass that calls a factory function to supply missing \values instead of raising KeyError \
d = defaultdict(list)

### 6.5 Deque

List-like container with fast appends and pops on either end \
d = deque('ghi') | d.append('j') | d.appendleft('f') | d.pop() | d.popleft()

```python
print("6.1 COUNTER")
# Counter is a dictionary subclass which helps count hashable objects, like strings, lists, etc.
# It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
# Counts are allowed to be any integer value including zero or negative counts.
# The Counter class is similar to bags or multisets in other languages.
# Counter objects have a dictionary interface except that they return a zero count for missing items instead of raising a KeyError.

from collections import Counter
f1="aaaaaaaaaabbbbbbcccccaabbcddxw"
f2=Counter(f1)
print(f2)       # returns a dictionary with key as the element and value as the count of the element
print(f2.items()) # returns a list of tuples, with each tuple containing the element and its count
print(f2.keys()) # returns a list of keys
print(f2.values()) # returns a list of values
print(f2.most_common(2)) # returns a list of tuples, with the most common n items
print(f2.most_common()[0][0])
print(f2.most_common()[0][1],"\n")

print(list(f2.elements())) # elements - returns an iterator object, with each element repeated as many times as its count

```

    6.1 COUNTER
    Counter({'a': 12, 'b': 8, 'c': 6, 'd': 2, 'x': 1, 'w': 1})
    dict_items([('a', 12), ('b', 8), ('c', 6), ('d', 2), ('x', 1), ('w', 1)])
    dict_keys(['a', 'b', 'c', 'd', 'x', 'w'])
    dict_values([12, 8, 6, 2, 1, 1])
    [('a', 12), ('b', 8)]
    a
    12

    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'x', 'w']

```python
print("6.2 NAMEDTUPLE")
# Namedtuple is a subclass of tuple, which has names for each position in the tuple and a named class
# Creates a class with a fixed set of attributes, which can be accessed by attribute names instead of index numbers
# Creates a class which is more memory efficient than a dictionary
# Creates a struct like data structure

from collections import namedtuple
Point = namedtuple('Point',"x,y") # namedtuple('ClassName','attributes')
p1=Point(1,2)
print(p1)
print(p1.x,p1.y)
```

    6.2 NAMEDTUPLE
    Point(x=1, y=2)
    1 2

```python
print("6.3 ORDEREDDICT")
# OrderedDict is a dictionary subclass which remembers the order in which the key-value pairs were added
# But it is slower than a normal dictionary, because it has to remember the order
# OrderedDict is used when the order of the key-value pairs is important
# OrderedDict is used when we want to create a FIFO queue, LIFO stack, cache.
# But now in python 3.7, normal dictionaries also remember the order in which the key-value pairs were added

from collections import OrderedDict

f3=OrderedDict()
f3['a']=1
f3['b']=2
f3['e']=5 # order is important
f3['c']=3
f3['d']=4

print(f3,"\n")

# normal dictionary
f4={}
f4['a']=1
f4['b']=2
f4['e']=5 # order is important
f4['c']=3
f4['d']=4
print(f4,"\n")
```

    6.3 ORDEREDDICT
    OrderedDict([('a', 1), ('b', 2), ('e', 5), ('c', 3), ('d', 4)])

    {'a': 1, 'b': 2, 'e': 5, 'c': 3, 'd': 4}

```python
print("6.4 DEFAULTDICT")
# Defaultdict is a dictionary subclass which calls a factory function to supply missing values, instead of raising a KeyError
# Defaultdict is used when we want to create a dictionary of lists, dictionaries , sets, tuples, int, float etc.

from collections import defaultdict

f5=defaultdict(int) # int is the factory function, which will be called to supply missing values
f5['a']=1
f5['b']=2
print(f5['a'])
print(f5['x']) # returns 0, because the factory function int is called to supply the missing value

f6=defaultdict(float) # float is the factory function, which will be called to supply missing values
f6['a']=1.1
print(f6['x']) # returns 0.0, because the factory function float is called to supply the missing value

f7=defaultdict(list) # list is the factory function
print(f7['a']) # returns [], because the factory function list is called to supply the missing value

f8={}
f8['a']=1
print(f8['x']) # returns KeyError, because the factory function is not called to supply the missing value
```

    6.4 DEFAULTDICT
    1
    0
    0.0
    []



    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    c:\Users\ASUS\Desktop\Intermediate python.ipynb Cell 22 in <cell line: 22>()
         <a href='vscode-notebook-cell:/c%3A/Users/ASUS/Desktop/Intermediate%20python.ipynb#X30sZmlsZQ%3D%3D?line=19'>20</a> f8={}
         <a href='vscode-notebook-cell:/c%3A/Users/ASUS/Desktop/Intermediate%20python.ipynb#X30sZmlsZQ%3D%3D?line=20'>21</a> f8['a']=1
    ---> <a href='vscode-notebook-cell:/c%3A/Users/ASUS/Desktop/Intermediate%20python.ipynb#X30sZmlsZQ%3D%3D?line=21'>22</a> print(f8['x'])


    KeyError: 'x'

```python
print("6.5 DEQUE")
# Deque is a list-like container with fast appends and pops on either end, Double Ended Queue
# Deque is used when we want to create a queue or a stack
# Deque is faster than a list, because it is implemented as a doubly linked list
# Deque is thread safe, unlike a list
# Deque is used when we want to create a queue or a stack

from collections import deque

f9=deque() # append, appendleft, extend, extendleft, rotate, pop, popleft, clear
f9.append(1) # append() method, adds the value at the back
f9.append(2)
f9.appendleft(3) # appendleft() method, adds the value at the front
f9.appendleft(4)

f9.extend([5,6,7]) # extend() method, adds the list at the back
f9.extendleft([8,9,10]) # extendleft() method, adds the list at the front
print(f9,"\n")

f9.rotate(1) # rotate() method, rotates the deque by the given value, positive value rotates to the right, negative value rotates to the left
print(f9)
f9.rotate(-1)
print(f9)
f9.rotate(2)
print(f9,"\n")

f9.pop() # pop() method, removes the value at the back
print(f9)

f9.popleft() # popleft() method, removes the value at the front
print(f9)
f9.clear() # clear() method, clears the deque
print(f9)
```

    6.5 DEQUE
    deque([10, 9, 8, 4, 3, 1, 2, 5, 6, 7])

    deque([7, 10, 9, 8, 4, 3, 1, 2, 5, 6])
    deque([10, 9, 8, 4, 3, 1, 2, 5, 6, 7])
    deque([6, 7, 10, 9, 8, 4, 3, 1, 2, 5])

    deque([6, 7, 10, 9, 8, 4, 3, 1, 2])
    deque([7, 10, 9, 8, 4, 3, 1, 2])
    deque([])

---

## 7. Iter-Tools

product, permutations, combinations, accumulate, groupby, infinite iterators

```python
print("7.1 Product")
# Product is a function which returns the cartesian product of the given iterables
# Product is used when we want to find all possible combinations of the given iterables

from itertools import product
g1=[1,2]
g2=[3,4]
g4=[9]
g3=product(g1,g2) # product() function, returns the cartesian product of the given iterables
print(g3)
print(list(g3),"\n") # output: [(1, 3), (1, 4), (2, 3), (2, 4)]

g5=product(g1,g2,g4)
print(list(g5),"\n") # output: [(1, 3, 9), (1, 4, 9), (2, 3, 9), (2, 4, 9)]

g6=product(g1,g4,repeat=2) # repeat keyword argument, repeats the given iterables
print(list(g6),"\n") # output: [(1, 9, 1, 9), (1, 9, 2, 9), (2, 9, 1, 9), (2, 9, 2, 9)]

# Program to brute force a 4 digit passcode
from string import digits, ascii_letters, punctuation
print(digits,"\n")
print(*product(digits, repeat=4),"\n")
print(list(product(ascii_letters+digits+punctuation, repeat=2)),"\n") #
```

    7.1 Product
    <itertools.product object at 0x000001F008353740>
    [(1, 3), (1, 4), (2, 3), (2, 4)]

    [(1, 3, 9), (1, 4, 9), (2, 3, 9), (2, 4, 9)]

    [(1, 9, 1, 9), (1, 9, 2, 9), (2, 9, 1, 9), (2, 9, 2, 9)]

    0123456789

    ('0', '0', '0', '0') ('0', '0', '0', '1') ('0', '0', '0', '2') ('0', '0', '0', '3') ('0', '0', '0', '4') ('0', '0', '0', '5') ('0', '0', '0', '6') ('0', '0', '0', '7') ('0', '0', '0', '8') ('0', '0', '0', '9') ('0', '0', '1', '0') ('0', '0', '1', '1') ('0', '0', '1', '2') ('0', '0', '1', '3') ('0', '0', '1', '4') ('0', '0', '1', '5') ('0', '0', '1', '6') ('0', '0', '1', '7') ('0', '0', '1', '8') ('0', '0', '1', '9') ('0', '0', '2', '0') ('0', '0', '2', '1') ('0', '0', '2', '2') ('0', '0', '2', '3') ('0', '0', '2', '4') ('0', '0', '2', '5') ('0', '0', '2', '6') ('0', '0', '2', '7') ('0', '0', '2', '8') ('0', '0', '2', '9') ('0', '0', '3', '0') ('0', '0', '3', '1') ('0', '0', '3', '2') ('0', '0', '3', '3') ('0', '0', '3', '4') ('0', '0', '3', '5') ('0', '0', '3', '6') ('0', '0', '3', '7') ('0', '0', '3', '8') ('0', '0', '3', '9') ('0', '0', '4', '0') ('0', '0', '4', '1') ('0', '0', '4', '2') ('0', '0', '4', '3') ('0', '0', '4', '4') ('0', '0', '4', '5') ('0', '0', '4', '6') ('0', '0', '4', '7') ('0', '0', '4', '8') ('0', '0', '4', '9') ('0', '0', '5', '0') ('0', '0', '5', '1') ('0', '0', '5', '2') ('0', '0', '5', '3') ('0', '0', '5', '4') ('0', '0', '5', '5') ('0', '0', '5', '6') ('0', '0', '5', '7') ('0', '0', '5', '8') ('0', '0', '5', '9') ('0', '0', '6', '0') ('0', '0', '6', '1') ('0', '0', '6', '2') ('0', '0', '6', '3') ('0', '0', '6', '4') ('0', '0', '6', '5') ('0', '0', '6', '6') ('0', '0', '6', '7') ('0', '0', '6', '8') ('0', '0', '6', '9') ('0', '0', '7', '0') ('0', '0', '7', '1') ('0', '0', '7', '2') ('0', '0', '7', '3') ('0', '0', '7', '4') ('0', '0', '7', '5') ('0', '0', '7', '6') ('0', '0', '7', '7') ('0', '0', '7', '8') ('0', '0', '7', '9') ('0', '0', '8', '0') ('0', '0', '8', '1') ('0', '0', '8', '2') ('0', '0', '8', '3') ('0', '0', '8', '4') ('0', '0', '8', '5') ('0', '0', '8', '6') ('0', '0', '8', '7') ('0', '0', '8', '8') ('0', '0', '8', '9') ('0', '0', '9', '0') ('0', '0', '9', '1') ('0', '0', '9', '2') ('0', '0', '9', '3') ('0', '0', '9', '4') ('0', '0', '9', '5') ('0', '0', '9', '6') ('0', '0', '9', '7') ('0', '0', '9', '8') ('0', '0', '9', '9') ('0', '1', '0', '0') ('0', '1', '0', '1') ('0', '1', '0', '2') ('0', '1', '0', '3') ('0', '1', '0', '4') ('0', '1', '0', '5') ('0', '1', '0', '6') ('0', '1', '0', '7') ('0', '1', '0', '8') ('0', '1', '0', '9') ('0', '1', '1', '0') ('0', '1', '1', '1') ('0', '1', '1', '2') ('0', '1', '1', '3') ('0', '1', '1', '4') ('0', '1', '1', '5') ('0', '1', '1', '6') ('0', '1', '1', '7') ('0', '1', '1', '8') ('0', '1', '1', '9') ('0', '1', '2', '0') ('0', '1', '2', '1') ('0', '1', '2', '2') ('0', '1', '2', '3') ('0', '1', '2', '4') ('0', '1', '2', '5') ('0', '1', '2', '6') ('0', '1', '2', '7') ('0', '1', '2', '8') ('0', '1', '2', '9') ('0', '1', '3', '0') ('0', '1', '3', '1') ('0', '1', '3', '2') ('0', '1', '3', '3') ('0', '1', '3', '4') ('0', '1', '3', '5') ('0', '1', '3', '6') ('0', '1', '3', '7') ('0', '1', '3', '8') ('0', '1', '3', '9') ('0', '1', '4', '0') ('0', '1', '4', '1') ('0', '1', '4', '2') ('0', '1', '4', '3') ('0', '1', '4', '4') ('0', '1', '4', '5') ('0', '1', '4', '6') ('0', '1', '4', '7') ('0', '1', '4', '8') ('0', '1', '4', '9') ('0', '1', '5', '0') ('0', '1', '5', '1') ('0', '1', '5', '2') ('0', '1', '5', '3') ('0', '1', '5', '4') ('0', '1', '5', '5') ('0', '1', '5', '6') ('0', '1', '5', '7') ('0', '1', '5', '8') ('0', '1', '5', '9') ('0', '1', '6', '0') ('0', '1', '6', '1') ('0', '1', '6', '2') ('0', '1', '6', '3') ('0', '1', '6', '4') ('0', '1', '6', '5') ('0', '1', '6', '6') ('0', '1', '6', '7') ('0', '1', '6', '8') ('0', '1', '6', '9') ('0', '1', '7', '0') ('0', '1', '7', '1') ('0', '1', '7', '2') ('0', '1', '7', '3') ('0', '1', '7', '4') ('0', '1', '7', '5') ('0', '1', '7', '6') ('0', '1', '7', '7') ('0', '1', '7', '8') ('0', '1', '7', '9') ('0', '1', '8', '0') ('0', '1', '8', '1') ('0', '1', '8', '2') ('0', '1', '8', '3') ('0', '1', '8', '4') ('0', '1', '8', '5') ('0', '1', '8', '6') ('0', '1', '8', '7') ('0', '1', '8', '8') ('0', '1', '8', '9') ('0', '1', '9', '0') ('0', '1', '9', '1') ('0', '1', '9', '2') ('0', '1', '9', '3') ('0', '1', '9', '4') ('0', '1', '9', '5') ('0', '1', '9', '6') ('0', '1', '9', '7') ('0', '1', '9', '8') ('0', '1', '9', '9') ('0', '2', '0', '0') ('0', '2', '0', '1') ('0', '2', '0', '2') ('0', '2', '0', '3') ('0', '2', '0', '4') ('0', '2', '0', '5') ('0', '2', '0', '6') ('0', '2', '0', '7') ('0', '2', '0', '8') ('0', '2', '0', '9') ('0', '2', '1', '0') ('0', '2', '1', '1') ('0', '2', '1', '2') ('0', '2', '1', '3') ('0', '2', '1', '4') ('0', '2', '1', '5') ('0', '2', '1', '6') ('0', '2', '1', '7') ('0', '2', '1', '8') ('0', '2', '1', '9') ('0', '2', '2', '0') ('0', '2', '2', '1') ('0', '2', '2', '2') ('0', '2', '2', '3') ('0', '2', '2', '4') ('0', '2', '2', '5') ('0', '2', '2', '6') ('0', '2', '2', '7') ('0', '2', '2', '8') ('0', '2', '2', '9') ('0', '2', '3', '0') ('0', '2', '3', '1') ('0', '2', '3', '2') ('0', '2', '3', '3') ('0', '2', '3', '4') ('0', '2', '3', '5') ('0', '2', '3', '6') ('0', '2', '3', '7') ('0', '2', '3', '8') ('0', '2', '3', '9') ('0', '2', '4', '0') ('0', '2', '4', '1') ('0', '2', '4', '2') ('0', '2', '4', '3') ('0', '2', '4', '4') ('0', '2', '4', '5') ('0', '2', '4', '6') ('0', '2', '4', '7') ('0', '2', '4', '8') ('0', '2', '4', '9') ('0', '2', '5', '0') ('0', '2', '5', '1') ('0', '2', '5', '2') ('0', '2', '5', '3') ('0', '2', '5', '4') ('0', '2', '5', '5') ('0', '2', '5', '6') ('0', '2', '5', '7') ('0', '2', '5', '8') ('0', '2', '5', '9') ('0', '2', '6', '0') ('0', '2', '6', '1') ('0', '2', '6', '2') ('0', '2', '6', '3') ('0', '2', '6', '4') ('0', '2', '6', '5') ('0', '2', '6', '6') ('0', '2', '6', '7') ('0', '2', '6', '8') ('0', '2', '6', '9') ('0', '2', '7', '0') ('0', '2', '7', '1') ('0', '2', '7', '2') ('0', '2', '7', '3') ('0', '2', '7', '4') ('0', '2', '7', '5') ('0', '2', '7', '6') ('0', '2', '7', '7') ('0', '2', '7', '8') ('0', '2', '7', '9') ('0', '2', '8', '0') ('0', '2', '8', '1') ('0', '2', '8', '2') ('0', '2', '8', '3') ('0', '2', '8', '4') ('0', '2', '8', '5') ('0', '2', '8', '6') ('0', '2', '8', '7') ('0', '2', '8', '8') ('0', '2', '8', '9') ('0', '2', '9', '0') ('0', '2', '9', '1') ('0', '2', '9', '2') ('0', '2', '9', '3') ('0', '2', '9', '4') ('0', '2', '9', '5') ('0', '2', '9', '6') ('0', '2', '9', '7') ('0', '2', '9', '8') ('0', '2', '9', '9') ('0', '3', '0', '0') ('0', '3', '0', '1') ('0', '3', '0', '2') ('0', '3', '0', '3') ('0', '3', '0', '4') ('0', '3', '0', '5') ('0', '3', '0', '6') ('0', '3', '0', '7') ('0', '3', '0', '8') ('0', '3', '0', '9') ('0', '3', '1', '0') ('0', '3', '1', '1') ('0', '3', '1', '2') ('0', '3', '1', '3') ('0', '3', '1', '4') ('0', '3', '1', '5') ('0', '3', '1', '6') ('0', '3', '1', '7') ('0', '3', '1', '8') ('0', '3', '1', '9') ('0', '3', '2', '0') ('0', '3', '2', '1') ('0', '3', '2', '2') ('0', '3', '2', '3') ('0', '3', '2', '4') ('0', '3', '2', '5') ('0', '3', '2', '6') ('0', '3', '2', '7') ('0', '3', '2', '8') ('0', '3', '2', '9') ('0', '3', '3', '0') ('0', '3', '3', '1') ('0', '3', '3', '2') ('0', '3', '3', '3') ('0', '3', '3', '4') ('0', '3', '3', '5') ('0', '3', '3', '6') ('0', '3', '3', '7') ('0', '3', '3', '8') ('0', '3', '3', '9') ('0', '3', '4', '0') ('0', '3', '4', '1') ('0', '3', '4', '2') ('0', '3', '4', '3') ('0', '3', '4', '4') ('0', '3', '4', '5') ('0', '3', '4', '6') ('0', '3', '4', '7') ('0', '3', '4', '8') ('0', '3', '4', '9') ('0', '3', '5', '0') ('0', '3', '5', '1') ('0', '3', '5', '2') ('0', '3', '5', '3') ('0', '3', '5', '4') ('0', '3', '5', '5') ('0', '3', '5', '6') ('0', '3', '5', '7') ('0', '3', '5', '8') ('0', '3', '5', '9') ('0', '3', '6', '0') ('0', '3', '6', '1') ('0', '3', '6', '2') ('0', '3', '6', '3') ('0', '3', '6', '4') ('0', '3', '6', '5') ('0', '3', '6', '6') ('0', '3', '6', '7') ('0', '3', '6', '8') ('0', '3', '6', '9') ('0', '3', '7', '0') ('0', '3', '7', '1') ('0', '3', '7', '2') ('0', '3', '7', '3') ('0', '3', '7', '4') ('0', '3', '7', '5') ('0', '3', '7', '6') ('0', '3', '7', '7') ('0', '3', '7', '8') ('0', '3', '7', '9') ('0', '3', '8', '0') ('0', '3', '8', '1') ('0', '3', '8', '2') ('0', '3', '8', '3') ('0', '3', '8', '4') ('0', '3', '8', '5') ('0', '3', '8', '6') ('0', '3', '8', '7') ('0', '3', '8', '8') ('0', '3', '8', '9') ('0', '3', '9', '0') ('0', '3', '9', '1') ('0', '3', '9', '2') ('0', '3', '9', '3') ('0', '3', '9', '4') ('0', '3', '9', '5') ('0', '3', '9', '6') ('0', '3', '9', '7') ('0', '3', '9', '8') ('0', '3', '9', '9') ('0', '4', '0', '0') ('0', '4', '0', '1') ('0', '4', '0', '2') ('0', '4', '0', '3') ('0', '4', '0', '4') ('0', '4', '0', '5') ('0', '4', '0', '6') ('0', '4', '0', '7') ('0', '4', '0', '8') ('0', '4', '0', '9') ('0', '4', '1', '0') ('0', '4', '1', '1') ('0', '4', '1', '2') ('0', '4', '1', '3') ('0', '4', '1', '4') ('0', '4', '1', '5') ('0', '4', '1', '6') ('0', '4', '1', '7') ('0', '4', '1', '8') ('0', '4', '1', '9') ('0', '4', '2', '0') ('0', '4', '2', '1') ('0', '4', '2', '2') ('0', '4', '2', '3') ('0', '4', '2', '4') ('0', '4', '2', '5') ('0', '4', '2', '6') ('0', '4', '2', '7') ('0', '4', '2', '8') ('0', '4', '2', '9') ('0', '4', '3', '0') ('0', '4', '3', '1') ('0', '4', '3', '2') ('0', '4', '3', '3') ('0', '4', '3', '4') ('0', '4', '3', '5') ('0', '4', '3', '6') ('0', '4', '3', '7') ('0', '4', '3', '8') ('0', '4', '3', '9') ('0', '4', '4', '0') ('0', '4', '4', '1') ('0', '4', '4', '2') ('0', '4', '4', '3') ('0', '4', '4', '4') ('0', '4', '4', '5') ('0', '4', '4', '6') ('0', '4', '4', '7') ('0', '4', '4', '8') ('0', '4', '4', '9') ('0', '4', '5', '0') ('0', '4', '5', '1') ('0', '4', '5', '2') ('0', '4', '5', '3') ('0', '4', '5', '4') ('0', '4', '5', '5') ('0', '4', '5', '6') ('0', '4', '5', '7') ('0', '4', '5', '8') ('0', '4', '5', '9') ('0', '4', '6', '0') ('0', '4', '6', '1') ('0', '4', '6', '2') ('0', '4', '6', '3') ('0', '4', '6', '4') ('0', '4', '6', '5') ('0', '4', '6', '6') ('0', '4', '6', '7') ('0', '4', '6', '8') ('0', '4', '6', '9') ('0', '4', '7', '0') ('0', '4', '7', '1') ('0', '4', '7', '2') ('0', '4', '7', '3') ('0', '4', '7', '4') ('0', '4', '7', '5') ('0', '4', '7', '6') ('0', '4', '7', '7') ('0', '4', '7', '8') ('0', '4', '7', '9') ('0', '4', '8', '0') ('0', '4', '8', '1') ('0', '4', '8', '2') ('0', '4', '8', '3') ('0', '4', '8', '4') ('0', '4', '8', '5') ('0', '4', '8', '6') ('0', '4', '8', '7') ('0', '4', '8', '8') ('0', '4', '8', '9') ('0', '4', '9', '0') ('0', '4', '9', '1') ('0', '4', '9', '2') ('0', '4', '9', '3') ('0', '4', '9', '4') ('0', '4', '9', '5') ('0', '4', '9', '6') ('0', '4', '9', '7') ('0', '4', '9', '8') ('0', '4', '9', '9') ('0', '5', '0', '0') ('0', '5', '0', '1') ('0', '5', '0', '2') ('0', '5', '0', '3') ('0', '5', '0', '4') ('0', '5', '0', '5') ('0', '5', '0', '6') ('0', '5', '0', '7') ('0', '5', '0', '8') ('0', '5', '0', '9') ('0', '5', '1', '0') ('0', '5', '1', '1') ('0', '5', '1', '2') ('0', '5', '1', '3') ('0', '5', '1', '4') ('0', '5', '1', '5') ('0', '5', '1', '6') ('0', '5', '1', '7') ('0', '5', '1', '8') ('0', '5', '1', '9') ('0', '5', '2', '0') ('0', '5', '2', '1') ('0', '5', '2', '2') ('0', '5', '2', '3') ('0', '5', '2', '4') ('0', '5', '2', '5') ('0', '5', '2', '6') ('0', '5', '2', '7') ('0', '5', '2', '8') ('0', '5', '2', '9') ('0', '5', '3', '0') ('0', '5', '3', '1') ('0', '5', '3', '2') ('0', '5', '3', '3') ('0', '5', '3', '4') ('0', '5', '3', '5') ('0', '5', '3', '6') ('0', '5', '3', '7') ('0', '5', '3', '8') ('0', '5', '3', '9') ('0', '5', '4', '0') ('0', '5', '4', '1') ('0', '5', '4', '2') ('0', '5', '4', '3') ('0', '5', '4', '4') ('0', '5', '4', '5') ('0', '5', '4', '6') ('0', '5', '4', '7') ('0', '5', '4', '8') ('0', '5', '4', '9') ('0', '5', '5', '0') ('0', '5', '5', '1') ('0', '5', '5', '2') ('0', '5', '5', '3') ('0', '5', '5', '4') ('0', '5', '5', '5') ('0', '5', '5', '6') ('0', '5', '5', '7') ('0', '5', '5', '8') ('0', '5', '5', '9') ('0', '5', '6', '0') ('0', '5', '6', '1') ('0', '5', '6', '2') ('0', '5', '6', '3') ('0', '5', '6', '4') ('0', '5', '6', '5') ('0', '5', '6', '6') ('0', '5', '6', '7') ('0', '5', '6', '8') ('0', '5', '6', '9') ('0', '5', '7', '0') ('0', '5', '7', '1') ('0', '5', '7', '2') ('0', '5', '7', '3') ('0', '5', '7', '4') ('0', '5', '7', '5') ('0', '5', '7', '6') ('0', '5', '7', '7') ('0', '5', '7', '8') ('0', '5', '7', '9') ('0', '5', '8', '0') ('0', '5', '8', '1') ('0', '5', '8', '2') ('0', '5', '8', '3') ('0', '5', '8', '4') ('0', '5', '8', '5') ('0', '5', '8', '6') ('0', '5', '8', '7') ('0', '5', '8', '8') ('0', '5', '8', '9') ('0', '5', '9', '0') ('0', '5', '9', '1') ('0', '5', '9', '2') ('0', '5', '9', '3') ('0', '5', '9', '4') ('0', '5', '9', '5') ('0', '5', '9', '6') ('0', '5', '9', '7') ('0', '5', '9', '8') ('0', '5', '9', '9') ('0', '6', '0', '0') ('0', '6', '0', '1') ('0', '6', '0', '2') ('0', '6', '0', '3') ('0', '6', '0', '4') ('0', '6', '0', '5') ('0', '6', '0', '6') ('0', '6', '0', '7') ('0', '6', '0', '8') ('0', '6', '0', '9') ('0', '6', '1', '0') ('0', '6', '1', '1') ('0', '6', '1', '2') ('0', '6', '1', '3') ('0', '6', '1', '4') ('0', '6', '1', '5') ('0', '6', '1', '6') ('0', '6', '1', '7') ('0', '6', '1', '8') ('0', '6', '1', '9') ('0', '6', '2', '0') ('0', '6', '2', '1') ('0', '6', '2', '2') ('0', '6', '2', '3') ('0', '6', '2', '4') ('0', '6', '2', '5') ('0', '6', '2', '6') ('0', '6', '2', '7') ('0', '6', '2', '8') ('0', '6', '2', '9') ('0', '6', '3', '0') ('0', '6', '3', '1') ('0', '6', '3', '2') ('0', '6', '3', '3') ('0', '6', '3', '4') ('0', '6', '3', '5') ('0', '6', '3', '6') ('0', '6', '3', '7') ('0', '6', '3', '8') ('0', '6', '3', '9') ('0', '6', '4', '0') ('0', '6', '4', '1') ('0', '6', '4', '2') ('0', '6', '4', '3') ('0', '6', '4', '4') ('0', '6', '4', '5') ('0', '6', '4', '6') ('0', '6', '4', '7') ('0', '6', '4', '8') ('0', '6', '4', '9') ('0', '6', '5', '0') ('0', '6', '5', '1') ('0', '6', '5', '2') ('0', '6', '5', '3') ('0', '6', '5', '4') ('0', '6', '5', '5') ('0', '6', '5', '6') ('0', '6', '5', '7') ('0', '6', '5', '8') ('0', '6', '5', '9') ('0', '6', '6', '0') ('0', '6', '6', '1') ('0', '6', '6', '2') ('0', '6', '6', '3') ('0', '6', '6', '4') ('0', '6', '6', '5') ('0', '6', '6', '6') ('0', '6', '6', '7') ('0', '6', '6', '8') ('0', '6', '6', '9') ('0', '6', '7', '0') ('0', '6', '7', '1') ('0', '6', '7', '2') ('0', '6', '7', '3') ('0', '6', '7', '4') ('0', '6', '7', '5') ('0', '6', '7', '6') ('0', '6', '7', '7') ('0', '6', '7', '8') ('0', '6', '7', '9') ('0', '6', '8', '0') ('0', '6', '8', '1') ('0', '6', '8', '2') ('0', '6', '8', '3') ('0', '6', '8', '4') ('0', '6', '8', '5') ('0', '6', '8', '6') ('0', '6', '8', '7') ('0', '6', '8', '8') ('0', '6', '8', '9') ('0', '6', '9', '0') ('0', '6', '9', '1') ('0', '6', '9', '2') ('0', '6', '9', '3') ('0', '6', '9', '4') ('0', '6', '9', '5') ('0', '6', '9', '6') ('0', '6', '9', '7') ('0', '6', '9', '8') ('0', '6', '9', '9') ('0', '7', '0', '0') ('0', '7', '0', '1') ('0', '7', '0', '2') ('0', '7', '0', '3') ('0', '7', '0', '4') ('0', '7', '0', '5') ('0', '7', '0', '6') ('0', '7', '0', '7') ('0', '7', '0', '8') ('0', '7', '0', '9') ('0', '7', '1', '0') ('0', '7', '1', '1') ('0', '7', '1', '2') ('0', '7', '1', '3') ('0', '7', '1', '4') ('0', '7', '1', '5') ('0', '7', '1', '6') ('0', '7', '1', '7') ('0', '7', '1', '8') ('0', '7', '1', '9') ('0', '7', '2', '0') ('0', '7', '2', '1') ('0', '7', '2', '2') ('0', '7', '2', '3') ('0', '7', '2', '4') ('0', '7', '2', '5') ('0', '7', '2', '6') ('0', '7', '2', '7') ('0', '7', '2', '8') ('0', '7', '2', '9') ('0', '7', '3', '0') ('0', '7', '3', '1') ('0', '7', '3', '2') ('0', '7', '3', '3') ('0', '7', '3', '4') ('0', '7', '3', '5') ('0', '7', '3', '6') ('0', '7', '3', '7') ('0', '7', '3', '8') ('0', '7', '3', '9') ('0', '7', '4', '0') ('0', '7', '4', '1') ('0', '7', '4', '2') ('0', '7', '4', '3') ('0', '7', '4', '4') ('0', '7', '4', '5') ('0', '7', '4', '6') ('0', '7', '4', '7') ('0', '7', '4', '8') ('0', '7', '4', '9') ('0', '7', '5', '0') ('0', '7', '5', '1') ('0', '7', '5', '2') ('0', '7', '5', '3') ('0', '7', '5', '4') ('0', '7', '5', '5') ('0', '7', '5', '6') ('0', '7', '5', '7') ('0', '7', '5', '8') ('0', '7', '5', '9') ('0', '7', '6', '0') ('0', '7', '6', '1') ('0', '7', '6', '2') ('0', '7', '6', '3') ('0', '7', '6', '4') ('0', '7', '6', '5') ('0', '7', '6', '6') ('0', '7', '6', '7') ('0', '7', '6', '8') ('0', '7', '6', '9') ('0', '7', '7', '0') ('0', '7', '7', '1') ('0', '7', '7', '2') ('0', '7', '7', '3') ('0', '7', '7', '4') ('0', '7', '7', '5') ('0', '7', '7', '6') ('0', '7', '7', '7') ('0', '7', '7', '8') ('0', '7', '7', '9') ('0', '7', '8', '0') ('0', '7', '8', '1') ('0', '7', '8', '2') ('0', '7', '8', '3') ('0', '7', '8', '4') ('0', '7', '8', '5') ('0', '7', '8', '6') ('0', '7', '8', '7') ('0', '7', '8', '8') ('0', '7', '8', '9') ('0', '7', '9', '0') ('0', '7', '9', '1') ('0', '7', '9', '2') ('0', '7', '9', '3') ('0', '7', '9', '4') ('0', '7', '9', '5') ('0', '7', '9', '6') ('0', '7', '9', '7') ('0', '7', '9', '8') ('0', '7', '9', '9') ('0', '8', '0', '0') ('0', '8', '0', '1') ('0', '8', '0', '2') ('0', '8', '0', '3') ('0', '8', '0', '4') ('0', '8', '0', '5') ('0', '8', '0', '6') ('0', '8', '0', '7') ('0', '8', '0', '8') ('0', '8', '0', '9') ('0', '8', '1', '0') ('0', '8', '1', '1') ('0', '8', '1', '2') ('0', '8', '1', '3') ('0', '8', '1', '4') ('0', '8', '1', '5') ('0', '8', '1', '6') ('0', '8', '1', '7') ('0', '8', '1', '8') ('0', '8', '1', '9') ('0', '8', '2', '0') ('0', '8', '2', '1') ('0', '8', '2', '2') ('0', '8', '2', '3') ('0', '8', '2', '4') ('0', '8', '2', '5') ('0', '8', '2', '6') ('0', '8', '2', '7') ('0', '8', '2', '8') ('0', '8', '2', '9') ('0', '8', '3', '0') ('0', '8', '3', '1') ('0', '8', '3', '2') ('0', '8', '3', '3') ('0', '8', '3', '4') ('0', '8', '3', '5') ('0', '8', '3', '6') ('0', '8', '3', '7') ('0', '8', '3', '8') ('0', '8', '3', '9') ('0', '8', '4', '0') ('0', '8', '4', '1') ('0', '8', '4', '2') ('0', '8', '4', '3') ('0', '8', '4', '4') ('0', '8', '4', '5') ('0', '8', '4', '6') ('0', '8', '4', '7') ('0', '8', '4', '8') ('0', '8', '4', '9') ('0', '8', '5', '0') ('0', '8', '5', '1') ('0', '8', '5', '2') ('0', '8', '5', '3') ('0', '8', '5', '4') ('0', '8', '5', '5') ('0', '8', '5', '6') ('0', '8', '5', '7') ('0', '8', '5', '8') ('0', '8', '5', '9') ('0', '8', '6', '0') ('0', '8', '6', '1') ('0', '8', '6', '2') ('0', '8', '6', '3') ('0', '8', '6', '4') ('0', '8', '6', '5') ('0', '8', '6', '6') ('0', '8', '6', '7') ('0', '8', '6', '8') ('0', '8', '6', '9') ('0', '8', '7', '0') ('0', '8', '7', '1') ('0', '8', '7', '2') ('0', '8', '7', '3') ('0', '8', '7', '4') ('0', '8', '7', '5') ('0', '8', '7', '6') ('0', '8', '7', '7') ('0', '8', '7', '8') ('0', '8', '7', '9') ('0', '8', '8', '0') ('0', '8', '8', '1') ('0', '8', '8', '2') ('0', '8', '8', '3') ('0', '8', '8', '4') ('0', '8', '8', '5') ('0', '8', '8', '6') ('0', '8', '8', '7') ('0', '8', '8', '8') ('0', '8', '8', '9') ('0', '8', '9', '0') ('0', '8', '9', '1') ('0', '8', '9', '2') ('0', '8', '9', '3') ('0', '8', '9', '4') ('0', '8', '9', '5') ('0', '8', '9', '6') ('0', '8', '9', '7') ('0', '8', '9', '8') ('0', '8', '9', '9') ('0', '9', '0', '0') ('0', '9', '0', '1') ('0', '9', '0', '2') ('0', '9', '0', '3') ('0', '9', '0', '4') ('0', '9', '0', '5') ('0', '9', '0', '6') ('0', '9', '0', '7') ('0', '9', '0', '8') ('0', '9', '0', '9') ('0', '9', '1', '0') ('0', '9', '1', '1') ('0', '9', '1', '2') ('0', '9', '1', '3') ('0', '9', '1', '4') ('0', '9', '1', '5') ('0', '9', '1', '6') ('0', '9', '1', '7') ('0', '9', '1', '8') ('0', '9', '1', '9') ('0', '9', '2', '0') ('0', '9', '2', '1') ('0', '9', '2', '2') ('0', '9', '2', '3') ('0', '9', '2', '4') ('0', '9', '2', '5') ('0', '9', '2', '6') ('0', '9', '2', '7') ('0', '9', '2', '8') ('0', '9', '2', '9') ('0', '9', '3', '0') ('0', '9', '3', '1') ('0', '9', '3', '2') ('0', '9', '3', '3') ('0', '9', '3', '4') ('0', '9', '3', '5') ('0', '9', '3', '6') ('0', '9', '3', '7') ('0', '9', '3', '8') ('0', '9', '3', '9') ('0', '9', '4', '0') ('0', '9', '4', '1') ('0', '9', '4', '2') ('0', '9', '4', '3') ('0', '9', '4', '4') ('0', '9', '4', '5') ('0', '9', '4', '6') ('0', '9', '4', '7') ('0', '9', '4', '8') ('0', '9', '4', '9') ('0', '9', '5', '0') ('0', '9', '5', '1') ('0', '9', '5', '2') ('0', '9', '5', '3') ('0', '9', '5', '4') ('0', '9', '5', '5') ('0', '9', '5', '6') ('0', '9', '5', '7') ('0', '9', '5', '8') ('0', '9', '5', '9') ('0', '9', '6', '0') ('0', '9', '6', '1') ('0', '9', '6', '2') ('0', '9', '6', '3') ('0', '9', '6', '4') ('0', '9', '6', '5') ('0', '9', '6', '6') ('0', '9', '6', '7') ('0', '9', '6', '8') ('0', '9', '6', '9') ('0', '9', '7', '0') ('0', '9', '7', '1') ('0', '9', '7', '2') ('0', '9', '7', '3') ('0', '9', '7', '4') ('0', '9', '7', '5') ('0', '9', '7', '6') ('0', '9', '7', '7') ('0', '9', '7', '8') ('0', '9', '7', '9') ('0', '9', '8', '0') ('0', '9', '8', '1') ('0', '9', '8', '2') ('0', '9', '8', '3') ('0', '9', '8', '4') ('0', '9', '8', '5') ('0', '9', '8', '6') ('0', '9', '8', '7') ('0', '9', '8', '8') ('0', '9', '8', '9') ('0', '9', '9', '0') ('0', '9', '9', '1') ('0', '9', '9', '2') ('0', '9', '9', '3') ('0', '9', '9', '4') ('0', '9', '9', '5') ('0', '9', '9', '6') ('0', '9', '9', '7') ('0', '9', '9', '8') ('0', '9', '9', '9') ('1', '0', '0', '0') ('1', '0', '0', '1') ('1', '0', '0', '2') ('1', '0', '0', '3') ('1', '0', '0', '4') ('1', '0', '0', '5') ('1', '0', '0', '6') ('1', '0', '0', '7') ('1', '0', '0', '8') ('1', '0', '0', '9') ('1', '0', '1', '0') ('1', '0', '1', '1') ('1', '0', '1', '2') ('1', '0', '1', '3') ('1', '0', '1', '4') ('1', '0', '1', '5') ('1', '0', '1', '6') ('1', '0', '1', '7') ('1', '0', '1', '8') ('1', '0', '1', '9') ('1', '0', '2', '0') ('1', '0', '2', '1') ('1', '0', '2', '2') ('1', '0', '2', '3') ('1', '0', '2', '4') ('1', '0', '2', '5') ('1', '0', '2', '6') ('1', '0', '2', '7') ('1', '0', '2', '8') ('1', '0', '2', '9') ('1', '0', '3', '0') ('1', '0', '3', '1') ('1', '0', '3', '2') ('1', '0', '3', '3') ('1', '0', '3', '4') ('1', '0', '3', '5') ('1', '0', '3', '6') ('1', '0', '3', '7') ('1', '0', '3', '8') ('1', '0', '3', '9') ('1', '0', '4', '0') ('1', '0', '4', '1') ('1', '0', '4', '2') ('1', '0', '4', '3') ('1', '0', '4', '4') ('1', '0', '4', '5') ('1', '0', '4', '6') ('1', '0', '4', '7') ('1', '0', '4', '8') ('1', '0', '4', '9') ('1', '0', '5', '0') ('1', '0', '5', '1') ('1', '0', '5', '2') ('1', '0', '5', '3') ('1', '0', '5', '4') ('1', '0', '5', '5') ('1', '0', '5', '6') ('1', '0', '5', '7') ('1', '0', '5', '8') ('1', '0', '5', '9') ('1', '0', '6', '0') ('1', '0', '6', '1') ('1', '0', '6', '2') ('1', '0', '6', '3') ('1', '0', '6', '4') ('1', '0', '6', '5') ('1', '0', '6', '6') ('1', '0', '6', '7') ('1', '0', '6', '8') ('1', '0', '6', '9') ('1', '0', '7', '0') ('1', '0', '7', '1') ('1', '0', '7', '2') ('1', '0', '7', '3') ('1', '0', '7', '4') ('1', '0', '7', '5') ('1', '0', '7', '6') ('1', '0', '7', '7') ('1', '0', '7', '8') ('1', '0', '7', '9') ('1', '0', '8', '0') ('1', '0', '8', '1') ('1', '0', '8', '2') ('1', '0', '8', '3') ('1', '0', '8', '4') ('1', '0', '8', '5') ('1', '0', '8', '6') ('1', '0', '8', '7') ('1', '0', '8', '8') ('1', '0', '8', '9') ('1', '0', '9', '0') ('1', '0', '9', '1') ('1', '0', '9', '2') ('1', '0', '9', '3') ('1', '0', '9', '4') ('1', '0', '9', '5') ('1', '0', '9', '6') ('1', '0', '9', '7') ('1', '0', '9', '8') ('1', '0', '9', '9') ('1', '1', '0', '0') ('1', '1', '0', '1') ('1', '1', '0', '2') ('1', '1', '0', '3') ('1', '1', '0', '4') ('1', '1', '0', '5') ('1', '1', '0', '6') ('1', '1', '0', '7') ('1', '1', '0', '8') ('1', '1', '0', '9') ('1', '1', '1', '0') ('1', '1', '1', '1') ('1', '1', '1', '2') ('1', '1', '1', '3') ('1', '1', '1', '4') ('1', '1', '1', '5') ('1', '1', '1', '6') ('1', '1', '1', '7') ('1', '1', '1', '8') ('1', '1', '1', '9') ('1', '1', '2', '0') ('1', '1', '2', '1') ('1', '1', '2', '2') ('1', '1', '2', '3') ('1', '1', '2', '4') ('1', '1', '2', '5') ('1', '1', '2', '6') ('1', '1', '2', '7') ('1', '1', '2', '8') ('1', '1', '2', '9') ('1', '1', '3', '0') ('1', '1', '3', '1') ('1', '1', '3', '2') ('1', '1', '3', '3') ('1', '1', '3', '4') ('1', '1', '3', '5') ('1', '1', '3', '6') ('1', '1', '3', '7') ('1', '1', '3', '8') ('1', '1', '3', '9') ('1', '1', '4', '0') ('1', '1', '4', '1') ('1', '1', '4', '2') ('1', '1', '4', '3') ('1', '1', '4', '4') ('1', '1', '4', '5') ('1', '1', '4', '6') ('1', '1', '4', '7') ('1', '1', '4', '8') ('1', '1', '4', '9') ('1', '1', '5', '0') ('1', '1', '5', '1') ('1', '1', '5', '2') ('1', '1', '5', '3') ('1', '1', '5', '4') ('1', '1', '5', '5') ('1', '1', '5', '6') ('1', '1', '5', '7') ('1', '1', '5', '8') ('1', '1', '5', '9') ('1', '1', '6', '0') ('1', '1', '6', '1') ('1', '1', '6', '2') ('1', '1', '6', '3') ('1', '1', '6', '4') ('1', '1', '6', '5') ('1', '1', '6', '6') ('1', '1', '6', '7') ('1', '1', '6', '8') ('1', '1', '6', '9') ('1', '1', '7', '0') ('1', '1', '7', '1') ('1', '1', '7', '2') ('1', '1', '7', '3') ('1', '1', '7', '4') ('1', '1', '7', '5') ('1', '1', '7', '6') ('1', '1', '7', '7') ('1', '1', '7', '8') ('1', '1', '7', '9') ('1', '1', '8', '0') ('1', '1', '8', '1') ('1', '1', '8', '2') ('1', '1', '8', '3') ('1', '1', '8', '4') ('1', '1', '8', '5') ('1', '1', '8', '6') ('1', '1', '8', '7') ('1', '1', '8', '8') ('1', '1', '8', '9') ('1', '1', '9', '0') ('1', '1', '9', '1') ('1', '1', '9', '2') ('1', '1', '9', '3') ('1', '1', '9', '4') ('1', '1', '9', '5') ('1', '1', '9', '6') ('1', '1', '9', '7') ('1', '1', '9', '8') ('1', '1', '9', '9') ('1', '2', '0', '0') ('1', '2', '0', '1') ('1', '2', '0', '2') ('1', '2', '0', '3') ('1', '2', '0', '4') ('1', '2', '0', '5') ('1', '2', '0', '6') ('1', '2', '0', '7') ('1', '2', '0', '8') ('1', '2', '0', '9') ('1', '2', '1', '0') ('1', '2', '1', '1') ('1', '2', '1', '2') ('1', '2', '1', '3') ('1', '2', '1', '4') ('1', '2', '1', '5') ('1', '2', '1', '6') ('1', '2', '1', '7') ('1', '2', '1', '8') ('1', '2', '1', '9') ('1', '2', '2', '0') ('1', '2', '2', '1') ('1', '2', '2', '2') ('1', '2', '2', '3') ('1', '2', '2', '4') ('1', '2', '2', '5') ('1', '2', '2', '6') ('1', '2', '2', '7') ('1', '2', '2', '8') ('1', '2', '2', '9') ('1', '2', '3', '0') ('1', '2', '3', '1') ('1', '2', '3', '2') ('1', '2', '3', '3') ('1', '2', '3', '4') ('1', '2', '3', '5') ('1', '2', '3', '6') ('1', '2', '3', '7') ('1', '2', '3', '8') ('1', '2', '3', '9') ('1', '2', '4', '0') ('1', '2', '4', '1') ('1', '2', '4', '2') ('1', '2', '4', '3') ('1', '2', '4', '4') ('1', '2', '4', '5') ('1', '2', '4', '6') ('1', '2', '4', '7') ('1', '2', '4', '8') ('1', '2', '4', '9') ('1', '2', '5', '0') ('1', '2', '5', '1') ('1', '2', '5', '2') ('1', '2', '5', '3') ('1', '2', '5', '4') ('1', '2', '5', '5') ('1', '2', '5', '6') ('1', '2', '5', '7') ('1', '2', '5', '8') ('1', '2', '5', '9') ('1', '2', '6', '0') ('1', '2', '6', '1') ('1', '2', '6', '2') ('1', '2', '6', '3') ('1', '2', '6', '4') ('1', '2', '6', '5') ('1', '2', '6', '6') ('1', '2', '6', '7') ('1', '2', '6', '8') ('1', '2', '6', '9') ('1', '2', '7', '0') ('1', '2', '7', '1') ('1', '2', '7', '2') ('1', '2', '7', '3') ('1', '2', '7', '4') ('1', '2', '7', '5') ('1', '2', '7', '6') ('1', '2', '7', '7') ('1', '2', '7', '8') ('1', '2', '7', '9') ('1', '2', '8', '0') ('1', '2', '8', '1') ('1', '2', '8', '2') ('1', '2', '8', '3') ('1', '2', '8', '4') ('1', '2', '8', '5') ('1', '2', '8', '6') ('1', '2', '8', '7') ('1', '2', '8', '8') ('1', '2', '8', '9') ('1', '2', '9', '0') ('1', '2', '9', '1') ('1', '2', '9', '2') ('1', '2', '9', '3') ('1', '2', '9', '4') ('1', '2', '9', '5') ('1', '2', '9', '6') ('1', '2', '9', '7') ('1', '2', '9', '8') ('1', '2', '9', '9') ('1', '3', '0', '0') ('1', '3', '0', '1') ('1', '3', '0', '2') ('1', '3', '0', '3') ('1', '3', '0', '4') ('1', '3', '0', '5') ('1', '3', '0', '6') ('1', '3', '0', '7') ('1', '3', '0', '8') ('1', '3', '0', '9') ('1', '3', '1', '0') ('1', '3', '1', '1') ('1', '3', '1', '2') ('1', '3', '1', '3') ('1', '3', '1', '4') ('1', '3', '1', '5') ('1', '3', '1', '6') ('1', '3', '1', '7') ('1', '3', '1', '8') ('1', '3', '1', '9') ('1', '3', '2', '0') ('1', '3', '2', '1') ('1', '3', '2', '2') ('1', '3', '2', '3') ('1', '3', '2', '4') ('1', '3', '2', '5') ('1', '3', '2', '6') ('1', '3', '2', '7') ('1', '3', '2', '8') ('1', '3', '2', '9') ('1', '3', '3', '0') ('1', '3', '3', '1') ('1', '3', '3', '2') ('1', '3', '3', '3') ('1', '3', '3', '4') ('1', '3', '3', '5') ('1', '3', '3', '6') ('1', '3', '3', '7') ('1', '3', '3', '8') ('1', '3', '3', '9') ('1', '3', '4', '0') ('1', '3', '4', '1') ('1', '3', '4', '2') ('1', '3', '4', '3') ('1', '3', '4', '4') ('1', '3', '4', '5') ('1', '3', '4', '6') ('1', '3', '4', '7') ('1', '3', '4', '8') ('1', '3', '4', '9') ('1', '3', '5', '0') ('1', '3', '5', '1') ('1', '3', '5', '2') ('1', '3', '5', '3') ('1', '3', '5', '4') ('1', '3', '5', '5') ('1', '3', '5', '6') ('1', '3', '5', '7') ('1', '3', '5', '8') ('1', '3', '5', '9') ('1', '3', '6', '0') ('1', '3', '6', '1') ('1', '3', '6', '2') ('1', '3', '6', '3') ('1', '3', '6', '4') ('1', '3', '6', '5') ('1', '3', '6', '6') ('1', '3', '6', '7') ('1', '3', '6', '8') ('1', '3', '6', '9') ('1', '3', '7', '0') ('1', '3', '7', '1') ('1', '3', '7', '2') ('1', '3', '7', '3') ('1', '3', '7', '4') ('1', '3', '7', '5') ('1', '3', '7', '6') ('1', '3', '7', '7') ('1', '3', '7', '8') ('1', '3', '7', '9') ('1', '3', '8', '0') ('1', '3', '8', '1') ('1', '3', '8', '2') ('1', '3', '8', '3') ('1', '3', '8', '4') ('1', '3', '8', '5') ('1', '3', '8', '6') ('1', '3', '8', '7') ('1', '3', '8', '8') ('1', '3', '8', '9') ('1', '3', '9', '0') ('1', '3', '9', '1') ('1', '3', '9', '2') ('1', '3', '9', '3') ('1', '3', '9', '4') ('1', '3', '9', '5') ('1', '3', '9', '6') ('1', '3', '9', '7') ('1', '3', '9', '8') ('1', '3', '9', '9') ('1', '4', '0', '0') ('1', '4', '0', '1') ('1', '4', '0', '2') ('1', '4', '0', '3') ('1', '4', '0', '4') ('1', '4', '0', '5') ('1', '4', '0', '6') ('1', '4', '0', '7') ('1', '4', '0', '8') ('1', '4', '0', '9') ('1', '4', '1', '0') ('1', '4', '1', '1') ('1', '4', '1', '2') ('1', '4', '1', '3') ('1', '4', '1', '4') ('1', '4', '1', '5') ('1', '4', '1', '6') ('1', '4', '1', '7') ('1', '4', '1', '8') ('1', '4', '1', '9') ('1', '4', '2', '0') ('1', '4', '2', '1') ('1', '4', '2', '2') ('1', '4', '2', '3') ('1', '4', '2', '4') ('1', '4', '2', '5') ('1', '4', '2', '6') ('1', '4', '2', '7') ('1', '4', '2', '8') ('1', '4', '2', '9') ('1', '4', '3', '0') ('1', '4', '3', '1') ('1', '4', '3', '2') ('1', '4', '3', '3') ('1', '4', '3', '4') ('1', '4', '3', '5') ('1', '4', '3', '6') ('1', '4', '3', '7') ('1', '4', '3', '8') ('1', '4', '3', '9') ('1', '4', '4', '0') ('1', '4', '4', '1') ('1', '4', '4', '2') ('1', '4', '4', '3') ('1', '4', '4', '4') ('1', '4', '4', '5') ('1', '4', '4', '6') ('1', '4', '4', '7') ('1', '4', '4', '8') ('1', '4', '4', '9') ('1', '4', '5', '0') ('1', '4', '5', '1') ('1', '4', '5', '2') ('1', '4', '5', '3') ('1', '4', '5', '4') ('1', '4', '5', '5') ('1', '4', '5', '6') ('1', '4', '5', '7') ('1', '4', '5', '8') ('1', '4', '5', '9') ('1', '4', '6', '0') ('1', '4', '6', '1') ('1', '4', '6', '2') ('1', '4', '6', '3') ('1', '4', '6', '4') ('1', '4', '6', '5') ('1', '4', '6', '6') ('1', '4', '6', '7') ('1', '4', '6', '8') ('1', '4', '6', '9') ('1', '4', '7', '0') ('1', '4', '7', '1') ('1', '4', '7', '2') ('1', '4', '7', '3') ('1', '4', '7', '4') ('1', '4', '7', '5') ('1', '4', '7', '6') ('1', '4', '7', '7') ('1', '4', '7', '8') ('1', '4', '7', '9') ('1', '4', '8', '0') ('1', '4', '8', '1') ('1', '4', '8', '2') ('1', '4', '8', '3') ('1', '4', '8', '4') ('1', '4', '8', '5') ('1', '4', '8', '6') ('1', '4', '8', '7') ('1', '4', '8', '8') ('1', '4', '8', '9') ('1', '4', '9', '0') ('1', '4', '9', '1') ('1', '4', '9', '2') ('1', '4', '9', '3') ('1', '4', '9', '4') ('1', '4', '9', '5') ('1', '4', '9', '6') ('1', '4', '9', '7') ('1', '4', '9', '8') ('1', '4', '9', '9') ('1', '5', '0', '0') ('1', '5', '0', '1') ('1', '5', '0', '2') ('1', '5', '0', '3') ('1', '5', '0', '4') ('1', '5', '0', '5') ('1', '5', '0', '6') ('1', '5', '0', '7') ('1', '5', '0', '8') ('1', '5', '0', '9') ('1', '5', '1', '0') ('1', '5', '1', '1') ('1', '5', '1', '2') ('1', '5', '1', '3') ('1', '5', '1', '4') ('1', '5', '1', '5') ('1', '5', '1', '6') ('1', '5', '1', '7') ('1', '5', '1', '8') ('1', '5', '1', '9') ('1', '5', '2', '0') ('1', '5', '2', '1') ('1', '5', '2', '2') ('1', '5', '2', '3') ('1', '5', '2', '4') ('1', '5', '2', '5') ('1', '5', '2', '6') ('1', '5', '2', '7') ('1', '5', '2', '8') ('1', '5', '2', '9') ('1', '5', '3', '0') ('1', '5', '3', '1') ('1', '5', '3', '2') ('1', '5', '3', '3') ('1', '5', '3', '4') ('1', '5', '3', '5') ('1', '5', '3', '6') ('1', '5', '3', '7') ('1', '5', '3', '8') ('1', '5', '3', '9') ('1', '5', '4', '0') ('1', '5', '4', '1') ('1', '5', '4', '2') ('1', '5', '4', '3') ('1', '5', '4', '4') ('1', '5', '4', '5') ('1', '5', '4', '6') ('1', '5', '4', '7') ('1', '5', '4', '8') ('1', '5', '4', '9') ('1', '5', '5', '0') ('1', '5', '5', '1') ('1', '5', '5', '2') ('1', '5', '5', '3') ('1', '5', '5', '4') ('1', '5', '5', '5') ('1', '5', '5', '6') ('1', '5', '5', '7') ('1', '5', '5', '8') ('1', '5', '5', '9') ('1', '5', '6', '0') ('1', '5', '6', '1') ('1', '5', '6', '2') ('1', '5', '6', '3') ('1', '5', '6', '4') ('1', '5', '6', '5') ('1', '5', '6', '6') ('1', '5', '6', '7') ('1', '5', '6', '8') ('1', '5', '6', '9') ('1', '5', '7', '0') ('1', '5', '7', '1') ('1', '5', '7', '2') ('1', '5', '7', '3') ('1', '5', '7', '4') ('1', '5', '7', '5') ('1', '5', '7', '6') ('1', '5', '7', '7') ('1', '5', '7', '8') ('1', '5', '7', '9') ('1', '5', '8', '0') ('1', '5', '8', '1') ('1', '5', '8', '2') ('1', '5', '8', '3') ('1', '5', '8', '4') ('1', '5', '8', '5') ('1', '5', '8', '6') ('1', '5', '8', '7') ('1', '5', '8', '8') ('1', '5', '8', '9') ('1', '5', '9', '0') ('1', '5', '9', '1') ('1', '5', '9', '2') ('1', '5', '9', '3') ('1', '5', '9', '4') ('1', '5', '9', '5') ('1', '5', '9', '6') ('1', '5', '9', '7') ('1', '5', '9', '8') ('1', '5', '9', '9') ('1', '6', '0', '0') ('1', '6', '0', '1') ('1', '6', '0', '2') ('1', '6', '0', '3') ('1', '6', '0', '4') ('1', '6', '0', '5') ('1', '6', '0', '6') ('1', '6', '0', '7') ('1', '6', '0', '8') ('1', '6', '0', '9') ('1', '6', '1', '0') ('1', '6', '1', '1') ('1', '6', '1', '2') ('1', '6', '1', '3') ('1', '6', '1', '4') ('1', '6', '1', '5') ('1', '6', '1', '6') ('1', '6', '1', '7') ('1', '6', '1', '8') ('1', '6', '1', '9') ('1', '6', '2', '0') ('1', '6', '2', '1') ('1', '6', '2', '2') ('1', '6', '2', '3') ('1', '6', '2', '4') ('1', '6', '2', '5') ('1', '6', '2', '6') ('1', '6', '2', '7') ('1', '6', '2', '8') ('1', '6', '2', '9') ('1', '6', '3', '0') ('1', '6', '3', '1') ('1', '6', '3', '2') ('1', '6', '3', '3') ('1', '6', '3', '4') ('1', '6', '3', '5') ('1', '6', '3', '6') ('1', '6', '3', '7') ('1', '6', '3', '8') ('1', '6', '3', '9') ('1', '6', '4', '0') ('1', '6', '4', '1') ('1', '6', '4', '2') ('1', '6', '4', '3') ('1', '6', '4', '4') ('1', '6', '4', '5') ('1', '6', '4', '6') ('1', '6', '4', '7') ('1', '6', '4', '8') ('1', '6', '4', '9') ('1', '6', '5', '0') ('1', '6', '5', '1') ('1', '6', '5', '2') ('1', '6', '5', '3') ('1', '6', '5', '4') ('1', '6', '5', '5') ('1', '6', '5', '6') ('1', '6', '5', '7') ('1', '6', '5', '8') ('1', '6', '5', '9') ('1', '6', '6', '0') ('1', '6', '6', '1') ('1', '6', '6', '2') ('1', '6', '6', '3') ('1', '6', '6', '4') ('1', '6', '6', '5') ('1', '6', '6', '6') ('1', '6', '6', '7') ('1', '6', '6', '8') ('1', '6', '6', '9') ('1', '6', '7', '0') ('1', '6', '7', '1') ('1', '6', '7', '2') ('1', '6', '7', '3') ('1', '6', '7', '4') ('1', '6', '7', '5') ('1', '6', '7', '6') ('1', '6', '7', '7') ('1', '6', '7', '8') ('1', '6', '7', '9') ('1', '6', '8', '0') ('1', '6', '8', '1') ('1', '6', '8', '2') ('1', '6', '8', '3') ('1', '6', '8', '4') ('1', '6', '8', '5') ('1', '6', '8', '6') ('1', '6', '8', '7') ('1', '6', '8', '8') ('1', '6', '8', '9') ('1', '6', '9', '0') ('1', '6', '9', '1') ('1', '6', '9', '2') ('1', '6', '9', '3') ('1', '6', '9', '4') ('1', '6', '9', '5') ('1', '6', '9', '6') ('1', '6', '9', '7') ('1', '6', '9', '8') ('1', '6', '9', '9') ('1', '7', '0', '0') ('1', '7', '0', '1') ('1', '7', '0', '2') ('1', '7', '0', '3') ('1', '7', '0', '4') ('1', '7', '0', '5') ('1', '7', '0', '6') ('1', '7', '0', '7') ('1', '7', '0', '8') ('1', '7', '0', '9') ('1', '7', '1', '0') ('1', '7', '1', '1') ('1', '7', '1', '2') ('1', '7', '1', '3') ('1', '7', '1', '4') ('1', '7', '1', '5') ('1', '7', '1', '6') ('1', '7', '1', '7') ('1', '7', '1', '8') ('1', '7', '1', '9') ('1', '7', '2', '0') ('1', '7', '2', '1') ('1', '7', '2', '2') ('1', '7', '2', '3') ('1', '7', '2', '4') ('1', '7', '2', '5') ('1', '7', '2', '6') ('1', '7', '2', '7') ('1', '7', '2', '8') ('1', '7', '2', '9') ('1', '7', '3', '0') ('1', '7', '3', '1') ('1', '7', '3', '2') ('1', '7', '3', '3') ('1', '7', '3', '4') ('1', '7', '3', '5') ('1', '7', '3', '6') ('1', '7', '3', '7') ('1', '7', '3', '8') ('1', '7', '3', '9') ('1', '7', '4', '0') ('1', '7', '4', '1') ('1', '7', '4', '2') ('1', '7', '4', '3') ('1', '7', '4', '4') ('1', '7', '4', '5') ('1', '7', '4', '6') ('1', '7', '4', '7') ('1', '7', '4', '8') ('1', '7', '4', '9') ('1', '7', '5', '0') ('1', '7', '5', '1') ('1', '7', '5', '2') ('1', '7', '5', '3') ('1', '7', '5', '4') ('1', '7', '5', '5') ('1', '7', '5', '6') ('1', '7', '5', '7') ('1', '7', '5', '8') ('1', '7', '5', '9') ('1', '7', '6', '0') ('1', '7', '6', '1') ('1', '7', '6', '2') ('1', '7', '6', '3') ('1', '7', '6', '4') ('1', '7', '6', '5') ('1', '7', '6', '6') ('1', '7', '6', '7') ('1', '7', '6', '8') ('1', '7', '6', '9') ('1', '7', '7', '0') ('1', '7', '7', '1') ('1', '7', '7', '2') ('1', '7', '7', '3') ('1', '7', '7', '4') ('1', '7', '7', '5') ('1', '7', '7', '6') ('1', '7', '7', '7') ('1', '7', '7', '8') ('1', '7', '7', '9') ('1', '7', '8', '0') ('1', '7', '8', '1') ('1', '7', '8', '2') ('1', '7', '8', '3') ('1', '7', '8', '4') ('1', '7', '8', '5') ('1', '7', '8', '6') ('1', '7', '8', '7') ('1', '7', '8', '8') ('1', '7', '8', '9') ('1', '7', '9', '0') ('1', '7', '9', '1') ('1', '7', '9', '2') ('1', '7', '9', '3') ('1', '7', '9', '4') ('1', '7', '9', '5') ('1', '7', '9', '6') ('1', '7', '9', '7') ('1', '7', '9', '8') ('1', '7', '9', '9') ('1', '8', '0', '0') ('1', '8', '0', '1') ('1', '8', '0', '2') ('1', '8', '0', '3') ('1', '8', '0', '4') ('1', '8', '0', '5') ('1', '8', '0', '6') ('1', '8', '0', '7') ('1', '8', '0', '8') ('1', '8', '0', '9') ('1', '8', '1', '0') ('1', '8', '1', '1') ('1', '8', '1', '2') ('1', '8', '1', '3') ('1', '8', '1', '4') ('1', '8', '1', '5') ('1', '8', '1', '6') ('1', '8', '1', '7') ('1', '8', '1', '8') ('1', '8', '1', '9') ('1', '8', '2', '0') ('1', '8', '2', '1') ('1', '8', '2', '2') ('1', '8', '2', '3') ('1', '8', '2', '4') ('1', '8', '2', '5') ('1', '8', '2', '6') ('1', '8', '2', '7') ('1', '8', '2', '8') ('1', '8', '2', '9') ('1', '8', '3', '0') ('1', '8', '3', '1') ('1', '8', '3', '2') ('1', '8', '3', '3') ('1', '8', '3', '4') ('1', '8', '3', '5') ('1', '8', '3', '6') ('1', '8', '3', '7') ('1', '8', '3', '8') ('1', '8', '3', '9') ('1', '8', '4', '0') ('1', '8', '4', '1') ('1', '8', '4', '2') ('1', '8', '4', '3') ('1', '8', '4', '4') ('1', '8', '4', '5') ('1', '8', '4', '6') ('1', '8', '4', '7') ('1', '8', '4', '8') ('1', '8', '4', '9') ('1', '8', '5', '0') ('1', '8', '5', '1') ('1', '8', '5', '2') ('1', '8', '5', '3') ('1', '8', '5', '4') ('1', '8', '5', '5') ('1', '8', '5', '6') ('1', '8', '5', '7') ('1', '8', '5', '8') ('1', '8', '5', '9') ('1', '8', '6', '0') ('1', '8', '6', '1') ('1', '8', '6', '2') ('1', '8', '6', '3') ('1', '8', '6', '4') ('1', '8', '6', '5') ('1', '8', '6', '6') ('1', '8', '6', '7') ('1', '8', '6', '8') ('1', '8', '6', '9') ('1', '8', '7', '0') ('1', '8', '7', '1') ('1', '8', '7', '2') ('1', '8', '7', '3') ('1', '8', '7', '4') ('1', '8', '7', '5') ('1', '8', '7', '6') ('1', '8', '7', '7') ('1', '8', '7', '8') ('1', '8', '7', '9') ('1', '8', '8', '0') ('1', '8', '8', '1') ('1', '8', '8', '2') ('1', '8', '8', '3') ('1', '8', '8', '4') ('1', '8', '8', '5') ('1', '8', '8', '6') ('1', '8', '8', '7') ('1', '8', '8', '8') ('1', '8', '8', '9') ('1', '8', '9', '0') ('1', '8', '9', '1') ('1', '8', '9', '2') ('1', '8', '9', '3') ('1', '8', '9', '4') ('1', '8', '9', '5') ('1', '8', '9', '6') ('1', '8', '9', '7') ('1', '8', '9', '8') ('1', '8', '9', '9') ('1', '9', '0', '0') ('1', '9', '0', '1') ('1', '9', '0', '2') ('1', '9', '0', '3') ('1', '9', '0', '4') ('1', '9', '0', '5') ('1', '9', '0', '6') ('1', '9', '0', '7') ('1', '9', '0', '8') ('1', '9', '0', '9') ('1', '9', '1', '0') ('1', '9', '1', '1') ('1', '9', '1', '2') ('1', '9', '1', '3') ('1', '9', '1', '4') ('1', '9', '1', '5') ('1', '9', '1', '6') ('1', '9', '1', '7') ('1', '9', '1', '8') ('1', '9', '1', '9') ('1', '9', '2', '0') ('1', '9', '2', '1') ('1', '9', '2', '2') ('1', '9', '2', '3') ('1', '9', '2', '4') ('1', '9', '2', '5') ('1', '9', '2', '6') ('1', '9', '2', '7') ('1', '9', '2', '8') ('1', '9', '2', '9') ('1', '9', '3', '0') ('1', '9', '3', '1') ('1', '9', '3', '2') ('1', '9', '3', '3') ('1', '9', '3', '4') ('1', '9', '3', '5') ('1', '9', '3', '6') ('1', '9', '3', '7') ('1', '9', '3', '8') ('1', '9', '3', '9') ('1', '9', '4', '0') ('1', '9', '4', '1') ('1', '9', '4', '2') ('1', '9', '4', '3') ('1', '9', '4', '4') ('1', '9', '4', '5') ('1', '9', '4', '6') ('1', '9', '4', '7') ('1', '9', '4', '8') ('1', '9', '4', '9') ('1', '9', '5', '0') ('1', '9', '5', '1') ('1', '9', '5', '2') ('1', '9', '5', '3') ('1', '9', '5', '4') ('1', '9', '5', '5') ('1', '9', '5', '6') ('1', '9', '5', '7') ('1', '9', '5', '8') ('1', '9', '5', '9') ('1', '9', '6', '0') ('1', '9', '6', '1') ('1', '9', '6', '2') ('1', '9', '6', '3') ('1', '9', '6', '4') ('1', '9', '6', '5') ('1', '9', '6', '6') ('1', '9', '6', '7') ('1', '9', '6', '8') ('1', '9', '6', '9') ('1', '9', '7', '0') ('1', '9', '7', '1') ('1', '9', '7', '2') ('1', '9', '7', '3') ('1', '9', '7', '4') ('1', '9', '7', '5') ('1', '9', '7', '6') ('1', '9', '7', '7') ('1', '9', '7', '8') ('1', '9', '7', '9') ('1', '9', '8', '0') ('1', '9', '8', '1') ('1', '9', '8', '2') ('1', '9', '8', '3') ('1', '9', '8', '4') ('1', '9', '8', '5') ('1', '9', '8', '6') ('1', '9', '8', '7') ('1', '9', '8', '8') ('1', '9', '8', '9') ('1', '9', '9', '0') ('1', '9', '9', '1') ('1', '9', '9', '2') ('1', '9', '9', '3') ('1', '9', '9', '4') ('1', '9', '9', '5') ('1', '9', '9', '6') ('1', '9', '9', '7') ('1', '9', '9', '8') ('1', '9', '9', '9') ('2', '0', '0', '0') ('2', '0', '0', '1') ('2', '0', '0', '2') ('2', '0', '0', '3') ('2', '0', '0', '4') ('2', '0', '0', '5') ('2', '0', '0', '6') ('2', '0', '0', '7') ('2', '0', '0', '8') ('2', '0', '0', '9') ('2', '0', '1', '0') ('2', '0', '1', '1') ('2', '0', '1', '2') ('2', '0', '1', '3') ('2', '0', '1', '4') ('2', '0', '1', '5') ('2', '0', '1', '6') ('2', '0', '1', '7') ('2', '0', '1', '8') ('2', '0', '1', '9') ('2', '0', '2', '0') ('2', '0', '2', '1') ('2', '0', '2', '2') ('2', '0', '2', '3') ('2', '0', '2', '4') ('2', '0', '2', '5') ('2', '0', '2', '6') ('2', '0', '2', '7') ('2', '0', '2', '8') ('2', '0', '2', '9') ('2', '0', '3', '0') ('2', '0', '3', '1') ('2', '0', '3', '2') ('2', '0', '3', '3') ('2', '0', '3', '4') ('2', '0', '3', '5') ('2', '0', '3', '6') ('2', '0', '3', '7') ('2', '0', '3', '8') ('2', '0', '3', '9') ('2', '0', '4', '0') ('2', '0', '4', '1') ('2', '0', '4', '2') ('2', '0', '4', '3') ('2', '0', '4', '4') ('2', '0', '4', '5') ('2', '0', '4', '6') ('2', '0', '4', '7') ('2', '0', '4', '8') ('2', '0', '4', '9') ('2', '0', '5', '0') ('2', '0', '5', '1') ('2', '0', '5', '2') ('2', '0', '5', '3') ('2', '0', '5', '4') ('2', '0', '5', '5') ('2', '0', '5', '6') ('2', '0', '5', '7') ('2', '0', '5', '8') ('2', '0', '5', '9') ('2', '0', '6', '0') ('2', '0', '6', '1') ('2', '0', '6', '2') ('2', '0', '6', '3') ('2', '0', '6', '4') ('2', '0', '6', '5') ('2', '0', '6', '6') ('2', '0', '6', '7') ('2', '0', '6', '8') ('2', '0', '6', '9') ('2', '0', '7', '0') ('2', '0', '7', '1') ('2', '0', '7', '2') ('2', '0', '7', '3') ('2', '0', '7', '4') ('2', '0', '7', '5') ('2', '0', '7', '6') ('2', '0', '7', '7') ('2', '0', '7', '8') ('2', '0', '7', '9') ('2', '0', '8', '0') ('2', '0', '8', '1') ('2', '0', '8', '2') ('2', '0', '8', '3') ('2', '0', '8', '4') ('2', '0', '8', '5') ('2', '0', '8', '6') ('2', '0', '8', '7') ('2', '0', '8', '8') ('2', '0', '8', '9') ('2', '0', '9', '0') ('2', '0', '9', '1') ('2', '0', '9', '2') ('2', '0', '9', '3') ('2', '0', '9', '4') ('2', '0', '9', '5') ('2', '0', '9', '6') ('2', '0', '9', '7') ('2', '0', '9', '8') ('2', '0', '9', '9') ('2', '1', '0', '0') ('2', '1', '0', '1') ('2', '1', '0', '2') ('2', '1', '0', '3') ('2', '1', '0', '4') ('2', '1', '0', '5') ('2', '1', '0', '6') ('2', '1', '0', '7') ('2', '1', '0', '8') ('2', '1', '0', '9') ('2', '1', '1', '0') ('2', '1', '1', '1') ('2', '1', '1', '2') ('2', '1', '1', '3') ('2', '1', '1', '4') ('2', '1', '1', '5') ('2', '1', '1', '6') ('2', '1', '1', '7') ('2', '1', '1', '8') ('2', '1', '1', '9') ('2', '1', '2', '0') ('2', '1', '2', '1') ('2', '1', '2', '2') ('2', '1', '2', '3') ('2', '1', '2', '4') ('2', '1', '2', '5') ('2', '1', '2', '6') ('2', '1', '2', '7') ('2', '1', '2', '8') ('2', '1', '2', '9') ('2', '1', '3', '0') ('2', '1', '3', '1') ('2', '1', '3', '2') ('2', '1', '3', '3') ('2', '1', '3', '4') ('2', '1', '3', '5') ('2', '1', '3', '6') ('2', '1', '3', '7') ('2', '1', '3', '8') ('2', '1', '3', '9') ('2', '1', '4', '0') ('2', '1', '4', '1') ('2', '1', '4', '2') ('2', '1', '4', '3') ('2', '1', '4', '4') ('2', '1', '4', '5') ('2', '1', '4', '6') ('2', '1', '4', '7') ('2', '1', '4', '8') ('2', '1', '4', '9') ('2', '1', '5', '0') ('2', '1', '5', '1') ('2', '1', '5', '2') ('2', '1', '5', '3') ('2', '1', '5', '4') ('2', '1', '5', '5') ('2', '1', '5', '6') ('2', '1', '5', '7') ('2', '1', '5', '8') ('2', '1', '5', '9') ('2', '1', '6', '0') ('2', '1', '6', '1') ('2', '1', '6', '2') ('2', '1', '6', '3') ('2', '1', '6', '4') ('2', '1', '6', '5') ('2', '1', '6', '6') ('2', '1', '6', '7') ('2', '1', '6', '8') ('2', '1', '6', '9') ('2', '1', '7', '0') ('2', '1', '7', '1') ('2', '1', '7', '2') ('2', '1', '7', '3') ('2', '1', '7', '4') ('2', '1', '7', '5') ('2', '1', '7', '6') ('2', '1', '7', '7') ('2', '1', '7', '8') ('2', '1', '7', '9') ('2', '1', '8', '0') ('2', '1', '8', '1') ('2', '1', '8', '2') ('2', '1', '8', '3') ('2', '1', '8', '4') ('2', '1', '8', '5') ('2', '1', '8', '6') ('2', '1', '8', '7') ('2', '1', '8', '8') ('2', '1', '8', '9') ('2', '1', '9', '0') ('2', '1', '9', '1') ('2', '1', '9', '2') ('2', '1', '9', '3') ('2', '1', '9', '4') ('2', '1', '9', '5') ('2', '1', '9', '6') ('2', '1', '9', '7') ('2', '1', '9', '8') ('2', '1', '9', '9') ('2', '2', '0', '0') ('2', '2', '0', '1') ('2', '2', '0', '2') ('2', '2', '0', '3') ('2', '2', '0', '4') ('2', '2', '0', '5') ('2', '2', '0', '6') ('2', '2', '0', '7') ('2', '2', '0', '8') ('2', '2', '0', '9') ('2', '2', '1', '0') ('2', '2', '1', '1') ('2', '2', '1', '2') ('2', '2', '1', '3') ('2', '2', '1', '4') ('2', '2', '1', '5') ('2', '2', '1', '6') ('2', '2', '1', '7') ('2', '2', '1', '8') ('2', '2', '1', '9') ('2', '2', '2', '0') ('2', '2', '2', '1') ('2', '2', '2', '2') ('2', '2', '2', '3') ('2', '2', '2', '4') ('2', '2', '2', '5') ('2', '2', '2', '6') ('2', '2', '2', '7') ('2', '2', '2', '8') ('2', '2', '2', '9') ('2', '2', '3', '0') ('2', '2', '3', '1') ('2', '2', '3', '2') ('2', '2', '3', '3') ('2', '2', '3', '4') ('2', '2', '3', '5') ('2', '2', '3', '6') ('2', '2', '3', '7') ('2', '2', '3', '8') ('2', '2', '3', '9') ('2', '2', '4', '0') ('2', '2', '4', '1') ('2', '2', '4', '2') ('2', '2', '4', '3') ('2', '2', '4', '4') ('2', '2', '4', '5') ('2', '2', '4', '6') ('2', '2', '4', '7') ('2', '2', '4', '8') ('2', '2', '4', '9') ('2', '2', '5', '0') ('2', '2', '5', '1') ('2', '2', '5', '2') ('2', '2', '5', '3') ('2', '2', '5', '4') ('2', '2', '5', '5') ('2', '2', '5', '6') ('2', '2', '5', '7') ('2', '2', '5', '8') ('2', '2', '5', '9') ('2', '2', '6', '0') ('2', '2', '6', '1') ('2', '2', '6', '2') ('2', '2', '6', '3') ('2', '2', '6', '4') ('2', '2', '6', '5') ('2', '2', '6', '6') ('2', '2', '6', '7') ('2', '2', '6', '8') ('2', '2', '6', '9') ('2', '2', '7', '0') ('2', '2', '7', '1') ('2', '2', '7', '2') ('2', '2', '7', '3') ('2', '2', '7', '4') ('2', '2', '7', '5') ('2', '2', '7', '6') ('2', '2', '7', '7') ('2', '2', '7', '8') ('2', '2', '7', '9') ('2', '2', '8', '0') ('2', '2', '8', '1') ('2', '2', '8', '2') ('2', '2', '8', '3') ('2', '2', '8', '4') ('2', '2', '8', '5') ('2', '2', '8', '6') ('2', '2', '8', '7') ('2', '2', '8', '8') ('2', '2', '8', '9') ('2', '2', '9', '0') ('2', '2', '9', '1') ('2', '2', '9', '2') ('2', '2', '9', '3') ('2', '2', '9', '4') ('2', '2', '9', '5') ('2', '2', '9', '6') ('2', '2', '9', '7') ('2', '2', '9', '8') ('2', '2', '9', '9') ('2', '3', '0', '0') ('2', '3', '0', '1') ('2', '3', '0', '2') ('2', '3', '0', '3') ('2', '3', '0', '4') ('2', '3', '0', '5') ('2', '3', '0', '6') ('2', '3', '0', '7') ('2', '3', '0', '8') ('2', '3', '0', '9') ('2', '3', '1', '0') ('2', '3', '1', '1') ('2', '3', '1', '2') ('2', '3', '1', '3') ('2', '3', '1', '4') ('2', '3', '1', '5') ('2', '3', '1', '6') ('2', '3', '1', '7') ('2', '3', '1', '8') ('2', '3', '1', '9') ('2', '3', '2', '0') ('2', '3', '2', '1') ('2', '3', '2', '2') ('2', '3', '2', '3') ('2', '3', '2', '4') ('2', '3', '2', '5') ('2', '3', '2', '6') ('2', '3', '2', '7') ('2', '3', '2', '8') ('2', '3', '2', '9') ('2', '3', '3', '0') ('2', '3', '3', '1') ('2', '3', '3', '2') ('2', '3', '3', '3') ('2', '3', '3', '4') ('2', '3', '3', '5') ('2', '3', '3', '6') ('2', '3', '3', '7') ('2', '3', '3', '8') ('2', '3', '3', '9') ('2', '3', '4', '0') ('2', '3', '4', '1') ('2', '3', '4', '2') ('2', '3', '4', '3') ('2', '3', '4', '4') ('2', '3', '4', '5') ('2', '3', '4', '6') ('2', '3', '4', '7') ('2', '3', '4', '8') ('2', '3', '4', '9') ('2', '3', '5', '0') ('2', '3', '5', '1') ('2', '3', '5', '2') ('2', '3', '5', '3') ('2', '3', '5', '4') ('2', '3', '5', '5') ('2', '3', '5', '6') ('2', '3', '5', '7') ('2', '3', '5', '8') ('2', '3', '5', '9') ('2', '3', '6', '0') ('2', '3', '6', '1') ('2', '3', '6', '2') ('2', '3', '6', '3') ('2', '3', '6', '4') ('2', '3', '6', '5') ('2', '3', '6', '6') ('2', '3', '6', '7') ('2', '3', '6', '8') ('2', '3', '6', '9') ('2', '3', '7', '0') ('2', '3', '7', '1') ('2', '3', '7', '2') ('2', '3', '7', '3') ('2', '3', '7', '4') ('2', '3', '7', '5') ('2', '3', '7', '6') ('2', '3', '7', '7') ('2', '3', '7', '8') ('2', '3', '7', '9') ('2', '3', '8', '0') ('2', '3', '8', '1') ('2', '3', '8', '2') ('2', '3', '8', '3') ('2', '3', '8', '4') ('2', '3', '8', '5') ('2', '3', '8', '6') ('2', '3', '8', '7') ('2', '3', '8', '8') ('2', '3', '8', '9') ('2', '3', '9', '0') ('2', '3', '9', '1') ('2', '3', '9', '2') ('2', '3', '9', '3') ('2', '3', '9', '4') ('2', '3', '9', '5') ('2', '3', '9', '6') ('2', '3', '9', '7') ('2', '3', '9', '8') ('2', '3', '9', '9') ('2', '4', '0', '0') ('2', '4', '0', '1') ('2', '4', '0', '2') ('2', '4', '0', '3') ('2', '4', '0', '4') ('2', '4', '0', '5') ('2', '4', '0', '6') ('2', '4', '0', '7') ('2', '4', '0', '8') ('2', '4', '0', '9') ('2', '4', '1', '0') ('2', '4', '1', '1') ('2', '4', '1', '2') ('2', '4', '1', '3') ('2', '4', '1', '4') ('2', '4', '1', '5') ('2', '4', '1', '6') ('2', '4', '1', '7') ('2', '4', '1', '8') ('2', '4', '1', '9') ('2', '4', '2', '0') ('2', '4', '2', '1') ('2', '4', '2', '2') ('2', '4', '2', '3') ('2', '4', '2', '4') ('2', '4', '2', '5') ('2', '4', '2', '6') ('2', '4', '2', '7') ('2', '4', '2', '8') ('2', '4', '2', '9') ('2', '4', '3', '0') ('2', '4', '3', '1') ('2', '4', '3', '2') ('2', '4', '3', '3') ('2', '4', '3', '4') ('2', '4', '3', '5') ('2', '4', '3', '6') ('2', '4', '3', '7') ('2', '4', '3', '8') ('2', '4', '3', '9') ('2', '4', '4', '0') ('2', '4', '4', '1') ('2', '4', '4', '2') ('2', '4', '4', '3') ('2', '4', '4', '4') ('2', '4', '4', '5') ('2', '4', '4', '6') ('2', '4', '4', '7') ('2', '4', '4', '8') ('2', '4', '4', '9') ('2', '4', '5', '0') ('2', '4', '5', '1') ('2', '4', '5', '2') ('2', '4', '5', '3') ('2', '4', '5', '4') ('2', '4', '5', '5') ('2', '4', '5', '6') ('2', '4', '5', '7') ('2', '4', '5', '8') ('2', '4', '5', '9') ('2', '4', '6', '0') ('2', '4', '6', '1') ('2', '4', '6', '2') ('2', '4', '6', '3') ('2', '4', '6', '4') ('2', '4', '6', '5') ('2', '4', '6', '6') ('2', '4', '6', '7') ('2', '4', '6', '8') ('2', '4', '6', '9') ('2', '4', '7', '0') ('2', '4', '7', '1') ('2', '4', '7', '2') ('2', '4', '7', '3') ('2', '4', '7', '4') ('2', '4', '7', '5') ('2', '4', '7', '6') ('2', '4', '7', '7') ('2', '4', '7', '8') ('2', '4', '7', '9') ('2', '4', '8', '0') ('2', '4', '8', '1') ('2', '4', '8', '2') ('2', '4', '8', '3') ('2', '4', '8', '4') ('2', '4', '8', '5') ('2', '4', '8', '6') ('2', '4', '8', '7') ('2', '4', '8', '8') ('2', '4', '8', '9') ('2', '4', '9', '0') ('2', '4', '9', '1') ('2', '4', '9', '2') ('2', '4', '9', '3') ('2', '4', '9', '4') ('2', '4', '9', '5') ('2', '4', '9', '6') ('2', '4', '9', '7') ('2', '4', '9', '8') ('2', '4', '9', '9') ('2', '5', '0', '0') ('2', '5', '0', '1') ('2', '5', '0', '2') ('2', '5', '0', '3') ('2', '5', '0', '4') ('2', '5', '0', '5') ('2', '5', '0', '6') ('2', '5', '0', '7') ('2', '5', '0', '8') ('2', '5', '0', '9') ('2', '5', '1', '0') ('2', '5', '1', '1') ('2', '5', '1', '2') ('2', '5', '1', '3') ('2', '5', '1', '4') ('2', '5', '1', '5') ('2', '5', '1', '6') ('2', '5', '1', '7') ('2', '5', '1', '8') ('2', '5', '1', '9') ('2', '5', '2', '0') ('2', '5', '2', '1') ('2', '5', '2', '2') ('2', '5', '2', '3') ('2', '5', '2', '4') ('2', '5', '2', '5') ('2', '5', '2', '6') ('2', '5', '2', '7') ('2', '5', '2', '8') ('2', '5', '2', '9') ('2', '5', '3', '0') ('2', '5', '3', '1') ('2', '5', '3', '2') ('2', '5', '3', '3') ('2', '5', '3', '4') ('2', '5', '3', '5') ('2', '5', '3', '6') ('2', '5', '3', '7') ('2', '5', '3', '8') ('2', '5', '3', '9') ('2', '5', '4', '0') ('2', '5', '4', '1') ('2', '5', '4', '2') ('2', '5', '4', '3') ('2', '5', '4', '4') ('2', '5', '4', '5') ('2', '5', '4', '6') ('2', '5', '4', '7') ('2', '5', '4', '8') ('2', '5', '4', '9') ('2', '5', '5', '0') ('2', '5', '5', '1') ('2', '5', '5', '2') ('2', '5', '5', '3') ('2', '5', '5', '4') ('2', '5', '5', '5') ('2', '5', '5', '6') ('2', '5', '5', '7') ('2', '5', '5', '8') ('2', '5', '5', '9') ('2', '5', '6', '0') ('2', '5', '6', '1') ('2', '5', '6', '2') ('2', '5', '6', '3') ('2', '5', '6', '4') ('2', '5', '6', '5') ('2', '5', '6', '6') ('2', '5', '6', '7') ('2', '5', '6', '8') ('2', '5', '6', '9') ('2', '5', '7', '0') ('2', '5', '7', '1') ('2', '5', '7', '2') ('2', '5', '7', '3') ('2', '5', '7', '4') ('2', '5', '7', '5') ('2', '5', '7', '6') ('2', '5', '7', '7') ('2', '5', '7', '8') ('2', '5', '7', '9') ('2', '5', '8', '0') ('2', '5', '8', '1') ('2', '5', '8', '2') ('2', '5', '8', '3') ('2', '5', '8', '4') ('2', '5', '8', '5') ('2', '5', '8', '6') ('2', '5', '8', '7') ('2', '5', '8', '8') ('2', '5', '8', '9') ('2', '5', '9', '0') ('2', '5', '9', '1') ('2', '5', '9', '2') ('2', '5', '9', '3') ('2', '5', '9', '4') ('2', '5', '9', '5') ('2', '5', '9', '6') ('2', '5', '9', '7') ('2', '5', '9', '8') ('2', '5', '9', '9') ('2', '6', '0', '0') ('2', '6', '0', '1') ('2', '6', '0', '2') ('2', '6', '0', '3') ('2', '6', '0', '4') ('2', '6', '0', '5') ('2', '6', '0', '6') ('2', '6', '0', '7') ('2', '6', '0', '8') ('2', '6', '0', '9') ('2', '6', '1', '0') ('2', '6', '1', '1') ('2', '6', '1', '2') ('2', '6', '1', '3') ('2', '6', '1', '4') ('2', '6', '1', '5') ('2', '6', '1', '6') ('2', '6', '1', '7') ('2', '6', '1', '8') ('2', '6', '1', '9') ('2', '6', '2', '0') ('2', '6', '2', '1') ('2', '6', '2', '2') ('2', '6', '2', '3') ('2', '6', '2', '4') ('2', '6', '2', '5') ('2', '6', '2', '6') ('2', '6', '2', '7') ('2', '6', '2', '8') ('2', '6', '2', '9') ('2', '6', '3', '0') ('2', '6', '3', '1') ('2', '6', '3', '2') ('2', '6', '3', '3') ('2', '6', '3', '4') ('2', '6', '3', '5') ('2', '6', '3', '6') ('2', '6', '3', '7') ('2', '6', '3', '8') ('2', '6', '3', '9') ('2', '6', '4', '0') ('2', '6', '4', '1') ('2', '6', '4', '2') ('2', '6', '4', '3') ('2', '6', '4', '4') ('2', '6', '4', '5') ('2', '6', '4', '6') ('2', '6', '4', '7') ('2', '6', '4', '8') ('2', '6', '4', '9') ('2', '6', '5', '0') ('2', '6', '5', '1') ('2', '6', '5', '2') ('2', '6', '5', '3') ('2', '6', '5', '4') ('2', '6', '5', '5') ('2', '6', '5', '6') ('2', '6', '5', '7') ('2', '6', '5', '8') ('2', '6', '5', '9') ('2', '6', '6', '0') ('2', '6', '6', '1') ('2', '6', '6', '2') ('2', '6', '6', '3') ('2', '6', '6', '4') ('2', '6', '6', '5') ('2', '6', '6', '6') ('2', '6', '6', '7') ('2', '6', '6', '8') ('2', '6', '6', '9') ('2', '6', '7', '0') ('2', '6', '7', '1') ('2', '6', '7', '2') ('2', '6', '7', '3') ('2', '6', '7', '4') ('2', '6', '7', '5') ('2', '6', '7', '6') ('2', '6', '7', '7') ('2', '6', '7', '8') ('2', '6', '7', '9') ('2', '6', '8', '0') ('2', '6', '8', '1') ('2', '6', '8', '2') ('2', '6', '8', '3') ('2', '6', '8', '4') ('2', '6', '8', '5') ('2', '6', '8', '6') ('2', '6', '8', '7') ('2', '6', '8', '8') ('2', '6', '8', '9') ('2', '6', '9', '0') ('2', '6', '9', '1') ('2', '6', '9', '2') ('2', '6', '9', '3') ('2', '6', '9', '4') ('2', '6', '9', '5') ('2', '6', '9', '6') ('2', '6', '9', '7') ('2', '6', '9', '8') ('2', '6', '9', '9') ('2', '7', '0', '0') ('2', '7', '0', '1') ('2', '7', '0', '2') ('2', '7', '0', '3') ('2', '7', '0', '4') ('2', '7', '0', '5') ('2', '7', '0', '6') ('2', '7', '0', '7') ('2', '7', '0', '8') ('2', '7', '0', '9') ('2', '7', '1', '0') ('2', '7', '1', '1') ('2', '7', '1', '2') ('2', '7', '1', '3') ('2', '7', '1', '4') ('2', '7', '1', '5') ('2', '7', '1', '6') ('2', '7', '1', '7') ('2', '7', '1', '8') ('2', '7', '1', '9') ('2', '7', '2', '0') ('2', '7', '2', '1') ('2', '7', '2', '2') ('2', '7', '2', '3') ('2', '7', '2', '4') ('2', '7', '2', '5') ('2', '7', '2', '6') ('2', '7', '2', '7') ('2', '7', '2', '8') ('2', '7', '2', '9') ('2', '7', '3', '0') ('2', '7', '3', '1') ('2', '7', '3', '2') ('2', '7', '3', '3') ('2', '7', '3', '4') ('2', '7', '3', '5') ('2', '7', '3', '6') ('2', '7', '3', '7') ('2', '7', '3', '8') ('2', '7', '3', '9') ('2', '7', '4', '0') ('2', '7', '4', '1') ('2', '7', '4', '2') ('2', '7', '4', '3') ('2', '7', '4', '4') ('2', '7', '4', '5') ('2', '7', '4', '6') ('2', '7', '4', '7') ('2', '7', '4', '8') ('2', '7', '4', '9') ('2', '7', '5', '0') ('2', '7', '5', '1') ('2', '7', '5', '2') ('2', '7', '5', '3') ('2', '7', '5', '4') ('2', '7', '5', '5') ('2', '7', '5', '6') ('2', '7', '5', '7') ('2', '7', '5', '8') ('2', '7', '5', '9') ('2', '7', '6', '0') ('2', '7', '6', '1') ('2', '7', '6', '2') ('2', '7', '6', '3') ('2', '7', '6', '4') ('2', '7', '6', '5') ('2', '7', '6', '6') ('2', '7', '6', '7') ('2', '7', '6', '8') ('2', '7', '6', '9') ('2', '7', '7', '0') ('2', '7', '7', '1') ('2', '7', '7', '2') ('2', '7', '7', '3') ('2', '7', '7', '4') ('2', '7', '7', '5') ('2', '7', '7', '6') ('2', '7', '7', '7') ('2', '7', '7', '8') ('2', '7', '7', '9') ('2', '7', '8', '0') ('2', '7', '8', '1') ('2', '7', '8', '2') ('2', '7', '8', '3') ('2', '7', '8', '4') ('2', '7', '8', '5') ('2', '7', '8', '6') ('2', '7', '8', '7') ('2', '7', '8', '8') ('2', '7', '8', '9') ('2', '7', '9', '0') ('2', '7', '9', '1') ('2', '7', '9', '2') ('2', '7', '9', '3') ('2', '7', '9', '4') ('2', '7', '9', '5') ('2', '7', '9', '6') ('2', '7', '9', '7') ('2', '7', '9', '8') ('2', '7', '9', '9') ('2', '8', '0', '0') ('2', '8', '0', '1') ('2', '8', '0', '2') ('2', '8', '0', '3') ('2', '8', '0', '4') ('2', '8', '0', '5') ('2', '8', '0', '6') ('2', '8', '0', '7') ('2', '8', '0', '8') ('2', '8', '0', '9') ('2', '8', '1', '0') ('2', '8', '1', '1') ('2', '8', '1', '2') ('2', '8', '1', '3') ('2', '8', '1', '4') ('2', '8', '1', '5') ('2', '8', '1', '6') ('2', '8', '1', '7') ('2', '8', '1', '8') ('2', '8', '1', '9') ('2', '8', '2', '0') ('2', '8', '2', '1') ('2', '8', '2', '2') ('2', '8', '2', '3') ('2', '8', '2', '4') ('2', '8', '2', '5') ('2', '8', '2', '6') ('2', '8', '2', '7') ('2', '8', '2', '8') ('2', '8', '2', '9') ('2', '8', '3', '0') ('2', '8', '3', '1') ('2', '8', '3', '2') ('2', '8', '3', '3') ('2', '8', '3', '4') ('2', '8', '3', '5') ('2', '8', '3', '6') ('2', '8', '3', '7') ('2', '8', '3', '8') ('2', '8', '3', '9') ('2', '8', '4', '0') ('2', '8', '4', '1') ('2', '8', '4', '2') ('2', '8', '4', '3') ('2', '8', '4', '4') ('2', '8', '4', '5') ('2', '8', '4', '6') ('2', '8', '4', '7') ('2', '8', '4', '8') ('2', '8', '4', '9') ('2', '8', '5', '0') ('2', '8', '5', '1') ('2', '8', '5', '2') ('2', '8', '5', '3') ('2', '8', '5', '4') ('2', '8', '5', '5') ('2', '8', '5', '6') ('2', '8', '5', '7') ('2', '8', '5', '8') ('2', '8', '5', '9') ('2', '8', '6', '0') ('2', '8', '6', '1') ('2', '8', '6', '2') ('2', '8', '6', '3') ('2', '8', '6', '4') ('2', '8', '6', '5') ('2', '8', '6', '6') ('2', '8', '6', '7') ('2', '8', '6', '8') ('2', '8', '6', '9') ('2', '8', '7', '0') ('2', '8', '7', '1') ('2', '8', '7', '2') ('2', '8', '7', '3') ('2', '8', '7', '4') ('2', '8', '7', '5') ('2', '8', '7', '6') ('2', '8', '7', '7') ('2', '8', '7', '8') ('2', '8', '7', '9') ('2', '8', '8', '0') ('2', '8', '8', '1') ('2', '8', '8', '2') ('2', '8', '8', '3') ('2', '8', '8', '4') ('2', '8', '8', '5') ('2', '8', '8', '6') ('2', '8', '8', '7') ('2', '8', '8', '8') ('2', '8', '8', '9') ('2', '8', '9', '0') ('2', '8', '9', '1') ('2', '8', '9', '2') ('2', '8', '9', '3') ('2', '8', '9', '4') ('2', '8', '9', '5') ('2', '8', '9', '6') ('2', '8', '9', '7') ('2', '8', '9', '8') ('2', '8', '9', '9') ('2', '9', '0', '0') ('2', '9', '0', '1') ('2', '9', '0', '2') ('2', '9', '0', '3') ('2', '9', '0', '4') ('2', '9', '0', '5') ('2', '9', '0', '6') ('2', '9', '0', '7') ('2', '9', '0', '8') ('2', '9', '0', '9') ('2', '9', '1', '0') ('2', '9', '1', '1') ('2', '9', '1', '2') ('2', '9', '1', '3') ('2', '9', '1', '4') ('2', '9', '1', '5') ('2', '9', '1', '6') ('2', '9', '1', '7') ('2', '9', '1', '8') ('2', '9', '1', '9') ('2', '9', '2', '0') ('2', '9', '2', '1') ('2', '9', '2', '2') ('2', '9', '2', '3') ('2', '9', '2', '4') ('2', '9', '2', '5') ('2', '9', '2', '6') ('2', '9', '2', '7') ('2', '9', '2', '8') ('2', '9', '2', '9') ('2', '9', '3', '0') ('2', '9', '3', '1') ('2', '9', '3', '2') ('2', '9', '3', '3') ('2', '9', '3', '4') ('2', '9', '3', '5') ('2', '9', '3', '6') ('2', '9', '3', '7') ('2', '9', '3', '8') ('2', '9', '3', '9') ('2', '9', '4', '0') ('2', '9', '4', '1') ('2', '9', '4', '2') ('2', '9', '4', '3') ('2', '9', '4', '4') ('2', '9', '4', '5') ('2', '9', '4', '6') ('2', '9', '4', '7') ('2', '9', '4', '8') ('2', '9', '4', '9') ('2', '9', '5', '0') ('2', '9', '5', '1') ('2', '9', '5', '2') ('2', '9', '5', '3') ('2', '9', '5', '4') ('2', '9', '5', '5') ('2', '9', '5', '6') ('2', '9', '5', '7') ('2', '9', '5', '8') ('2', '9', '5', '9') ('2', '9', '6', '0') ('2', '9', '6', '1') ('2', '9', '6', '2') ('2', '9', '6', '3') ('2', '9', '6', '4') ('2', '9', '6', '5') ('2', '9', '6', '6') ('2', '9', '6', '7') ('2', '9', '6', '8') ('2', '9', '6', '9') ('2', '9', '7', '0') ('2', '9', '7', '1') ('2', '9', '7', '2') ('2', '9', '7', '3') ('2', '9', '7', '4') ('2', '9', '7', '5') ('2', '9', '7', '6') ('2', '9', '7', '7') ('2', '9', '7', '8') ('2', '9', '7', '9') ('2', '9', '8', '0') ('2', '9', '8', '1') ('2', '9', '8', '2') ('2', '9', '8', '3') ('2', '9', '8', '4') ('2', '9', '8', '5') ('2', '9', '8', '6') ('2', '9', '8', '7') ('2', '9', '8', '8') ('2', '9', '8', '9') ('2', '9', '9', '0') ('2', '9', '9', '1') ('2', '9', '9', '2') ('2', '9', '9', '3') ('2', '9', '9', '4') ('2', '9', '9', '5') ('2', '9', '9', '6') ('2', '9', '9', '7') ('2', '9', '9', '8') ('2', '9', '9', '9') ('3', '0', '0', '0') ('3', '0', '0', '1') ('3', '0', '0', '2') ('3', '0', '0', '3') ('3', '0', '0', '4') ('3', '0', '0', '5') ('3', '0', '0', '6') ('3', '0', '0', '7') ('3', '0', '0', '8') ('3', '0', '0', '9') ('3', '0', '1', '0') ('3', '0', '1', '1') ('3', '0', '1', '2') ('3', '0', '1', '3') ('3', '0', '1', '4') ('3', '0', '1', '5') ('3', '0', '1', '6') ('3', '0', '1', '7') ('3', '0', '1', '8') ('3', '0', '1', '9') ('3', '0', '2', '0') ('3', '0', '2', '1') ('3', '0', '2', '2') ('3', '0', '2', '3') ('3', '0', '2', '4') ('3', '0', '2', '5') ('3', '0', '2', '6') ('3', '0', '2', '7') ('3', '0', '2', '8') ('3', '0', '2', '9') ('3', '0', '3', '0') ('3', '0', '3', '1') ('3', '0', '3', '2') ('3', '0', '3', '3') ('3', '0', '3', '4') ('3', '0', '3', '5') ('3', '0', '3', '6') ('3', '0', '3', '7') ('3', '0', '3', '8') ('3', '0', '3', '9') ('3', '0', '4', '0') ('3', '0', '4', '1') ('3', '0', '4', '2') ('3', '0', '4', '3') ('3', '0', '4', '4') ('3', '0', '4', '5') ('3', '0', '4', '6') ('3', '0', '4', '7') ('3', '0', '4', '8') ('3', '0', '4', '9') ('3', '0', '5', '0') ('3', '0', '5', '1') ('3', '0', '5', '2') ('3', '0', '5', '3') ('3', '0', '5', '4') ('3', '0', '5', '5') ('3', '0', '5', '6') ('3', '0', '5', '7') ('3', '0', '5', '8') ('3', '0', '5', '9') ('3', '0', '6', '0') ('3', '0', '6', '1') ('3', '0', '6', '2') ('3', '0', '6', '3') ('3', '0', '6', '4') ('3', '0', '6', '5') ('3', '0', '6', '6') ('3', '0', '6', '7') ('3', '0', '6', '8') ('3', '0', '6', '9') ('3', '0', '7', '0') ('3', '0', '7', '1') ('3', '0', '7', '2') ('3', '0', '7', '3') ('3', '0', '7', '4') ('3', '0', '7', '5') ('3', '0', '7', '6') ('3', '0', '7', '7') ('3', '0', '7', '8') ('3', '0', '7', '9') ('3', '0', '8', '0') ('3', '0', '8', '1') ('3', '0', '8', '2') ('3', '0', '8', '3') ('3', '0', '8', '4') ('3', '0', '8', '5') ('3', '0', '8', '6') ('3', '0', '8', '7') ('3', '0', '8', '8') ('3', '0', '8', '9') ('3', '0', '9', '0') ('3', '0', '9', '1') ('3', '0', '9', '2') ('3', '0', '9', '3') ('3', '0', '9', '4') ('3', '0', '9', '5') ('3', '0', '9', '6') ('3', '0', '9', '7') ('3', '0', '9', '8') ('3', '0', '9', '9') ('3', '1', '0', '0') ('3', '1', '0', '1') ('3', '1', '0', '2') ('3', '1', '0', '3') ('3', '1', '0', '4') ('3', '1', '0', '5') ('3', '1', '0', '6') ('3', '1', '0', '7') ('3', '1', '0', '8') ('3', '1', '0', '9') ('3', '1', '1', '0') ('3', '1', '1', '1') ('3', '1', '1', '2') ('3', '1', '1', '3') ('3', '1', '1', '4') ('3', '1', '1', '5') ('3', '1', '1', '6') ('3', '1', '1', '7') ('3', '1', '1', '8') ('3', '1', '1', '9') ('3', '1', '2', '0') ('3', '1', '2', '1') ('3', '1', '2', '2') ('3', '1', '2', '3') ('3', '1', '2', '4') ('3', '1', '2', '5') ('3', '1', '2', '6') ('3', '1', '2', '7') ('3', '1', '2', '8') ('3', '1', '2', '9') ('3', '1', '3', '0') ('3', '1', '3', '1') ('3', '1', '3', '2') ('3', '1', '3', '3') ('3', '1', '3', '4') ('3', '1', '3', '5') ('3', '1', '3', '6') ('3', '1', '3', '7') ('3', '1', '3', '8') ('3', '1', '3', '9') ('3', '1', '4', '0') ('3', '1', '4', '1') ('3', '1', '4', '2') ('3', '1', '4', '3') ('3', '1', '4', '4') ('3', '1', '4', '5') ('3', '1', '4', '6') ('3', '1', '4', '7') ('3', '1', '4', '8') ('3', '1', '4', '9') ('3', '1', '5', '0') ('3', '1', '5', '1') ('3', '1', '5', '2') ('3', '1', '5', '3') ('3', '1', '5', '4') ('3', '1', '5', '5') ('3', '1', '5', '6') ('3', '1', '5', '7') ('3', '1', '5', '8') ('3', '1', '5', '9') ('3', '1', '6', '0') ('3', '1', '6', '1') ('3', '1', '6', '2') ('3', '1', '6', '3') ('3', '1', '6', '4') ('3', '1', '6', '5') ('3', '1', '6', '6') ('3', '1', '6', '7') ('3', '1', '6', '8') ('3', '1', '6', '9') ('3', '1', '7', '0') ('3', '1', '7', '1') ('3', '1', '7', '2') ('3', '1', '7', '3') ('3', '1', '7', '4') ('3', '1', '7', '5') ('3', '1', '7', '6') ('3', '1', '7', '7') ('3', '1', '7', '8') ('3', '1', '7', '9') ('3', '1', '8', '0') ('3', '1', '8', '1') ('3', '1', '8', '2') ('3', '1', '8', '3') ('3', '1', '8', '4') ('3', '1', '8', '5') ('3', '1', '8', '6') ('3', '1', '8', '7') ('3', '1', '8', '8') ('3', '1', '8', '9') ('3', '1', '9', '0') ('3', '1', '9', '1') ('3', '1', '9', '2') ('3', '1', '9', '3') ('3', '1', '9', '4') ('3', '1', '9', '5') ('3', '1', '9', '6') ('3', '1', '9', '7') ('3', '1', '9', '8') ('3', '1', '9', '9') ('3', '2', '0', '0') ('3', '2', '0', '1') ('3', '2', '0', '2') ('3', '2', '0', '3') ('3', '2', '0', '4') ('3', '2', '0', '5') ('3', '2', '0', '6') ('3', '2', '0', '7') ('3', '2', '0', '8') ('3', '2', '0', '9') ('3', '2', '1', '0') ('3', '2', '1', '1') ('3', '2', '1', '2') ('3', '2', '1', '3') ('3', '2', '1', '4') ('3', '2', '1', '5') ('3', '2', '1', '6') ('3', '2', '1', '7') ('3', '2', '1', '8') ('3', '2', '1', '9') ('3', '2', '2', '0') ('3', '2', '2', '1') ('3', '2', '2', '2') ('3', '2', '2', '3') ('3', '2', '2', '4') ('3', '2', '2', '5') ('3', '2', '2', '6') ('3', '2', '2', '7') ('3', '2', '2', '8') ('3', '2', '2', '9') ('3', '2', '3', '0') ('3', '2', '3', '1') ('3', '2', '3', '2') ('3', '2', '3', '3') ('3', '2', '3', '4') ('3', '2', '3', '5') ('3', '2', '3', '6') ('3', '2', '3', '7') ('3', '2', '3', '8') ('3', '2', '3', '9') ('3', '2', '4', '0') ('3', '2', '4', '1') ('3', '2', '4', '2') ('3', '2', '4', '3') ('3', '2', '4', '4') ('3', '2', '4', '5') ('3', '2', '4', '6') ('3', '2', '4', '7') ('3', '2', '4', '8') ('3', '2', '4', '9') ('3', '2', '5', '0') ('3', '2', '5', '1') ('3', '2', '5', '2') ('3', '2', '5', '3') ('3', '2', '5', '4') ('3', '2', '5', '5') ('3', '2', '5', '6') ('3', '2', '5', '7') ('3', '2', '5', '8') ('3', '2', '5', '9') ('3', '2', '6', '0') ('3', '2', '6', '1') ('3', '2', '6', '2') ('3', '2', '6', '3') ('3', '2', '6', '4') ('3', '2', '6', '5') ('3', '2', '6', '6') ('3', '2', '6', '7') ('3', '2', '6', '8') ('3', '2', '6', '9') ('3', '2', '7', '0') ('3', '2', '7', '1') ('3', '2', '7', '2') ('3', '2', '7', '3') ('3', '2', '7', '4') ('3', '2', '7', '5') ('3', '2', '7', '6') ('3', '2', '7', '7') ('3', '2', '7', '8') ('3', '2', '7', '9') ('3', '2', '8', '0') ('3', '2', '8', '1') ('3', '2', '8', '2') ('3', '2', '8', '3') ('3', '2', '8', '4') ('3', '2', '8', '5') ('3', '2', '8', '6') ('3', '2', '8', '7') ('3', '2', '8', '8') ('3', '2', '8', '9') ('3', '2', '9', '0') ('3', '2', '9', '1') ('3', '2', '9', '2') ('3', '2', '9', '3') ('3', '2', '9', '4') ('3', '2', '9', '5') ('3', '2', '9', '6') ('3', '2', '9', '7') ('3', '2', '9', '8') ('3', '2', '9', '9') ('3', '3', '0', '0') ('3', '3', '0', '1') ('3', '3', '0', '2') ('3', '3', '0', '3') ('3', '3', '0', '4') ('3', '3', '0', '5') ('3', '3', '0', '6') ('3', '3', '0', '7') ('3', '3', '0', '8') ('3', '3', '0', '9') ('3', '3', '1', '0') ('3', '3', '1', '1') ('3', '3', '1', '2') ('3', '3', '1', '3') ('3', '3', '1', '4') ('3', '3', '1', '5') ('3', '3', '1', '6') ('3', '3', '1', '7') ('3', '3', '1', '8') ('3', '3', '1', '9') ('3', '3', '2', '0') ('3', '3', '2', '1') ('3', '3', '2', '2') ('3', '3', '2', '3') ('3', '3', '2', '4') ('3', '3', '2', '5') ('3', '3', '2', '6') ('3', '3', '2', '7') ('3', '3', '2', '8') ('3', '3', '2', '9') ('3', '3', '3', '0') ('3', '3', '3', '1') ('3', '3', '3', '2') ('3', '3', '3', '3') ('3', '3', '3', '4') ('3', '3', '3', '5') ('3', '3', '3', '6') ('3', '3', '3', '7') ('3', '3', '3', '8') ('3', '3', '3', '9') ('3', '3', '4', '0') ('3', '3', '4', '1') ('3', '3', '4', '2') ('3', '3', '4', '3') ('3', '3', '4', '4') ('3', '3', '4', '5') ('3', '3', '4', '6') ('3', '3', '4', '7') ('3', '3', '4', '8') ('3', '3', '4', '9') ('3', '3', '5', '0') ('3', '3', '5', '1') ('3', '3', '5', '2') ('3', '3', '5', '3') ('3', '3', '5', '4') ('3', '3', '5', '5') ('3', '3', '5', '6') ('3', '3', '5', '7') ('3', '3', '5', '8') ('3', '3', '5', '9') ('3', '3', '6', '0') ('3', '3', '6', '1') ('3', '3', '6', '2') ('3', '3', '6', '3') ('3', '3', '6', '4') ('3', '3', '6', '5') ('3', '3', '6', '6') ('3', '3', '6', '7') ('3', '3', '6', '8') ('3', '3', '6', '9') ('3', '3', '7', '0') ('3', '3', '7', '1') ('3', '3', '7', '2') ('3', '3', '7', '3') ('3', '3', '7', '4') ('3', '3', '7', '5') ('3', '3', '7', '6') ('3', '3', '7', '7') ('3', '3', '7', '8') ('3', '3', '7', '9') ('3', '3', '8', '0') ('3', '3', '8', '1') ('3', '3', '8', '2') ('3', '3', '8', '3') ('3', '3', '8', '4') ('3', '3', '8', '5') ('3', '3', '8', '6') ('3', '3', '8', '7') ('3', '3', '8', '8') ('3', '3', '8', '9') ('3', '3', '9', '0') ('3', '3', '9', '1') ('3', '3', '9', '2') ('3', '3', '9', '3') ('3', '3', '9', '4') ('3', '3', '9', '5') ('3', '3', '9', '6') ('3', '3', '9', '7') ('3', '3', '9', '8') ('3', '3', '9', '9') ('3', '4', '0', '0') ('3', '4', '0', '1') ('3', '4', '0', '2') ('3', '4', '0', '3') ('3', '4', '0', '4') ('3', '4', '0', '5') ('3', '4', '0', '6') ('3', '4', '0', '7') ('3', '4', '0', '8') ('3', '4', '0', '9') ('3', '4', '1', '0') ('3', '4', '1', '1') ('3', '4', '1', '2') ('3', '4', '1', '3') ('3', '4', '1', '4') ('3', '4', '1', '5') ('3', '4', '1', '6') ('3', '4', '1', '7') ('3', '4', '1', '8') ('3', '4', '1', '9') ('3', '4', '2', '0') ('3', '4', '2', '1') ('3', '4', '2', '2') ('3', '4', '2', '3') ('3', '4', '2', '4') ('3', '4', '2', '5') ('3', '4', '2', '6') ('3', '4', '2', '7') ('3', '4', '2', '8') ('3', '4', '2', '9') ('3', '4', '3', '0') ('3', '4', '3', '1') ('3', '4', '3', '2') ('3', '4', '3', '3') ('3', '4', '3', '4') ('3', '4', '3', '5') ('3', '4', '3', '6') ('3', '4', '3', '7') ('3', '4', '3', '8') ('3', '4', '3', '9') ('3', '4', '4', '0') ('3', '4', '4', '1') ('3', '4', '4', '2') ('3', '4', '4', '3') ('3', '4', '4', '4') ('3', '4', '4', '5') ('3', '4', '4', '6') ('3', '4', '4', '7') ('3', '4', '4', '8') ('3', '4', '4', '9') ('3', '4', '5', '0') ('3', '4', '5', '1') ('3', '4', '5', '2') ('3', '4', '5', '3') ('3', '4', '5', '4') ('3', '4', '5', '5') ('3', '4', '5', '6') ('3', '4', '5', '7') ('3', '4', '5', '8') ('3', '4', '5', '9') ('3', '4', '6', '0') ('3', '4', '6', '1') ('3', '4', '6', '2') ('3', '4', '6', '3') ('3', '4', '6', '4') ('3', '4', '6', '5') ('3', '4', '6', '6') ('3', '4', '6', '7') ('3', '4', '6', '8') ('3', '4', '6', '9') ('3', '4', '7', '0') ('3', '4', '7', '1') ('3', '4', '7', '2') ('3', '4', '7', '3') ('3', '4', '7', '4') ('3', '4', '7', '5') ('3', '4', '7', '6') ('3', '4', '7', '7') ('3', '4', '7', '8') ('3', '4', '7', '9') ('3', '4', '8', '0') ('3', '4', '8', '1') ('3', '4', '8', '2') ('3', '4', '8', '3') ('3', '4', '8', '4') ('3', '4', '8', '5') ('3', '4', '8', '6') ('3', '4', '8', '7') ('3', '4', '8', '8') ('3', '4', '8', '9') ('3', '4', '9', '0') ('3', '4', '9', '1') ('3', '4', '9', '2') ('3', '4', '9', '3') ('3', '4', '9', '4') ('3', '4', '9', '5') ('3', '4', '9', '6') ('3', '4', '9', '7') ('3', '4', '9', '8') ('3', '4', '9', '9') ('3', '5', '0', '0') ('3', '5', '0', '1') ('3', '5', '0', '2') ('3', '5', '0', '3') ('3', '5', '0', '4') ('3', '5', '0', '5') ('3', '5', '0', '6') ('3', '5', '0', '7') ('3', '5', '0', '8') ('3', '5', '0', '9') ('3', '5', '1', '0') ('3', '5', '1', '1') ('3', '5', '1', '2') ('3', '5', '1', '3') ('3', '5', '1', '4') ('3', '5', '1', '5') ('3', '5', '1', '6') ('3', '5', '1', '7') ('3', '5', '1', '8') ('3', '5', '1', '9') ('3', '5', '2', '0') ('3', '5', '2', '1') ('3', '5', '2', '2') ('3', '5', '2', '3') ('3', '5', '2', '4') ('3', '5', '2', '5') ('3', '5', '2', '6') ('3', '5', '2', '7') ('3', '5', '2', '8') ('3', '5', '2', '9') ('3', '5', '3', '0') ('3', '5', '3', '1') ('3', '5', '3', '2') ('3', '5', '3', '3') ('3', '5', '3', '4') ('3', '5', '3', '5') ('3', '5', '3', '6') ('3', '5', '3', '7') ('3', '5', '3', '8') ('3', '5', '3', '9') ('3', '5', '4', '0') ('3', '5', '4', '1') ('3', '5', '4', '2') ('3', '5', '4', '3') ('3', '5', '4', '4') ('3', '5', '4', '5') ('3', '5', '4', '6') ('3', '5', '4', '7') ('3', '5', '4', '8') ('3', '5', '4', '9') ('3', '5', '5', '0') ('3', '5', '5', '1') ('3', '5', '5', '2') ('3', '5', '5', '3') ('3', '5', '5', '4') ('3', '5', '5', '5') ('3', '5', '5', '6') ('3', '5', '5', '7') ('3', '5', '5', '8') ('3', '5', '5', '9') ('3', '5', '6', '0') ('3', '5', '6', '1') ('3', '5', '6', '2') ('3', '5', '6', '3') ('3', '5', '6', '4') ('3', '5', '6', '5') ('3', '5', '6', '6') ('3', '5', '6', '7') ('3', '5', '6', '8') ('3', '5', '6', '9') ('3', '5', '7', '0') ('3', '5', '7', '1') ('3', '5', '7', '2') ('3', '5', '7', '3') ('3', '5', '7', '4') ('3', '5', '7', '5') ('3', '5', '7', '6') ('3', '5', '7', '7') ('3', '5', '7', '8') ('3', '5', '7', '9') ('3', '5', '8', '0') ('3', '5', '8', '1') ('3', '5', '8', '2') ('3', '5', '8', '3') ('3', '5', '8', '4') ('3', '5', '8', '5') ('3', '5', '8', '6') ('3', '5', '8', '7') ('3', '5', '8', '8') ('3', '5', '8', '9') ('3', '5', '9', '0') ('3', '5', '9', '1') ('3', '5', '9', '2') ('3', '5', '9', '3') ('3', '5', '9', '4') ('3', '5', '9', '5') ('3', '5', '9', '6') ('3', '5', '9', '7') ('3', '5', '9', '8') ('3', '5', '9', '9') ('3', '6', '0', '0') ('3', '6', '0', '1') ('3', '6', '0', '2') ('3', '6', '0', '3') ('3', '6', '0', '4') ('3', '6', '0', '5') ('3', '6', '0', '6') ('3', '6', '0', '7') ('3', '6', '0', '8') ('3', '6', '0', '9') ('3', '6', '1', '0') ('3', '6', '1', '1') ('3', '6', '1', '2') ('3', '6', '1', '3') ('3', '6', '1', '4') ('3', '6', '1', '5') ('3', '6', '1', '6') ('3', '6', '1', '7') ('3', '6', '1', '8') ('3', '6', '1', '9') ('3', '6', '2', '0') ('3', '6', '2', '1') ('3', '6', '2', '2') ('3', '6', '2', '3') ('3', '6', '2', '4') ('3', '6', '2', '5') ('3', '6', '2', '6') ('3', '6', '2', '7') ('3', '6', '2', '8') ('3', '6', '2', '9') ('3', '6', '3', '0') ('3', '6', '3', '1') ('3', '6', '3', '2') ('3', '6', '3', '3') ('3', '6', '3', '4') ('3', '6', '3', '5') ('3', '6', '3', '6') ('3', '6', '3', '7') ('3', '6', '3', '8') ('3', '6', '3', '9') ('3', '6', '4', '0') ('3', '6', '4', '1') ('3', '6', '4', '2') ('3', '6', '4', '3') ('3', '6', '4', '4') ('3', '6', '4', '5') ('3', '6', '4', '6') ('3', '6', '4', '7') ('3', '6', '4', '8') ('3', '6', '4', '9') ('3', '6', '5', '0') ('3', '6', '5', '1') ('3', '6', '5', '2') ('3', '6', '5', '3') ('3', '6', '5', '4') ('3', '6', '5', '5') ('3', '6', '5', '6') ('3', '6', '5', '7') ('3', '6', '5', '8') ('3', '6', '5', '9') ('3', '6', '6', '0') ('3', '6', '6', '1') ('3', '6', '6', '2') ('3', '6', '6', '3') ('3', '6', '6', '4') ('3', '6', '6', '5') ('3', '6', '6', '6') ('3', '6', '6', '7') ('3', '6', '6', '8') ('3', '6', '6', '9') ('3', '6', '7', '0') ('3', '6', '7', '1') ('3', '6', '7', '2') ('3', '6', '7', '3') ('3', '6', '7', '4') ('3', '6', '7', '5') ('3', '6', '7', '6') ('3', '6', '7', '7') ('3', '6', '7', '8') ('3', '6', '7', '9') ('3', '6', '8', '0') ('3', '6', '8', '1') ('3', '6', '8', '2') ('3', '6', '8', '3') ('3', '6', '8', '4') ('3', '6', '8', '5') ('3', '6', '8', '6') ('3', '6', '8', '7') ('3', '6', '8', '8') ('3', '6', '8', '9') ('3', '6', '9', '0') ('3', '6', '9', '1') ('3', '6', '9', '2') ('3', '6', '9', '3') ('3', '6', '9', '4') ('3', '6', '9', '5') ('3', '6', '9', '6') ('3', '6', '9', '7') ('3', '6', '9', '8') ('3', '6', '9', '9') ('3', '7', '0', '0') ('3', '7', '0', '1') ('3', '7', '0', '2') ('3', '7', '0', '3') ('3', '7', '0', '4') ('3', '7', '0', '5') ('3', '7', '0', '6') ('3', '7', '0', '7') ('3', '7', '0', '8') ('3', '7', '0', '9') ('3', '7', '1', '0') ('3', '7', '1', '1') ('3', '7', '1', '2') ('3', '7', '1', '3') ('3', '7', '1', '4') ('3', '7', '1', '5') ('3', '7', '1', '6') ('3', '7', '1', '7') ('3', '7', '1', '8') ('3', '7', '1', '9') ('3', '7', '2', '0') ('3', '7', '2', '1') ('3', '7', '2', '2') ('3', '7', '2', '3') ('3', '7', '2', '4') ('3', '7', '2', '5') ('3', '7', '2', '6') ('3', '7', '2', '7') ('3', '7', '2', '8') ('3', '7', '2', '9') ('3', '7', '3', '0') ('3', '7', '3', '1') ('3', '7', '3', '2') ('3', '7', '3', '3') ('3', '7', '3', '4') ('3', '7', '3', '5') ('3', '7', '3', '6') ('3', '7', '3', '7') ('3', '7', '3', '8') ('3', '7', '3', '9') ('3', '7', '4', '0') ('3', '7', '4', '1') ('3', '7', '4', '2') ('3', '7', '4', '3') ('3', '7', '4', '4') ('3', '7', '4', '5') ('3', '7', '4', '6') ('3', '7', '4', '7') ('3', '7', '4', '8') ('3', '7', '4', '9') ('3', '7', '5', '0') ('3', '7', '5', '1') ('3', '7', '5', '2') ('3', '7', '5', '3') ('3', '7', '5', '4') ('3', '7', '5', '5') ('3', '7', '5', '6') ('3', '7', '5', '7') ('3', '7', '5', '8') ('3', '7', '5', '9') ('3', '7', '6', '0') ('3', '7', '6', '1') ('3', '7', '6', '2') ('3', '7', '6', '3') ('3', '7', '6', '4') ('3', '7', '6', '5') ('3', '7', '6', '6') ('3', '7', '6', '7') ('3', '7', '6', '8') ('3', '7', '6', '9') ('3', '7', '7', '0') ('3', '7', '7', '1') ('3', '7', '7', '2') ('3', '7', '7', '3') ('3', '7', '7', '4') ('3', '7', '7', '5') ('3', '7', '7', '6') ('3', '7', '7', '7') ('3', '7', '7', '8') ('3', '7', '7', '9') ('3', '7', '8', '0') ('3', '7', '8', '1') ('3', '7', '8', '2') ('3', '7', '8', '3') ('3', '7', '8', '4') ('3', '7', '8', '5') ('3', '7', '8', '6') ('3', '7', '8', '7') ('3', '7', '8', '8') ('3', '7', '8', '9') ('3', '7', '9', '0') ('3', '7', '9', '1') ('3', '7', '9', '2') ('3', '7', '9', '3') ('3', '7', '9', '4') ('3', '7', '9', '5') ('3', '7', '9', '6') ('3', '7', '9', '7') ('3', '7', '9', '8') ('3', '7', '9', '9') ('3', '8', '0', '0') ('3', '8', '0', '1') ('3', '8', '0', '2') ('3', '8', '0', '3') ('3', '8', '0', '4') ('3', '8', '0', '5') ('3', '8', '0', '6') ('3', '8', '0', '7') ('3', '8', '0', '8') ('3', '8', '0', '9') ('3', '8', '1', '0') ('3', '8', '1', '1') ('3', '8', '1', '2') ('3', '8', '1', '3') ('3', '8', '1', '4') ('3', '8', '1', '5') ('3', '8', '1', '6') ('3', '8', '1', '7') ('3', '8', '1', '8') ('3', '8', '1', '9') ('3', '8', '2', '0') ('3', '8', '2', '1') ('3', '8', '2', '2') ('3', '8', '2', '3') ('3', '8', '2', '4') ('3', '8', '2', '5') ('3', '8', '2', '6') ('3', '8', '2', '7') ('3', '8', '2', '8') ('3', '8', '2', '9') ('3', '8', '3', '0') ('3', '8', '3', '1') ('3', '8', '3', '2') ('3', '8', '3', '3') ('3', '8', '3', '4') ('3', '8', '3', '5') ('3', '8', '3', '6') ('3', '8', '3', '7') ('3', '8', '3', '8') ('3', '8', '3', '9') ('3', '8', '4', '0') ('3', '8', '4', '1') ('3', '8', '4', '2') ('3', '8', '4', '3') ('3', '8', '4', '4') ('3', '8', '4', '5') ('3', '8', '4', '6') ('3', '8', '4', '7') ('3', '8', '4', '8') ('3', '8', '4', '9') ('3', '8', '5', '0') ('3', '8', '5', '1') ('3', '8', '5', '2') ('3', '8', '5', '3') ('3', '8', '5', '4') ('3', '8', '5', '5') ('3', '8', '5', '6') ('3', '8', '5', '7') ('3', '8', '5', '8') ('3', '8', '5', '9') ('3', '8', '6', '0') ('3', '8', '6', '1') ('3', '8', '6', '2') ('3', '8', '6', '3') ('3', '8', '6', '4') ('3', '8', '6', '5') ('3', '8', '6', '6') ('3', '8', '6', '7') ('3', '8', '6', '8') ('3', '8', '6', '9') ('3', '8', '7', '0') ('3', '8', '7', '1') ('3', '8', '7', '2') ('3', '8', '7', '3') ('3', '8', '7', '4') ('3', '8', '7', '5') ('3', '8', '7', '6') ('3', '8', '7', '7') ('3', '8', '7', '8') ('3', '8', '7', '9') ('3', '8', '8', '0') ('3', '8', '8', '1') ('3', '8', '8', '2') ('3', '8', '8', '3') ('3', '8', '8', '4') ('3', '8', '8', '5') ('3', '8', '8', '6') ('3', '8', '8', '7') ('3', '8', '8', '8') ('3', '8', '8', '9') ('3', '8', '9', '0') ('3', '8', '9', '1') ('3', '8', '9', '2') ('3', '8', '9', '3') ('3', '8', '9', '4') ('3', '8', '9', '5') ('3', '8', '9', '6') ('3', '8', '9', '7') ('3', '8', '9', '8') ('3', '8', '9', '9') ('3', '9', '0', '0') ('3', '9', '0', '1') ('3', '9', '0', '2') ('3', '9', '0', '3') ('3', '9', '0', '4') ('3', '9', '0', '5') ('3', '9', '0', '6') ('3', '9', '0', '7') ('3', '9', '0', '8') ('3', '9', '0', '9') ('3', '9', '1', '0') ('3', '9', '1', '1') ('3', '9', '1', '2') ('3', '9', '1', '3') ('3', '9', '1', '4') ('3', '9', '1', '5') ('3', '9', '1', '6') ('3', '9', '1', '7') ('3', '9', '1', '8') ('3', '9', '1', '9') ('3', '9', '2', '0') ('3', '9', '2', '1') ('3', '9', '2', '2') ('3', '9', '2', '3') ('3', '9', '2', '4') ('3', '9', '2', '5') ('3', '9', '2', '6') ('3', '9', '2', '7') ('3', '9', '2', '8') ('3', '9', '2', '9') ('3', '9', '3', '0') ('3', '9', '3', '1') ('3', '9', '3', '2') ('3', '9', '3', '3') ('3', '9', '3', '4') ('3', '9', '3', '5') ('3', '9', '3', '6') ('3', '9', '3', '7') ('3', '9', '3', '8') ('3', '9', '3', '9') ('3', '9', '4', '0') ('3', '9', '4', '1') ('3', '9', '4', '2') ('3', '9', '4', '3') ('3', '9', '4', '4') ('3', '9', '4', '5') ('3', '9', '4', '6') ('3', '9', '4', '7') ('3', '9', '4', '8') ('3', '9', '4', '9') ('3', '9', '5', '0') ('3', '9', '5', '1') ('3', '9', '5', '2') ('3', '9', '5', '3') ('3', '9', '5', '4') ('3', '9', '5', '5') ('3', '9', '5', '6') ('3', '9', '5', '7') ('3', '9', '5', '8') ('3', '9', '5', '9') ('3', '9', '6', '0') ('3', '9', '6', '1') ('3', '9', '6', '2') ('3', '9', '6', '3') ('3', '9', '6', '4') ('3', '9', '6', '5') ('3', '9', '6', '6') ('3', '9', '6', '7') ('3', '9', '6', '8') ('3', '9', '6', '9') ('3', '9', '7', '0') ('3', '9', '7', '1') ('3', '9', '7', '2') ('3', '9', '7', '3') ('3', '9', '7', '4') ('3', '9', '7', '5') ('3', '9', '7', '6') ('3', '9', '7', '7') ('3', '9', '7', '8') ('3', '9', '7', '9') ('3', '9', '8', '0') ('3', '9', '8', '1') ('3', '9', '8', '2') ('3', '9', '8', '3') ('3', '9', '8', '4') ('3', '9', '8', '5') ('3', '9', '8', '6') ('3', '9', '8', '7') ('3', '9', '8', '8') ('3', '9', '8', '9') ('3', '9', '9', '0') ('3', '9', '9', '1') ('3', '9', '9', '2') ('3', '9', '9', '3') ('3', '9', '9', '4') ('3', '9', '9', '5') ('3', '9', '9', '6') ('3', '9', '9', '7') ('3', '9', '9', '8') ('3', '9', '9', '9') ('4', '0', '0', '0') ('4', '0', '0', '1') ('4', '0', '0', '2') ('4', '0', '0', '3') ('4', '0', '0', '4') ('4', '0', '0', '5') ('4', '0', '0', '6') ('4', '0', '0', '7') ('4', '0', '0', '8') ('4', '0', '0', '9') ('4', '0', '1', '0') ('4', '0', '1', '1') ('4', '0', '1', '2') ('4', '0', '1', '3') ('4', '0', '1', '4') ('4', '0', '1', '5') ('4', '0', '1', '6') ('4', '0', '1', '7') ('4', '0', '1', '8') ('4', '0', '1', '9') ('4', '0', '2', '0') ('4', '0', '2', '1') ('4', '0', '2', '2') ('4', '0', '2', '3') ('4', '0', '2', '4') ('4', '0', '2', '5') ('4', '0', '2', '6') ('4', '0', '2', '7') ('4', '0', '2', '8') ('4', '0', '2', '9') ('4', '0', '3', '0') ('4', '0', '3', '1') ('4', '0', '3', '2') ('4', '0', '3', '3') ('4', '0', '3', '4') ('4', '0', '3', '5') ('4', '0', '3', '6') ('4', '0', '3', '7') ('4', '0', '3', '8') ('4', '0', '3', '9') ('4', '0', '4', '0') ('4', '0', '4', '1') ('4', '0', '4', '2') ('4', '0', '4', '3') ('4', '0', '4', '4') ('4', '0', '4', '5') ('4', '0', '4', '6') ('4', '0', '4', '7') ('4', '0', '4', '8') ('4', '0', '4', '9') ('4', '0', '5', '0') ('4', '0', '5', '1') ('4', '0', '5', '2') ('4', '0', '5', '3') ('4', '0', '5', '4') ('4', '0', '5', '5') ('4', '0', '5', '6') ('4', '0', '5', '7') ('4', '0', '5', '8') ('4', '0', '5', '9') ('4', '0', '6', '0') ('4', '0', '6', '1') ('4', '0', '6', '2') ('4', '0', '6', '3') ('4', '0', '6', '4') ('4', '0', '6', '5') ('4', '0', '6', '6') ('4', '0', '6', '7') ('4', '0', '6', '8') ('4', '0', '6', '9') ('4', '0', '7', '0') ('4', '0', '7', '1') ('4', '0', '7', '2') ('4', '0', '7', '3') ('4', '0', '7', '4') ('4', '0', '7', '5') ('4', '0', '7', '6') ('4', '0', '7', '7') ('4', '0', '7', '8') ('4', '0', '7', '9') ('4', '0', '8', '0') ('4', '0', '8', '1') ('4', '0', '8', '2') ('4', '0', '8', '3') ('4', '0', '8', '4') ('4', '0', '8', '5') ('4', '0', '8', '6') ('4', '0', '8', '7') ('4', '0', '8', '8') ('4', '0', '8', '9') ('4', '0', '9', '0') ('4', '0', '9', '1') ('4', '0', '9', '2') ('4', '0', '9', '3') ('4', '0', '9', '4') ('4', '0', '9', '5') ('4', '0', '9', '6') ('4', '0', '9', '7') ('4', '0', '9', '8') ('4', '0', '9', '9') ('4', '1', '0', '0') ('4', '1', '0', '1') ('4', '1', '0', '2') ('4', '1', '0', '3') ('4', '1', '0', '4') ('4', '1', '0', '5') ('4', '1', '0', '6') ('4', '1', '0', '7') ('4', '1', '0', '8') ('4', '1', '0', '9') ('4', '1', '1', '0') ('4', '1', '1', '1') ('4', '1', '1', '2') ('4', '1', '1', '3') ('4', '1', '1', '4') ('4', '1', '1', '5') ('4', '1', '1', '6') ('4', '1', '1', '7') ('4', '1', '1', '8') ('4', '1', '1', '9') ('4', '1', '2', '0') ('4', '1', '2', '1') ('4', '1', '2', '2') ('4', '1', '2', '3') ('4', '1', '2', '4') ('4', '1', '2', '5') ('4', '1', '2', '6') ('4', '1', '2', '7') ('4', '1', '2', '8') ('4', '1', '2', '9') ('4', '1', '3', '0') ('4', '1', '3', '1') ('4', '1', '3', '2') ('4', '1', '3', '3') ('4', '1', '3', '4') ('4', '1', '3', '5') ('4', '1', '3', '6') ('4', '1', '3', '7') ('4', '1', '3', '8') ('4', '1', '3', '9') ('4', '1', '4', '0') ('4', '1', '4', '1') ('4', '1', '4', '2') ('4', '1', '4', '3') ('4', '1', '4', '4') ('4', '1', '4', '5') ('4', '1', '4', '6') ('4', '1', '4', '7') ('4', '1', '4', '8') ('4', '1', '4', '9') ('4', '1', '5', '0') ('4', '1', '5', '1') ('4', '1', '5', '2') ('4', '1', '5', '3') ('4', '1', '5', '4') ('4', '1', '5', '5') ('4', '1', '5', '6') ('4', '1', '5', '7') ('4', '1', '5', '8') ('4', '1', '5', '9') ('4', '1', '6', '0') ('4', '1', '6', '1') ('4', '1', '6', '2') ('4', '1', '6', '3') ('4', '1', '6', '4') ('4', '1', '6', '5') ('4', '1', '6', '6') ('4', '1', '6', '7') ('4', '1', '6', '8') ('4', '1', '6', '9') ('4', '1', '7', '0') ('4', '1', '7', '1') ('4', '1', '7', '2') ('4', '1', '7', '3') ('4', '1', '7', '4') ('4', '1', '7', '5') ('4', '1', '7', '6') ('4', '1', '7', '7') ('4', '1', '7', '8') ('4', '1', '7', '9') ('4', '1', '8', '0') ('4', '1', '8', '1') ('4', '1', '8', '2') ('4', '1', '8', '3') ('4', '1', '8', '4') ('4', '1', '8', '5') ('4', '1', '8', '6') ('4', '1', '8', '7') ('4', '1', '8', '8') ('4', '1', '8', '9') ('4', '1', '9', '0') ('4', '1', '9', '1') ('4', '1', '9', '2') ('4', '1', '9', '3') ('4', '1', '9', '4') ('4', '1', '9', '5') ('4', '1', '9', '6') ('4', '1', '9', '7') ('4', '1', '9', '8') ('4', '1', '9', '9') ('4', '2', '0', '0') ('4', '2', '0', '1') ('4', '2', '0', '2') ('4', '2', '0', '3') ('4', '2', '0', '4') ('4', '2', '0', '5') ('4', '2', '0', '6') ('4', '2', '0', '7') ('4', '2', '0', '8') ('4', '2', '0', '9') ('4', '2', '1', '0') ('4', '2', '1', '1') ('4', '2', '1', '2') ('4', '2', '1', '3') ('4', '2', '1', '4') ('4', '2', '1', '5') ('4', '2', '1', '6') ('4', '2', '1', '7') ('4', '2', '1', '8') ('4', '2', '1', '9') ('4', '2', '2', '0') ('4', '2', '2', '1') ('4', '2', '2', '2') ('4', '2', '2', '3') ('4', '2', '2', '4') ('4', '2', '2', '5') ('4', '2', '2', '6') ('4', '2', '2', '7') ('4', '2', '2', '8') ('4', '2', '2', '9') ('4', '2', '3', '0') ('4', '2', '3', '1') ('4', '2', '3', '2') ('4', '2', '3', '3') ('4', '2', '3', '4') ('4', '2', '3', '5') ('4', '2', '3', '6') ('4', '2', '3', '7') ('4', '2', '3', '8') ('4', '2', '3', '9') ('4', '2', '4', '0') ('4', '2', '4', '1') ('4', '2', '4', '2') ('4', '2', '4', '3') ('4', '2', '4', '4') ('4', '2', '4', '5') ('4', '2', '4', '6') ('4', '2', '4', '7') ('4', '2', '4', '8') ('4', '2', '4', '9') ('4', '2', '5', '0') ('4', '2', '5', '1') ('4', '2', '5', '2') ('4', '2', '5', '3') ('4', '2', '5', '4') ('4', '2', '5', '5') ('4', '2', '5', '6') ('4', '2', '5', '7') ('4', '2', '5', '8') ('4', '2', '5', '9') ('4', '2', '6', '0') ('4', '2', '6', '1') ('4', '2', '6', '2') ('4', '2', '6', '3') ('4', '2', '6', '4') ('4', '2', '6', '5') ('4', '2', '6', '6') ('4', '2', '6', '7') ('4', '2', '6', '8') ('4', '2', '6', '9') ('4', '2', '7', '0') ('4', '2', '7', '1') ('4', '2', '7', '2') ('4', '2', '7', '3') ('4', '2', '7', '4') ('4', '2', '7', '5') ('4', '2', '7', '6') ('4', '2', '7', '7') ('4', '2', '7', '8') ('4', '2', '7', '9') ('4', '2', '8', '0') ('4', '2', '8', '1') ('4', '2', '8', '2') ('4', '2', '8', '3') ('4', '2', '8', '4') ('4', '2', '8', '5') ('4', '2', '8', '6') ('4', '2', '8', '7') ('4', '2', '8', '8') ('4', '2', '8', '9') ('4', '2', '9', '0') ('4', '2', '9', '1') ('4', '2', '9', '2') ('4', '2', '9', '3') ('4', '2', '9', '4') ('4', '2', '9', '5') ('4', '2', '9', '6') ('4', '2', '9', '7') ('4', '2', '9', '8') ('4', '2', '9', '9') ('4', '3', '0', '0') ('4', '3', '0', '1') ('4', '3', '0', '2') ('4', '3', '0', '3') ('4', '3', '0', '4') ('4', '3', '0', '5') ('4', '3', '0', '6') ('4', '3', '0', '7') ('4', '3', '0', '8') ('4', '3', '0', '9') ('4', '3', '1', '0') ('4', '3', '1', '1') ('4', '3', '1', '2') ('4', '3', '1', '3') ('4', '3', '1', '4') ('4', '3', '1', '5') ('4', '3', '1', '6') ('4', '3', '1', '7') ('4', '3', '1', '8') ('4', '3', '1', '9') ('4', '3', '2', '0') ('4', '3', '2', '1') ('4', '3', '2', '2') ('4', '3', '2', '3') ('4', '3', '2', '4') ('4', '3', '2', '5') ('4', '3', '2', '6') ('4', '3', '2', '7') ('4', '3', '2', '8') ('4', '3', '2', '9') ('4', '3', '3', '0') ('4', '3', '3', '1') ('4', '3', '3', '2') ('4', '3', '3', '3') ('4', '3', '3', '4') ('4', '3', '3', '5') ('4', '3', '3', '6') ('4', '3', '3', '7') ('4', '3', '3', '8') ('4', '3', '3', '9') ('4', '3', '4', '0') ('4', '3', '4', '1') ('4', '3', '4', '2') ('4', '3', '4', '3') ('4', '3', '4', '4') ('4', '3', '4', '5') ('4', '3', '4', '6') ('4', '3', '4', '7') ('4', '3', '4', '8') ('4', '3', '4', '9') ('4', '3', '5', '0') ('4', '3', '5', '1') ('4', '3', '5', '2') ('4', '3', '5', '3') ('4', '3', '5', '4') ('4', '3', '5', '5') ('4', '3', '5', '6') ('4', '3', '5', '7') ('4', '3', '5', '8') ('4', '3', '5', '9') ('4', '3', '6', '0') ('4', '3', '6', '1') ('4', '3', '6', '2') ('4', '3', '6', '3') ('4', '3', '6', '4') ('4', '3', '6', '5') ('4', '3', '6', '6') ('4', '3', '6', '7') ('4', '3', '6', '8') ('4', '3', '6', '9') ('4', '3', '7', '0') ('4', '3', '7', '1') ('4', '3', '7', '2') ('4', '3', '7', '3') ('4', '3', '7', '4') ('4', '3', '7', '5') ('4', '3', '7', '6') ('4', '3', '7', '7') ('4', '3', '7', '8') ('4', '3', '7', '9') ('4', '3', '8', '0') ('4', '3', '8', '1') ('4', '3', '8', '2') ('4', '3', '8', '3') ('4', '3', '8', '4') ('4', '3', '8', '5') ('4', '3', '8', '6') ('4', '3', '8', '7') ('4', '3', '8', '8') ('4', '3', '8', '9') ('4', '3', '9', '0') ('4', '3', '9', '1') ('4', '3', '9', '2') ('4', '3', '9', '3') ('4', '3', '9', '4') ('4', '3', '9', '5') ('4', '3', '9', '6') ('4', '3', '9', '7') ('4', '3', '9', '8') ('4', '3', '9', '9') ('4', '4', '0', '0') ('4', '4', '0', '1') ('4', '4', '0', '2') ('4', '4', '0', '3') ('4', '4', '0', '4') ('4', '4', '0', '5') ('4', '4', '0', '6') ('4', '4', '0', '7') ('4', '4', '0', '8') ('4', '4', '0', '9') ('4', '4', '1', '0') ('4', '4', '1', '1') ('4', '4', '1', '2') ('4', '4', '1', '3') ('4', '4', '1', '4') ('4', '4', '1', '5') ('4', '4', '1', '6') ('4', '4', '1', '7') ('4', '4', '1', '8') ('4', '4', '1', '9') ('4', '4', '2', '0') ('4', '4', '2', '1') ('4', '4', '2', '2') ('4', '4', '2', '3') ('4', '4', '2', '4') ('4', '4', '2', '5') ('4', '4', '2', '6') ('4', '4', '2', '7') ('4', '4', '2', '8') ('4', '4', '2', '9') ('4', '4', '3', '0') ('4', '4', '3', '1') ('4', '4', '3', '2') ('4', '4', '3', '3') ('4', '4', '3', '4') ('4', '4', '3', '5') ('4', '4', '3', '6') ('4', '4', '3', '7') ('4', '4', '3', '8') ('4', '4', '3', '9') ('4', '4', '4', '0') ('4', '4', '4', '1') ('4', '4', '4', '2') ('4', '4', '4', '3') ('4', '4', '4', '4') ('4', '4', '4', '5') ('4', '4', '4', '6') ('4', '4', '4', '7') ('4', '4', '4', '8') ('4', '4', '4', '9') ('4', '4', '5', '0') ('4', '4', '5', '1') ('4', '4', '5', '2') ('4', '4', '5', '3') ('4', '4', '5', '4') ('4', '4', '5', '5') ('4', '4', '5', '6') ('4', '4', '5', '7') ('4', '4', '5', '8') ('4', '4', '5', '9') ('4', '4', '6', '0') ('4', '4', '6', '1') ('4', '4', '6', '2') ('4', '4', '6', '3') ('4', '4', '6', '4') ('4', '4', '6', '5') ('4', '4', '6', '6') ('4', '4', '6', '7') ('4', '4', '6', '8') ('4', '4', '6', '9') ('4', '4', '7', '0') ('4', '4', '7', '1') ('4', '4', '7', '2') ('4', '4', '7', '3') ('4', '4', '7', '4') ('4', '4', '7', '5') ('4', '4', '7', '6') ('4', '4', '7', '7') ('4', '4', '7', '8') ('4', '4', '7', '9') ('4', '4', '8', '0') ('4', '4', '8', '1') ('4', '4', '8', '2') ('4', '4', '8', '3') ('4', '4', '8', '4') ('4', '4', '8', '5') ('4', '4', '8', '6') ('4', '4', '8', '7') ('4', '4', '8', '8') ('4', '4', '8', '9') ('4', '4', '9', '0') ('4', '4', '9', '1') ('4', '4', '9', '2') ('4', '4', '9', '3') ('4', '4', '9', '4') ('4', '4', '9', '5') ('4', '4', '9', '6') ('4', '4', '9', '7') ('4', '4', '9', '8') ('4', '4', '9', '9') ('4', '5', '0', '0') ('4', '5', '0', '1') ('4', '5', '0', '2') ('4', '5', '0', '3') ('4', '5', '0', '4') ('4', '5', '0', '5') ('4', '5', '0', '6') ('4', '5', '0', '7') ('4', '5', '0', '8') ('4', '5', '0', '9') ('4', '5', '1', '0') ('4', '5', '1', '1') ('4', '5', '1', '2') ('4', '5', '1', '3') ('4', '5', '1', '4') ('4', '5', '1', '5') ('4', '5', '1', '6') ('4', '5', '1', '7') ('4', '5', '1', '8') ('4', '5', '1', '9') ('4', '5', '2', '0') ('4', '5', '2', '1') ('4', '5', '2', '2') ('4', '5', '2', '3') ('4', '5', '2', '4') ('4', '5', '2', '5') ('4', '5', '2', '6') ('4', '5', '2', '7') ('4', '5', '2', '8') ('4', '5', '2', '9') ('4', '5', '3', '0') ('4', '5', '3', '1') ('4', '5', '3', '2') ('4', '5', '3', '3') ('4', '5', '3', '4') ('4', '5', '3', '5') ('4', '5', '3', '6') ('4', '5', '3', '7') ('4', '5', '3', '8') ('4', '5', '3', '9') ('4', '5', '4', '0') ('4', '5', '4', '1') ('4', '5', '4', '2') ('4', '5', '4', '3') ('4', '5', '4', '4') ('4', '5', '4', '5') ('4', '5', '4', '6') ('4', '5', '4', '7') ('4', '5', '4', '8') ('4', '5', '4', '9') ('4', '5', '5', '0') ('4', '5', '5', '1') ('4', '5', '5', '2') ('4', '5', '5', '3') ('4', '5', '5', '4') ('4', '5', '5', '5') ('4', '5', '5', '6') ('4', '5', '5', '7') ('4', '5', '5', '8') ('4', '5', '5', '9') ('4', '5', '6', '0') ('4', '5', '6', '1') ('4', '5', '6', '2') ('4', '5', '6', '3') ('4', '5', '6', '4') ('4', '5', '6', '5') ('4', '5', '6', '6') ('4', '5', '6', '7') ('4', '5', '6', '8') ('4', '5', '6', '9') ('4', '5', '7', '0') ('4', '5', '7', '1') ('4', '5', '7', '2') ('4', '5', '7', '3') ('4', '5', '7', '4') ('4', '5', '7', '5') ('4', '5', '7', '6') ('4', '5', '7', '7') ('4', '5', '7', '8') ('4', '5', '7', '9') ('4', '5', '8', '0') ('4', '5', '8', '1') ('4', '5', '8', '2') ('4', '5', '8', '3') ('4', '5', '8', '4') ('4', '5', '8', '5') ('4', '5', '8', '6') ('4', '5', '8', '7') ('4', '5', '8', '8') ('4', '5', '8', '9') ('4', '5', '9', '0') ('4', '5', '9', '1') ('4', '5', '9', '2') ('4', '5', '9', '3') ('4', '5', '9', '4') ('4', '5', '9', '5') ('4', '5', '9', '6') ('4', '5', '9', '7') ('4', '5', '9', '8') ('4', '5', '9', '9') ('4', '6', '0', '0') ('4', '6', '0', '1') ('4', '6', '0', '2') ('4', '6', '0', '3') ('4', '6', '0', '4') ('4', '6', '0', '5') ('4', '6', '0', '6') ('4', '6', '0', '7') ('4', '6', '0', '8') ('4', '6', '0', '9') ('4', '6', '1', '0') ('4', '6', '1', '1') ('4', '6', '1', '2') ('4', '6', '1', '3') ('4', '6', '1', '4') ('4', '6', '1', '5') ('4', '6', '1', '6') ('4', '6', '1', '7') ('4', '6', '1', '8') ('4', '6', '1', '9') ('4', '6', '2', '0') ('4', '6', '2', '1') ('4', '6', '2', '2') ('4', '6', '2', '3') ('4', '6', '2', '4') ('4', '6', '2', '5') ('4', '6', '2', '6') ('4', '6', '2', '7') ('4', '6', '2', '8') ('4', '6', '2', '9') ('4', '6', '3', '0') ('4', '6', '3', '1') ('4', '6', '3', '2') ('4', '6', '3', '3') ('4', '6', '3', '4') ('4', '6', '3', '5') ('4', '6', '3', '6') ('4', '6', '3', '7') ('4', '6', '3', '8') ('4', '6', '3', '9') ('4', '6', '4', '0') ('4', '6', '4', '1') ('4', '6', '4', '2') ('4', '6', '4', '3') ('4', '6', '4', '4') ('4', '6', '4', '5') ('4', '6', '4', '6') ('4', '6', '4', '7') ('4', '6', '4', '8') ('4', '6', '4', '9') ('4', '6', '5', '0') ('4', '6', '5', '1') ('4', '6', '5', '2') ('4', '6', '5', '3') ('4', '6', '5', '4') ('4', '6', '5', '5') ('4', '6', '5', '6') ('4', '6', '5', '7') ('4', '6', '5', '8') ('4', '6', '5', '9') ('4', '6', '6', '0') ('4', '6', '6', '1') ('4', '6', '6', '2') ('4', '6', '6', '3') ('4', '6', '6', '4') ('4', '6', '6', '5') ('4', '6', '6', '6') ('4', '6', '6', '7') ('4', '6', '6', '8') ('4', '6', '6', '9') ('4', '6', '7', '0') ('4', '6', '7', '1') ('4', '6', '7', '2') ('4', '6', '7', '3') ('4', '6', '7', '4') ('4', '6', '7', '5') ('4', '6', '7', '6') ('4', '6', '7', '7') ('4', '6', '7', '8') ('4', '6', '7', '9') ('4', '6', '8', '0') ('4', '6', '8', '1') ('4', '6', '8', '2') ('4', '6', '8', '3') ('4', '6', '8', '4') ('4', '6', '8', '5') ('4', '6', '8', '6') ('4', '6', '8', '7') ('4', '6', '8', '8') ('4', '6', '8', '9') ('4', '6', '9', '0') ('4', '6', '9', '1') ('4', '6', '9', '2') ('4', '6', '9', '3') ('4', '6', '9', '4') ('4', '6', '9', '5') ('4', '6', '9', '6') ('4', '6', '9', '7') ('4', '6', '9', '8') ('4', '6', '9', '9') ('4', '7', '0', '0') ('4', '7', '0', '1') ('4', '7', '0', '2') ('4', '7', '0', '3') ('4', '7', '0', '4') ('4', '7', '0', '5') ('4', '7', '0', '6') ('4', '7', '0', '7') ('4', '7', '0', '8') ('4', '7', '0', '9') ('4', '7', '1', '0') ('4', '7', '1', '1') ('4', '7', '1', '2') ('4', '7', '1', '3') ('4', '7', '1', '4') ('4', '7', '1', '5') ('4', '7', '1', '6') ('4', '7', '1', '7') ('4', '7', '1', '8') ('4', '7', '1', '9') ('4', '7', '2', '0') ('4', '7', '2', '1') ('4', '7', '2', '2') ('4', '7', '2', '3') ('4', '7', '2', '4') ('4', '7', '2', '5') ('4', '7', '2', '6') ('4', '7', '2', '7') ('4', '7', '2', '8') ('4', '7', '2', '9') ('4', '7', '3', '0') ('4', '7', '3', '1') ('4', '7', '3', '2') ('4', '7', '3', '3') ('4', '7', '3', '4') ('4', '7', '3', '5') ('4', '7', '3', '6') ('4', '7', '3', '7') ('4', '7', '3', '8') ('4', '7', '3', '9') ('4', '7', '4', '0') ('4', '7', '4', '1') ('4', '7', '4', '2') ('4', '7', '4', '3') ('4', '7', '4', '4') ('4', '7', '4', '5') ('4', '7', '4', '6') ('4', '7', '4', '7') ('4', '7', '4', '8') ('4', '7', '4', '9') ('4', '7', '5', '0') ('4', '7', '5', '1') ('4', '7', '5', '2') ('4', '7', '5', '3') ('4', '7', '5', '4') ('4', '7', '5', '5') ('4', '7', '5', '6') ('4', '7', '5', '7') ('4', '7', '5', '8') ('4', '7', '5', '9') ('4', '7', '6', '0') ('4', '7', '6', '1') ('4', '7', '6', '2') ('4', '7', '6', '3') ('4', '7', '6', '4') ('4', '7', '6', '5') ('4', '7', '6', '6') ('4', '7', '6', '7') ('4', '7', '6', '8') ('4', '7', '6', '9') ('4', '7', '7', '0') ('4', '7', '7', '1') ('4', '7', '7', '2') ('4', '7', '7', '3') ('4', '7', '7', '4') ('4', '7', '7', '5') ('4', '7', '7', '6') ('4', '7', '7', '7') ('4', '7', '7', '8') ('4', '7', '7', '9') ('4', '7', '8', '0') ('4', '7', '8', '1') ('4', '7', '8', '2') ('4', '7', '8', '3') ('4', '7', '8', '4') ('4', '7', '8', '5') ('4', '7', '8', '6') ('4', '7', '8', '7') ('4', '7', '8', '8') ('4', '7', '8', '9') ('4', '7', '9', '0') ('4', '7', '9', '1') ('4', '7', '9', '2') ('4', '7', '9', '3') ('4', '7', '9', '4') ('4', '7', '9', '5') ('4', '7', '9', '6') ('4', '7', '9', '7') ('4', '7', '9', '8') ('4', '7', '9', '9') ('4', '8', '0', '0') ('4', '8', '0', '1') ('4', '8', '0', '2') ('4', '8', '0', '3') ('4', '8', '0', '4') ('4', '8', '0', '5') ('4', '8', '0', '6') ('4', '8', '0', '7') ('4', '8', '0', '8') ('4', '8', '0', '9') ('4', '8', '1', '0') ('4', '8', '1', '1') ('4', '8', '1', '2') ('4', '8', '1', '3') ('4', '8', '1', '4') ('4', '8', '1', '5') ('4', '8', '1', '6') ('4', '8', '1', '7') ('4', '8', '1', '8') ('4', '8', '1', '9') ('4', '8', '2', '0') ('4', '8', '2', '1') ('4', '8', '2', '2') ('4', '8', '2', '3') ('4', '8', '2', '4') ('4', '8', '2', '5') ('4', '8', '2', '6') ('4', '8', '2', '7') ('4', '8', '2', '8') ('4', '8', '2', '9') ('4', '8', '3', '0') ('4', '8', '3', '1') ('4', '8', '3', '2') ('4', '8', '3', '3') ('4', '8', '3', '4') ('4', '8', '3', '5') ('4', '8', '3', '6') ('4', '8', '3', '7') ('4', '8', '3', '8') ('4', '8', '3', '9') ('4', '8', '4', '0') ('4', '8', '4', '1') ('4', '8', '4', '2') ('4', '8', '4', '3') ('4', '8', '4', '4') ('4', '8', '4', '5') ('4', '8', '4', '6') ('4', '8', '4', '7') ('4', '8', '4', '8') ('4', '8', '4', '9') ('4', '8', '5', '0') ('4', '8', '5', '1') ('4', '8', '5', '2') ('4', '8', '5', '3') ('4', '8', '5', '4') ('4', '8', '5', '5') ('4', '8', '5', '6') ('4', '8', '5', '7') ('4', '8', '5', '8') ('4', '8', '5', '9') ('4', '8', '6', '0') ('4', '8', '6', '1') ('4', '8', '6', '2') ('4', '8', '6', '3') ('4', '8', '6', '4') ('4', '8', '6', '5') ('4', '8', '6', '6') ('4', '8', '6', '7') ('4', '8', '6', '8') ('4', '8', '6', '9') ('4', '8', '7', '0') ('4', '8', '7', '1') ('4', '8', '7', '2') ('4', '8', '7', '3') ('4', '8', '7', '4') ('4', '8', '7', '5') ('4', '8', '7', '6') ('4', '8', '7', '7') ('4', '8', '7', '8') ('4', '8', '7', '9') ('4', '8', '8', '0') ('4', '8', '8', '1') ('4', '8', '8', '2') ('4', '8', '8', '3') ('4', '8', '8', '4') ('4', '8', '8', '5') ('4', '8', '8', '6') ('4', '8', '8', '7') ('4', '8', '8', '8') ('4', '8', '8', '9') ('4', '8', '9', '0') ('4', '8', '9', '1') ('4', '8', '9', '2') ('4', '8', '9', '3') ('4', '8', '9', '4') ('4', '8', '9', '5') ('4', '8', '9', '6') ('4', '8', '9', '7') ('4', '8', '9', '8') ('4', '8', '9', '9') ('4', '9', '0', '0') ('4', '9', '0', '1') ('4', '9', '0', '2') ('4', '9', '0', '3') ('4', '9', '0', '4') ('4', '9', '0', '5') ('4', '9', '0', '6') ('4', '9', '0', '7') ('4', '9', '0', '8') ('4', '9', '0', '9') ('4', '9', '1', '0') ('4', '9', '1', '1') ('4', '9', '1', '2') ('4', '9', '1', '3') ('4', '9', '1', '4') ('4', '9', '1', '5') ('4', '9', '1', '6') ('4', '9', '1', '7') ('4', '9', '1', '8') ('4', '9', '1', '9') ('4', '9', '2', '0') ('4', '9', '2', '1') ('4', '9', '2', '2') ('4', '9', '2', '3') ('4', '9', '2', '4') ('4', '9', '2', '5') ('4', '9', '2', '6') ('4', '9', '2', '7') ('4', '9', '2', '8') ('4', '9', '2', '9') ('4', '9', '3', '0') ('4', '9', '3', '1') ('4', '9', '3', '2') ('4', '9', '3', '3') ('4', '9', '3', '4') ('4', '9', '3', '5') ('4', '9', '3', '6') ('4', '9', '3', '7') ('4', '9', '3', '8') ('4', '9', '3', '9') ('4', '9', '4', '0') ('4', '9', '4', '1') ('4', '9', '4', '2') ('4', '9', '4', '3') ('4', '9', '4', '4') ('4', '9', '4', '5') ('4', '9', '4', '6') ('4', '9', '4', '7') ('4', '9', '4', '8') ('4', '9', '4', '9') ('4', '9', '5', '0') ('4', '9', '5', '1') ('4', '9', '5', '2') ('4', '9', '5', '3') ('4', '9', '5', '4') ('4', '9', '5', '5') ('4', '9', '5', '6') ('4', '9', '5', '7') ('4', '9', '5', '8') ('4', '9', '5', '9') ('4', '9', '6', '0') ('4', '9', '6', '1') ('4', '9', '6', '2') ('4', '9', '6', '3') ('4', '9', '6', '4') ('4', '9', '6', '5') ('4', '9', '6', '6') ('4', '9', '6', '7') ('4', '9', '6', '8') ('4', '9', '6', '9') ('4', '9', '7', '0') ('4', '9', '7', '1') ('4', '9', '7', '2') ('4', '9', '7', '3') ('4', '9', '7', '4') ('4', '9', '7', '5') ('4', '9', '7', '6') ('4', '9', '7', '7') ('4', '9', '7', '8') ('4', '9', '7', '9') ('4', '9', '8', '0') ('4', '9', '8', '1') ('4', '9', '8', '2') ('4', '9', '8', '3') ('4', '9', '8', '4') ('4', '9', '8', '5') ('4', '9', '8', '6') ('4', '9', '8', '7') ('4', '9', '8', '8') ('4', '9', '8', '9') ('4', '9', '9', '0') ('4', '9', '9', '1') ('4', '9', '9', '2') ('4', '9', '9', '3') ('4', '9', '9', '4') ('4', '9', '9', '5') ('4', '9', '9', '6') ('4', '9', '9', '7') ('4', '9', '9', '8') ('4', '9', '9', '9') ('5', '0', '0', '0') ('5', '0', '0', '1') ('5', '0', '0', '2') ('5', '0', '0', '3') ('5', '0', '0', '4') ('5', '0', '0', '5') ('5', '0', '0', '6') ('5', '0', '0', '7') ('5', '0', '0', '8') ('5', '0', '0', '9') ('5', '0', '1', '0') ('5', '0', '1', '1') ('5', '0', '1', '2') ('5', '0', '1', '3') ('5', '0', '1', '4') ('5', '0', '1', '5') ('5', '0', '1', '6') ('5', '0', '1', '7') ('5', '0', '1', '8') ('5', '0', '1', '9') ('5', '0', '2', '0') ('5', '0', '2', '1') ('5', '0', '2', '2') ('5', '0', '2', '3') ('5', '0', '2', '4') ('5', '0', '2', '5') ('5', '0', '2', '6') ('5', '0', '2', '7') ('5', '0', '2', '8') ('5', '0', '2', '9') ('5', '0', '3', '0') ('5', '0', '3', '1') ('5', '0', '3', '2') ('5', '0', '3', '3') ('5', '0', '3', '4') ('5', '0', '3', '5') ('5', '0', '3', '6') ('5', '0', '3', '7') ('5', '0', '3', '8') ('5', '0', '3', '9') ('5', '0', '4', '0') ('5', '0', '4', '1') ('5', '0', '4', '2') ('5', '0', '4', '3') ('5', '0', '4', '4') ('5', '0', '4', '5') ('5', '0', '4', '6') ('5', '0', '4', '7') ('5', '0', '4', '8') ('5', '0', '4', '9') ('5', '0', '5', '0') ('5', '0', '5', '1') ('5', '0', '5', '2') ('5', '0', '5', '3') ('5', '0', '5', '4') ('5', '0', '5', '5') ('5', '0', '5', '6') ('5', '0', '5', '7') ('5', '0', '5', '8') ('5', '0', '5', '9') ('5', '0', '6', '0') ('5', '0', '6', '1') ('5', '0', '6', '2') ('5', '0', '6', '3') ('5', '0', '6', '4') ('5', '0', '6', '5') ('5', '0', '6', '6') ('5', '0', '6', '7') ('5', '0', '6', '8') ('5', '0', '6', '9') ('5', '0', '7', '0') ('5', '0', '7', '1') ('5', '0', '7', '2') ('5', '0', '7', '3') ('5', '0', '7', '4') ('5', '0', '7', '5') ('5', '0', '7', '6') ('5', '0', '7', '7') ('5', '0', '7', '8') ('5', '0', '7', '9') ('5', '0', '8', '0') ('5', '0', '8', '1') ('5', '0', '8', '2') ('5', '0', '8', '3') ('5', '0', '8', '4') ('5', '0', '8', '5') ('5', '0', '8', '6') ('5', '0', '8', '7') ('5', '0', '8', '8') ('5', '0', '8', '9') ('5', '0', '9', '0') ('5', '0', '9', '1') ('5', '0', '9', '2') ('5', '0', '9', '3') ('5', '0', '9', '4') ('5', '0', '9', '5') ('5', '0', '9', '6') ('5', '0', '9', '7') ('5', '0', '9', '8') ('5', '0', '9', '9') ('5', '1', '0', '0') ('5', '1', '0', '1') ('5', '1', '0', '2') ('5', '1', '0', '3') ('5', '1', '0', '4') ('5', '1', '0', '5') ('5', '1', '0', '6') ('5', '1', '0', '7') ('5', '1', '0', '8') ('5', '1', '0', '9') ('5', '1', '1', '0') ('5', '1', '1', '1') ('5', '1', '1', '2') ('5', '1', '1', '3') ('5', '1', '1', '4') ('5', '1', '1', '5') ('5', '1', '1', '6') ('5', '1', '1', '7') ('5', '1', '1', '8') ('5', '1', '1', '9') ('5', '1', '2', '0') ('5', '1', '2', '1') ('5', '1', '2', '2') ('5', '1', '2', '3') ('5', '1', '2', '4') ('5', '1', '2', '5') ('5', '1', '2', '6') ('5', '1', '2', '7') ('5', '1', '2', '8') ('5', '1', '2', '9') ('5', '1', '3', '0') ('5', '1', '3', '1') ('5', '1', '3', '2') ('5', '1', '3', '3') ('5', '1', '3', '4') ('5', '1', '3', '5') ('5', '1', '3', '6') ('5', '1', '3', '7') ('5', '1', '3', '8') ('5', '1', '3', '9') ('5', '1', '4', '0') ('5', '1', '4', '1') ('5', '1', '4', '2') ('5', '1', '4', '3') ('5', '1', '4', '4') ('5', '1', '4', '5') ('5', '1', '4', '6') ('5', '1', '4', '7') ('5', '1', '4', '8') ('5', '1', '4', '9') ('5', '1', '5', '0') ('5', '1', '5', '1') ('5', '1', '5', '2') ('5', '1', '5', '3') ('5', '1', '5', '4') ('5', '1', '5', '5') ('5', '1', '5', '6') ('5', '1', '5', '7') ('5', '1', '5', '8') ('5', '1', '5', '9') ('5', '1', '6', '0') ('5', '1', '6', '1') ('5', '1', '6', '2') ('5', '1', '6', '3') ('5', '1', '6', '4') ('5', '1', '6', '5') ('5', '1', '6', '6') ('5', '1', '6', '7') ('5', '1', '6', '8') ('5', '1', '6', '9') ('5', '1', '7', '0') ('5', '1', '7', '1') ('5', '1', '7', '2') ('5', '1', '7', '3') ('5', '1', '7', '4') ('5', '1', '7', '5') ('5', '1', '7', '6') ('5', '1', '7', '7') ('5', '1', '7', '8') ('5', '1', '7', '9') ('5', '1', '8', '0') ('5', '1', '8', '1') ('5', '1', '8', '2') ('5', '1', '8', '3') ('5', '1', '8', '4') ('5', '1', '8', '5') ('5', '1', '8', '6') ('5', '1', '8', '7') ('5', '1', '8', '8') ('5', '1', '8', '9') ('5', '1', '9', '0') ('5', '1', '9', '1') ('5', '1', '9', '2') ('5', '1', '9', '3') ('5', '1', '9', '4') ('5', '1', '9', '5') ('5', '1', '9', '6') ('5', '1', '9', '7') ('5', '1', '9', '8') ('5', '1', '9', '9') ('5', '2', '0', '0') ('5', '2', '0', '1') ('5', '2', '0', '2') ('5', '2', '0', '3') ('5', '2', '0', '4') ('5', '2', '0', '5') ('5', '2', '0', '6') ('5', '2', '0', '7') ('5', '2', '0', '8') ('5', '2', '0', '9') ('5', '2', '1', '0') ('5', '2', '1', '1') ('5', '2', '1', '2') ('5', '2', '1', '3') ('5', '2', '1', '4') ('5', '2', '1', '5') ('5', '2', '1', '6') ('5', '2', '1', '7') ('5', '2', '1', '8') ('5', '2', '1', '9') ('5', '2', '2', '0') ('5', '2', '2', '1') ('5', '2', '2', '2') ('5', '2', '2', '3') ('5', '2', '2', '4') ('5', '2', '2', '5') ('5', '2', '2', '6') ('5', '2', '2', '7') ('5', '2', '2', '8') ('5', '2', '2', '9') ('5', '2', '3', '0') ('5', '2', '3', '1') ('5', '2', '3', '2') ('5', '2', '3', '3') ('5', '2', '3', '4') ('5', '2', '3', '5') ('5', '2', '3', '6') ('5', '2', '3', '7') ('5', '2', '3', '8') ('5', '2', '3', '9') ('5', '2', '4', '0') ('5', '2', '4', '1') ('5', '2', '4', '2') ('5', '2', '4', '3') ('5', '2', '4', '4') ('5', '2', '4', '5') ('5', '2', '4', '6') ('5', '2', '4', '7') ('5', '2', '4', '8') ('5', '2', '4', '9') ('5', '2', '5', '0') ('5', '2', '5', '1') ('5', '2', '5', '2') ('5', '2', '5', '3') ('5', '2', '5', '4') ('5', '2', '5', '5') ('5', '2', '5', '6') ('5', '2', '5', '7') ('5', '2', '5', '8') ('5', '2', '5', '9') ('5', '2', '6', '0') ('5', '2', '6', '1') ('5', '2', '6', '2') ('5', '2', '6', '3') ('5', '2', '6', '4') ('5', '2', '6', '5') ('5', '2', '6', '6') ('5', '2', '6', '7') ('5', '2', '6', '8') ('5', '2', '6', '9') ('5', '2', '7', '0') ('5', '2', '7', '1') ('5', '2', '7', '2') ('5', '2', '7', '3') ('5', '2', '7', '4') ('5', '2', '7', '5') ('5', '2', '7', '6') ('5', '2', '7', '7') ('5', '2', '7', '8') ('5', '2', '7', '9') ('5', '2', '8', '0') ('5', '2', '8', '1') ('5', '2', '8', '2') ('5', '2', '8', '3') ('5', '2', '8', '4') ('5', '2', '8', '5') ('5', '2', '8', '6') ('5', '2', '8', '7') ('5', '2', '8', '8') ('5', '2', '8', '9') ('5', '2', '9', '0') ('5', '2', '9', '1') ('5', '2', '9', '2') ('5', '2', '9', '3') ('5', '2', '9', '4') ('5', '2', '9', '5') ('5', '2', '9', '6') ('5', '2', '9', '7') ('5', '2', '9', '8') ('5', '2', '9', '9') ('5', '3', '0', '0') ('5', '3', '0', '1') ('5', '3', '0', '2') ('5', '3', '0', '3') ('5', '3', '0', '4') ('5', '3', '0', '5') ('5', '3', '0', '6') ('5', '3', '0', '7') ('5', '3', '0', '8') ('5', '3', '0', '9') ('5', '3', '1', '0') ('5', '3', '1', '1') ('5', '3', '1', '2') ('5', '3', '1', '3') ('5', '3', '1', '4') ('5', '3', '1', '5') ('5', '3', '1', '6') ('5', '3', '1', '7') ('5', '3', '1', '8') ('5', '3', '1', '9') ('5', '3', '2', '0') ('5', '3', '2', '1') ('5', '3', '2', '2') ('5', '3', '2', '3') ('5', '3', '2', '4') ('5', '3', '2', '5') ('5', '3', '2', '6') ('5', '3', '2', '7') ('5', '3', '2', '8') ('5', '3', '2', '9') ('5', '3', '3', '0') ('5', '3', '3', '1') ('5', '3', '3', '2') ('5', '3', '3', '3') ('5', '3', '3', '4') ('5', '3', '3', '5') ('5', '3', '3', '6') ('5', '3', '3', '7') ('5', '3', '3', '8') ('5', '3', '3', '9') ('5', '3', '4', '0') ('5', '3', '4', '1') ('5', '3', '4', '2') ('5', '3', '4', '3') ('5', '3', '4', '4') ('5', '3', '4', '5') ('5', '3', '4', '6') ('5', '3', '4', '7') ('5', '3', '4', '8') ('5', '3', '4', '9') ('5', '3', '5', '0') ('5', '3', '5', '1') ('5', '3', '5', '2') ('5', '3', '5', '3') ('5', '3', '5', '4') ('5', '3', '5', '5') ('5', '3', '5', '6') ('5', '3', '5', '7') ('5', '3', '5', '8') ('5', '3', '5', '9') ('5', '3', '6', '0') ('5', '3', '6', '1') ('5', '3', '6', '2') ('5', '3', '6', '3') ('5', '3', '6', '4') ('5', '3', '6', '5') ('5', '3', '6', '6') ('5', '3', '6', '7') ('5', '3', '6', '8') ('5', '3', '6', '9') ('5', '3', '7', '0') ('5', '3', '7', '1') ('5', '3', '7', '2') ('5', '3', '7', '3') ('5', '3', '7', '4') ('5', '3', '7', '5') ('5', '3', '7', '6') ('5', '3', '7', '7') ('5', '3', '7', '8') ('5', '3', '7', '9') ('5', '3', '8', '0') ('5', '3', '8', '1') ('5', '3', '8', '2') ('5', '3', '8', '3') ('5', '3', '8', '4') ('5', '3', '8', '5') ('5', '3', '8', '6') ('5', '3', '8', '7') ('5', '3', '8', '8') ('5', '3', '8', '9') ('5', '3', '9', '0') ('5', '3', '9', '1') ('5', '3', '9', '2') ('5', '3', '9', '3') ('5', '3', '9', '4') ('5', '3', '9', '5') ('5', '3', '9', '6') ('5', '3', '9', '7') ('5', '3', '9', '8') ('5', '3', '9', '9') ('5', '4', '0', '0') ('5', '4', '0', '1') ('5', '4', '0', '2') ('5', '4', '0', '3') ('5', '4', '0', '4') ('5', '4', '0', '5') ('5', '4', '0', '6') ('5', '4', '0', '7') ('5', '4', '0', '8') ('5', '4', '0', '9') ('5', '4', '1', '0') ('5', '4', '1', '1') ('5', '4', '1', '2') ('5', '4', '1', '3') ('5', '4', '1', '4') ('5', '4', '1', '5') ('5', '4', '1', '6') ('5', '4', '1', '7') ('5', '4', '1', '8') ('5', '4', '1', '9') ('5', '4', '2', '0') ('5', '4', '2', '1') ('5', '4', '2', '2') ('5', '4', '2', '3') ('5', '4', '2', '4') ('5', '4', '2', '5') ('5', '4', '2', '6') ('5', '4', '2', '7') ('5', '4', '2', '8') ('5', '4', '2', '9') ('5', '4', '3', '0') ('5', '4', '3', '1') ('5', '4', '3', '2') ('5', '4', '3', '3') ('5', '4', '3', '4') ('5', '4', '3', '5') ('5', '4', '3', '6') ('5', '4', '3', '7') ('5', '4', '3', '8') ('5', '4', '3', '9') ('5', '4', '4', '0') ('5', '4', '4', '1') ('5', '4', '4', '2') ('5', '4', '4', '3') ('5', '4', '4', '4') ('5', '4', '4', '5') ('5', '4', '4', '6') ('5', '4', '4', '7') ('5', '4', '4', '8') ('5', '4', '4', '9') ('5', '4', '5', '0') ('5', '4', '5', '1') ('5', '4', '5', '2') ('5', '4', '5', '3') ('5', '4', '5', '4') ('5', '4', '5', '5') ('5', '4', '5', '6') ('5', '4', '5', '7') ('5', '4', '5', '8') ('5', '4', '5', '9') ('5', '4', '6', '0') ('5', '4', '6', '1') ('5', '4', '6', '2') ('5', '4', '6', '3') ('5', '4', '6', '4') ('5', '4', '6', '5') ('5', '4', '6', '6') ('5', '4', '6', '7') ('5', '4', '6', '8') ('5', '4', '6', '9') ('5', '4', '7', '0') ('5', '4', '7', '1') ('5', '4', '7', '2') ('5', '4', '7', '3') ('5', '4', '7', '4') ('5', '4', '7', '5') ('5', '4', '7', '6') ('5', '4', '7', '7') ('5', '4', '7', '8') ('5', '4', '7', '9') ('5', '4', '8', '0') ('5', '4', '8', '1') ('5', '4', '8', '2') ('5', '4', '8', '3') ('5', '4', '8', '4') ('5', '4', '8', '5') ('5', '4', '8', '6') ('5', '4', '8', '7') ('5', '4', '8', '8') ('5', '4', '8', '9') ('5', '4', '9', '0') ('5', '4', '9', '1') ('5', '4', '9', '2') ('5', '4', '9', '3') ('5', '4', '9', '4') ('5', '4', '9', '5') ('5', '4', '9', '6') ('5', '4', '9', '7') ('5', '4', '9', '8') ('5', '4', '9', '9') ('5', '5', '0', '0') ('5', '5', '0', '1') ('5', '5', '0', '2') ('5', '5', '0', '3') ('5', '5', '0', '4') ('5', '5', '0', '5') ('5', '5', '0', '6') ('5', '5', '0', '7') ('5', '5', '0', '8') ('5', '5', '0', '9') ('5', '5', '1', '0') ('5', '5', '1', '1') ('5', '5', '1', '2') ('5', '5', '1', '3') ('5', '5', '1', '4') ('5', '5', '1', '5') ('5', '5', '1', '6') ('5', '5', '1', '7') ('5', '5', '1', '8') ('5', '5', '1', '9') ('5', '5', '2', '0') ('5', '5', '2', '1') ('5', '5', '2', '2') ('5', '5', '2', '3') ('5', '5', '2', '4') ('5', '5', '2', '5') ('5', '5', '2', '6') ('5', '5', '2', '7') ('5', '5', '2', '8') ('5', '5', '2', '9') ('5', '5', '3', '0') ('5', '5', '3', '1') ('5', '5', '3', '2') ('5', '5', '3', '3') ('5', '5', '3', '4') ('5', '5', '3', '5') ('5', '5', '3', '6') ('5', '5', '3', '7') ('5', '5', '3', '8') ('5', '5', '3', '9') ('5', '5', '4', '0') ('5', '5', '4', '1') ('5', '5', '4', '2') ('5', '5', '4', '3') ('5', '5', '4', '4') ('5', '5', '4', '5') ('5', '5', '4', '6') ('5', '5', '4', '7') ('5', '5', '4', '8') ('5', '5', '4', '9') ('5', '5', '5', '0') ('5', '5', '5', '1') ('5', '5', '5', '2') ('5', '5', '5', '3') ('5', '5', '5', '4') ('5', '5', '5', '5') ('5', '5', '5', '6') ('5', '5', '5', '7') ('5', '5', '5', '8') ('5', '5', '5', '9') ('5', '5', '6', '0') ('5', '5', '6', '1') ('5', '5', '6', '2') ('5', '5', '6', '3') ('5', '5', '6', '4') ('5', '5', '6', '5') ('5', '5', '6', '6') ('5', '5', '6', '7') ('5', '5', '6', '8') ('5', '5', '6', '9') ('5', '5', '7', '0') ('5', '5', '7', '1') ('5', '5', '7', '2') ('5', '5', '7', '3') ('5', '5', '7', '4') ('5', '5', '7', '5') ('5', '5', '7', '6') ('5', '5', '7', '7') ('5', '5', '7', '8') ('5', '5', '7', '9') ('5', '5', '8', '0') ('5', '5', '8', '1') ('5', '5', '8', '2') ('5', '5', '8', '3') ('5', '5', '8', '4') ('5', '5', '8', '5') ('5', '5', '8', '6') ('5', '5', '8', '7') ('5', '5', '8', '8') ('5', '5', '8', '9') ('5', '5', '9', '0') ('5', '5', '9', '1') ('5', '5', '9', '2') ('5', '5', '9', '3') ('5', '5', '9', '4') ('5', '5', '9', '5') ('5', '5', '9', '6') ('5', '5', '9', '7') ('5', '5', '9', '8') ('5', '5', '9', '9') ('5', '6', '0', '0') ('5', '6', '0', '1') ('5', '6', '0', '2') ('5', '6', '0', '3') ('5', '6', '0', '4') ('5', '6', '0', '5') ('5', '6', '0', '6') ('5', '6', '0', '7') ('5', '6', '0', '8') ('5', '6', '0', '9') ('5', '6', '1', '0') ('5', '6', '1', '1') ('5', '6', '1', '2') ('5', '6', '1', '3') ('5', '6', '1', '4') ('5', '6', '1', '5') ('5', '6', '1', '6') ('5', '6', '1', '7') ('5', '6', '1', '8') ('5', '6', '1', '9') ('5', '6', '2', '0') ('5', '6', '2', '1') ('5', '6', '2', '2') ('5', '6', '2', '3') ('5', '6', '2', '4') ('5', '6', '2', '5') ('5', '6', '2', '6') ('5', '6', '2', '7') ('5', '6', '2', '8') ('5', '6', '2', '9') ('5', '6', '3', '0') ('5', '6', '3', '1') ('5', '6', '3', '2') ('5', '6', '3', '3') ('5', '6', '3', '4') ('5', '6', '3', '5') ('5', '6', '3', '6') ('5', '6', '3', '7') ('5', '6', '3', '8') ('5', '6', '3', '9') ('5', '6', '4', '0') ('5', '6', '4', '1') ('5', '6', '4', '2') ('5', '6', '4', '3') ('5', '6', '4', '4') ('5', '6', '4', '5') ('5', '6', '4', '6') ('5', '6', '4', '7') ('5', '6', '4', '8') ('5', '6', '4', '9') ('5', '6', '5', '0') ('5', '6', '5', '1') ('5', '6', '5', '2') ('5', '6', '5', '3') ('5', '6', '5', '4') ('5', '6', '5', '5') ('5', '6', '5', '6') ('5', '6', '5', '7') ('5', '6', '5', '8') ('5', '6', '5', '9') ('5', '6', '6', '0') ('5', '6', '6', '1') ('5', '6', '6', '2') ('5', '6', '6', '3') ('5', '6', '6', '4') ('5', '6', '6', '5') ('5', '6', '6', '6') ('5', '6', '6', '7') ('5', '6', '6', '8') ('5', '6', '6', '9') ('5', '6', '7', '0') ('5', '6', '7', '1') ('5', '6', '7', '2') ('5', '6', '7', '3') ('5', '6', '7', '4') ('5', '6', '7', '5') ('5', '6', '7', '6') ('5', '6', '7', '7') ('5', '6', '7', '8') ('5', '6', '7', '9') ('5', '6', '8', '0') ('5', '6', '8', '1') ('5', '6', '8', '2') ('5', '6', '8', '3') ('5', '6', '8', '4') ('5', '6', '8', '5') ('5', '6', '8', '6') ('5', '6', '8', '7') ('5', '6', '8', '8') ('5', '6', '8', '9') ('5', '6', '9', '0') ('5', '6', '9', '1') ('5', '6', '9', '2') ('5', '6', '9', '3') ('5', '6', '9', '4') ('5', '6', '9', '5') ('5', '6', '9', '6') ('5', '6', '9', '7') ('5', '6', '9', '8') ('5', '6', '9', '9') ('5', '7', '0', '0') ('5', '7', '0', '1') ('5', '7', '0', '2') ('5', '7', '0', '3') ('5', '7', '0', '4') ('5', '7', '0', '5') ('5', '7', '0', '6') ('5', '7', '0', '7') ('5', '7', '0', '8') ('5', '7', '0', '9') ('5', '7', '1', '0') ('5', '7', '1', '1') ('5', '7', '1', '2') ('5', '7', '1', '3') ('5', '7', '1', '4') ('5', '7', '1', '5') ('5', '7', '1', '6') ('5', '7', '1', '7') ('5', '7', '1', '8') ('5', '7', '1', '9') ('5', '7', '2', '0') ('5', '7', '2', '1') ('5', '7', '2', '2') ('5', '7', '2', '3') ('5', '7', '2', '4') ('5', '7', '2', '5') ('5', '7', '2', '6') ('5', '7', '2', '7') ('5', '7', '2', '8') ('5', '7', '2', '9') ('5', '7', '3', '0') ('5', '7', '3', '1') ('5', '7', '3', '2') ('5', '7', '3', '3') ('5', '7', '3', '4') ('5', '7', '3', '5') ('5', '7', '3', '6') ('5', '7', '3', '7') ('5', '7', '3', '8') ('5', '7', '3', '9') ('5', '7', '4', '0') ('5', '7', '4', '1') ('5', '7', '4', '2') ('5', '7', '4', '3') ('5', '7', '4', '4') ('5', '7', '4', '5') ('5', '7', '4', '6') ('5', '7', '4', '7') ('5', '7', '4', '8') ('5', '7', '4', '9') ('5', '7', '5', '0') ('5', '7', '5', '1') ('5', '7', '5', '2') ('5', '7', '5', '3') ('5', '7', '5', '4') ('5', '7', '5', '5') ('5', '7', '5', '6') ('5', '7', '5', '7') ('5', '7', '5', '8') ('5', '7', '5', '9') ('5', '7', '6', '0') ('5', '7', '6', '1') ('5', '7', '6', '2') ('5', '7', '6', '3') ('5', '7', '6', '4') ('5', '7', '6', '5') ('5', '7', '6', '6') ('5', '7', '6', '7') ('5', '7', '6', '8') ('5', '7', '6', '9') ('5', '7', '7', '0') ('5', '7', '7', '1') ('5', '7', '7', '2') ('5', '7', '7', '3') ('5', '7', '7', '4') ('5', '7', '7', '5') ('5', '7', '7', '6') ('5', '7', '7', '7') ('5', '7', '7', '8') ('5', '7', '7', '9') ('5', '7', '8', '0') ('5', '7', '8', '1') ('5', '7', '8', '2') ('5', '7', '8', '3') ('5', '7', '8', '4') ('5', '7', '8', '5') ('5', '7', '8', '6') ('5', '7', '8', '7') ('5', '7', '8', '8') ('5', '7', '8', '9') ('5', '7', '9', '0') ('5', '7', '9', '1') ('5', '7', '9', '2') ('5', '7', '9', '3') ('5', '7', '9', '4') ('5', '7', '9', '5') ('5', '7', '9', '6') ('5', '7', '9', '7') ('5', '7', '9', '8') ('5', '7', '9', '9') ('5', '8', '0', '0') ('5', '8', '0', '1') ('5', '8', '0', '2') ('5', '8', '0', '3') ('5', '8', '0', '4') ('5', '8', '0', '5') ('5', '8', '0', '6') ('5', '8', '0', '7') ('5', '8', '0', '8') ('5', '8', '0', '9') ('5', '8', '1', '0') ('5', '8', '1', '1') ('5', '8', '1', '2') ('5', '8', '1', '3') ('5', '8', '1', '4') ('5', '8', '1', '5') ('5', '8', '1', '6') ('5', '8', '1', '7') ('5', '8', '1', '8') ('5', '8', '1', '9') ('5', '8', '2', '0') ('5', '8', '2', '1') ('5', '8', '2', '2') ('5', '8', '2', '3') ('5', '8', '2', '4') ('5', '8', '2', '5') ('5', '8', '2', '6') ('5', '8', '2', '7') ('5', '8', '2', '8') ('5', '8', '2', '9') ('5', '8', '3', '0') ('5', '8', '3', '1') ('5', '8', '3', '2') ('5', '8', '3', '3') ('5', '8', '3', '4') ('5', '8', '3', '5') ('5', '8', '3', '6') ('5', '8', '3', '7') ('5', '8', '3', '8') ('5', '8', '3', '9') ('5', '8', '4', '0') ('5', '8', '4', '1') ('5', '8', '4', '2') ('5', '8', '4', '3') ('5', '8', '4', '4') ('5', '8', '4', '5') ('5', '8', '4', '6') ('5', '8', '4', '7') ('5', '8', '4', '8') ('5', '8', '4', '9') ('5', '8', '5', '0') ('5', '8', '5', '1') ('5', '8', '5', '2') ('5', '8', '5', '3') ('5', '8', '5', '4') ('5', '8', '5', '5') ('5', '8', '5', '6') ('5', '8', '5', '7') ('5', '8', '5', '8') ('5', '8', '5', '9') ('5', '8', '6', '0') ('5', '8', '6', '1') ('5', '8', '6', '2') ('5', '8', '6', '3') ('5', '8', '6', '4') ('5', '8', '6', '5') ('5', '8', '6', '6') ('5', '8', '6', '7') ('5', '8', '6', '8') ('5', '8', '6', '9') ('5', '8', '7', '0') ('5', '8', '7', '1') ('5', '8', '7', '2') ('5', '8', '7', '3') ('5', '8', '7', '4') ('5', '8', '7', '5') ('5', '8', '7', '6') ('5', '8', '7', '7') ('5', '8', '7', '8') ('5', '8', '7', '9') ('5', '8', '8', '0') ('5', '8', '8', '1') ('5', '8', '8', '2') ('5', '8', '8', '3') ('5', '8', '8', '4') ('5', '8', '8', '5') ('5', '8', '8', '6') ('5', '8', '8', '7') ('5', '8', '8', '8') ('5', '8', '8', '9') ('5', '8', '9', '0') ('5', '8', '9', '1') ('5', '8', '9', '2') ('5', '8', '9', '3') ('5', '8', '9', '4') ('5', '8', '9', '5') ('5', '8', '9', '6') ('5', '8', '9', '7') ('5', '8', '9', '8') ('5', '8', '9', '9') ('5', '9', '0', '0') ('5', '9', '0', '1') ('5', '9', '0', '2') ('5', '9', '0', '3') ('5', '9', '0', '4') ('5', '9', '0', '5') ('5', '9', '0', '6') ('5', '9', '0', '7') ('5', '9', '0', '8') ('5', '9', '0', '9') ('5', '9', '1', '0') ('5', '9', '1', '1') ('5', '9', '1', '2') ('5', '9', '1', '3') ('5', '9', '1', '4') ('5', '9', '1', '5') ('5', '9', '1', '6') ('5', '9', '1', '7') ('5', '9', '1', '8') ('5', '9', '1', '9') ('5', '9', '2', '0') ('5', '9', '2', '1') ('5', '9', '2', '2') ('5', '9', '2', '3') ('5', '9', '2', '4') ('5', '9', '2', '5') ('5', '9', '2', '6') ('5', '9', '2', '7') ('5', '9', '2', '8') ('5', '9', '2', '9') ('5', '9', '3', '0') ('5', '9', '3', '1') ('5', '9', '3', '2') ('5', '9', '3', '3') ('5', '9', '3', '4') ('5', '9', '3', '5') ('5', '9', '3', '6') ('5', '9', '3', '7') ('5', '9', '3', '8') ('5', '9', '3', '9') ('5', '9', '4', '0') ('5', '9', '4', '1') ('5', '9', '4', '2') ('5', '9', '4', '3') ('5', '9', '4', '4') ('5', '9', '4', '5') ('5', '9', '4', '6') ('5', '9', '4', '7') ('5', '9', '4', '8') ('5', '9', '4', '9') ('5', '9', '5', '0') ('5', '9', '5', '1') ('5', '9', '5', '2') ('5', '9', '5', '3') ('5', '9', '5', '4') ('5', '9', '5', '5') ('5', '9', '5', '6') ('5', '9', '5', '7') ('5', '9', '5', '8') ('5', '9', '5', '9') ('5', '9', '6', '0') ('5', '9', '6', '1') ('5', '9', '6', '2') ('5', '9', '6', '3') ('5', '9', '6', '4') ('5', '9', '6', '5') ('5', '9', '6', '6') ('5', '9', '6', '7') ('5', '9', '6', '8') ('5', '9', '6', '9') ('5', '9', '7', '0') ('5', '9', '7', '1') ('5', '9', '7', '2') ('5', '9', '7', '3') ('5', '9', '7', '4') ('5', '9', '7', '5') ('5', '9', '7', '6') ('5', '9', '7', '7') ('5', '9', '7', '8') ('5', '9', '7', '9') ('5', '9', '8', '0') ('5', '9', '8', '1') ('5', '9', '8', '2') ('5', '9', '8', '3') ('5', '9', '8', '4') ('5', '9', '8', '5') ('5', '9', '8', '6') ('5', '9', '8', '7') ('5', '9', '8', '8') ('5', '9', '8', '9') ('5', '9', '9', '0') ('5', '9', '9', '1') ('5', '9', '9', '2') ('5', '9', '9', '3') ('5', '9', '9', '4') ('5', '9', '9', '5') ('5', '9', '9', '6') ('5', '9', '9', '7') ('5', '9', '9', '8') ('5', '9', '9', '9') ('6', '0', '0', '0') ('6', '0', '0', '1') ('6', '0', '0', '2') ('6', '0', '0', '3') ('6', '0', '0', '4') ('6', '0', '0', '5') ('6', '0', '0', '6') ('6', '0', '0', '7') ('6', '0', '0', '8') ('6', '0', '0', '9') ('6', '0', '1', '0') ('6', '0', '1', '1') ('6', '0', '1', '2') ('6', '0', '1', '3') ('6', '0', '1', '4') ('6', '0', '1', '5') ('6', '0', '1', '6') ('6', '0', '1', '7') ('6', '0', '1', '8') ('6', '0', '1', '9') ('6', '0', '2', '0') ('6', '0', '2', '1') ('6', '0', '2', '2') ('6', '0', '2', '3') ('6', '0', '2', '4') ('6', '0', '2', '5') ('6', '0', '2', '6') ('6', '0', '2', '7') ('6', '0', '2', '8') ('6', '0', '2', '9') ('6', '0', '3', '0') ('6', '0', '3', '1') ('6', '0', '3', '2') ('6', '0', '3', '3') ('6', '0', '3', '4') ('6', '0', '3', '5') ('6', '0', '3', '6') ('6', '0', '3', '7') ('6', '0', '3', '8') ('6', '0', '3', '9') ('6', '0', '4', '0') ('6', '0', '4', '1') ('6', '0', '4', '2') ('6', '0', '4', '3') ('6', '0', '4', '4') ('6', '0', '4', '5') ('6', '0', '4', '6') ('6', '0', '4', '7') ('6', '0', '4', '8') ('6', '0', '4', '9') ('6', '0', '5', '0') ('6', '0', '5', '1') ('6', '0', '5', '2') ('6', '0', '5', '3') ('6', '0', '5', '4') ('6', '0', '5', '5') ('6', '0', '5', '6') ('6', '0', '5', '7') ('6', '0', '5', '8') ('6', '0', '5', '9') ('6', '0', '6', '0') ('6', '0', '6', '1') ('6', '0', '6', '2') ('6', '0', '6', '3') ('6', '0', '6', '4') ('6', '0', '6', '5') ('6', '0', '6', '6') ('6', '0', '6', '7') ('6', '0', '6', '8') ('6', '0', '6', '9') ('6', '0', '7', '0') ('6', '0', '7', '1') ('6', '0', '7', '2') ('6', '0', '7', '3') ('6', '0', '7', '4') ('6', '0', '7', '5') ('6', '0', '7', '6') ('6', '0', '7', '7') ('6', '0', '7', '8') ('6', '0', '7', '9') ('6', '0', '8', '0') ('6', '0', '8', '1') ('6', '0', '8', '2') ('6', '0', '8', '3') ('6', '0', '8', '4') ('6', '0', '8', '5') ('6', '0', '8', '6') ('6', '0', '8', '7') ('6', '0', '8', '8') ('6', '0', '8', '9') ('6', '0', '9', '0') ('6', '0', '9', '1') ('6', '0', '9', '2') ('6', '0', '9', '3') ('6', '0', '9', '4') ('6', '0', '9', '5') ('6', '0', '9', '6') ('6', '0', '9', '7') ('6', '0', '9', '8') ('6', '0', '9', '9') ('6', '1', '0', '0') ('6', '1', '0', '1') ('6', '1', '0', '2') ('6', '1', '0', '3') ('6', '1', '0', '4') ('6', '1', '0', '5') ('6', '1', '0', '6') ('6', '1', '0', '7') ('6', '1', '0', '8') ('6', '1', '0', '9') ('6', '1', '1', '0') ('6', '1', '1', '1') ('6', '1', '1', '2') ('6', '1', '1', '3') ('6', '1', '1', '4') ('6', '1', '1', '5') ('6', '1', '1', '6') ('6', '1', '1', '7') ('6', '1', '1', '8') ('6', '1', '1', '9') ('6', '1', '2', '0') ('6', '1', '2', '1') ('6', '1', '2', '2') ('6', '1', '2', '3') ('6', '1', '2', '4') ('6', '1', '2', '5') ('6', '1', '2', '6') ('6', '1', '2', '7') ('6', '1', '2', '8') ('6', '1', '2', '9') ('6', '1', '3', '0') ('6', '1', '3', '1') ('6', '1', '3', '2') ('6', '1', '3', '3') ('6', '1', '3', '4') ('6', '1', '3', '5') ('6', '1', '3', '6') ('6', '1', '3', '7') ('6', '1', '3', '8') ('6', '1', '3', '9') ('6', '1', '4', '0') ('6', '1', '4', '1') ('6', '1', '4', '2') ('6', '1', '4', '3') ('6', '1', '4', '4') ('6', '1', '4', '5') ('6', '1', '4', '6') ('6', '1', '4', '7') ('6', '1', '4', '8') ('6', '1', '4', '9') ('6', '1', '5', '0') ('6', '1', '5', '1') ('6', '1', '5', '2') ('6', '1', '5', '3') ('6', '1', '5', '4') ('6', '1', '5', '5') ('6', '1', '5', '6') ('6', '1', '5', '7') ('6', '1', '5', '8') ('6', '1', '5', '9') ('6', '1', '6', '0') ('6', '1', '6', '1') ('6', '1', '6', '2') ('6', '1', '6', '3') ('6', '1', '6', '4') ('6', '1', '6', '5') ('6', '1', '6', '6') ('6', '1', '6', '7') ('6', '1', '6', '8') ('6', '1', '6', '9') ('6', '1', '7', '0') ('6', '1', '7', '1') ('6', '1', '7', '2') ('6', '1', '7', '3') ('6', '1', '7', '4') ('6', '1', '7', '5') ('6', '1', '7', '6') ('6', '1', '7', '7') ('6', '1', '7', '8') ('6', '1', '7', '9') ('6', '1', '8', '0') ('6', '1', '8', '1') ('6', '1', '8', '2') ('6', '1', '8', '3') ('6', '1', '8', '4') ('6', '1', '8', '5') ('6', '1', '8', '6') ('6', '1', '8', '7') ('6', '1', '8', '8') ('6', '1', '8', '9') ('6', '1', '9', '0') ('6', '1', '9', '1') ('6', '1', '9', '2') ('6', '1', '9', '3') ('6', '1', '9', '4') ('6', '1', '9', '5') ('6', '1', '9', '6') ('6', '1', '9', '7') ('6', '1', '9', '8') ('6', '1', '9', '9') ('6', '2', '0', '0') ('6', '2', '0', '1') ('6', '2', '0', '2') ('6', '2', '0', '3') ('6', '2', '0', '4') ('6', '2', '0', '5') ('6', '2', '0', '6') ('6', '2', '0', '7') ('6', '2', '0', '8') ('6', '2', '0', '9') ('6', '2', '1', '0') ('6', '2', '1', '1') ('6', '2', '1', '2') ('6', '2', '1', '3') ('6', '2', '1', '4') ('6', '2', '1', '5') ('6', '2', '1', '6') ('6', '2', '1', '7') ('6', '2', '1', '8') ('6', '2', '1', '9') ('6', '2', '2', '0') ('6', '2', '2', '1') ('6', '2', '2', '2') ('6', '2', '2', '3') ('6', '2', '2', '4') ('6', '2', '2', '5') ('6', '2', '2', '6') ('6', '2', '2', '7') ('6', '2', '2', '8') ('6', '2', '2', '9') ('6', '2', '3', '0') ('6', '2', '3', '1') ('6', '2', '3', '2') ('6', '2', '3', '3') ('6', '2', '3', '4') ('6', '2', '3', '5') ('6', '2', '3', '6') ('6', '2', '3', '7') ('6', '2', '3', '8') ('6', '2', '3', '9') ('6', '2', '4', '0') ('6', '2', '4', '1') ('6', '2', '4', '2') ('6', '2', '4', '3') ('6', '2', '4', '4') ('6', '2', '4', '5') ('6', '2', '4', '6') ('6', '2', '4', '7') ('6', '2', '4', '8') ('6', '2', '4', '9') ('6', '2', '5', '0') ('6', '2', '5', '1') ('6', '2', '5', '2') ('6', '2', '5', '3') ('6', '2', '5', '4') ('6', '2', '5', '5') ('6', '2', '5', '6') ('6', '2', '5', '7') ('6', '2', '5', '8') ('6', '2', '5', '9') ('6', '2', '6', '0') ('6', '2', '6', '1') ('6', '2', '6', '2') ('6', '2', '6', '3') ('6', '2', '6', '4') ('6', '2', '6', '5') ('6', '2', '6', '6') ('6', '2', '6', '7') ('6', '2', '6', '8') ('6', '2', '6', '9') ('6', '2', '7', '0') ('6', '2', '7', '1') ('6', '2', '7', '2') ('6', '2', '7', '3') ('6', '2', '7', '4') ('6', '2', '7', '5') ('6', '2', '7', '6') ('6', '2', '7', '7') ('6', '2', '7', '8') ('6', '2', '7', '9') ('6', '2', '8', '0') ('6', '2', '8', '1') ('6', '2', '8', '2') ('6', '2', '8', '3') ('6', '2', '8', '4') ('6', '2', '8', '5') ('6', '2', '8', '6') ('6', '2', '8', '7') ('6', '2', '8', '8') ('6', '2', '8', '9') ('6', '2', '9', '0') ('6', '2', '9', '1') ('6', '2', '9', '2') ('6', '2', '9', '3') ('6', '2', '9', '4') ('6', '2', '9', '5') ('6', '2', '9', '6') ('6', '2', '9', '7') ('6', '2', '9', '8') ('6', '2', '9', '9') ('6', '3', '0', '0') ('6', '3', '0', '1') ('6', '3', '0', '2') ('6', '3', '0', '3') ('6', '3', '0', '4') ('6', '3', '0', '5') ('6', '3', '0', '6') ('6', '3', '0', '7') ('6', '3', '0', '8') ('6', '3', '0', '9') ('6', '3', '1', '0') ('6', '3', '1', '1') ('6', '3', '1', '2') ('6', '3', '1', '3') ('6', '3', '1', '4') ('6', '3', '1', '5') ('6', '3', '1', '6') ('6', '3', '1', '7') ('6', '3', '1', '8') ('6', '3', '1', '9') ('6', '3', '2', '0') ('6', '3', '2', '1') ('6', '3', '2', '2') ('6', '3', '2', '3') ('6', '3', '2', '4') ('6', '3', '2', '5') ('6', '3', '2', '6') ('6', '3', '2', '7') ('6', '3', '2', '8') ('6', '3', '2', '9') ('6', '3', '3', '0') ('6', '3', '3', '1') ('6', '3', '3', '2') ('6', '3', '3', '3') ('6', '3', '3', '4') ('6', '3', '3', '5') ('6', '3', '3', '6') ('6', '3', '3', '7') ('6', '3', '3', '8') ('6', '3', '3', '9') ('6', '3', '4', '0') ('6', '3', '4', '1') ('6', '3', '4', '2') ('6', '3', '4', '3') ('6', '3', '4', '4') ('6', '3', '4', '5') ('6', '3', '4', '6') ('6', '3', '4', '7') ('6', '3', '4', '8') ('6', '3', '4', '9') ('6', '3', '5', '0') ('6', '3', '5', '1') ('6', '3', '5', '2') ('6', '3', '5', '3') ('6', '3', '5', '4') ('6', '3', '5', '5') ('6', '3', '5', '6') ('6', '3', '5', '7') ('6', '3', '5', '8') ('6', '3', '5', '9') ('6', '3', '6', '0') ('6', '3', '6', '1') ('6', '3', '6', '2') ('6', '3', '6', '3') ('6', '3', '6', '4') ('6', '3', '6', '5') ('6', '3', '6', '6') ('6', '3', '6', '7') ('6', '3', '6', '8') ('6', '3', '6', '9') ('6', '3', '7', '0') ('6', '3', '7', '1') ('6', '3', '7', '2') ('6', '3', '7', '3') ('6', '3', '7', '4') ('6', '3', '7', '5') ('6', '3', '7', '6') ('6', '3', '7', '7') ('6', '3', '7', '8') ('6', '3', '7', '9') ('6', '3', '8', '0') ('6', '3', '8', '1') ('6', '3', '8', '2') ('6', '3', '8', '3') ('6', '3', '8', '4') ('6', '3', '8', '5') ('6', '3', '8', '6') ('6', '3', '8', '7') ('6', '3', '8', '8') ('6', '3', '8', '9') ('6', '3', '9', '0') ('6', '3', '9', '1') ('6', '3', '9', '2') ('6', '3', '9', '3') ('6', '3', '9', '4') ('6', '3', '9', '5') ('6', '3', '9', '6') ('6', '3', '9', '7') ('6', '3', '9', '8') ('6', '3', '9', '9') ('6', '4', '0', '0') ('6', '4', '0', '1') ('6', '4', '0', '2') ('6', '4', '0', '3') ('6', '4', '0', '4') ('6', '4', '0', '5') ('6', '4', '0', '6') ('6', '4', '0', '7') ('6', '4', '0', '8') ('6', '4', '0', '9') ('6', '4', '1', '0') ('6', '4', '1', '1') ('6', '4', '1', '2') ('6', '4', '1', '3') ('6', '4', '1', '4') ('6', '4', '1', '5') ('6', '4', '1', '6') ('6', '4', '1', '7') ('6', '4', '1', '8') ('6', '4', '1', '9') ('6', '4', '2', '0') ('6', '4', '2', '1') ('6', '4', '2', '2') ('6', '4', '2', '3') ('6', '4', '2', '4') ('6', '4', '2', '5') ('6', '4', '2', '6') ('6', '4', '2', '7') ('6', '4', '2', '8') ('6', '4', '2', '9') ('6', '4', '3', '0') ('6', '4', '3', '1') ('6', '4', '3', '2') ('6', '4', '3', '3') ('6', '4', '3', '4') ('6', '4', '3', '5') ('6', '4', '3', '6') ('6', '4', '3', '7') ('6', '4', '3', '8') ('6', '4', '3', '9') ('6', '4', '4', '0') ('6', '4', '4', '1') ('6', '4', '4', '2') ('6', '4', '4', '3') ('6', '4', '4', '4') ('6', '4', '4', '5') ('6', '4', '4', '6') ('6', '4', '4', '7') ('6', '4', '4', '8') ('6', '4', '4', '9') ('6', '4', '5', '0') ('6', '4', '5', '1') ('6', '4', '5', '2') ('6', '4', '5', '3') ('6', '4', '5', '4') ('6', '4', '5', '5') ('6', '4', '5', '6') ('6', '4', '5', '7') ('6', '4', '5', '8') ('6', '4', '5', '9') ('6', '4', '6', '0') ('6', '4', '6', '1') ('6', '4', '6', '2') ('6', '4', '6', '3') ('6', '4', '6', '4') ('6', '4', '6', '5') ('6', '4', '6', '6') ('6', '4', '6', '7') ('6', '4', '6', '8') ('6', '4', '6', '9') ('6', '4', '7', '0') ('6', '4', '7', '1') ('6', '4', '7', '2') ('6', '4', '7', '3') ('6', '4', '7', '4') ('6', '4', '7', '5') ('6', '4', '7', '6') ('6', '4', '7', '7') ('6', '4', '7', '8') ('6', '4', '7', '9') ('6', '4', '8', '0') ('6', '4', '8', '1') ('6', '4', '8', '2') ('6', '4', '8', '3') ('6', '4', '8', '4') ('6', '4', '8', '5') ('6', '4', '8', '6') ('6', '4', '8', '7') ('6', '4', '8', '8') ('6', '4', '8', '9') ('6', '4', '9', '0') ('6', '4', '9', '1') ('6', '4', '9', '2') ('6', '4', '9', '3') ('6', '4', '9', '4') ('6', '4', '9', '5') ('6', '4', '9', '6') ('6', '4', '9', '7') ('6', '4', '9', '8') ('6', '4', '9', '9') ('6', '5', '0', '0') ('6', '5', '0', '1') ('6', '5', '0', '2') ('6', '5', '0', '3') ('6', '5', '0', '4') ('6', '5', '0', '5') ('6', '5', '0', '6') ('6', '5', '0', '7') ('6', '5', '0', '8') ('6', '5', '0', '9') ('6', '5', '1', '0') ('6', '5', '1', '1') ('6', '5', '1', '2') ('6', '5', '1', '3') ('6', '5', '1', '4') ('6', '5', '1', '5') ('6', '5', '1', '6') ('6', '5', '1', '7') ('6', '5', '1', '8') ('6', '5', '1', '9') ('6', '5', '2', '0') ('6', '5', '2', '1') ('6', '5', '2', '2') ('6', '5', '2', '3') ('6', '5', '2', '4') ('6', '5', '2', '5') ('6', '5', '2', '6') ('6', '5', '2', '7') ('6', '5', '2', '8') ('6', '5', '2', '9') ('6', '5', '3', '0') ('6', '5', '3', '1') ('6', '5', '3', '2') ('6', '5', '3', '3') ('6', '5', '3', '4') ('6', '5', '3', '5') ('6', '5', '3', '6') ('6', '5', '3', '7') ('6', '5', '3', '8') ('6', '5', '3', '9') ('6', '5', '4', '0') ('6', '5', '4', '1') ('6', '5', '4', '2') ('6', '5', '4', '3') ('6', '5', '4', '4') ('6', '5', '4', '5') ('6', '5', '4', '6') ('6', '5', '4', '7') ('6', '5', '4', '8') ('6', '5', '4', '9') ('6', '5', '5', '0') ('6', '5', '5', '1') ('6', '5', '5', '2') ('6', '5', '5', '3') ('6', '5', '5', '4') ('6', '5', '5', '5') ('6', '5', '5', '6') ('6', '5', '5', '7') ('6', '5', '5', '8') ('6', '5', '5', '9') ('6', '5', '6', '0') ('6', '5', '6', '1') ('6', '5', '6', '2') ('6', '5', '6', '3') ('6', '5', '6', '4') ('6', '5', '6', '5') ('6', '5', '6', '6') ('6', '5', '6', '7') ('6', '5', '6', '8') ('6', '5', '6', '9') ('6', '5', '7', '0') ('6', '5', '7', '1') ('6', '5', '7', '2') ('6', '5', '7', '3') ('6', '5', '7', '4') ('6', '5', '7', '5') ('6', '5', '7', '6') ('6', '5', '7', '7') ('6', '5', '7', '8') ('6', '5', '7', '9') ('6', '5', '8', '0') ('6', '5', '8', '1') ('6', '5', '8', '2') ('6', '5', '8', '3') ('6', '5', '8', '4') ('6', '5', '8', '5') ('6', '5', '8', '6') ('6', '5', '8', '7') ('6', '5', '8', '8') ('6', '5', '8', '9') ('6', '5', '9', '0') ('6', '5', '9', '1') ('6', '5', '9', '2') ('6', '5', '9', '3') ('6', '5', '9', '4') ('6', '5', '9', '5') ('6', '5', '9', '6') ('6', '5', '9', '7') ('6', '5', '9', '8') ('6', '5', '9', '9') ('6', '6', '0', '0') ('6', '6', '0', '1') ('6', '6', '0', '2') ('6', '6', '0', '3') ('6', '6', '0', '4') ('6', '6', '0', '5') ('6', '6', '0', '6') ('6', '6', '0', '7') ('6', '6', '0', '8') ('6', '6', '0', '9') ('6', '6', '1', '0') ('6', '6', '1', '1') ('6', '6', '1', '2') ('6', '6', '1', '3') ('6', '6', '1', '4') ('6', '6', '1', '5') ('6', '6', '1', '6') ('6', '6', '1', '7') ('6', '6', '1', '8') ('6', '6', '1', '9') ('6', '6', '2', '0') ('6', '6', '2', '1') ('6', '6', '2', '2') ('6', '6', '2', '3') ('6', '6', '2', '4') ('6', '6', '2', '5') ('6', '6', '2', '6') ('6', '6', '2', '7') ('6', '6', '2', '8') ('6', '6', '2', '9') ('6', '6', '3', '0') ('6', '6', '3', '1') ('6', '6', '3', '2') ('6', '6', '3', '3') ('6', '6', '3', '4') ('6', '6', '3', '5') ('6', '6', '3', '6') ('6', '6', '3', '7') ('6', '6', '3', '8') ('6', '6', '3', '9') ('6', '6', '4', '0') ('6', '6', '4', '1') ('6', '6', '4', '2') ('6', '6', '4', '3') ('6', '6', '4', '4') ('6', '6', '4', '5') ('6', '6', '4', '6') ('6', '6', '4', '7') ('6', '6', '4', '8') ('6', '6', '4', '9') ('6', '6', '5', '0') ('6', '6', '5', '1') ('6', '6', '5', '2') ('6', '6', '5', '3') ('6', '6', '5', '4') ('6', '6', '5', '5') ('6', '6', '5', '6') ('6', '6', '5', '7') ('6', '6', '5', '8') ('6', '6', '5', '9') ('6', '6', '6', '0') ('6', '6', '6', '1') ('6', '6', '6', '2') ('6', '6', '6', '3') ('6', '6', '6', '4') ('6', '6', '6', '5') ('6', '6', '6', '6') ('6', '6', '6', '7') ('6', '6', '6', '8') ('6', '6', '6', '9') ('6', '6', '7', '0') ('6', '6', '7', '1') ('6', '6', '7', '2') ('6', '6', '7', '3') ('6', '6', '7', '4') ('6', '6', '7', '5') ('6', '6', '7', '6') ('6', '6', '7', '7') ('6', '6', '7', '8') ('6', '6', '7', '9') ('6', '6', '8', '0') ('6', '6', '8', '1') ('6', '6', '8', '2') ('6', '6', '8', '3') ('6', '6', '8', '4') ('6', '6', '8', '5') ('6', '6', '8', '6') ('6', '6', '8', '7') ('6', '6', '8', '8') ('6', '6', '8', '9') ('6', '6', '9', '0') ('6', '6', '9', '1') ('6', '6', '9', '2') ('6', '6', '9', '3') ('6', '6', '9', '4') ('6', '6', '9', '5') ('6', '6', '9', '6') ('6', '6', '9', '7') ('6', '6', '9', '8') ('6', '6', '9', '9') ('6', '7', '0', '0') ('6', '7', '0', '1') ('6', '7', '0', '2') ('6', '7', '0', '3') ('6', '7', '0', '4') ('6', '7', '0', '5') ('6', '7', '0', '6') ('6', '7', '0', '7') ('6', '7', '0', '8') ('6', '7', '0', '9') ('6', '7', '1', '0') ('6', '7', '1', '1') ('6', '7', '1', '2') ('6', '7', '1', '3') ('6', '7', '1', '4') ('6', '7', '1', '5') ('6', '7', '1', '6') ('6', '7', '1', '7') ('6', '7', '1', '8') ('6', '7', '1', '9') ('6', '7', '2', '0') ('6', '7', '2', '1') ('6', '7', '2', '2') ('6', '7', '2', '3') ('6', '7', '2', '4') ('6', '7', '2', '5') ('6', '7', '2', '6') ('6', '7', '2', '7') ('6', '7', '2', '8') ('6', '7', '2', '9') ('6', '7', '3', '0') ('6', '7', '3', '1') ('6', '7', '3', '2') ('6', '7', '3', '3') ('6', '7', '3', '4') ('6', '7', '3', '5') ('6', '7', '3', '6') ('6', '7', '3', '7') ('6', '7', '3', '8') ('6', '7', '3', '9') ('6', '7', '4', '0') ('6', '7', '4', '1') ('6', '7', '4', '2') ('6', '7', '4', '3') ('6', '7', '4', '4') ('6', '7', '4', '5') ('6', '7', '4', '6') ('6', '7', '4', '7') ('6', '7', '4', '8') ('6', '7', '4', '9') ('6', '7', '5', '0') ('6', '7', '5', '1') ('6', '7', '5', '2') ('6', '7', '5', '3') ('6', '7', '5', '4') ('6', '7', '5', '5') ('6', '7', '5', '6') ('6', '7', '5', '7') ('6', '7', '5', '8') ('6', '7', '5', '9') ('6', '7', '6', '0') ('6', '7', '6', '1') ('6', '7', '6', '2') ('6', '7', '6', '3') ('6', '7', '6', '4') ('6', '7', '6', '5') ('6', '7', '6', '6') ('6', '7', '6', '7') ('6', '7', '6', '8') ('6', '7', '6', '9') ('6', '7', '7', '0') ('6', '7', '7', '1') ('6', '7', '7', '2') ('6', '7', '7', '3') ('6', '7', '7', '4') ('6', '7', '7', '5') ('6', '7', '7', '6') ('6', '7', '7', '7') ('6', '7', '7', '8') ('6', '7', '7', '9') ('6', '7', '8', '0') ('6', '7', '8', '1') ('6', '7', '8', '2') ('6', '7', '8', '3') ('6', '7', '8', '4') ('6', '7', '8', '5') ('6', '7', '8', '6') ('6', '7', '8', '7') ('6', '7', '8', '8') ('6', '7', '8', '9') ('6', '7', '9', '0') ('6', '7', '9', '1') ('6', '7', '9', '2') ('6', '7', '9', '3') ('6', '7', '9', '4') ('6', '7', '9', '5') ('6', '7', '9', '6') ('6', '7', '9', '7') ('6', '7', '9', '8') ('6', '7', '9', '9') ('6', '8', '0', '0') ('6', '8', '0', '1') ('6', '8', '0', '2') ('6', '8', '0', '3') ('6', '8', '0', '4') ('6', '8', '0', '5') ('6', '8', '0', '6') ('6', '8', '0', '7') ('6', '8', '0', '8') ('6', '8', '0', '9') ('6', '8', '1', '0') ('6', '8', '1', '1') ('6', '8', '1', '2') ('6', '8', '1', '3') ('6', '8', '1', '4') ('6', '8', '1', '5') ('6', '8', '1', '6') ('6', '8', '1', '7') ('6', '8', '1', '8') ('6', '8', '1', '9') ('6', '8', '2', '0') ('6', '8', '2', '1') ('6', '8', '2', '2') ('6', '8', '2', '3') ('6', '8', '2', '4') ('6', '8', '2', '5') ('6', '8', '2', '6') ('6', '8', '2', '7') ('6', '8', '2', '8') ('6', '8', '2', '9') ('6', '8', '3', '0') ('6', '8', '3', '1') ('6', '8', '3', '2') ('6', '8', '3', '3') ('6', '8', '3', '4') ('6', '8', '3', '5') ('6', '8', '3', '6') ('6', '8', '3', '7') ('6', '8', '3', '8') ('6', '8', '3', '9') ('6', '8', '4', '0') ('6', '8', '4', '1') ('6', '8', '4', '2') ('6', '8', '4', '3') ('6', '8', '4', '4') ('6', '8', '4', '5') ('6', '8', '4', '6') ('6', '8', '4', '7') ('6', '8', '4', '8') ('6', '8', '4', '9') ('6', '8', '5', '0') ('6', '8', '5', '1') ('6', '8', '5', '2') ('6', '8', '5', '3') ('6', '8', '5', '4') ('6', '8', '5', '5') ('6', '8', '5', '6') ('6', '8', '5', '7') ('6', '8', '5', '8') ('6', '8', '5', '9') ('6', '8', '6', '0') ('6', '8', '6', '1') ('6', '8', '6', '2') ('6', '8', '6', '3') ('6', '8', '6', '4') ('6', '8', '6', '5') ('6', '8', '6', '6') ('6', '8', '6', '7') ('6', '8', '6', '8') ('6', '8', '6', '9') ('6', '8', '7', '0') ('6', '8', '7', '1') ('6', '8', '7', '2') ('6', '8', '7', '3') ('6', '8', '7', '4') ('6', '8', '7', '5') ('6', '8', '7', '6') ('6', '8', '7', '7') ('6', '8', '7', '8') ('6', '8', '7', '9') ('6', '8', '8', '0') ('6', '8', '8', '1') ('6', '8', '8', '2') ('6', '8', '8', '3') ('6', '8', '8', '4') ('6', '8', '8', '5') ('6', '8', '8', '6') ('6', '8', '8', '7') ('6', '8', '8', '8') ('6', '8', '8', '9') ('6', '8', '9', '0') ('6', '8', '9', '1') ('6', '8', '9', '2') ('6', '8', '9', '3') ('6', '8', '9', '4') ('6', '8', '9', '5') ('6', '8', '9', '6') ('6', '8', '9', '7') ('6', '8', '9', '8') ('6', '8', '9', '9') ('6', '9', '0', '0') ('6', '9', '0', '1') ('6', '9', '0', '2') ('6', '9', '0', '3') ('6', '9', '0', '4') ('6', '9', '0', '5') ('6', '9', '0', '6') ('6', '9', '0', '7') ('6', '9', '0', '8') ('6', '9', '0', '9') ('6', '9', '1', '0') ('6', '9', '1', '1') ('6', '9', '1', '2') ('6', '9', '1', '3') ('6', '9', '1', '4') ('6', '9', '1', '5') ('6', '9', '1', '6') ('6', '9', '1', '7') ('6', '9', '1', '8') ('6', '9', '1', '9') ('6', '9', '2', '0') ('6', '9', '2', '1') ('6', '9', '2', '2') ('6', '9', '2', '3') ('6', '9', '2', '4') ('6', '9', '2', '5') ('6', '9', '2', '6') ('6', '9', '2', '7') ('6', '9', '2', '8') ('6', '9', '2', '9') ('6', '9', '3', '0') ('6', '9', '3', '1') ('6', '9', '3', '2') ('6', '9', '3', '3') ('6', '9', '3', '4') ('6', '9', '3', '5') ('6', '9', '3', '6') ('6', '9', '3', '7') ('6', '9', '3', '8') ('6', '9', '3', '9') ('6', '9', '4', '0') ('6', '9', '4', '1') ('6', '9', '4', '2') ('6', '9', '4', '3') ('6', '9', '4', '4') ('6', '9', '4', '5') ('6', '9', '4', '6') ('6', '9', '4', '7') ('6', '9', '4', '8') ('6', '9', '4', '9') ('6', '9', '5', '0') ('6', '9', '5', '1') ('6', '9', '5', '2') ('6', '9', '5', '3') ('6', '9', '5', '4') ('6', '9', '5', '5') ('6', '9', '5', '6') ('6', '9', '5', '7') ('6', '9', '5', '8') ('6', '9', '5', '9') ('6', '9', '6', '0') ('6', '9', '6', '1') ('6', '9', '6', '2') ('6', '9', '6', '3') ('6', '9', '6', '4') ('6', '9', '6', '5') ('6', '9', '6', '6') ('6', '9', '6', '7') ('6', '9', '6', '8') ('6', '9', '6', '9') ('6', '9', '7', '0') ('6', '9', '7', '1') ('6', '9', '7', '2') ('6', '9', '7', '3') ('6', '9', '7', '4') ('6', '9', '7', '5') ('6', '9', '7', '6') ('6', '9', '7', '7') ('6', '9', '7', '8') ('6', '9', '7', '9') ('6', '9', '8', '0') ('6', '9', '8', '1') ('6', '9', '8', '2') ('6', '9', '8', '3') ('6', '9', '8', '4') ('6', '9', '8', '5') ('6', '9', '8', '6') ('6', '9', '8', '7') ('6', '9', '8', '8') ('6', '9', '8', '9') ('6', '9', '9', '0') ('6', '9', '9', '1') ('6', '9', '9', '2') ('6', '9', '9', '3') ('6', '9', '9', '4') ('6', '9', '9', '5') ('6', '9', '9', '6') ('6', '9', '9', '7') ('6', '9', '9', '8') ('6', '9', '9', '9') ('7', '0', '0', '0') ('7', '0', '0', '1') ('7', '0', '0', '2') ('7', '0', '0', '3') ('7', '0', '0', '4') ('7', '0', '0', '5') ('7', '0', '0', '6') ('7', '0', '0', '7') ('7', '0', '0', '8') ('7', '0', '0', '9') ('7', '0', '1', '0') ('7', '0', '1', '1') ('7', '0', '1', '2') ('7', '0', '1', '3') ('7', '0', '1', '4') ('7', '0', '1', '5') ('7', '0', '1', '6') ('7', '0', '1', '7') ('7', '0', '1', '8') ('7', '0', '1', '9') ('7', '0', '2', '0') ('7', '0', '2', '1') ('7', '0', '2', '2') ('7', '0', '2', '3') ('7', '0', '2', '4') ('7', '0', '2', '5') ('7', '0', '2', '6') ('7', '0', '2', '7') ('7', '0', '2', '8') ('7', '0', '2', '9') ('7', '0', '3', '0') ('7', '0', '3', '1') ('7', '0', '3', '2') ('7', '0', '3', '3') ('7', '0', '3', '4') ('7', '0', '3', '5') ('7', '0', '3', '6') ('7', '0', '3', '7') ('7', '0', '3', '8') ('7', '0', '3', '9') ('7', '0', '4', '0') ('7', '0', '4', '1') ('7', '0', '4', '2') ('7', '0', '4', '3') ('7', '0', '4', '4') ('7', '0', '4', '5') ('7', '0', '4', '6') ('7', '0', '4', '7') ('7', '0', '4', '8') ('7', '0', '4', '9') ('7', '0', '5', '0') ('7', '0', '5', '1') ('7', '0', '5', '2') ('7', '0', '5', '3') ('7', '0', '5', '4') ('7', '0', '5', '5') ('7', '0', '5', '6') ('7', '0', '5', '7') ('7', '0', '5', '8') ('7', '0', '5', '9') ('7', '0', '6', '0') ('7', '0', '6', '1') ('7', '0', '6', '2') ('7', '0', '6', '3') ('7', '0', '6', '4') ('7', '0', '6', '5') ('7', '0', '6', '6') ('7', '0', '6', '7') ('7', '0', '6', '8') ('7', '0', '6', '9') ('7', '0', '7', '0') ('7', '0', '7', '1') ('7', '0', '7', '2') ('7', '0', '7', '3') ('7', '0', '7', '4') ('7', '0', '7', '5') ('7', '0', '7', '6') ('7', '0', '7', '7') ('7', '0', '7', '8') ('7', '0', '7', '9') ('7', '0', '8', '0') ('7', '0', '8', '1') ('7', '0', '8', '2') ('7', '0', '8', '3') ('7', '0', '8', '4') ('7', '0', '8', '5') ('7', '0', '8', '6') ('7', '0', '8', '7') ('7', '0', '8', '8') ('7', '0', '8', '9') ('7', '0', '9', '0') ('7', '0', '9', '1') ('7', '0', '9', '2') ('7', '0', '9', '3') ('7', '0', '9', '4') ('7', '0', '9', '5') ('7', '0', '9', '6') ('7', '0', '9', '7') ('7', '0', '9', '8') ('7', '0', '9', '9') ('7', '1', '0', '0') ('7', '1', '0', '1') ('7', '1', '0', '2') ('7', '1', '0', '3') ('7', '1', '0', '4') ('7', '1', '0', '5') ('7', '1', '0', '6') ('7', '1', '0', '7') ('7', '1', '0', '8') ('7', '1', '0', '9') ('7', '1', '1', '0') ('7', '1', '1', '1') ('7', '1', '1', '2') ('7', '1', '1', '3') ('7', '1', '1', '4') ('7', '1', '1', '5') ('7', '1', '1', '6') ('7', '1', '1', '7') ('7', '1', '1', '8') ('7', '1', '1', '9') ('7', '1', '2', '0') ('7', '1', '2', '1') ('7', '1', '2', '2') ('7', '1', '2', '3') ('7', '1', '2', '4') ('7', '1', '2', '5') ('7', '1', '2', '6') ('7', '1', '2', '7') ('7', '1', '2', '8') ('7', '1', '2', '9') ('7', '1', '3', '0') ('7', '1', '3', '1') ('7', '1', '3', '2') ('7', '1', '3', '3') ('7', '1', '3', '4') ('7', '1', '3', '5') ('7', '1', '3', '6') ('7', '1', '3', '7') ('7', '1', '3', '8') ('7', '1', '3', '9') ('7', '1', '4', '0') ('7', '1', '4', '1') ('7', '1', '4', '2') ('7', '1', '4', '3') ('7', '1', '4', '4') ('7', '1', '4', '5') ('7', '1', '4', '6') ('7', '1', '4', '7') ('7', '1', '4', '8') ('7', '1', '4', '9') ('7', '1', '5', '0') ('7', '1', '5', '1') ('7', '1', '5', '2') ('7', '1', '5', '3') ('7', '1', '5', '4') ('7', '1', '5', '5') ('7', '1', '5', '6') ('7', '1', '5', '7') ('7', '1', '5', '8') ('7', '1', '5', '9') ('7', '1', '6', '0') ('7', '1', '6', '1') ('7', '1', '6', '2') ('7', '1', '6', '3') ('7', '1', '6', '4') ('7', '1', '6', '5') ('7', '1', '6', '6') ('7', '1', '6', '7') ('7', '1', '6', '8') ('7', '1', '6', '9') ('7', '1', '7', '0') ('7', '1', '7', '1') ('7', '1', '7', '2') ('7', '1', '7', '3') ('7', '1', '7', '4') ('7', '1', '7', '5') ('7', '1', '7', '6') ('7', '1', '7', '7') ('7', '1', '7', '8') ('7', '1', '7', '9') ('7', '1', '8', '0') ('7', '1', '8', '1') ('7', '1', '8', '2') ('7', '1', '8', '3') ('7', '1', '8', '4') ('7', '1', '8', '5') ('7', '1', '8', '6') ('7', '1', '8', '7') ('7', '1', '8', '8') ('7', '1', '8', '9') ('7', '1', '9', '0') ('7', '1', '9', '1') ('7', '1', '9', '2') ('7', '1', '9', '3') ('7', '1', '9', '4') ('7', '1', '9', '5') ('7', '1', '9', '6') ('7', '1', '9', '7') ('7', '1', '9', '8') ('7', '1', '9', '9') ('7', '2', '0', '0') ('7', '2', '0', '1') ('7', '2', '0', '2') ('7', '2', '0', '3') ('7', '2', '0', '4') ('7', '2', '0', '5') ('7', '2', '0', '6') ('7', '2', '0', '7') ('7', '2', '0', '8') ('7', '2', '0', '9') ('7', '2', '1', '0') ('7', '2', '1', '1') ('7', '2', '1', '2') ('7', '2', '1', '3') ('7', '2', '1', '4') ('7', '2', '1', '5') ('7', '2', '1', '6') ('7', '2', '1', '7') ('7', '2', '1', '8') ('7', '2', '1', '9') ('7', '2', '2', '0') ('7', '2', '2', '1') ('7', '2', '2', '2') ('7', '2', '2', '3') ('7', '2', '2', '4') ('7', '2', '2', '5') ('7', '2', '2', '6') ('7', '2', '2', '7') ('7', '2', '2', '8') ('7', '2', '2', '9') ('7', '2', '3', '0') ('7', '2', '3', '1') ('7', '2', '3', '2') ('7', '2', '3', '3') ('7', '2', '3', '4') ('7', '2', '3', '5') ('7', '2', '3', '6') ('7', '2', '3', '7') ('7', '2', '3', '8') ('7', '2', '3', '9') ('7', '2', '4', '0') ('7', '2', '4', '1') ('7', '2', '4', '2') ('7', '2', '4', '3') ('7', '2', '4', '4') ('7', '2', '4', '5') ('7', '2', '4', '6') ('7', '2', '4', '7') ('7', '2', '4', '8') ('7', '2', '4', '9') ('7', '2', '5', '0') ('7', '2', '5', '1') ('7', '2', '5', '2') ('7', '2', '5', '3') ('7', '2', '5', '4') ('7', '2', '5', '5') ('7', '2', '5', '6') ('7', '2', '5', '7') ('7', '2', '5', '8') ('7', '2', '5', '9') ('7', '2', '6', '0') ('7', '2', '6', '1') ('7', '2', '6', '2') ('7', '2', '6', '3') ('7', '2', '6', '4') ('7', '2', '6', '5') ('7', '2', '6', '6') ('7', '2', '6', '7') ('7', '2', '6', '8') ('7', '2', '6', '9') ('7', '2', '7', '0') ('7', '2', '7', '1') ('7', '2', '7', '2') ('7', '2', '7', '3') ('7', '2', '7', '4') ('7', '2', '7', '5') ('7', '2', '7', '6') ('7', '2', '7', '7') ('7', '2', '7', '8') ('7', '2', '7', '9') ('7', '2', '8', '0') ('7', '2', '8', '1') ('7', '2', '8', '2') ('7', '2', '8', '3') ('7', '2', '8', '4') ('7', '2', '8', '5') ('7', '2', '8', '6') ('7', '2', '8', '7') ('7', '2', '8', '8') ('7', '2', '8', '9') ('7', '2', '9', '0') ('7', '2', '9', '1') ('7', '2', '9', '2') ('7', '2', '9', '3') ('7', '2', '9', '4') ('7', '2', '9', '5') ('7', '2', '9', '6') ('7', '2', '9', '7') ('7', '2', '9', '8') ('7', '2', '9', '9') ('7', '3', '0', '0') ('7', '3', '0', '1') ('7', '3', '0', '2') ('7', '3', '0', '3') ('7', '3', '0', '4') ('7', '3', '0', '5') ('7', '3', '0', '6') ('7', '3', '0', '7') ('7', '3', '0', '8') ('7', '3', '0', '9') ('7', '3', '1', '0') ('7', '3', '1', '1') ('7', '3', '1', '2') ('7', '3', '1', '3') ('7', '3', '1', '4') ('7', '3', '1', '5') ('7', '3', '1', '6') ('7', '3', '1', '7') ('7', '3', '1', '8') ('7', '3', '1', '9') ('7', '3', '2', '0') ('7', '3', '2', '1') ('7', '3', '2', '2') ('7', '3', '2', '3') ('7', '3', '2', '4') ('7', '3', '2', '5') ('7', '3', '2', '6') ('7', '3', '2', '7') ('7', '3', '2', '8') ('7', '3', '2', '9') ('7', '3', '3', '0') ('7', '3', '3', '1') ('7', '3', '3', '2') ('7', '3', '3', '3') ('7', '3', '3', '4') ('7', '3', '3', '5') ('7', '3', '3', '6') ('7', '3', '3', '7') ('7', '3', '3', '8') ('7', '3', '3', '9') ('7', '3', '4', '0') ('7', '3', '4', '1') ('7', '3', '4', '2') ('7', '3', '4', '3') ('7', '3', '4', '4') ('7', '3', '4', '5') ('7', '3', '4', '6') ('7', '3', '4', '7') ('7', '3', '4', '8') ('7', '3', '4', '9') ('7', '3', '5', '0') ('7', '3', '5', '1') ('7', '3', '5', '2') ('7', '3', '5', '3') ('7', '3', '5', '4') ('7', '3', '5', '5') ('7', '3', '5', '6') ('7', '3', '5', '7') ('7', '3', '5', '8') ('7', '3', '5', '9') ('7', '3', '6', '0') ('7', '3', '6', '1') ('7', '3', '6', '2') ('7', '3', '6', '3') ('7', '3', '6', '4') ('7', '3', '6', '5') ('7', '3', '6', '6') ('7', '3', '6', '7') ('7', '3', '6', '8') ('7', '3', '6', '9') ('7', '3', '7', '0') ('7', '3', '7', '1') ('7', '3', '7', '2') ('7', '3', '7', '3') ('7', '3', '7', '4') ('7', '3', '7', '5') ('7', '3', '7', '6') ('7', '3', '7', '7') ('7', '3', '7', '8') ('7', '3', '7', '9') ('7', '3', '8', '0') ('7', '3', '8', '1') ('7', '3', '8', '2') ('7', '3', '8', '3') ('7', '3', '8', '4') ('7', '3', '8', '5') ('7', '3', '8', '6') ('7', '3', '8', '7') ('7', '3', '8', '8') ('7', '3', '8', '9') ('7', '3', '9', '0') ('7', '3', '9', '1') ('7', '3', '9', '2') ('7', '3', '9', '3') ('7', '3', '9', '4') ('7', '3', '9', '5') ('7', '3', '9', '6') ('7', '3', '9', '7') ('7', '3', '9', '8') ('7', '3', '9', '9') ('7', '4', '0', '0') ('7', '4', '0', '1') ('7', '4', '0', '2') ('7', '4', '0', '3') ('7', '4', '0', '4') ('7', '4', '0', '5') ('7', '4', '0', '6') ('7', '4', '0', '7') ('7', '4', '0', '8') ('7', '4', '0', '9') ('7', '4', '1', '0') ('7', '4', '1', '1') ('7', '4', '1', '2') ('7', '4', '1', '3') ('7', '4', '1', '4') ('7', '4', '1', '5') ('7', '4', '1', '6') ('7', '4', '1', '7') ('7', '4', '1', '8') ('7', '4', '1', '9') ('7', '4', '2', '0') ('7', '4', '2', '1') ('7', '4', '2', '2') ('7', '4', '2', '3') ('7', '4', '2', '4') ('7', '4', '2', '5') ('7', '4', '2', '6') ('7', '4', '2', '7') ('7', '4', '2', '8') ('7', '4', '2', '9') ('7', '4', '3', '0') ('7', '4', '3', '1') ('7', '4', '3', '2') ('7', '4', '3', '3') ('7', '4', '3', '4') ('7', '4', '3', '5') ('7', '4', '3', '6') ('7', '4', '3', '7') ('7', '4', '3', '8') ('7', '4', '3', '9') ('7', '4', '4', '0') ('7', '4', '4', '1') ('7', '4', '4', '2') ('7', '4', '4', '3') ('7', '4', '4', '4') ('7', '4', '4', '5') ('7', '4', '4', '6') ('7', '4', '4', '7') ('7', '4', '4', '8') ('7', '4', '4', '9') ('7', '4', '5', '0') ('7', '4', '5', '1') ('7', '4', '5', '2') ('7', '4', '5', '3') ('7', '4', '5', '4') ('7', '4', '5', '5') ('7', '4', '5', '6') ('7', '4', '5', '7') ('7', '4', '5', '8') ('7', '4', '5', '9') ('7', '4', '6', '0') ('7', '4', '6', '1') ('7', '4', '6', '2') ('7', '4', '6', '3') ('7', '4', '6', '4') ('7', '4', '6', '5') ('7', '4', '6', '6') ('7', '4', '6', '7') ('7', '4', '6', '8') ('7', '4', '6', '9') ('7', '4', '7', '0') ('7', '4', '7', '1') ('7', '4', '7', '2') ('7', '4', '7', '3') ('7', '4', '7', '4') ('7', '4', '7', '5') ('7', '4', '7', '6') ('7', '4', '7', '7') ('7', '4', '7', '8') ('7', '4', '7', '9') ('7', '4', '8', '0') ('7', '4', '8', '1') ('7', '4', '8', '2') ('7', '4', '8', '3') ('7', '4', '8', '4') ('7', '4', '8', '5') ('7', '4', '8', '6') ('7', '4', '8', '7') ('7', '4', '8', '8') ('7', '4', '8', '9') ('7', '4', '9', '0') ('7', '4', '9', '1') ('7', '4', '9', '2') ('7', '4', '9', '3') ('7', '4', '9', '4') ('7', '4', '9', '5') ('7', '4', '9', '6') ('7', '4', '9', '7') ('7', '4', '9', '8') ('7', '4', '9', '9') ('7', '5', '0', '0') ('7', '5', '0', '1') ('7', '5', '0', '2') ('7', '5', '0', '3') ('7', '5', '0', '4') ('7', '5', '0', '5') ('7', '5', '0', '6') ('7', '5', '0', '7') ('7', '5', '0', '8') ('7', '5', '0', '9') ('7', '5', '1', '0') ('7', '5', '1', '1') ('7', '5', '1', '2') ('7', '5', '1', '3') ('7', '5', '1', '4') ('7', '5', '1', '5') ('7', '5', '1', '6') ('7', '5', '1', '7') ('7', '5', '1', '8') ('7', '5', '1', '9') ('7', '5', '2', '0') ('7', '5', '2', '1') ('7', '5', '2', '2') ('7', '5', '2', '3') ('7', '5', '2', '4') ('7', '5', '2', '5') ('7', '5', '2', '6') ('7', '5', '2', '7') ('7', '5', '2', '8') ('7', '5', '2', '9') ('7', '5', '3', '0') ('7', '5', '3', '1') ('7', '5', '3', '2') ('7', '5', '3', '3') ('7', '5', '3', '4') ('7', '5', '3', '5') ('7', '5', '3', '6') ('7', '5', '3', '7') ('7', '5', '3', '8') ('7', '5', '3', '9') ('7', '5', '4', '0') ('7', '5', '4', '1') ('7', '5', '4', '2') ('7', '5', '4', '3') ('7', '5', '4', '4') ('7', '5', '4', '5') ('7', '5', '4', '6') ('7', '5', '4', '7') ('7', '5', '4', '8') ('7', '5', '4', '9') ('7', '5', '5', '0') ('7', '5', '5', '1') ('7', '5', '5', '2') ('7', '5', '5', '3') ('7', '5', '5', '4') ('7', '5', '5', '5') ('7', '5', '5', '6') ('7', '5', '5', '7') ('7', '5', '5', '8') ('7', '5', '5', '9') ('7', '5', '6', '0') ('7', '5', '6', '1') ('7', '5', '6', '2') ('7', '5', '6', '3') ('7', '5', '6', '4') ('7', '5', '6', '5') ('7', '5', '6', '6') ('7', '5', '6', '7') ('7', '5', '6', '8') ('7', '5', '6', '9') ('7', '5', '7', '0') ('7', '5', '7', '1') ('7', '5', '7', '2') ('7', '5', '7', '3') ('7', '5', '7', '4') ('7', '5', '7', '5') ('7', '5', '7', '6') ('7', '5', '7', '7') ('7', '5', '7', '8') ('7', '5', '7', '9') ('7', '5', '8', '0') ('7', '5', '8', '1') ('7', '5', '8', '2') ('7', '5', '8', '3') ('7', '5', '8', '4') ('7', '5', '8', '5') ('7', '5', '8', '6') ('7', '5', '8', '7') ('7', '5', '8', '8') ('7', '5', '8', '9') ('7', '5', '9', '0') ('7', '5', '9', '1') ('7', '5', '9', '2') ('7', '5', '9', '3') ('7', '5', '9', '4') ('7', '5', '9', '5') ('7', '5', '9', '6') ('7', '5', '9', '7') ('7', '5', '9', '8') ('7', '5', '9', '9') ('7', '6', '0', '0') ('7', '6', '0', '1') ('7', '6', '0', '2') ('7', '6', '0', '3') ('7', '6', '0', '4') ('7', '6', '0', '5') ('7', '6', '0', '6') ('7', '6', '0', '7') ('7', '6', '0', '8') ('7', '6', '0', '9') ('7', '6', '1', '0') ('7', '6', '1', '1') ('7', '6', '1', '2') ('7', '6', '1', '3') ('7', '6', '1', '4') ('7', '6', '1', '5') ('7', '6', '1', '6') ('7', '6', '1', '7') ('7', '6', '1', '8') ('7', '6', '1', '9') ('7', '6', '2', '0') ('7', '6', '2', '1') ('7', '6', '2', '2') ('7', '6', '2', '3') ('7', '6', '2', '4') ('7', '6', '2', '5') ('7', '6', '2', '6') ('7', '6', '2', '7') ('7', '6', '2', '8') ('7', '6', '2', '9') ('7', '6', '3', '0') ('7', '6', '3', '1') ('7', '6', '3', '2') ('7', '6', '3', '3') ('7', '6', '3', '4') ('7', '6', '3', '5') ('7', '6', '3', '6') ('7', '6', '3', '7') ('7', '6', '3', '8') ('7', '6', '3', '9') ('7', '6', '4', '0') ('7', '6', '4', '1') ('7', '6', '4', '2') ('7', '6', '4', '3') ('7', '6', '4', '4') ('7', '6', '4', '5') ('7', '6', '4', '6') ('7', '6', '4', '7') ('7', '6', '4', '8') ('7', '6', '4', '9') ('7', '6', '5', '0') ('7', '6', '5', '1') ('7', '6', '5', '2') ('7', '6', '5', '3') ('7', '6', '5', '4') ('7', '6', '5', '5') ('7', '6', '5', '6') ('7', '6', '5', '7') ('7', '6', '5', '8') ('7', '6', '5', '9') ('7', '6', '6', '0') ('7', '6', '6', '1') ('7', '6', '6', '2') ('7', '6', '6', '3') ('7', '6', '6', '4') ('7', '6', '6', '5') ('7', '6', '6', '6') ('7', '6', '6', '7') ('7', '6', '6', '8') ('7', '6', '6', '9') ('7', '6', '7', '0') ('7', '6', '7', '1') ('7', '6', '7', '2') ('7', '6', '7', '3') ('7', '6', '7', '4') ('7', '6', '7', '5') ('7', '6', '7', '6') ('7', '6', '7', '7') ('7', '6', '7', '8') ('7', '6', '7', '9') ('7', '6', '8', '0') ('7', '6', '8', '1') ('7', '6', '8', '2') ('7', '6', '8', '3') ('7', '6', '8', '4') ('7', '6', '8', '5') ('7', '6', '8', '6') ('7', '6', '8', '7') ('7', '6', '8', '8') ('7', '6', '8', '9') ('7', '6', '9', '0') ('7', '6', '9', '1') ('7', '6', '9', '2') ('7', '6', '9', '3') ('7', '6', '9', '4') ('7', '6', '9', '5') ('7', '6', '9', '6') ('7', '6', '9', '7') ('7', '6', '9', '8') ('7', '6', '9', '9') ('7', '7', '0', '0') ('7', '7', '0', '1') ('7', '7', '0', '2') ('7', '7', '0', '3') ('7', '7', '0', '4') ('7', '7', '0', '5') ('7', '7', '0', '6') ('7', '7', '0', '7') ('7', '7', '0', '8') ('7', '7', '0', '9') ('7', '7', '1', '0') ('7', '7', '1', '1') ('7', '7', '1', '2') ('7', '7', '1', '3') ('7', '7', '1', '4') ('7', '7', '1', '5') ('7', '7', '1', '6') ('7', '7', '1', '7') ('7', '7', '1', '8') ('7', '7', '1', '9') ('7', '7', '2', '0') ('7', '7', '2', '1') ('7', '7', '2', '2') ('7', '7', '2', '3') ('7', '7', '2', '4') ('7', '7', '2', '5') ('7', '7', '2', '6') ('7', '7', '2', '7') ('7', '7', '2', '8') ('7', '7', '2', '9') ('7', '7', '3', '0') ('7', '7', '3', '1') ('7', '7', '3', '2') ('7', '7', '3', '3') ('7', '7', '3', '4') ('7', '7', '3', '5') ('7', '7', '3', '6') ('7', '7', '3', '7') ('7', '7', '3', '8') ('7', '7', '3', '9') ('7', '7', '4', '0') ('7', '7', '4', '1') ('7', '7', '4', '2') ('7', '7', '4', '3') ('7', '7', '4', '4') ('7', '7', '4', '5') ('7', '7', '4', '6') ('7', '7', '4', '7') ('7', '7', '4', '8') ('7', '7', '4', '9') ('7', '7', '5', '0') ('7', '7', '5', '1') ('7', '7', '5', '2') ('7', '7', '5', '3') ('7', '7', '5', '4') ('7', '7', '5', '5') ('7', '7', '5', '6') ('7', '7', '5', '7') ('7', '7', '5', '8') ('7', '7', '5', '9') ('7', '7', '6', '0') ('7', '7', '6', '1') ('7', '7', '6', '2') ('7', '7', '6', '3') ('7', '7', '6', '4') ('7', '7', '6', '5') ('7', '7', '6', '6') ('7', '7', '6', '7') ('7', '7', '6', '8') ('7', '7', '6', '9') ('7', '7', '7', '0') ('7', '7', '7', '1') ('7', '7', '7', '2') ('7', '7', '7', '3') ('7', '7', '7', '4') ('7', '7', '7', '5') ('7', '7', '7', '6') ('7', '7', '7', '7') ('7', '7', '7', '8') ('7', '7', '7', '9') ('7', '7', '8', '0') ('7', '7', '8', '1') ('7', '7', '8', '2') ('7', '7', '8', '3') ('7', '7', '8', '4') ('7', '7', '8', '5') ('7', '7', '8', '6') ('7', '7', '8', '7') ('7', '7', '8', '8') ('7', '7', '8', '9') ('7', '7', '9', '0') ('7', '7', '9', '1') ('7', '7', '9', '2') ('7', '7', '9', '3') ('7', '7', '9', '4') ('7', '7', '9', '5') ('7', '7', '9', '6') ('7', '7', '9', '7') ('7', '7', '9', '8') ('7', '7', '9', '9') ('7', '8', '0', '0') ('7', '8', '0', '1') ('7', '8', '0', '2') ('7', '8', '0', '3') ('7', '8', '0', '4') ('7', '8', '0', '5') ('7', '8', '0', '6') ('7', '8', '0', '7') ('7', '8', '0', '8') ('7', '8', '0', '9') ('7', '8', '1', '0') ('7', '8', '1', '1') ('7', '8', '1', '2') ('7', '8', '1', '3') ('7', '8', '1', '4') ('7', '8', '1', '5') ('7', '8', '1', '6') ('7', '8', '1', '7') ('7', '8', '1', '8') ('7', '8', '1', '9') ('7', '8', '2', '0') ('7', '8', '2', '1') ('7', '8', '2', '2') ('7', '8', '2', '3') ('7', '8', '2', '4') ('7', '8', '2', '5') ('7', '8', '2', '6') ('7', '8', '2', '7') ('7', '8', '2', '8') ('7', '8', '2', '9') ('7', '8', '3', '0') ('7', '8', '3', '1') ('7', '8', '3', '2') ('7', '8', '3', '3') ('7', '8', '3', '4') ('7', '8', '3', '5') ('7', '8', '3', '6') ('7', '8', '3', '7') ('7', '8', '3', '8') ('7', '8', '3', '9') ('7', '8', '4', '0') ('7', '8', '4', '1') ('7', '8', '4', '2') ('7', '8', '4', '3') ('7', '8', '4', '4') ('7', '8', '4', '5') ('7', '8', '4', '6') ('7', '8', '4', '7') ('7', '8', '4', '8') ('7', '8', '4', '9') ('7', '8', '5', '0') ('7', '8', '5', '1') ('7', '8', '5', '2') ('7', '8', '5', '3') ('7', '8', '5', '4') ('7', '8', '5', '5') ('7', '8', '5', '6') ('7', '8', '5', '7') ('7', '8', '5', '8') ('7', '8', '5', '9') ('7', '8', '6', '0') ('7', '8', '6', '1') ('7', '8', '6', '2') ('7', '8', '6', '3') ('7', '8', '6', '4') ('7', '8', '6', '5') ('7', '8', '6', '6') ('7', '8', '6', '7') ('7', '8', '6', '8') ('7', '8', '6', '9') ('7', '8', '7', '0') ('7', '8', '7', '1') ('7', '8', '7', '2') ('7', '8', '7', '3') ('7', '8', '7', '4') ('7', '8', '7', '5') ('7', '8', '7', '6') ('7', '8', '7', '7') ('7', '8', '7', '8') ('7', '8', '7', '9') ('7', '8', '8', '0') ('7', '8', '8', '1') ('7', '8', '8', '2') ('7', '8', '8', '3') ('7', '8', '8', '4') ('7', '8', '8', '5') ('7', '8', '8', '6') ('7', '8', '8', '7') ('7', '8', '8', '8') ('7', '8', '8', '9') ('7', '8', '9', '0') ('7', '8', '9', '1') ('7', '8', '9', '2') ('7', '8', '9', '3') ('7', '8', '9', '4') ('7', '8', '9', '5') ('7', '8', '9', '6') ('7', '8', '9', '7') ('7', '8', '9', '8') ('7', '8', '9', '9') ('7', '9', '0', '0') ('7', '9', '0', '1') ('7', '9', '0', '2') ('7', '9', '0', '3') ('7', '9', '0', '4') ('7', '9', '0', '5') ('7', '9', '0', '6') ('7', '9', '0', '7') ('7', '9', '0', '8') ('7', '9', '0', '9') ('7', '9', '1', '0') ('7', '9', '1', '1') ('7', '9', '1', '2') ('7', '9', '1', '3') ('7', '9', '1', '4') ('7', '9', '1', '5') ('7', '9', '1', '6') ('7', '9', '1', '7') ('7', '9', '1', '8') ('7', '9', '1', '9') ('7', '9', '2', '0') ('7', '9', '2', '1') ('7', '9', '2', '2') ('7', '9', '2', '3') ('7', '9', '2', '4') ('7', '9', '2', '5') ('7', '9', '2', '6') ('7', '9', '2', '7') ('7', '9', '2', '8') ('7', '9', '2', '9') ('7', '9', '3', '0') ('7', '9', '3', '1') ('7', '9', '3', '2') ('7', '9', '3', '3') ('7', '9', '3', '4') ('7', '9', '3', '5') ('7', '9', '3', '6') ('7', '9', '3', '7') ('7', '9', '3', '8') ('7', '9', '3', '9') ('7', '9', '4', '0') ('7', '9', '4', '1') ('7', '9', '4', '2') ('7', '9', '4', '3') ('7', '9', '4', '4') ('7', '9', '4', '5') ('7', '9', '4', '6') ('7', '9', '4', '7') ('7', '9', '4', '8') ('7', '9', '4', '9') ('7', '9', '5', '0') ('7', '9', '5', '1') ('7', '9', '5', '2') ('7', '9', '5', '3') ('7', '9', '5', '4') ('7', '9', '5', '5') ('7', '9', '5', '6') ('7', '9', '5', '7') ('7', '9', '5', '8') ('7', '9', '5', '9') ('7', '9', '6', '0') ('7', '9', '6', '1') ('7', '9', '6', '2') ('7', '9', '6', '3') ('7', '9', '6', '4') ('7', '9', '6', '5') ('7', '9', '6', '6') ('7', '9', '6', '7') ('7', '9', '6', '8') ('7', '9', '6', '9') ('7', '9', '7', '0') ('7', '9', '7', '1') ('7', '9', '7', '2') ('7', '9', '7', '3') ('7', '9', '7', '4') ('7', '9', '7', '5') ('7', '9', '7', '6') ('7', '9', '7', '7') ('7', '9', '7', '8') ('7', '9', '7', '9') ('7', '9', '8', '0') ('7', '9', '8', '1') ('7', '9', '8', '2') ('7', '9', '8', '3') ('7', '9', '8', '4') ('7', '9', '8', '5') ('7', '9', '8', '6') ('7', '9', '8', '7') ('7', '9', '8', '8') ('7', '9', '8', '9') ('7', '9', '9', '0') ('7', '9', '9', '1') ('7', '9', '9', '2') ('7', '9', '9', '3') ('7', '9', '9', '4') ('7', '9', '9', '5') ('7', '9', '9', '6') ('7', '9', '9', '7') ('7', '9', '9', '8') ('7', '9', '9', '9') ('8', '0', '0', '0') ('8', '0', '0', '1') ('8', '0', '0', '2') ('8', '0', '0', '3') ('8', '0', '0', '4') ('8', '0', '0', '5') ('8', '0', '0', '6') ('8', '0', '0', '7') ('8', '0', '0', '8') ('8', '0', '0', '9') ('8', '0', '1', '0') ('8', '0', '1', '1') ('8', '0', '1', '2') ('8', '0', '1', '3') ('8', '0', '1', '4') ('8', '0', '1', '5') ('8', '0', '1', '6') ('8', '0', '1', '7') ('8', '0', '1', '8') ('8', '0', '1', '9') ('8', '0', '2', '0') ('8', '0', '2', '1') ('8', '0', '2', '2') ('8', '0', '2', '3') ('8', '0', '2', '4') ('8', '0', '2', '5') ('8', '0', '2', '6') ('8', '0', '2', '7') ('8', '0', '2', '8') ('8', '0', '2', '9') ('8', '0', '3', '0') ('8', '0', '3', '1') ('8', '0', '3', '2') ('8', '0', '3', '3') ('8', '0', '3', '4') ('8', '0', '3', '5') ('8', '0', '3', '6') ('8', '0', '3', '7') ('8', '0', '3', '8') ('8', '0', '3', '9') ('8', '0', '4', '0') ('8', '0', '4', '1') ('8', '0', '4', '2') ('8', '0', '4', '3') ('8', '0', '4', '4') ('8', '0', '4', '5') ('8', '0', '4', '6') ('8', '0', '4', '7') ('8', '0', '4', '8') ('8', '0', '4', '9') ('8', '0', '5', '0') ('8', '0', '5', '1') ('8', '0', '5', '2') ('8', '0', '5', '3') ('8', '0', '5', '4') ('8', '0', '5', '5') ('8', '0', '5', '6') ('8', '0', '5', '7') ('8', '0', '5', '8') ('8', '0', '5', '9') ('8', '0', '6', '0') ('8', '0', '6', '1') ('8', '0', '6', '2') ('8', '0', '6', '3') ('8', '0', '6', '4') ('8', '0', '6', '5') ('8', '0', '6', '6') ('8', '0', '6', '7') ('8', '0', '6', '8') ('8', '0', '6', '9') ('8', '0', '7', '0') ('8', '0', '7', '1') ('8', '0', '7', '2') ('8', '0', '7', '3') ('8', '0', '7', '4') ('8', '0', '7', '5') ('8', '0', '7', '6') ('8', '0', '7', '7') ('8', '0', '7', '8') ('8', '0', '7', '9') ('8', '0', '8', '0') ('8', '0', '8', '1') ('8', '0', '8', '2') ('8', '0', '8', '3') ('8', '0', '8', '4') ('8', '0', '8', '5') ('8', '0', '8', '6') ('8', '0', '8', '7') ('8', '0', '8', '8') ('8', '0', '8', '9') ('8', '0', '9', '0') ('8', '0', '9', '1') ('8', '0', '9', '2') ('8', '0', '9', '3') ('8', '0', '9', '4') ('8', '0', '9', '5') ('8', '0', '9', '6') ('8', '0', '9', '7') ('8', '0', '9', '8') ('8', '0', '9', '9') ('8', '1', '0', '0') ('8', '1', '0', '1') ('8', '1', '0', '2') ('8', '1', '0', '3') ('8', '1', '0', '4') ('8', '1', '0', '5') ('8', '1', '0', '6') ('8', '1', '0', '7') ('8', '1', '0', '8') ('8', '1', '0', '9') ('8', '1', '1', '0') ('8', '1', '1', '1') ('8', '1', '1', '2') ('8', '1', '1', '3') ('8', '1', '1', '4') ('8', '1', '1', '5') ('8', '1', '1', '6') ('8', '1', '1', '7') ('8', '1', '1', '8') ('8', '1', '1', '9') ('8', '1', '2', '0') ('8', '1', '2', '1') ('8', '1', '2', '2') ('8', '1', '2', '3') ('8', '1', '2', '4') ('8', '1', '2', '5') ('8', '1', '2', '6') ('8', '1', '2', '7') ('8', '1', '2', '8') ('8', '1', '2', '9') ('8', '1', '3', '0') ('8', '1', '3', '1') ('8', '1', '3', '2') ('8', '1', '3', '3') ('8', '1', '3', '4') ('8', '1', '3', '5') ('8', '1', '3', '6') ('8', '1', '3', '7') ('8', '1', '3', '8') ('8', '1', '3', '9') ('8', '1', '4', '0') ('8', '1', '4', '1') ('8', '1', '4', '2') ('8', '1', '4', '3') ('8', '1', '4', '4') ('8', '1', '4', '5') ('8', '1', '4', '6') ('8', '1', '4', '7') ('8', '1', '4', '8') ('8', '1', '4', '9') ('8', '1', '5', '0') ('8', '1', '5', '1') ('8', '1', '5', '2') ('8', '1', '5', '3') ('8', '1', '5', '4') ('8', '1', '5', '5') ('8', '1', '5', '6') ('8', '1', '5', '7') ('8', '1', '5', '8') ('8', '1', '5', '9') ('8', '1', '6', '0') ('8', '1', '6', '1') ('8', '1', '6', '2') ('8', '1', '6', '3') ('8', '1', '6', '4') ('8', '1', '6', '5') ('8', '1', '6', '6') ('8', '1', '6', '7') ('8', '1', '6', '8') ('8', '1', '6', '9') ('8', '1', '7', '0') ('8', '1', '7', '1') ('8', '1', '7', '2') ('8', '1', '7', '3') ('8', '1', '7', '4') ('8', '1', '7', '5') ('8', '1', '7', '6') ('8', '1', '7', '7') ('8', '1', '7', '8') ('8', '1', '7', '9') ('8', '1', '8', '0') ('8', '1', '8', '1') ('8', '1', '8', '2') ('8', '1', '8', '3') ('8', '1', '8', '4') ('8', '1', '8', '5') ('8', '1', '8', '6') ('8', '1', '8', '7') ('8', '1', '8', '8') ('8', '1', '8', '9') ('8', '1', '9', '0') ('8', '1', '9', '1') ('8', '1', '9', '2') ('8', '1', '9', '3') ('8', '1', '9', '4') ('8', '1', '9', '5') ('8', '1', '9', '6') ('8', '1', '9', '7') ('8', '1', '9', '8') ('8', '1', '9', '9') ('8', '2', '0', '0') ('8', '2', '0', '1') ('8', '2', '0', '2') ('8', '2', '0', '3') ('8', '2', '0', '4') ('8', '2', '0', '5') ('8', '2', '0', '6') ('8', '2', '0', '7') ('8', '2', '0', '8') ('8', '2', '0', '9') ('8', '2', '1', '0') ('8', '2', '1', '1') ('8', '2', '1', '2') ('8', '2', '1', '3') ('8', '2', '1', '4') ('8', '2', '1', '5') ('8', '2', '1', '6') ('8', '2', '1', '7') ('8', '2', '1', '8') ('8', '2', '1', '9') ('8', '2', '2', '0') ('8', '2', '2', '1') ('8', '2', '2', '2') ('8', '2', '2', '3') ('8', '2', '2', '4') ('8', '2', '2', '5') ('8', '2', '2', '6') ('8', '2', '2', '7') ('8', '2', '2', '8') ('8', '2', '2', '9') ('8', '2', '3', '0') ('8', '2', '3', '1') ('8', '2', '3', '2') ('8', '2', '3', '3') ('8', '2', '3', '4') ('8', '2', '3', '5') ('8', '2', '3', '6') ('8', '2', '3', '7') ('8', '2', '3', '8') ('8', '2', '3', '9') ('8', '2', '4', '0') ('8', '2', '4', '1') ('8', '2', '4', '2') ('8', '2', '4', '3') ('8', '2', '4', '4') ('8', '2', '4', '5') ('8', '2', '4', '6') ('8', '2', '4', '7') ('8', '2', '4', '8') ('8', '2', '4', '9') ('8', '2', '5', '0') ('8', '2', '5', '1') ('8', '2', '5', '2') ('8', '2', '5', '3') ('8', '2', '5', '4') ('8', '2', '5', '5') ('8', '2', '5', '6') ('8', '2', '5', '7') ('8', '2', '5', '8') ('8', '2', '5', '9') ('8', '2', '6', '0') ('8', '2', '6', '1') ('8', '2', '6', '2') ('8', '2', '6', '3') ('8', '2', '6', '4') ('8', '2', '6', '5') ('8', '2', '6', '6') ('8', '2', '6', '7') ('8', '2', '6', '8') ('8', '2', '6', '9') ('8', '2', '7', '0') ('8', '2', '7', '1') ('8', '2', '7', '2') ('8', '2', '7', '3') ('8', '2', '7', '4') ('8', '2', '7', '5') ('8', '2', '7', '6') ('8', '2', '7', '7') ('8', '2', '7', '8') ('8', '2', '7', '9') ('8', '2', '8', '0') ('8', '2', '8', '1') ('8', '2', '8', '2') ('8', '2', '8', '3') ('8', '2', '8', '4') ('8', '2', '8', '5') ('8', '2', '8', '6') ('8', '2', '8', '7') ('8', '2', '8', '8') ('8', '2', '8', '9') ('8', '2', '9', '0') ('8', '2', '9', '1') ('8', '2', '9', '2') ('8', '2', '9', '3') ('8', '2', '9', '4') ('8', '2', '9', '5') ('8', '2', '9', '6') ('8', '2', '9', '7') ('8', '2', '9', '8') ('8', '2', '9', '9') ('8', '3', '0', '0') ('8', '3', '0', '1') ('8', '3', '0', '2') ('8', '3', '0', '3') ('8', '3', '0', '4') ('8', '3', '0', '5') ('8', '3', '0', '6') ('8', '3', '0', '7') ('8', '3', '0', '8') ('8', '3', '0', '9') ('8', '3', '1', '0') ('8', '3', '1', '1') ('8', '3', '1', '2') ('8', '3', '1', '3') ('8', '3', '1', '4') ('8', '3', '1', '5') ('8', '3', '1', '6') ('8', '3', '1', '7') ('8', '3', '1', '8') ('8', '3', '1', '9') ('8', '3', '2', '0') ('8', '3', '2', '1') ('8', '3', '2', '2') ('8', '3', '2', '3') ('8', '3', '2', '4') ('8', '3', '2', '5') ('8', '3', '2', '6') ('8', '3', '2', '7') ('8', '3', '2', '8') ('8', '3', '2', '9') ('8', '3', '3', '0') ('8', '3', '3', '1') ('8', '3', '3', '2') ('8', '3', '3', '3') ('8', '3', '3', '4') ('8', '3', '3', '5') ('8', '3', '3', '6') ('8', '3', '3', '7') ('8', '3', '3', '8') ('8', '3', '3', '9') ('8', '3', '4', '0') ('8', '3', '4', '1') ('8', '3', '4', '2') ('8', '3', '4', '3') ('8', '3', '4', '4') ('8', '3', '4', '5') ('8', '3', '4', '6') ('8', '3', '4', '7') ('8', '3', '4', '8') ('8', '3', '4', '9') ('8', '3', '5', '0') ('8', '3', '5', '1') ('8', '3', '5', '2') ('8', '3', '5', '3') ('8', '3', '5', '4') ('8', '3', '5', '5') ('8', '3', '5', '6') ('8', '3', '5', '7') ('8', '3', '5', '8') ('8', '3', '5', '9') ('8', '3', '6', '0') ('8', '3', '6', '1') ('8', '3', '6', '2') ('8', '3', '6', '3') ('8', '3', '6', '4') ('8', '3', '6', '5') ('8', '3', '6', '6') ('8', '3', '6', '7') ('8', '3', '6', '8') ('8', '3', '6', '9') ('8', '3', '7', '0') ('8', '3', '7', '1') ('8', '3', '7', '2') ('8', '3', '7', '3') ('8', '3', '7', '4') ('8', '3', '7', '5') ('8', '3', '7', '6') ('8', '3', '7', '7') ('8', '3', '7', '8') ('8', '3', '7', '9') ('8', '3', '8', '0') ('8', '3', '8', '1') ('8', '3', '8', '2') ('8', '3', '8', '3') ('8', '3', '8', '4') ('8', '3', '8', '5') ('8', '3', '8', '6') ('8', '3', '8', '7') ('8', '3', '8', '8') ('8', '3', '8', '9') ('8', '3', '9', '0') ('8', '3', '9', '1') ('8', '3', '9', '2') ('8', '3', '9', '3') ('8', '3', '9', '4') ('8', '3', '9', '5') ('8', '3', '9', '6') ('8', '3', '9', '7') ('8', '3', '9', '8') ('8', '3', '9', '9') ('8', '4', '0', '0') ('8', '4', '0', '1') ('8', '4', '0', '2') ('8', '4', '0', '3') ('8', '4', '0', '4') ('8', '4', '0', '5') ('8', '4', '0', '6') ('8', '4', '0', '7') ('8', '4', '0', '8') ('8', '4', '0', '9') ('8', '4', '1', '0') ('8', '4', '1', '1') ('8', '4', '1', '2') ('8', '4', '1', '3') ('8', '4', '1', '4') ('8', '4', '1', '5') ('8', '4', '1', '6') ('8', '4', '1', '7') ('8', '4', '1', '8') ('8', '4', '1', '9') ('8', '4', '2', '0') ('8', '4', '2', '1') ('8', '4', '2', '2') ('8', '4', '2', '3') ('8', '4', '2', '4') ('8', '4', '2', '5') ('8', '4', '2', '6') ('8', '4', '2', '7') ('8', '4', '2', '8') ('8', '4', '2', '9') ('8', '4', '3', '0') ('8', '4', '3', '1') ('8', '4', '3', '2') ('8', '4', '3', '3') ('8', '4', '3', '4') ('8', '4', '3', '5') ('8', '4', '3', '6') ('8', '4', '3', '7') ('8', '4', '3', '8') ('8', '4', '3', '9') ('8', '4', '4', '0') ('8', '4', '4', '1') ('8', '4', '4', '2') ('8', '4', '4', '3') ('8', '4', '4', '4') ('8', '4', '4', '5') ('8', '4', '4', '6') ('8', '4', '4', '7') ('8', '4', '4', '8') ('8', '4', '4', '9') ('8', '4', '5', '0') ('8', '4', '5', '1') ('8', '4', '5', '2') ('8', '4', '5', '3') ('8', '4', '5', '4') ('8', '4', '5', '5') ('8', '4', '5', '6') ('8', '4', '5', '7') ('8', '4', '5', '8') ('8', '4', '5', '9') ('8', '4', '6', '0') ('8', '4', '6', '1') ('8', '4', '6', '2') ('8', '4', '6', '3') ('8', '4', '6', '4') ('8', '4', '6', '5') ('8', '4', '6', '6') ('8', '4', '6', '7') ('8', '4', '6', '8') ('8', '4', '6', '9') ('8', '4', '7', '0') ('8', '4', '7', '1') ('8', '4', '7', '2') ('8', '4', '7', '3') ('8', '4', '7', '4') ('8', '4', '7', '5') ('8', '4', '7', '6') ('8', '4', '7', '7') ('8', '4', '7', '8') ('8', '4', '7', '9') ('8', '4', '8', '0') ('8', '4', '8', '1') ('8', '4', '8', '2') ('8', '4', '8', '3') ('8', '4', '8', '4') ('8', '4', '8', '5') ('8', '4', '8', '6') ('8', '4', '8', '7') ('8', '4', '8', '8') ('8', '4', '8', '9') ('8', '4', '9', '0') ('8', '4', '9', '1') ('8', '4', '9', '2') ('8', '4', '9', '3') ('8', '4', '9', '4') ('8', '4', '9', '5') ('8', '4', '9', '6') ('8', '4', '9', '7') ('8', '4', '9', '8') ('8', '4', '9', '9') ('8', '5', '0', '0') ('8', '5', '0', '1') ('8', '5', '0', '2') ('8', '5', '0', '3') ('8', '5', '0', '4') ('8', '5', '0', '5') ('8', '5', '0', '6') ('8', '5', '0', '7') ('8', '5', '0', '8') ('8', '5', '0', '9') ('8', '5', '1', '0') ('8', '5', '1', '1') ('8', '5', '1', '2') ('8', '5', '1', '3') ('8', '5', '1', '4') ('8', '5', '1', '5') ('8', '5', '1', '6') ('8', '5', '1', '7') ('8', '5', '1', '8') ('8', '5', '1', '9') ('8', '5', '2', '0') ('8', '5', '2', '1') ('8', '5', '2', '2') ('8', '5', '2', '3') ('8', '5', '2', '4') ('8', '5', '2', '5') ('8', '5', '2', '6') ('8', '5', '2', '7') ('8', '5', '2', '8') ('8', '5', '2', '9') ('8', '5', '3', '0') ('8', '5', '3', '1') ('8', '5', '3', '2') ('8', '5', '3', '3') ('8', '5', '3', '4') ('8', '5', '3', '5') ('8', '5', '3', '6') ('8', '5', '3', '7') ('8', '5', '3', '8') ('8', '5', '3', '9') ('8', '5', '4', '0') ('8', '5', '4', '1') ('8', '5', '4', '2') ('8', '5', '4', '3') ('8', '5', '4', '4') ('8', '5', '4', '5') ('8', '5', '4', '6') ('8', '5', '4', '7') ('8', '5', '4', '8') ('8', '5', '4', '9') ('8', '5', '5', '0') ('8', '5', '5', '1') ('8', '5', '5', '2') ('8', '5', '5', '3') ('8', '5', '5', '4') ('8', '5', '5', '5') ('8', '5', '5', '6') ('8', '5', '5', '7') ('8', '5', '5', '8') ('8', '5', '5', '9') ('8', '5', '6', '0') ('8', '5', '6', '1') ('8', '5', '6', '2') ('8', '5', '6', '3') ('8', '5', '6', '4') ('8', '5', '6', '5') ('8', '5', '6', '6') ('8', '5', '6', '7') ('8', '5', '6', '8') ('8', '5', '6', '9') ('8', '5', '7', '0') ('8', '5', '7', '1') ('8', '5', '7', '2') ('8', '5', '7', '3') ('8', '5', '7', '4') ('8', '5', '7', '5') ('8', '5', '7', '6') ('8', '5', '7', '7') ('8', '5', '7', '8') ('8', '5', '7', '9') ('8', '5', '8', '0') ('8', '5', '8', '1') ('8', '5', '8', '2') ('8', '5', '8', '3') ('8', '5', '8', '4') ('8', '5', '8', '5') ('8', '5', '8', '6') ('8', '5', '8', '7') ('8', '5', '8', '8') ('8', '5', '8', '9') ('8', '5', '9', '0') ('8', '5', '9', '1') ('8', '5', '9', '2') ('8', '5', '9', '3') ('8', '5', '9', '4') ('8', '5', '9', '5') ('8', '5', '9', '6') ('8', '5', '9', '7') ('8', '5', '9', '8') ('8', '5', '9', '9') ('8', '6', '0', '0') ('8', '6', '0', '1') ('8', '6', '0', '2') ('8', '6', '0', '3') ('8', '6', '0', '4') ('8', '6', '0', '5') ('8', '6', '0', '6') ('8', '6', '0', '7') ('8', '6', '0', '8') ('8', '6', '0', '9') ('8', '6', '1', '0') ('8', '6', '1', '1') ('8', '6', '1', '2') ('8', '6', '1', '3') ('8', '6', '1', '4') ('8', '6', '1', '5') ('8', '6', '1', '6') ('8', '6', '1', '7') ('8', '6', '1', '8') ('8', '6', '1', '9') ('8', '6', '2', '0') ('8', '6', '2', '1') ('8', '6', '2', '2') ('8', '6', '2', '3') ('8', '6', '2', '4') ('8', '6', '2', '5') ('8', '6', '2', '6') ('8', '6', '2', '7') ('8', '6', '2', '8') ('8', '6', '2', '9') ('8', '6', '3', '0') ('8', '6', '3', '1') ('8', '6', '3', '2') ('8', '6', '3', '3') ('8', '6', '3', '4') ('8', '6', '3', '5') ('8', '6', '3', '6') ('8', '6', '3', '7') ('8', '6', '3', '8') ('8', '6', '3', '9') ('8', '6', '4', '0') ('8', '6', '4', '1') ('8', '6', '4', '2') ('8', '6', '4', '3') ('8', '6', '4', '4') ('8', '6', '4', '5') ('8', '6', '4', '6') ('8', '6', '4', '7') ('8', '6', '4', '8') ('8', '6', '4', '9') ('8', '6', '5', '0') ('8', '6', '5', '1') ('8', '6', '5', '2') ('8', '6', '5', '3') ('8', '6', '5', '4') ('8', '6', '5', '5') ('8', '6', '5', '6') ('8', '6', '5', '7') ('8', '6', '5', '8') ('8', '6', '5', '9') ('8', '6', '6', '0') ('8', '6', '6', '1') ('8', '6', '6', '2') ('8', '6', '6', '3') ('8', '6', '6', '4') ('8', '6', '6', '5') ('8', '6', '6', '6') ('8', '6', '6', '7') ('8', '6', '6', '8') ('8', '6', '6', '9') ('8', '6', '7', '0') ('8', '6', '7', '1') ('8', '6', '7', '2') ('8', '6', '7', '3') ('8', '6', '7', '4') ('8', '6', '7', '5') ('8', '6', '7', '6') ('8', '6', '7', '7') ('8', '6', '7', '8') ('8', '6', '7', '9') ('8', '6', '8', '0') ('8', '6', '8', '1') ('8', '6', '8', '2') ('8', '6', '8', '3') ('8', '6', '8', '4') ('8', '6', '8', '5') ('8', '6', '8', '6') ('8', '6', '8', '7') ('8', '6', '8', '8') ('8', '6', '8', '9') ('8', '6', '9', '0') ('8', '6', '9', '1') ('8', '6', '9', '2') ('8', '6', '9', '3') ('8', '6', '9', '4') ('8', '6', '9', '5') ('8', '6', '9', '6') ('8', '6', '9', '7') ('8', '6', '9', '8') ('8', '6', '9', '9') ('8', '7', '0', '0') ('8', '7', '0', '1') ('8', '7', '0', '2') ('8', '7', '0', '3') ('8', '7', '0', '4') ('8', '7', '0', '5') ('8', '7', '0', '6') ('8', '7', '0', '7') ('8', '7', '0', '8') ('8', '7', '0', '9') ('8', '7', '1', '0') ('8', '7', '1', '1') ('8', '7', '1', '2') ('8', '7', '1', '3') ('8', '7', '1', '4') ('8', '7', '1', '5') ('8', '7', '1', '6') ('8', '7', '1', '7') ('8', '7', '1', '8') ('8', '7', '1', '9') ('8', '7', '2', '0') ('8', '7', '2', '1') ('8', '7', '2', '2') ('8', '7', '2', '3') ('8', '7', '2', '4') ('8', '7', '2', '5') ('8', '7', '2', '6') ('8', '7', '2', '7') ('8', '7', '2', '8') ('8', '7', '2', '9') ('8', '7', '3', '0') ('8', '7', '3', '1') ('8', '7', '3', '2') ('8', '7', '3', '3') ('8', '7', '3', '4') ('8', '7', '3', '5') ('8', '7', '3', '6') ('8', '7', '3', '7') ('8', '7', '3', '8') ('8', '7', '3', '9') ('8', '7', '4', '0') ('8', '7', '4', '1') ('8', '7', '4', '2') ('8', '7', '4', '3') ('8', '7', '4', '4') ('8', '7', '4', '5') ('8', '7', '4', '6') ('8', '7', '4', '7') ('8', '7', '4', '8') ('8', '7', '4', '9') ('8', '7', '5', '0') ('8', '7', '5', '1') ('8', '7', '5', '2') ('8', '7', '5', '3') ('8', '7', '5', '4') ('8', '7', '5', '5') ('8', '7', '5', '6') ('8', '7', '5', '7') ('8', '7', '5', '8') ('8', '7', '5', '9') ('8', '7', '6', '0') ('8', '7', '6', '1') ('8', '7', '6', '2') ('8', '7', '6', '3') ('8', '7', '6', '4') ('8', '7', '6', '5') ('8', '7', '6', '6') ('8', '7', '6', '7') ('8', '7', '6', '8') ('8', '7', '6', '9') ('8', '7', '7', '0') ('8', '7', '7', '1') ('8', '7', '7', '2') ('8', '7', '7', '3') ('8', '7', '7', '4') ('8', '7', '7', '5') ('8', '7', '7', '6') ('8', '7', '7', '7') ('8', '7', '7', '8') ('8', '7', '7', '9') ('8', '7', '8', '0') ('8', '7', '8', '1') ('8', '7', '8', '2') ('8', '7', '8', '3') ('8', '7', '8', '4') ('8', '7', '8', '5') ('8', '7', '8', '6') ('8', '7', '8', '7') ('8', '7', '8', '8') ('8', '7', '8', '9') ('8', '7', '9', '0') ('8', '7', '9', '1') ('8', '7', '9', '2') ('8', '7', '9', '3') ('8', '7', '9', '4') ('8', '7', '9', '5') ('8', '7', '9', '6') ('8', '7', '9', '7') ('8', '7', '9', '8') ('8', '7', '9', '9') ('8', '8', '0', '0') ('8', '8', '0', '1') ('8', '8', '0', '2') ('8', '8', '0', '3') ('8', '8', '0', '4') ('8', '8', '0', '5') ('8', '8', '0', '6') ('8', '8', '0', '7') ('8', '8', '0', '8') ('8', '8', '0', '9') ('8', '8', '1', '0') ('8', '8', '1', '1') ('8', '8', '1', '2') ('8', '8', '1', '3') ('8', '8', '1', '4') ('8', '8', '1', '5') ('8', '8', '1', '6') ('8', '8', '1', '7') ('8', '8', '1', '8') ('8', '8', '1', '9') ('8', '8', '2', '0') ('8', '8', '2', '1') ('8', '8', '2', '2') ('8', '8', '2', '3') ('8', '8', '2', '4') ('8', '8', '2', '5') ('8', '8', '2', '6') ('8', '8', '2', '7') ('8', '8', '2', '8') ('8', '8', '2', '9') ('8', '8', '3', '0') ('8', '8', '3', '1') ('8', '8', '3', '2') ('8', '8', '3', '3') ('8', '8', '3', '4') ('8', '8', '3', '5') ('8', '8', '3', '6') ('8', '8', '3', '7') ('8', '8', '3', '8') ('8', '8', '3', '9') ('8', '8', '4', '0') ('8', '8', '4', '1') ('8', '8', '4', '2') ('8', '8', '4', '3') ('8', '8', '4', '4') ('8', '8', '4', '5') ('8', '8', '4', '6') ('8', '8', '4', '7') ('8', '8', '4', '8') ('8', '8', '4', '9') ('8', '8', '5', '0') ('8', '8', '5', '1') ('8', '8', '5', '2') ('8', '8', '5', '3') ('8', '8', '5', '4') ('8', '8', '5', '5') ('8', '8', '5', '6') ('8', '8', '5', '7') ('8', '8', '5', '8') ('8', '8', '5', '9') ('8', '8', '6', '0') ('8', '8', '6', '1') ('8', '8', '6', '2') ('8', '8', '6', '3') ('8', '8', '6', '4') ('8', '8', '6', '5') ('8', '8', '6', '6') ('8', '8', '6', '7') ('8', '8', '6', '8') ('8', '8', '6', '9') ('8', '8', '7', '0') ('8', '8', '7', '1') ('8', '8', '7', '2') ('8', '8', '7', '3') ('8', '8', '7', '4') ('8', '8', '7', '5') ('8', '8', '7', '6') ('8', '8', '7', '7') ('8', '8', '7', '8') ('8', '8', '7', '9') ('8', '8', '8', '0') ('8', '8', '8', '1') ('8', '8', '8', '2') ('8', '8', '8', '3') ('8', '8', '8', '4') ('8', '8', '8', '5') ('8', '8', '8', '6') ('8', '8', '8', '7') ('8', '8', '8', '8') ('8', '8', '8', '9') ('8', '8', '9', '0') ('8', '8', '9', '1') ('8', '8', '9', '2') ('8', '8', '9', '3') ('8', '8', '9', '4') ('8', '8', '9', '5') ('8', '8', '9', '6') ('8', '8', '9', '7') ('8', '8', '9', '8') ('8', '8', '9', '9') ('8', '9', '0', '0') ('8', '9', '0', '1') ('8', '9', '0', '2') ('8', '9', '0', '3') ('8', '9', '0', '4') ('8', '9', '0', '5') ('8', '9', '0', '6') ('8', '9', '0', '7') ('8', '9', '0', '8') ('8', '9', '0', '9') ('8', '9', '1', '0') ('8', '9', '1', '1') ('8', '9', '1', '2') ('8', '9', '1', '3') ('8', '9', '1', '4') ('8', '9', '1', '5') ('8', '9', '1', '6') ('8', '9', '1', '7') ('8', '9', '1', '8') ('8', '9', '1', '9') ('8', '9', '2', '0') ('8', '9', '2', '1') ('8', '9', '2', '2') ('8', '9', '2', '3') ('8', '9', '2', '4') ('8', '9', '2', '5') ('8', '9', '2', '6') ('8', '9', '2', '7') ('8', '9', '2', '8') ('8', '9', '2', '9') ('8', '9', '3', '0') ('8', '9', '3', '1') ('8', '9', '3', '2') ('8', '9', '3', '3') ('8', '9', '3', '4') ('8', '9', '3', '5') ('8', '9', '3', '6') ('8', '9', '3', '7') ('8', '9', '3', '8') ('8', '9', '3', '9') ('8', '9', '4', '0') ('8', '9', '4', '1') ('8', '9', '4', '2') ('8', '9', '4', '3') ('8', '9', '4', '4') ('8', '9', '4', '5') ('8', '9', '4', '6') ('8', '9', '4', '7') ('8', '9', '4', '8') ('8', '9', '4', '9') ('8', '9', '5', '0') ('8', '9', '5', '1') ('8', '9', '5', '2') ('8', '9', '5', '3') ('8', '9', '5', '4') ('8', '9', '5', '5') ('8', '9', '5', '6') ('8', '9', '5', '7') ('8', '9', '5', '8') ('8', '9', '5', '9') ('8', '9', '6', '0') ('8', '9', '6', '1') ('8', '9', '6', '2') ('8', '9', '6', '3') ('8', '9', '6', '4') ('8', '9', '6', '5') ('8', '9', '6', '6') ('8', '9', '6', '7') ('8', '9', '6', '8') ('8', '9', '6', '9') ('8', '9', '7', '0') ('8', '9', '7', '1') ('8', '9', '7', '2') ('8', '9', '7', '3') ('8', '9', '7', '4') ('8', '9', '7', '5') ('8', '9', '7', '6') ('8', '9', '7', '7') ('8', '9', '7', '8') ('8', '9', '7', '9') ('8', '9', '8', '0') ('8', '9', '8', '1') ('8', '9', '8', '2') ('8', '9', '8', '3') ('8', '9', '8', '4') ('8', '9', '8', '5') ('8', '9', '8', '6') ('8', '9', '8', '7') ('8', '9', '8', '8') ('8', '9', '8', '9') ('8', '9', '9', '0') ('8', '9', '9', '1') ('8', '9', '9', '2') ('8', '9', '9', '3') ('8', '9', '9', '4') ('8', '9', '9', '5') ('8', '9', '9', '6') ('8', '9', '9', '7') ('8', '9', '9', '8') ('8', '9', '9', '9') ('9', '0', '0', '0') ('9', '0', '0', '1') ('9', '0', '0', '2') ('9', '0', '0', '3') ('9', '0', '0', '4') ('9', '0', '0', '5') ('9', '0', '0', '6') ('9', '0', '0', '7') ('9', '0', '0', '8') ('9', '0', '0', '9') ('9', '0', '1', '0') ('9', '0', '1', '1') ('9', '0', '1', '2') ('9', '0', '1', '3') ('9', '0', '1', '4') ('9', '0', '1', '5') ('9', '0', '1', '6') ('9', '0', '1', '7') ('9', '0', '1', '8') ('9', '0', '1', '9') ('9', '0', '2', '0') ('9', '0', '2', '1') ('9', '0', '2', '2') ('9', '0', '2', '3') ('9', '0', '2', '4') ('9', '0', '2', '5') ('9', '0', '2', '6') ('9', '0', '2', '7') ('9', '0', '2', '8') ('9', '0', '2', '9') ('9', '0', '3', '0') ('9', '0', '3', '1') ('9', '0', '3', '2') ('9', '0', '3', '3') ('9', '0', '3', '4') ('9', '0', '3', '5') ('9', '0', '3', '6') ('9', '0', '3', '7') ('9', '0', '3', '8') ('9', '0', '3', '9') ('9', '0', '4', '0') ('9', '0', '4', '1') ('9', '0', '4', '2') ('9', '0', '4', '3') ('9', '0', '4', '4') ('9', '0', '4', '5') ('9', '0', '4', '6') ('9', '0', '4', '7') ('9', '0', '4', '8') ('9', '0', '4', '9') ('9', '0', '5', '0') ('9', '0', '5', '1') ('9', '0', '5', '2') ('9', '0', '5', '3') ('9', '0', '5', '4') ('9', '0', '5', '5') ('9', '0', '5', '6') ('9', '0', '5', '7') ('9', '0', '5', '8') ('9', '0', '5', '9') ('9', '0', '6', '0') ('9', '0', '6', '1') ('9', '0', '6', '2') ('9', '0', '6', '3') ('9', '0', '6', '4') ('9', '0', '6', '5') ('9', '0', '6', '6') ('9', '0', '6', '7') ('9', '0', '6', '8') ('9', '0', '6', '9') ('9', '0', '7', '0') ('9', '0', '7', '1') ('9', '0', '7', '2') ('9', '0', '7', '3') ('9', '0', '7', '4') ('9', '0', '7', '5') ('9', '0', '7', '6') ('9', '0', '7', '7') ('9', '0', '7', '8') ('9', '0', '7', '9') ('9', '0', '8', '0') ('9', '0', '8', '1') ('9', '0', '8', '2') ('9', '0', '8', '3') ('9', '0', '8', '4') ('9', '0', '8', '5') ('9', '0', '8', '6') ('9', '0', '8', '7') ('9', '0', '8', '8') ('9', '0', '8', '9') ('9', '0', '9', '0') ('9', '0', '9', '1') ('9', '0', '9', '2') ('9', '0', '9', '3') ('9', '0', '9', '4') ('9', '0', '9', '5') ('9', '0', '9', '6') ('9', '0', '9', '7') ('9', '0', '9', '8') ('9', '0', '9', '9') ('9', '1', '0', '0') ('9', '1', '0', '1') ('9', '1', '0', '2') ('9', '1', '0', '3') ('9', '1', '0', '4') ('9', '1', '0', '5') ('9', '1', '0', '6') ('9', '1', '0', '7') ('9', '1', '0', '8') ('9', '1', '0', '9') ('9', '1', '1', '0') ('9', '1', '1', '1') ('9', '1', '1', '2') ('9', '1', '1', '3') ('9', '1', '1', '4') ('9', '1', '1', '5') ('9', '1', '1', '6') ('9', '1', '1', '7') ('9', '1', '1', '8') ('9', '1', '1', '9') ('9', '1', '2', '0') ('9', '1', '2', '1') ('9', '1', '2', '2') ('9', '1', '2', '3') ('9', '1', '2', '4') ('9', '1', '2', '5') ('9', '1', '2', '6') ('9', '1', '2', '7') ('9', '1', '2', '8') ('9', '1', '2', '9') ('9', '1', '3', '0') ('9', '1', '3', '1') ('9', '1', '3', '2') ('9', '1', '3', '3') ('9', '1', '3', '4') ('9', '1', '3', '5') ('9', '1', '3', '6') ('9', '1', '3', '7') ('9', '1', '3', '8') ('9', '1', '3', '9') ('9', '1', '4', '0') ('9', '1', '4', '1') ('9', '1', '4', '2') ('9', '1', '4', '3') ('9', '1', '4', '4') ('9', '1', '4', '5') ('9', '1', '4', '6') ('9', '1', '4', '7') ('9', '1', '4', '8') ('9', '1', '4', '9') ('9', '1', '5', '0') ('9', '1', '5', '1') ('9', '1', '5', '2') ('9', '1', '5', '3') ('9', '1', '5', '4') ('9', '1', '5', '5') ('9', '1', '5', '6') ('9', '1', '5', '7') ('9', '1', '5', '8') ('9', '1', '5', '9') ('9', '1', '6', '0') ('9', '1', '6', '1') ('9', '1', '6', '2') ('9', '1', '6', '3') ('9', '1', '6', '4') ('9', '1', '6', '5') ('9', '1', '6', '6') ('9', '1', '6', '7') ('9', '1', '6', '8') ('9', '1', '6', '9') ('9', '1', '7', '0') ('9', '1', '7', '1') ('9', '1', '7', '2') ('9', '1', '7', '3') ('9', '1', '7', '4') ('9', '1', '7', '5') ('9', '1', '7', '6') ('9', '1', '7', '7') ('9', '1', '7', '8') ('9', '1', '7', '9') ('9', '1', '8', '0') ('9', '1', '8', '1') ('9', '1', '8', '2') ('9', '1', '8', '3') ('9', '1', '8', '4') ('9', '1', '8', '5') ('9', '1', '8', '6') ('9', '1', '8', '7') ('9', '1', '8', '8') ('9', '1', '8', '9') ('9', '1', '9', '0') ('9', '1', '9', '1') ('9', '1', '9', '2') ('9', '1', '9', '3') ('9', '1', '9', '4') ('9', '1', '9', '5') ('9', '1', '9', '6') ('9', '1', '9', '7') ('9', '1', '9', '8') ('9', '1', '9', '9') ('9', '2', '0', '0') ('9', '2', '0', '1') ('9', '2', '0', '2') ('9', '2', '0', '3') ('9', '2', '0', '4') ('9', '2', '0', '5') ('9', '2', '0', '6') ('9', '2', '0', '7') ('9', '2', '0', '8') ('9', '2', '0', '9') ('9', '2', '1', '0') ('9', '2', '1', '1') ('9', '2', '1', '2') ('9', '2', '1', '3') ('9', '2', '1', '4') ('9', '2', '1', '5') ('9', '2', '1', '6') ('9', '2', '1', '7') ('9', '2', '1', '8') ('9', '2', '1', '9') ('9', '2', '2', '0') ('9', '2', '2', '1') ('9', '2', '2', '2') ('9', '2', '2', '3') ('9', '2', '2', '4') ('9', '2', '2', '5') ('9', '2', '2', '6') ('9', '2', '2', '7') ('9', '2', '2', '8') ('9', '2', '2', '9') ('9', '2', '3', '0') ('9', '2', '3', '1') ('9', '2', '3', '2') ('9', '2', '3', '3') ('9', '2', '3', '4') ('9', '2', '3', '5') ('9', '2', '3', '6') ('9', '2', '3', '7') ('9', '2', '3', '8') ('9', '2', '3', '9') ('9', '2', '4', '0') ('9', '2', '4', '1') ('9', '2', '4', '2') ('9', '2', '4', '3') ('9', '2', '4', '4') ('9', '2', '4', '5') ('9', '2', '4', '6') ('9', '2', '4', '7') ('9', '2', '4', '8') ('9', '2', '4', '9') ('9', '2', '5', '0') ('9', '2', '5', '1') ('9', '2', '5', '2') ('9', '2', '5', '3') ('9', '2', '5', '4') ('9', '2', '5', '5') ('9', '2', '5', '6') ('9', '2', '5', '7') ('9', '2', '5', '8') ('9', '2', '5', '9') ('9', '2', '6', '0') ('9', '2', '6', '1') ('9', '2', '6', '2') ('9', '2', '6', '3') ('9', '2', '6', '4') ('9', '2', '6', '5') ('9', '2', '6', '6') ('9', '2', '6', '7') ('9', '2', '6', '8') ('9', '2', '6', '9') ('9', '2', '7', '0') ('9', '2', '7', '1') ('9', '2', '7', '2') ('9', '2', '7', '3') ('9', '2', '7', '4') ('9', '2', '7', '5') ('9', '2', '7', '6') ('9', '2', '7', '7') ('9', '2', '7', '8') ('9', '2', '7', '9') ('9', '2', '8', '0') ('9', '2', '8', '1') ('9', '2', '8', '2') ('9', '2', '8', '3') ('9', '2', '8', '4') ('9', '2', '8', '5') ('9', '2', '8', '6') ('9', '2', '8', '7') ('9', '2', '8', '8') ('9', '2', '8', '9') ('9', '2', '9', '0') ('9', '2', '9', '1') ('9', '2', '9', '2') ('9', '2', '9', '3') ('9', '2', '9', '4') ('9', '2', '9', '5') ('9', '2', '9', '6') ('9', '2', '9', '7') ('9', '2', '9', '8') ('9', '2', '9', '9') ('9', '3', '0', '0') ('9', '3', '0', '1') ('9', '3', '0', '2') ('9', '3', '0', '3') ('9', '3', '0', '4') ('9', '3', '0', '5') ('9', '3', '0', '6') ('9', '3', '0', '7') ('9', '3', '0', '8') ('9', '3', '0', '9') ('9', '3', '1', '0') ('9', '3', '1', '1') ('9', '3', '1', '2') ('9', '3', '1', '3') ('9', '3', '1', '4') ('9', '3', '1', '5') ('9', '3', '1', '6') ('9', '3', '1', '7') ('9', '3', '1', '8') ('9', '3', '1', '9') ('9', '3', '2', '0') ('9', '3', '2', '1') ('9', '3', '2', '2') ('9', '3', '2', '3') ('9', '3', '2', '4') ('9', '3', '2', '5') ('9', '3', '2', '6') ('9', '3', '2', '7') ('9', '3', '2', '8') ('9', '3', '2', '9') ('9', '3', '3', '0') ('9', '3', '3', '1') ('9', '3', '3', '2') ('9', '3', '3', '3') ('9', '3', '3', '4') ('9', '3', '3', '5') ('9', '3', '3', '6') ('9', '3', '3', '7') ('9', '3', '3', '8') ('9', '3', '3', '9') ('9', '3', '4', '0') ('9', '3', '4', '1') ('9', '3', '4', '2') ('9', '3', '4', '3') ('9', '3', '4', '4') ('9', '3', '4', '5') ('9', '3', '4', '6') ('9', '3', '4', '7') ('9', '3', '4', '8') ('9', '3', '4', '9') ('9', '3', '5', '0') ('9', '3', '5', '1') ('9', '3', '5', '2') ('9', '3', '5', '3') ('9', '3', '5', '4') ('9', '3', '5', '5') ('9', '3', '5', '6') ('9', '3', '5', '7') ('9', '3', '5', '8') ('9', '3', '5', '9') ('9', '3', '6', '0') ('9', '3', '6', '1') ('9', '3', '6', '2') ('9', '3', '6', '3') ('9', '3', '6', '4') ('9', '3', '6', '5') ('9', '3', '6', '6') ('9', '3', '6', '7') ('9', '3', '6', '8') ('9', '3', '6', '9') ('9', '3', '7', '0') ('9', '3', '7', '1') ('9', '3', '7', '2') ('9', '3', '7', '3') ('9', '3', '7', '4') ('9', '3', '7', '5') ('9', '3', '7', '6') ('9', '3', '7', '7') ('9', '3', '7', '8') ('9', '3', '7', '9') ('9', '3', '8', '0') ('9', '3', '8', '1') ('9', '3', '8', '2') ('9', '3', '8', '3') ('9', '3', '8', '4') ('9', '3', '8', '5') ('9', '3', '8', '6') ('9', '3', '8', '7') ('9', '3', '8', '8') ('9', '3', '8', '9') ('9', '3', '9', '0') ('9', '3', '9', '1') ('9', '3', '9', '2') ('9', '3', '9', '3') ('9', '3', '9', '4') ('9', '3', '9', '5') ('9', '3', '9', '6') ('9', '3', '9', '7') ('9', '3', '9', '8') ('9', '3', '9', '9') ('9', '4', '0', '0') ('9', '4', '0', '1') ('9', '4', '0', '2') ('9', '4', '0', '3') ('9', '4', '0', '4') ('9', '4', '0', '5') ('9', '4', '0', '6') ('9', '4', '0', '7') ('9', '4', '0', '8') ('9', '4', '0', '9') ('9', '4', '1', '0') ('9', '4', '1', '1') ('9', '4', '1', '2') ('9', '4', '1', '3') ('9', '4', '1', '4') ('9', '4', '1', '5') ('9', '4', '1', '6') ('9', '4', '1', '7') ('9', '4', '1', '8') ('9', '4', '1', '9') ('9', '4', '2', '0') ('9', '4', '2', '1') ('9', '4', '2', '2') ('9', '4', '2', '3') ('9', '4', '2', '4') ('9', '4', '2', '5') ('9', '4', '2', '6') ('9', '4', '2', '7') ('9', '4', '2', '8') ('9', '4', '2', '9') ('9', '4', '3', '0') ('9', '4', '3', '1') ('9', '4', '3', '2') ('9', '4', '3', '3') ('9', '4', '3', '4') ('9', '4', '3', '5') ('9', '4', '3', '6') ('9', '4', '3', '7') ('9', '4', '3', '8') ('9', '4', '3', '9') ('9', '4', '4', '0') ('9', '4', '4', '1') ('9', '4', '4', '2') ('9', '4', '4', '3') ('9', '4', '4', '4') ('9', '4', '4', '5') ('9', '4', '4', '6') ('9', '4', '4', '7') ('9', '4', '4', '8') ('9', '4', '4', '9') ('9', '4', '5', '0') ('9', '4', '5', '1') ('9', '4', '5', '2') ('9', '4', '5', '3') ('9', '4', '5', '4') ('9', '4', '5', '5') ('9', '4', '5', '6') ('9', '4', '5', '7') ('9', '4', '5', '8') ('9', '4', '5', '9') ('9', '4', '6', '0') ('9', '4', '6', '1') ('9', '4', '6', '2') ('9', '4', '6', '3') ('9', '4', '6', '4') ('9', '4', '6', '5') ('9', '4', '6', '6') ('9', '4', '6', '7') ('9', '4', '6', '8') ('9', '4', '6', '9') ('9', '4', '7', '0') ('9', '4', '7', '1') ('9', '4', '7', '2') ('9', '4', '7', '3') ('9', '4', '7', '4') ('9', '4', '7', '5') ('9', '4', '7', '6') ('9', '4', '7', '7') ('9', '4', '7', '8') ('9', '4', '7', '9') ('9', '4', '8', '0') ('9', '4', '8', '1') ('9', '4', '8', '2') ('9', '4', '8', '3') ('9', '4', '8', '4') ('9', '4', '8', '5') ('9', '4', '8', '6') ('9', '4', '8', '7') ('9', '4', '8', '8') ('9', '4', '8', '9') ('9', '4', '9', '0') ('9', '4', '9', '1') ('9', '4', '9', '2') ('9', '4', '9', '3') ('9', '4', '9', '4') ('9', '4', '9', '5') ('9', '4', '9', '6') ('9', '4', '9', '7') ('9', '4', '9', '8') ('9', '4', '9', '9') ('9', '5', '0', '0') ('9', '5', '0', '1') ('9', '5', '0', '2') ('9', '5', '0', '3') ('9', '5', '0', '4') ('9', '5', '0', '5') ('9', '5', '0', '6') ('9', '5', '0', '7') ('9', '5', '0', '8') ('9', '5', '0', '9') ('9', '5', '1', '0') ('9', '5', '1', '1') ('9', '5', '1', '2') ('9', '5', '1', '3') ('9', '5', '1', '4') ('9', '5', '1', '5') ('9', '5', '1', '6') ('9', '5', '1', '7') ('9', '5', '1', '8') ('9', '5', '1', '9') ('9', '5', '2', '0') ('9', '5', '2', '1') ('9', '5', '2', '2') ('9', '5', '2', '3') ('9', '5', '2', '4') ('9', '5', '2', '5') ('9', '5', '2', '6') ('9', '5', '2', '7') ('9', '5', '2', '8') ('9', '5', '2', '9') ('9', '5', '3', '0') ('9', '5', '3', '1') ('9', '5', '3', '2') ('9', '5', '3', '3') ('9', '5', '3', '4') ('9', '5', '3', '5') ('9', '5', '3', '6') ('9', '5', '3', '7') ('9', '5', '3', '8') ('9', '5', '3', '9') ('9', '5', '4', '0') ('9', '5', '4', '1') ('9', '5', '4', '2') ('9', '5', '4', '3') ('9', '5', '4', '4') ('9', '5', '4', '5') ('9', '5', '4', '6') ('9', '5', '4', '7') ('9', '5', '4', '8') ('9', '5', '4', '9') ('9', '5', '5', '0') ('9', '5', '5', '1') ('9', '5', '5', '2') ('9', '5', '5', '3') ('9', '5', '5', '4') ('9', '5', '5', '5') ('9', '5', '5', '6') ('9', '5', '5', '7') ('9', '5', '5', '8') ('9', '5', '5', '9') ('9', '5', '6', '0') ('9', '5', '6', '1') ('9', '5', '6', '2') ('9', '5', '6', '3') ('9', '5', '6', '4') ('9', '5', '6', '5') ('9', '5', '6', '6') ('9', '5', '6', '7') ('9', '5', '6', '8') ('9', '5', '6', '9') ('9', '5', '7', '0') ('9', '5', '7', '1') ('9', '5', '7', '2') ('9', '5', '7', '3') ('9', '5', '7', '4') ('9', '5', '7', '5') ('9', '5', '7', '6') ('9', '5', '7', '7') ('9', '5', '7', '8') ('9', '5', '7', '9') ('9', '5', '8', '0') ('9', '5', '8', '1') ('9', '5', '8', '2') ('9', '5', '8', '3') ('9', '5', '8', '4') ('9', '5', '8', '5') ('9', '5', '8', '6') ('9', '5', '8', '7') ('9', '5', '8', '8') ('9', '5', '8', '9') ('9', '5', '9', '0') ('9', '5', '9', '1') ('9', '5', '9', '2') ('9', '5', '9', '3') ('9', '5', '9', '4') ('9', '5', '9', '5') ('9', '5', '9', '6') ('9', '5', '9', '7') ('9', '5', '9', '8') ('9', '5', '9', '9') ('9', '6', '0', '0') ('9', '6', '0', '1') ('9', '6', '0', '2') ('9', '6', '0', '3') ('9', '6', '0', '4') ('9', '6', '0', '5') ('9', '6', '0', '6') ('9', '6', '0', '7') ('9', '6', '0', '8') ('9', '6', '0', '9') ('9', '6', '1', '0') ('9', '6', '1', '1') ('9', '6', '1', '2') ('9', '6', '1', '3') ('9', '6', '1', '4') ('9', '6', '1', '5') ('9', '6', '1', '6') ('9', '6', '1', '7') ('9', '6', '1', '8') ('9', '6', '1', '9') ('9', '6', '2', '0') ('9', '6', '2', '1') ('9', '6', '2', '2') ('9', '6', '2', '3') ('9', '6', '2', '4') ('9', '6', '2', '5') ('9', '6', '2', '6') ('9', '6', '2', '7') ('9', '6', '2', '8') ('9', '6', '2', '9') ('9', '6', '3', '0') ('9', '6', '3', '1') ('9', '6', '3', '2') ('9', '6', '3', '3') ('9', '6', '3', '4') ('9', '6', '3', '5') ('9', '6', '3', '6') ('9', '6', '3', '7') ('9', '6', '3', '8') ('9', '6', '3', '9') ('9', '6', '4', '0') ('9', '6', '4', '1') ('9', '6', '4', '2') ('9', '6', '4', '3') ('9', '6', '4', '4') ('9', '6', '4', '5') ('9', '6', '4', '6') ('9', '6', '4', '7') ('9', '6', '4', '8') ('9', '6', '4', '9') ('9', '6', '5', '0') ('9', '6', '5', '1') ('9', '6', '5', '2') ('9', '6', '5', '3') ('9', '6', '5', '4') ('9', '6', '5', '5') ('9', '6', '5', '6') ('9', '6', '5', '7') ('9', '6', '5', '8') ('9', '6', '5', '9') ('9', '6', '6', '0') ('9', '6', '6', '1') ('9', '6', '6', '2') ('9', '6', '6', '3') ('9', '6', '6', '4') ('9', '6', '6', '5') ('9', '6', '6', '6') ('9', '6', '6', '7') ('9', '6', '6', '8') ('9', '6', '6', '9') ('9', '6', '7', '0') ('9', '6', '7', '1') ('9', '6', '7', '2') ('9', '6', '7', '3') ('9', '6', '7', '4') ('9', '6', '7', '5') ('9', '6', '7', '6') ('9', '6', '7', '7') ('9', '6', '7', '8') ('9', '6', '7', '9') ('9', '6', '8', '0') ('9', '6', '8', '1') ('9', '6', '8', '2') ('9', '6', '8', '3') ('9', '6', '8', '4') ('9', '6', '8', '5') ('9', '6', '8', '6') ('9', '6', '8', '7') ('9', '6', '8', '8') ('9', '6', '8', '9') ('9', '6', '9', '0') ('9', '6', '9', '1') ('9', '6', '9', '2') ('9', '6', '9', '3') ('9', '6', '9', '4') ('9', '6', '9', '5') ('9', '6', '9', '6') ('9', '6', '9', '7') ('9', '6', '9', '8') ('9', '6', '9', '9') ('9', '7', '0', '0') ('9', '7', '0', '1') ('9', '7', '0', '2') ('9', '7', '0', '3') ('9', '7', '0', '4') ('9', '7', '0', '5') ('9', '7', '0', '6') ('9', '7', '0', '7') ('9', '7', '0', '8') ('9', '7', '0', '9') ('9', '7', '1', '0') ('9', '7', '1', '1') ('9', '7', '1', '2') ('9', '7', '1', '3') ('9', '7', '1', '4') ('9', '7', '1', '5') ('9', '7', '1', '6') ('9', '7', '1', '7') ('9', '7', '1', '8') ('9', '7', '1', '9') ('9', '7', '2', '0') ('9', '7', '2', '1') ('9', '7', '2', '2') ('9', '7', '2', '3') ('9', '7', '2', '4') ('9', '7', '2', '5') ('9', '7', '2', '6') ('9', '7', '2', '7') ('9', '7', '2', '8') ('9', '7', '2', '9') ('9', '7', '3', '0') ('9', '7', '3', '1') ('9', '7', '3', '2') ('9', '7', '3', '3') ('9', '7', '3', '4') ('9', '7', '3', '5') ('9', '7', '3', '6') ('9', '7', '3', '7') ('9', '7', '3', '8') ('9', '7', '3', '9') ('9', '7', '4', '0') ('9', '7', '4', '1') ('9', '7', '4', '2') ('9', '7', '4', '3') ('9', '7', '4', '4') ('9', '7', '4', '5') ('9', '7', '4', '6') ('9', '7', '4', '7') ('9', '7', '4', '8') ('9', '7', '4', '9') ('9', '7', '5', '0') ('9', '7', '5', '1') ('9', '7', '5', '2') ('9', '7', '5', '3') ('9', '7', '5', '4') ('9', '7', '5', '5') ('9', '7', '5', '6') ('9', '7', '5', '7') ('9', '7', '5', '8') ('9', '7', '5', '9') ('9', '7', '6', '0') ('9', '7', '6', '1') ('9', '7', '6', '2') ('9', '7', '6', '3') ('9', '7', '6', '4') ('9', '7', '6', '5') ('9', '7', '6', '6') ('9', '7', '6', '7') ('9', '7', '6', '8') ('9', '7', '6', '9') ('9', '7', '7', '0') ('9', '7', '7', '1') ('9', '7', '7', '2') ('9', '7', '7', '3') ('9', '7', '7', '4') ('9', '7', '7', '5') ('9', '7', '7', '6') ('9', '7', '7', '7') ('9', '7', '7', '8') ('9', '7', '7', '9') ('9', '7', '8', '0') ('9', '7', '8', '1') ('9', '7', '8', '2') ('9', '7', '8', '3') ('9', '7', '8', '4') ('9', '7', '8', '5') ('9', '7', '8', '6') ('9', '7', '8', '7') ('9', '7', '8', '8') ('9', '7', '8', '9') ('9', '7', '9', '0') ('9', '7', '9', '1') ('9', '7', '9', '2') ('9', '7', '9', '3') ('9', '7', '9', '4') ('9', '7', '9', '5') ('9', '7', '9', '6') ('9', '7', '9', '7') ('9', '7', '9', '8') ('9', '7', '9', '9') ('9', '8', '0', '0') ('9', '8', '0', '1') ('9', '8', '0', '2') ('9', '8', '0', '3') ('9', '8', '0', '4') ('9', '8', '0', '5') ('9', '8', '0', '6') ('9', '8', '0', '7') ('9', '8', '0', '8') ('9', '8', '0', '9') ('9', '8', '1', '0') ('9', '8', '1', '1') ('9', '8', '1', '2') ('9', '8', '1', '3') ('9', '8', '1', '4') ('9', '8', '1', '5') ('9', '8', '1', '6') ('9', '8', '1', '7') ('9', '8', '1', '8') ('9', '8', '1', '9') ('9', '8', '2', '0') ('9', '8', '2', '1') ('9', '8', '2', '2') ('9', '8', '2', '3') ('9', '8', '2', '4') ('9', '8', '2', '5') ('9', '8', '2', '6') ('9', '8', '2', '7') ('9', '8', '2', '8') ('9', '8', '2', '9') ('9', '8', '3', '0') ('9', '8', '3', '1') ('9', '8', '3', '2') ('9', '8', '3', '3') ('9', '8', '3', '4') ('9', '8', '3', '5') ('9', '8', '3', '6') ('9', '8', '3', '7') ('9', '8', '3', '8') ('9', '8', '3', '9') ('9', '8', '4', '0') ('9', '8', '4', '1') ('9', '8', '4', '2') ('9', '8', '4', '3') ('9', '8', '4', '4') ('9', '8', '4', '5') ('9', '8', '4', '6') ('9', '8', '4', '7') ('9', '8', '4', '8') ('9', '8', '4', '9') ('9', '8', '5', '0') ('9', '8', '5', '1') ('9', '8', '5', '2') ('9', '8', '5', '3') ('9', '8', '5', '4') ('9', '8', '5', '5') ('9', '8', '5', '6') ('9', '8', '5', '7') ('9', '8', '5', '8') ('9', '8', '5', '9') ('9', '8', '6', '0') ('9', '8', '6', '1') ('9', '8', '6', '2') ('9', '8', '6', '3') ('9', '8', '6', '4') ('9', '8', '6', '5') ('9', '8', '6', '6') ('9', '8', '6', '7') ('9', '8', '6', '8') ('9', '8', '6', '9') ('9', '8', '7', '0') ('9', '8', '7', '1') ('9', '8', '7', '2') ('9', '8', '7', '3') ('9', '8', '7', '4') ('9', '8', '7', '5') ('9', '8', '7', '6') ('9', '8', '7', '7') ('9', '8', '7', '8') ('9', '8', '7', '9') ('9', '8', '8', '0') ('9', '8', '8', '1') ('9', '8', '8', '2') ('9', '8', '8', '3') ('9', '8', '8', '4') ('9', '8', '8', '5') ('9', '8', '8', '6') ('9', '8', '8', '7') ('9', '8', '8', '8') ('9', '8', '8', '9') ('9', '8', '9', '0') ('9', '8', '9', '1') ('9', '8', '9', '2') ('9', '8', '9', '3') ('9', '8', '9', '4') ('9', '8', '9', '5') ('9', '8', '9', '6') ('9', '8', '9', '7') ('9', '8', '9', '8') ('9', '8', '9', '9') ('9', '9', '0', '0') ('9', '9', '0', '1') ('9', '9', '0', '2') ('9', '9', '0', '3') ('9', '9', '0', '4') ('9', '9', '0', '5') ('9', '9', '0', '6') ('9', '9', '0', '7') ('9', '9', '0', '8') ('9', '9', '0', '9') ('9', '9', '1', '0') ('9', '9', '1', '1') ('9', '9', '1', '2') ('9', '9', '1', '3') ('9', '9', '1', '4') ('9', '9', '1', '5') ('9', '9', '1', '6') ('9', '9', '1', '7') ('9', '9', '1', '8') ('9', '9', '1', '9') ('9', '9', '2', '0') ('9', '9', '2', '1') ('9', '9', '2', '2') ('9', '9', '2', '3') ('9', '9', '2', '4') ('9', '9', '2', '5') ('9', '9', '2', '6') ('9', '9', '2', '7') ('9', '9', '2', '8') ('9', '9', '2', '9') ('9', '9', '3', '0') ('9', '9', '3', '1') ('9', '9', '3', '2') ('9', '9', '3', '3') ('9', '9', '3', '4') ('9', '9', '3', '5') ('9', '9', '3', '6') ('9', '9', '3', '7') ('9', '9', '3', '8') ('9', '9', '3', '9') ('9', '9', '4', '0') ('9', '9', '4', '1') ('9', '9', '4', '2') ('9', '9', '4', '3') ('9', '9', '4', '4') ('9', '9', '4', '5') ('9', '9', '4', '6') ('9', '9', '4', '7') ('9', '9', '4', '8') ('9', '9', '4', '9') ('9', '9', '5', '0') ('9', '9', '5', '1') ('9', '9', '5', '2') ('9', '9', '5', '3') ('9', '9', '5', '4') ('9', '9', '5', '5') ('9', '9', '5', '6') ('9', '9', '5', '7') ('9', '9', '5', '8') ('9', '9', '5', '9') ('9', '9', '6', '0') ('9', '9', '6', '1') ('9', '9', '6', '2') ('9', '9', '6', '3') ('9', '9', '6', '4') ('9', '9', '6', '5') ('9', '9', '6', '6') ('9', '9', '6', '7') ('9', '9', '6', '8') ('9', '9', '6', '9') ('9', '9', '7', '0') ('9', '9', '7', '1') ('9', '9', '7', '2') ('9', '9', '7', '3') ('9', '9', '7', '4') ('9', '9', '7', '5') ('9', '9', '7', '6') ('9', '9', '7', '7') ('9', '9', '7', '8') ('9', '9', '7', '9') ('9', '9', '8', '0') ('9', '9', '8', '1') ('9', '9', '8', '2') ('9', '9', '8', '3') ('9', '9', '8', '4') ('9', '9', '8', '5') ('9', '9', '8', '6') ('9', '9', '8', '7') ('9', '9', '8', '8') ('9', '9', '8', '9') ('9', '9', '9', '0') ('9', '9', '9', '1') ('9', '9', '9', '2') ('9', '9', '9', '3') ('9', '9', '9', '4') ('9', '9', '9', '5') ('9', '9', '9', '6') ('9', '9', '9', '7') ('9', '9', '9', '8') ('9', '9', '9', '9')

    [('a', 'a'), ('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('a', 'f'), ('a', 'g'), ('a', 'h'), ('a', 'i'), ('a', 'j'), ('a', 'k'), ('a', 'l'), ('a', 'm'), ('a', 'n'), ('a', 'o'), ('a', 'p'), ('a', 'q'), ('a', 'r'), ('a', 's'), ('a', 't'), ('a', 'u'), ('a', 'v'), ('a', 'w'), ('a', 'x'), ('a', 'y'), ('a', 'z'), ('a', 'A'), ('a', 'B'), ('a', 'C'), ('a', 'D'), ('a', 'E'), ('a', 'F'), ('a', 'G'), ('a', 'H'), ('a', 'I'), ('a', 'J'), ('a', 'K'), ('a', 'L'), ('a', 'M'), ('a', 'N'), ('a', 'O'), ('a', 'P'), ('a', 'Q'), ('a', 'R'), ('a', 'S'), ('a', 'T'), ('a', 'U'), ('a', 'V'), ('a', 'W'), ('a', 'X'), ('a', 'Y'), ('a', 'Z'), ('a', '0'), ('a', '1'), ('a', '2'), ('a', '3'), ('a', '4'), ('a', '5'), ('a', '6'), ('a', '7'), ('a', '8'), ('a', '9'), ('a', '!'), ('a', '"'), ('a', '#'), ('a', '$'), ('a', '%'), ('a', '&'), ('a', "'"), ('a', '('), ('a', ')'), ('a', '*'), ('a', '+'), ('a', ','), ('a', '-'), ('a', '.'), ('a', '/'), ('a', ':'), ('a', ';'), ('a', '<'), ('a', '='), ('a', '>'), ('a', '?'), ('a', '@'), ('a', '['), ('a', '\\'), ('a', ']'), ('a', '^'), ('a', '_'), ('a', '`'), ('a', '{'), ('a', '|'), ('a', '}'), ('a', '~'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('b', 'd'), ('b', 'e'), ('b', 'f'), ('b', 'g'), ('b', 'h'), ('b', 'i'), ('b', 'j'), ('b', 'k'), ('b', 'l'), ('b', 'm'), ('b', 'n'), ('b', 'o'), ('b', 'p'), ('b', 'q'), ('b', 'r'), ('b', 's'), ('b', 't'), ('b', 'u'), ('b', 'v'), ('b', 'w'), ('b', 'x'), ('b', 'y'), ('b', 'z'), ('b', 'A'), ('b', 'B'), ('b', 'C'), ('b', 'D'), ('b', 'E'), ('b', 'F'), ('b', 'G'), ('b', 'H'), ('b', 'I'), ('b', 'J'), ('b', 'K'), ('b', 'L'), ('b', 'M'), ('b', 'N'), ('b', 'O'), ('b', 'P'), ('b', 'Q'), ('b', 'R'), ('b', 'S'), ('b', 'T'), ('b', 'U'), ('b', 'V'), ('b', 'W'), ('b', 'X'), ('b', 'Y'), ('b', 'Z'), ('b', '0'), ('b', '1'), ('b', '2'), ('b', '3'), ('b', '4'), ('b', '5'), ('b', '6'), ('b', '7'), ('b', '8'), ('b', '9'), ('b', '!'), ('b', '"'), ('b', '#'), ('b', '$'), ('b', '%'), ('b', '&'), ('b', "'"), ('b', '('), ('b', ')'), ('b', '*'), ('b', '+'), ('b', ','), ('b', '-'), ('b', '.'), ('b', '/'), ('b', ':'), ('b', ';'), ('b', '<'), ('b', '='), ('b', '>'), ('b', '?'), ('b', '@'), ('b', '['), ('b', '\\'), ('b', ']'), ('b', '^'), ('b', '_'), ('b', '`'), ('b', '{'), ('b', '|'), ('b', '}'), ('b', '~'), ('c', 'a'), ('c', 'b'), ('c', 'c'), ('c', 'd'), ('c', 'e'), ('c', 'f'), ('c', 'g'), ('c', 'h'), ('c', 'i'), ('c', 'j'), ('c', 'k'), ('c', 'l'), ('c', 'm'), ('c', 'n'), ('c', 'o'), ('c', 'p'), ('c', 'q'), ('c', 'r'), ('c', 's'), ('c', 't'), ('c', 'u'), ('c', 'v'), ('c', 'w'), ('c', 'x'), ('c', 'y'), ('c', 'z'), ('c', 'A'), ('c', 'B'), ('c', 'C'), ('c', 'D'), ('c', 'E'), ('c', 'F'), ('c', 'G'), ('c', 'H'), ('c', 'I'), ('c', 'J'), ('c', 'K'), ('c', 'L'), ('c', 'M'), ('c', 'N'), ('c', 'O'), ('c', 'P'), ('c', 'Q'), ('c', 'R'), ('c', 'S'), ('c', 'T'), ('c', 'U'), ('c', 'V'), ('c', 'W'), ('c', 'X'), ('c', 'Y'), ('c', 'Z'), ('c', '0'), ('c', '1'), ('c', '2'), ('c', '3'), ('c', '4'), ('c', '5'), ('c', '6'), ('c', '7'), ('c', '8'), ('c', '9'), ('c', '!'), ('c', '"'), ('c', '#'), ('c', '$'), ('c', '%'), ('c', '&'), ('c', "'"), ('c', '('), ('c', ')'), ('c', '*'), ('c', '+'), ('c', ','), ('c', '-'), ('c', '.'), ('c', '/'), ('c', ':'), ('c', ';'), ('c', '<'), ('c', '='), ('c', '>'), ('c', '?'), ('c', '@'), ('c', '['), ('c', '\\'), ('c', ']'), ('c', '^'), ('c', '_'), ('c', '`'), ('c', '{'), ('c', '|'), ('c', '}'), ('c', '~'), ('d', 'a'), ('d', 'b'), ('d', 'c'), ('d', 'd'), ('d', 'e'), ('d', 'f'), ('d', 'g'), ('d', 'h'), ('d', 'i'), ('d', 'j'), ('d', 'k'), ('d', 'l'), ('d', 'm'), ('d', 'n'), ('d', 'o'), ('d', 'p'), ('d', 'q'), ('d', 'r'), ('d', 's'), ('d', 't'), ('d', 'u'), ('d', 'v'), ('d', 'w'), ('d', 'x'), ('d', 'y'), ('d', 'z'), ('d', 'A'), ('d', 'B'), ('d', 'C'), ('d', 'D'), ('d', 'E'), ('d', 'F'), ('d', 'G'), ('d', 'H'), ('d', 'I'), ('d', 'J'), ('d', 'K'), ('d', 'L'), ('d', 'M'), ('d', 'N'), ('d', 'O'), ('d', 'P'), ('d', 'Q'), ('d', 'R'), ('d', 'S'), ('d', 'T'), ('d', 'U'), ('d', 'V'), ('d', 'W'), ('d', 'X'), ('d', 'Y'), ('d', 'Z'), ('d', '0'), ('d', '1'), ('d', '2'), ('d', '3'), ('d', '4'), ('d', '5'), ('d', '6'), ('d', '7'), ('d', '8'), ('d', '9'), ('d', '!'), ('d', '"'), ('d', '#'), ('d', '$'), ('d', '%'), ('d', '&'), ('d', "'"), ('d', '('), ('d', ')'), ('d', '*'), ('d', '+'), ('d', ','), ('d', '-'), ('d', '.'), ('d', '/'), ('d', ':'), ('d', ';'), ('d', '<'), ('d', '='), ('d', '>'), ('d', '?'), ('d', '@'), ('d', '['), ('d', '\\'), ('d', ']'), ('d', '^'), ('d', '_'), ('d', '`'), ('d', '{'), ('d', '|'), ('d', '}'), ('d', '~'), ('e', 'a'), ('e', 'b'), ('e', 'c'), ('e', 'd'), ('e', 'e'), ('e', 'f'), ('e', 'g'), ('e', 'h'), ('e', 'i'), ('e', 'j'), ('e', 'k'), ('e', 'l'), ('e', 'm'), ('e', 'n'), ('e', 'o'), ('e', 'p'), ('e', 'q'), ('e', 'r'), ('e', 's'), ('e', 't'), ('e', 'u'), ('e', 'v'), ('e', 'w'), ('e', 'x'), ('e', 'y'), ('e', 'z'), ('e', 'A'), ('e', 'B'), ('e', 'C'), ('e', 'D'), ('e', 'E'), ('e', 'F'), ('e', 'G'), ('e', 'H'), ('e', 'I'), ('e', 'J'), ('e', 'K'), ('e', 'L'), ('e', 'M'), ('e', 'N'), ('e', 'O'), ('e', 'P'), ('e', 'Q'), ('e', 'R'), ('e', 'S'), ('e', 'T'), ('e', 'U'), ('e', 'V'), ('e', 'W'), ('e', 'X'), ('e', 'Y'), ('e', 'Z'), ('e', '0'), ('e', '1'), ('e', '2'), ('e', '3'), ('e', '4'), ('e', '5'), ('e', '6'), ('e', '7'), ('e', '8'), ('e', '9'), ('e', '!'), ('e', '"'), ('e', '#'), ('e', '$'), ('e', '%'), ('e', '&'), ('e', "'"), ('e', '('), ('e', ')'), ('e', '*'), ('e', '+'), ('e', ','), ('e', '-'), ('e', '.'), ('e', '/'), ('e', ':'), ('e', ';'), ('e', '<'), ('e', '='), ('e', '>'), ('e', '?'), ('e', '@'), ('e', '['), ('e', '\\'), ('e', ']'), ('e', '^'), ('e', '_'), ('e', '`'), ('e', '{'), ('e', '|'), ('e', '}'), ('e', '~'), ('f', 'a'), ('f', 'b'), ('f', 'c'), ('f', 'd'), ('f', 'e'), ('f', 'f'), ('f', 'g'), ('f', 'h'), ('f', 'i'), ('f', 'j'), ('f', 'k'), ('f', 'l'), ('f', 'm'), ('f', 'n'), ('f', 'o'), ('f', 'p'), ('f', 'q'), ('f', 'r'), ('f', 's'), ('f', 't'), ('f', 'u'), ('f', 'v'), ('f', 'w'), ('f', 'x'), ('f', 'y'), ('f', 'z'), ('f', 'A'), ('f', 'B'), ('f', 'C'), ('f', 'D'), ('f', 'E'), ('f', 'F'), ('f', 'G'), ('f', 'H'), ('f', 'I'), ('f', 'J'), ('f', 'K'), ('f', 'L'), ('f', 'M'), ('f', 'N'), ('f', 'O'), ('f', 'P'), ('f', 'Q'), ('f', 'R'), ('f', 'S'), ('f', 'T'), ('f', 'U'), ('f', 'V'), ('f', 'W'), ('f', 'X'), ('f', 'Y'), ('f', 'Z'), ('f', '0'), ('f', '1'), ('f', '2'), ('f', '3'), ('f', '4'), ('f', '5'), ('f', '6'), ('f', '7'), ('f', '8'), ('f', '9'), ('f', '!'), ('f', '"'), ('f', '#'), ('f', '$'), ('f', '%'), ('f', '&'), ('f', "'"), ('f', '('), ('f', ')'), ('f', '*'), ('f', '+'), ('f', ','), ('f', '-'), ('f', '.'), ('f', '/'), ('f', ':'), ('f', ';'), ('f', '<'), ('f', '='), ('f', '>'), ('f', '?'), ('f', '@'), ('f', '['), ('f', '\\'), ('f', ']'), ('f', '^'), ('f', '_'), ('f', '`'), ('f', '{'), ('f', '|'), ('f', '}'), ('f', '~'), ('g', 'a'), ('g', 'b'), ('g', 'c'), ('g', 'd'), ('g', 'e'), ('g', 'f'), ('g', 'g'), ('g', 'h'), ('g', 'i'), ('g', 'j'), ('g', 'k'), ('g', 'l'), ('g', 'm'), ('g', 'n'), ('g', 'o'), ('g', 'p'), ('g', 'q'), ('g', 'r'), ('g', 's'), ('g', 't'), ('g', 'u'), ('g', 'v'), ('g', 'w'), ('g', 'x'), ('g', 'y'), ('g', 'z'), ('g', 'A'), ('g', 'B'), ('g', 'C'), ('g', 'D'), ('g', 'E'), ('g', 'F'), ('g', 'G'), ('g', 'H'), ('g', 'I'), ('g', 'J'), ('g', 'K'), ('g', 'L'), ('g', 'M'), ('g', 'N'), ('g', 'O'), ('g', 'P'), ('g', 'Q'), ('g', 'R'), ('g', 'S'), ('g', 'T'), ('g', 'U'), ('g', 'V'), ('g', 'W'), ('g', 'X'), ('g', 'Y'), ('g', 'Z'), ('g', '0'), ('g', '1'), ('g', '2'), ('g', '3'), ('g', '4'), ('g', '5'), ('g', '6'), ('g', '7'), ('g', '8'), ('g', '9'), ('g', '!'), ('g', '"'), ('g', '#'), ('g', '$'), ('g', '%'), ('g', '&'), ('g', "'"), ('g', '('), ('g', ')'), ('g', '*'), ('g', '+'), ('g', ','), ('g', '-'), ('g', '.'), ('g', '/'), ('g', ':'), ('g', ';'), ('g', '<'), ('g', '='), ('g', '>'), ('g', '?'), ('g', '@'), ('g', '['), ('g', '\\'), ('g', ']'), ('g', '^'), ('g', '_'), ('g', '`'), ('g', '{'), ('g', '|'), ('g', '}'), ('g', '~'), ('h', 'a'), ('h', 'b'), ('h', 'c'), ('h', 'd'), ('h', 'e'), ('h', 'f'), ('h', 'g'), ('h', 'h'), ('h', 'i'), ('h', 'j'), ('h', 'k'), ('h', 'l'), ('h', 'm'), ('h', 'n'), ('h', 'o'), ('h', 'p'), ('h', 'q'), ('h', 'r'), ('h', 's'), ('h', 't'), ('h', 'u'), ('h', 'v'), ('h', 'w'), ('h', 'x'), ('h', 'y'), ('h', 'z'), ('h', 'A'), ('h', 'B'), ('h', 'C'), ('h', 'D'), ('h', 'E'), ('h', 'F'), ('h', 'G'), ('h', 'H'), ('h', 'I'), ('h', 'J'), ('h', 'K'), ('h', 'L'), ('h', 'M'), ('h', 'N'), ('h', 'O'), ('h', 'P'), ('h', 'Q'), ('h', 'R'), ('h', 'S'), ('h', 'T'), ('h', 'U'), ('h', 'V'), ('h', 'W'), ('h', 'X'), ('h', 'Y'), ('h', 'Z'), ('h', '0'), ('h', '1'), ('h', '2'), ('h', '3'), ('h', '4'), ('h', '5'), ('h', '6'), ('h', '7'), ('h', '8'), ('h', '9'), ('h', '!'), ('h', '"'), ('h', '#'), ('h', '$'), ('h', '%'), ('h', '&'), ('h', "'"), ('h', '('), ('h', ')'), ('h', '*'), ('h', '+'), ('h', ','), ('h', '-'), ('h', '.'), ('h', '/'), ('h', ':'), ('h', ';'), ('h', '<'), ('h', '='), ('h', '>'), ('h', '?'), ('h', '@'), ('h', '['), ('h', '\\'), ('h', ']'), ('h', '^'), ('h', '_'), ('h', '`'), ('h', '{'), ('h', '|'), ('h', '}'), ('h', '~'), ('i', 'a'), ('i', 'b'), ('i', 'c'), ('i', 'd'), ('i', 'e'), ('i', 'f'), ('i', 'g'), ('i', 'h'), ('i', 'i'), ('i', 'j'), ('i', 'k'), ('i', 'l'), ('i', 'm'), ('i', 'n'), ('i', 'o'), ('i', 'p'), ('i', 'q'), ('i', 'r'), ('i', 's'), ('i', 't'), ('i', 'u'), ('i', 'v'), ('i', 'w'), ('i', 'x'), ('i', 'y'), ('i', 'z'), ('i', 'A'), ('i', 'B'), ('i', 'C'), ('i', 'D'), ('i', 'E'), ('i', 'F'), ('i', 'G'), ('i', 'H'), ('i', 'I'), ('i', 'J'), ('i', 'K'), ('i', 'L'), ('i', 'M'), ('i', 'N'), ('i', 'O'), ('i', 'P'), ('i', 'Q'), ('i', 'R'), ('i', 'S'), ('i', 'T'), ('i', 'U'), ('i', 'V'), ('i', 'W'), ('i', 'X'), ('i', 'Y'), ('i', 'Z'), ('i', '0'), ('i', '1'), ('i', '2'), ('i', '3'), ('i', '4'), ('i', '5'), ('i', '6'), ('i', '7'), ('i', '8'), ('i', '9'), ('i', '!'), ('i', '"'), ('i', '#'), ('i', '$'), ('i', '%'), ('i', '&'), ('i', "'"), ('i', '('), ('i', ')'), ('i', '*'), ('i', '+'), ('i', ','), ('i', '-'), ('i', '.'), ('i', '/'), ('i', ':'), ('i', ';'), ('i', '<'), ('i', '='), ('i', '>'), ('i', '?'), ('i', '@'), ('i', '['), ('i', '\\'), ('i', ']'), ('i', '^'), ('i', '_'), ('i', '`'), ('i', '{'), ('i', '|'), ('i', '}'), ('i', '~'), ('j', 'a'), ('j', 'b'), ('j', 'c'), ('j', 'd'), ('j', 'e'), ('j', 'f'), ('j', 'g'), ('j', 'h'), ('j', 'i'), ('j', 'j'), ('j', 'k'), ('j', 'l'), ('j', 'm'), ('j', 'n'), ('j', 'o'), ('j', 'p'), ('j', 'q'), ('j', 'r'), ('j', 's'), ('j', 't'), ('j', 'u'), ('j', 'v'), ('j', 'w'), ('j', 'x'), ('j', 'y'), ('j', 'z'), ('j', 'A'), ('j', 'B'), ('j', 'C'), ('j', 'D'), ('j', 'E'), ('j', 'F'), ('j', 'G'), ('j', 'H'), ('j', 'I'), ('j', 'J'), ('j', 'K'), ('j', 'L'), ('j', 'M'), ('j', 'N'), ('j', 'O'), ('j', 'P'), ('j', 'Q'), ('j', 'R'), ('j', 'S'), ('j', 'T'), ('j', 'U'), ('j', 'V'), ('j', 'W'), ('j', 'X'), ('j', 'Y'), ('j', 'Z'), ('j', '0'), ('j', '1'), ('j', '2'), ('j', '3'), ('j', '4'), ('j', '5'), ('j', '6'), ('j', '7'), ('j', '8'), ('j', '9'), ('j', '!'), ('j', '"'), ('j', '#'), ('j', '$'), ('j', '%'), ('j', '&'), ('j', "'"), ('j', '('), ('j', ')'), ('j', '*'), ('j', '+'), ('j', ','), ('j', '-'), ('j', '.'), ('j', '/'), ('j', ':'), ('j', ';'), ('j', '<'), ('j', '='), ('j', '>'), ('j', '?'), ('j', '@'), ('j', '['), ('j', '\\'), ('j', ']'), ('j', '^'), ('j', '_'), ('j', '`'), ('j', '{'), ('j', '|'), ('j', '}'), ('j', '~'), ('k', 'a'), ('k', 'b'), ('k', 'c'), ('k', 'd'), ('k', 'e'), ('k', 'f'), ('k', 'g'), ('k', 'h'), ('k', 'i'), ('k', 'j'), ('k', 'k'), ('k', 'l'), ('k', 'm'), ('k', 'n'), ('k', 'o'), ('k', 'p'), ('k', 'q'), ('k', 'r'), ('k', 's'), ('k', 't'), ('k', 'u'), ('k', 'v'), ('k', 'w'), ('k', 'x'), ('k', 'y'), ('k', 'z'), ('k', 'A'), ('k', 'B'), ('k', 'C'), ('k', 'D'), ('k', 'E'), ('k', 'F'), ('k', 'G'), ('k', 'H'), ('k', 'I'), ('k', 'J'), ('k', 'K'), ('k', 'L'), ('k', 'M'), ('k', 'N'), ('k', 'O'), ('k', 'P'), ('k', 'Q'), ('k', 'R'), ('k', 'S'), ('k', 'T'), ('k', 'U'), ('k', 'V'), ('k', 'W'), ('k', 'X'), ('k', 'Y'), ('k', 'Z'), ('k', '0'), ('k', '1'), ('k', '2'), ('k', '3'), ('k', '4'), ('k', '5'), ('k', '6'), ('k', '7'), ('k', '8'), ('k', '9'), ('k', '!'), ('k', '"'), ('k', '#'), ('k', '$'), ('k', '%'), ('k', '&'), ('k', "'"), ('k', '('), ('k', ')'), ('k', '*'), ('k', '+'), ('k', ','), ('k', '-'), ('k', '.'), ('k', '/'), ('k', ':'), ('k', ';'), ('k', '<'), ('k', '='), ('k', '>'), ('k', '?'), ('k', '@'), ('k', '['), ('k', '\\'), ('k', ']'), ('k', '^'), ('k', '_'), ('k', '`'), ('k', '{'), ('k', '|'), ('k', '}'), ('k', '~'), ('l', 'a'), ('l', 'b'), ('l', 'c'), ('l', 'd'), ('l', 'e'), ('l', 'f'), ('l', 'g'), ('l', 'h'), ('l', 'i'), ('l', 'j'), ('l', 'k'), ('l', 'l'), ('l', 'm'), ('l', 'n'), ('l', 'o'), ('l', 'p'), ('l', 'q'), ('l', 'r'), ('l', 's'), ('l', 't'), ('l', 'u'), ('l', 'v'), ('l', 'w'), ('l', 'x'), ('l', 'y'), ('l', 'z'), ('l', 'A'), ('l', 'B'), ('l', 'C'), ('l', 'D'), ('l', 'E'), ('l', 'F'), ('l', 'G'), ('l', 'H'), ('l', 'I'), ('l', 'J'), ('l', 'K'), ('l', 'L'), ('l', 'M'), ('l', 'N'), ('l', 'O'), ('l', 'P'), ('l', 'Q'), ('l', 'R'), ('l', 'S'), ('l', 'T'), ('l', 'U'), ('l', 'V'), ('l', 'W'), ('l', 'X'), ('l', 'Y'), ('l', 'Z'), ('l', '0'), ('l', '1'), ('l', '2'), ('l', '3'), ('l', '4'), ('l', '5'), ('l', '6'), ('l', '7'), ('l', '8'), ('l', '9'), ('l', '!'), ('l', '"'), ('l', '#'), ('l', '$'), ('l', '%'), ('l', '&'), ('l', "'"), ('l', '('), ('l', ')'), ('l', '*'), ('l', '+'), ('l', ','), ('l', '-'), ('l', '.'), ('l', '/'), ('l', ':'), ('l', ';'), ('l', '<'), ('l', '='), ('l', '>'), ('l', '?'), ('l', '@'), ('l', '['), ('l', '\\'), ('l', ']'), ('l', '^'), ('l', '_'), ('l', '`'), ('l', '{'), ('l', '|'), ('l', '}'), ('l', '~'), ('m', 'a'), ('m', 'b'), ('m', 'c'), ('m', 'd'), ('m', 'e'), ('m', 'f'), ('m', 'g'), ('m', 'h'), ('m', 'i'), ('m', 'j'), ('m', 'k'), ('m', 'l'), ('m', 'm'), ('m', 'n'), ('m', 'o'), ('m', 'p'), ('m', 'q'), ('m', 'r'), ('m', 's'), ('m', 't'), ('m', 'u'), ('m', 'v'), ('m', 'w'), ('m', 'x'), ('m', 'y'), ('m', 'z'), ('m', 'A'), ('m', 'B'), ('m', 'C'), ('m', 'D'), ('m', 'E'), ('m', 'F'), ('m', 'G'), ('m', 'H'), ('m', 'I'), ('m', 'J'), ('m', 'K'), ('m', 'L'), ('m', 'M'), ('m', 'N'), ('m', 'O'), ('m', 'P'), ('m', 'Q'), ('m', 'R'), ('m', 'S'), ('m', 'T'), ('m', 'U'), ('m', 'V'), ('m', 'W'), ('m', 'X'), ('m', 'Y'), ('m', 'Z'), ('m', '0'), ('m', '1'), ('m', '2'), ('m', '3'), ('m', '4'), ('m', '5'), ('m', '6'), ('m', '7'), ('m', '8'), ('m', '9'), ('m', '!'), ('m', '"'), ('m', '#'), ('m', '$'), ('m', '%'), ('m', '&'), ('m', "'"), ('m', '('), ('m', ')'), ('m', '*'), ('m', '+'), ('m', ','), ('m', '-'), ('m', '.'), ('m', '/'), ('m', ':'), ('m', ';'), ('m', '<'), ('m', '='), ('m', '>'), ('m', '?'), ('m', '@'), ('m', '['), ('m', '\\'), ('m', ']'), ('m', '^'), ('m', '_'), ('m', '`'), ('m', '{'), ('m', '|'), ('m', '}'), ('m', '~'), ('n', 'a'), ('n', 'b'), ('n', 'c'), ('n', 'd'), ('n', 'e'), ('n', 'f'), ('n', 'g'), ('n', 'h'), ('n', 'i'), ('n', 'j'), ('n', 'k'), ('n', 'l'), ('n', 'm'), ('n', 'n'), ('n', 'o'), ('n', 'p'), ('n', 'q'), ('n', 'r'), ('n', 's'), ('n', 't'), ('n', 'u'), ('n', 'v'), ('n', 'w'), ('n', 'x'), ('n', 'y'), ('n', 'z'), ('n', 'A'), ('n', 'B'), ('n', 'C'), ('n', 'D'), ('n', 'E'), ('n', 'F'), ('n', 'G'), ('n', 'H'), ('n', 'I'), ('n', 'J'), ('n', 'K'), ('n', 'L'), ('n', 'M'), ('n', 'N'), ('n', 'O'), ('n', 'P'), ('n', 'Q'), ('n', 'R'), ('n', 'S'), ('n', 'T'), ('n', 'U'), ('n', 'V'), ('n', 'W'), ('n', 'X'), ('n', 'Y'), ('n', 'Z'), ('n', '0'), ('n', '1'), ('n', '2'), ('n', '3'), ('n', '4'), ('n', '5'), ('n', '6'), ('n', '7'), ('n', '8'), ('n', '9'), ('n', '!'), ('n', '"'), ('n', '#'), ('n', '$'), ('n', '%'), ('n', '&'), ('n', "'"), ('n', '('), ('n', ')'), ('n', '*'), ('n', '+'), ('n', ','), ('n', '-'), ('n', '.'), ('n', '/'), ('n', ':'), ('n', ';'), ('n', '<'), ('n', '='), ('n', '>'), ('n', '?'), ('n', '@'), ('n', '['), ('n', '\\'), ('n', ']'), ('n', '^'), ('n', '_'), ('n', '`'), ('n', '{'), ('n', '|'), ('n', '}'), ('n', '~'), ('o', 'a'), ('o', 'b'), ('o', 'c'), ('o', 'd'), ('o', 'e'), ('o', 'f'), ('o', 'g'), ('o', 'h'), ('o', 'i'), ('o', 'j'), ('o', 'k'), ('o', 'l'), ('o', 'm'), ('o', 'n'), ('o', 'o'), ('o', 'p'), ('o', 'q'), ('o', 'r'), ('o', 's'), ('o', 't'), ('o', 'u'), ('o', 'v'), ('o', 'w'), ('o', 'x'), ('o', 'y'), ('o', 'z'), ('o', 'A'), ('o', 'B'), ('o', 'C'), ('o', 'D'), ('o', 'E'), ('o', 'F'), ('o', 'G'), ('o', 'H'), ('o', 'I'), ('o', 'J'), ('o', 'K'), ('o', 'L'), ('o', 'M'), ('o', 'N'), ('o', 'O'), ('o', 'P'), ('o', 'Q'), ('o', 'R'), ('o', 'S'), ('o', 'T'), ('o', 'U'), ('o', 'V'), ('o', 'W'), ('o', 'X'), ('o', 'Y'), ('o', 'Z'), ('o', '0'), ('o', '1'), ('o', '2'), ('o', '3'), ('o', '4'), ('o', '5'), ('o', '6'), ('o', '7'), ('o', '8'), ('o', '9'), ('o', '!'), ('o', '"'), ('o', '#'), ('o', '$'), ('o', '%'), ('o', '&'), ('o', "'"), ('o', '('), ('o', ')'), ('o', '*'), ('o', '+'), ('o', ','), ('o', '-'), ('o', '.'), ('o', '/'), ('o', ':'), ('o', ';'), ('o', '<'), ('o', '='), ('o', '>'), ('o', '?'), ('o', '@'), ('o', '['), ('o', '\\'), ('o', ']'), ('o', '^'), ('o', '_'), ('o', '`'), ('o', '{'), ('o', '|'), ('o', '}'), ('o', '~'), ('p', 'a'), ('p', 'b'), ('p', 'c'), ('p', 'd'), ('p', 'e'), ('p', 'f'), ('p', 'g'), ('p', 'h'), ('p', 'i'), ('p', 'j'), ('p', 'k'), ('p', 'l'), ('p', 'm'), ('p', 'n'), ('p', 'o'), ('p', 'p'), ('p', 'q'), ('p', 'r'), ('p', 's'), ('p', 't'), ('p', 'u'), ('p', 'v'), ('p', 'w'), ('p', 'x'), ('p', 'y'), ('p', 'z'), ('p', 'A'), ('p', 'B'), ('p', 'C'), ('p', 'D'), ('p', 'E'), ('p', 'F'), ('p', 'G'), ('p', 'H'), ('p', 'I'), ('p', 'J'), ('p', 'K'), ('p', 'L'), ('p', 'M'), ('p', 'N'), ('p', 'O'), ('p', 'P'), ('p', 'Q'), ('p', 'R'), ('p', 'S'), ('p', 'T'), ('p', 'U'), ('p', 'V'), ('p', 'W'), ('p', 'X'), ('p', 'Y'), ('p', 'Z'), ('p', '0'), ('p', '1'), ('p', '2'), ('p', '3'), ('p', '4'), ('p', '5'), ('p', '6'), ('p', '7'), ('p', '8'), ('p', '9'), ('p', '!'), ('p', '"'), ('p', '#'), ('p', '$'), ('p', '%'), ('p', '&'), ('p', "'"), ('p', '('), ('p', ')'), ('p', '*'), ('p', '+'), ('p', ','), ('p', '-'), ('p', '.'), ('p', '/'), ('p', ':'), ('p', ';'), ('p', '<'), ('p', '='), ('p', '>'), ('p', '?'), ('p', '@'), ('p', '['), ('p', '\\'), ('p', ']'), ('p', '^'), ('p', '_'), ('p', '`'), ('p', '{'), ('p', '|'), ('p', '}'), ('p', '~'), ('q', 'a'), ('q', 'b'), ('q', 'c'), ('q', 'd'), ('q', 'e'), ('q', 'f'), ('q', 'g'), ('q', 'h'), ('q', 'i'), ('q', 'j'), ('q', 'k'), ('q', 'l'), ('q', 'm'), ('q', 'n'), ('q', 'o'), ('q', 'p'), ('q', 'q'), ('q', 'r'), ('q', 's'), ('q', 't'), ('q', 'u'), ('q', 'v'), ('q', 'w'), ('q', 'x'), ('q', 'y'), ('q', 'z'), ('q', 'A'), ('q', 'B'), ('q', 'C'), ('q', 'D'), ('q', 'E'), ('q', 'F'), ('q', 'G'), ('q', 'H'), ('q', 'I'), ('q', 'J'), ('q', 'K'), ('q', 'L'), ('q', 'M'), ('q', 'N'), ('q', 'O'), ('q', 'P'), ('q', 'Q'), ('q', 'R'), ('q', 'S'), ('q', 'T'), ('q', 'U'), ('q', 'V'), ('q', 'W'), ('q', 'X'), ('q', 'Y'), ('q', 'Z'), ('q', '0'), ('q', '1'), ('q', '2'), ('q', '3'), ('q', '4'), ('q', '5'), ('q', '6'), ('q', '7'), ('q', '8'), ('q', '9'), ('q', '!'), ('q', '"'), ('q', '#'), ('q', '$'), ('q', '%'), ('q', '&'), ('q', "'"), ('q', '('), ('q', ')'), ('q', '*'), ('q', '+'), ('q', ','), ('q', '-'), ('q', '.'), ('q', '/'), ('q', ':'), ('q', ';'), ('q', '<'), ('q', '='), ('q', '>'), ('q', '?'), ('q', '@'), ('q', '['), ('q', '\\'), ('q', ']'), ('q', '^'), ('q', '_'), ('q', '`'), ('q', '{'), ('q', '|'), ('q', '}'), ('q', '~'), ('r', 'a'), ('r', 'b'), ('r', 'c'), ('r', 'd'), ('r', 'e'), ('r', 'f'), ('r', 'g'), ('r', 'h'), ('r', 'i'), ('r', 'j'), ('r', 'k'), ('r', 'l'), ('r', 'm'), ('r', 'n'), ('r', 'o'), ('r', 'p'), ('r', 'q'), ('r', 'r'), ('r', 's'), ('r', 't'), ('r', 'u'), ('r', 'v'), ('r', 'w'), ('r', 'x'), ('r', 'y'), ('r', 'z'), ('r', 'A'), ('r', 'B'), ('r', 'C'), ('r', 'D'), ('r', 'E'), ('r', 'F'), ('r', 'G'), ('r', 'H'), ('r', 'I'), ('r', 'J'), ('r', 'K'), ('r', 'L'), ('r', 'M'), ('r', 'N'), ('r', 'O'), ('r', 'P'), ('r', 'Q'), ('r', 'R'), ('r', 'S'), ('r', 'T'), ('r', 'U'), ('r', 'V'), ('r', 'W'), ('r', 'X'), ('r', 'Y'), ('r', 'Z'), ('r', '0'), ('r', '1'), ('r', '2'), ('r', '3'), ('r', '4'), ('r', '5'), ('r', '6'), ('r', '7'), ('r', '8'), ('r', '9'), ('r', '!'), ('r', '"'), ('r', '#'), ('r', '$'), ('r', '%'), ('r', '&'), ('r', "'"), ('r', '('), ('r', ')'), ('r', '*'), ('r', '+'), ('r', ','), ('r', '-'), ('r', '.'), ('r', '/'), ('r', ':'), ('r', ';'), ('r', '<'), ('r', '='), ('r', '>'), ('r', '?'), ('r', '@'), ('r', '['), ('r', '\\'), ('r', ']'), ('r', '^'), ('r', '_'), ('r', '`'), ('r', '{'), ('r', '|'), ('r', '}'), ('r', '~'), ('s', 'a'), ('s', 'b'), ('s', 'c'), ('s', 'd'), ('s', 'e'), ('s', 'f'), ('s', 'g'), ('s', 'h'), ('s', 'i'), ('s', 'j'), ('s', 'k'), ('s', 'l'), ('s', 'm'), ('s', 'n'), ('s', 'o'), ('s', 'p'), ('s', 'q'), ('s', 'r'), ('s', 's'), ('s', 't'), ('s', 'u'), ('s', 'v'), ('s', 'w'), ('s', 'x'), ('s', 'y'), ('s', 'z'), ('s', 'A'), ('s', 'B'), ('s', 'C'), ('s', 'D'), ('s', 'E'), ('s', 'F'), ('s', 'G'), ('s', 'H'), ('s', 'I'), ('s', 'J'), ('s', 'K'), ('s', 'L'), ('s', 'M'), ('s', 'N'), ('s', 'O'), ('s', 'P'), ('s', 'Q'), ('s', 'R'), ('s', 'S'), ('s', 'T'), ('s', 'U'), ('s', 'V'), ('s', 'W'), ('s', 'X'), ('s', 'Y'), ('s', 'Z'), ('s', '0'), ('s', '1'), ('s', '2'), ('s', '3'), ('s', '4'), ('s', '5'), ('s', '6'), ('s', '7'), ('s', '8'), ('s', '9'), ('s', '!'), ('s', '"'), ('s', '#'), ('s', '$'), ('s', '%'), ('s', '&'), ('s', "'"), ('s', '('), ('s', ')'), ('s', '*'), ('s', '+'), ('s', ','), ('s', '-'), ('s', '.'), ('s', '/'), ('s', ':'), ('s', ';'), ('s', '<'), ('s', '='), ('s', '>'), ('s', '?'), ('s', '@'), ('s', '['), ('s', '\\'), ('s', ']'), ('s', '^'), ('s', '_'), ('s', '`'), ('s', '{'), ('s', '|'), ('s', '}'), ('s', '~'), ('t', 'a'), ('t', 'b'), ('t', 'c'), ('t', 'd'), ('t', 'e'), ('t', 'f'), ('t', 'g'), ('t', 'h'), ('t', 'i'), ('t', 'j'), ('t', 'k'), ('t', 'l'), ('t', 'm'), ('t', 'n'), ('t', 'o'), ('t', 'p'), ('t', 'q'), ('t', 'r'), ('t', 's'), ('t', 't'), ('t', 'u'), ('t', 'v'), ('t', 'w'), ('t', 'x'), ('t', 'y'), ('t', 'z'), ('t', 'A'), ('t', 'B'), ('t', 'C'), ('t', 'D'), ('t', 'E'), ('t', 'F'), ('t', 'G'), ('t', 'H'), ('t', 'I'), ('t', 'J'), ('t', 'K'), ('t', 'L'), ('t', 'M'), ('t', 'N'), ('t', 'O'), ('t', 'P'), ('t', 'Q'), ('t', 'R'), ('t', 'S'), ('t', 'T'), ('t', 'U'), ('t', 'V'), ('t', 'W'), ('t', 'X'), ('t', 'Y'), ('t', 'Z'), ('t', '0'), ('t', '1'), ('t', '2'), ('t', '3'), ('t', '4'), ('t', '5'), ('t', '6'), ('t', '7'), ('t', '8'), ('t', '9'), ('t', '!'), ('t', '"'), ('t', '#'), ('t', '$'), ('t', '%'), ('t', '&'), ('t', "'"), ('t', '('), ('t', ')'), ('t', '*'), ('t', '+'), ('t', ','), ('t', '-'), ('t', '.'), ('t', '/'), ('t', ':'), ('t', ';'), ('t', '<'), ('t', '='), ('t', '>'), ('t', '?'), ('t', '@'), ('t', '['), ('t', '\\'), ('t', ']'), ('t', '^'), ('t', '_'), ('t', '`'), ('t', '{'), ('t', '|'), ('t', '}'), ('t', '~'), ('u', 'a'), ('u', 'b'), ('u', 'c'), ('u', 'd'), ('u', 'e'), ('u', 'f'), ('u', 'g'), ('u', 'h'), ('u', 'i'), ('u', 'j'), ('u', 'k'), ('u', 'l'), ('u', 'm'), ('u', 'n'), ('u', 'o'), ('u', 'p'), ('u', 'q'), ('u', 'r'), ('u', 's'), ('u', 't'), ('u', 'u'), ('u', 'v'), ('u', 'w'), ('u', 'x'), ('u', 'y'), ('u', 'z'), ('u', 'A'), ('u', 'B'), ('u', 'C'), ('u', 'D'), ('u', 'E'), ('u', 'F'), ('u', 'G'), ('u', 'H'), ('u', 'I'), ('u', 'J'), ('u', 'K'), ('u', 'L'), ('u', 'M'), ('u', 'N'), ('u', 'O'), ('u', 'P'), ('u', 'Q'), ('u', 'R'), ('u', 'S'), ('u', 'T'), ('u', 'U'), ('u', 'V'), ('u', 'W'), ('u', 'X'), ('u', 'Y'), ('u', 'Z'), ('u', '0'), ('u', '1'), ('u', '2'), ('u', '3'), ('u', '4'), ('u', '5'), ('u', '6'), ('u', '7'), ('u', '8'), ('u', '9'), ('u', '!'), ('u', '"'), ('u', '#'), ('u', '$'), ('u', '%'), ('u', '&'), ('u', "'"), ('u', '('), ('u', ')'), ('u', '*'), ('u', '+'), ('u', ','), ('u', '-'), ('u', '.'), ('u', '/'), ('u', ':'), ('u', ';'), ('u', '<'), ('u', '='), ('u', '>'), ('u', '?'), ('u', '@'), ('u', '['), ('u', '\\'), ('u', ']'), ('u', '^'), ('u', '_'), ('u', '`'), ('u', '{'), ('u', '|'), ('u', '}'), ('u', '~'), ('v', 'a'), ('v', 'b'), ('v', 'c'), ('v', 'd'), ('v', 'e'), ('v', 'f'), ('v', 'g'), ('v', 'h'), ('v', 'i'), ('v', 'j'), ('v', 'k'), ('v', 'l'), ('v', 'm'), ('v', 'n'), ('v', 'o'), ('v', 'p'), ('v', 'q'), ('v', 'r'), ('v', 's'), ('v', 't'), ('v', 'u'), ('v', 'v'), ('v', 'w'), ('v', 'x'), ('v', 'y'), ('v', 'z'), ('v', 'A'), ('v', 'B'), ('v', 'C'), ('v', 'D'), ('v', 'E'), ('v', 'F'), ('v', 'G'), ('v', 'H'), ('v', 'I'), ('v', 'J'), ('v', 'K'), ('v', 'L'), ('v', 'M'), ('v', 'N'), ('v', 'O'), ('v', 'P'), ('v', 'Q'), ('v', 'R'), ('v', 'S'), ('v', 'T'), ('v', 'U'), ('v', 'V'), ('v', 'W'), ('v', 'X'), ('v', 'Y'), ('v', 'Z'), ('v', '0'), ('v', '1'), ('v', '2'), ('v', '3'), ('v', '4'), ('v', '5'), ('v', '6'), ('v', '7'), ('v', '8'), ('v', '9'), ('v', '!'), ('v', '"'), ('v', '#'), ('v', '$'), ('v', '%'), ('v', '&'), ('v', "'"), ('v', '('), ('v', ')'), ('v', '*'), ('v', '+'), ('v', ','), ('v', '-'), ('v', '.'), ('v', '/'), ('v', ':'), ('v', ';'), ('v', '<'), ('v', '='), ('v', '>'), ('v', '?'), ('v', '@'), ('v', '['), ('v', '\\'), ('v', ']'), ('v', '^'), ('v', '_'), ('v', '`'), ('v', '{'), ('v', '|'), ('v', '}'), ('v', '~'), ('w', 'a'), ('w', 'b'), ('w', 'c'), ('w', 'd'), ('w', 'e'), ('w', 'f'), ('w', 'g'), ('w', 'h'), ('w', 'i'), ('w', 'j'), ('w', 'k'), ('w', 'l'), ('w', 'm'), ('w', 'n'), ('w', 'o'), ('w', 'p'), ('w', 'q'), ('w', 'r'), ('w', 's'), ('w', 't'), ('w', 'u'), ('w', 'v'), ('w', 'w'), ('w', 'x'), ('w', 'y'), ('w', 'z'), ('w', 'A'), ('w', 'B'), ('w', 'C'), ('w', 'D'), ('w', 'E'), ('w', 'F'), ('w', 'G'), ('w', 'H'), ('w', 'I'), ('w', 'J'), ('w', 'K'), ('w', 'L'), ('w', 'M'), ('w', 'N'), ('w', 'O'), ('w', 'P'), ('w', 'Q'), ('w', 'R'), ('w', 'S'), ('w', 'T'), ('w', 'U'), ('w', 'V'), ('w', 'W'), ('w', 'X'), ('w', 'Y'), ('w', 'Z'), ('w', '0'), ('w', '1'), ('w', '2'), ('w', '3'), ('w', '4'), ('w', '5'), ('w', '6'), ('w', '7'), ('w', '8'), ('w', '9'), ('w', '!'), ('w', '"'), ('w', '#'), ('w', '$'), ('w', '%'), ('w', '&'), ('w', "'"), ('w', '('), ('w', ')'), ('w', '*'), ('w', '+'), ('w', ','), ('w', '-'), ('w', '.'), ('w', '/'), ('w', ':'), ('w', ';'), ('w', '<'), ('w', '='), ('w', '>'), ('w', '?'), ('w', '@'), ('w', '['), ('w', '\\'), ('w', ']'), ('w', '^'), ('w', '_'), ('w', '`'), ('w', '{'), ('w', '|'), ('w', '}'), ('w', '~'), ('x', 'a'), ('x', 'b'), ('x', 'c'), ('x', 'd'), ('x', 'e'), ('x', 'f'), ('x', 'g'), ('x', 'h'), ('x', 'i'), ('x', 'j'), ('x', 'k'), ('x', 'l'), ('x', 'm'), ('x', 'n'), ('x', 'o'), ('x', 'p'), ('x', 'q'), ('x', 'r'), ('x', 's'), ('x', 't'), ('x', 'u'), ('x', 'v'), ('x', 'w'), ('x', 'x'), ('x', 'y'), ('x', 'z'), ('x', 'A'), ('x', 'B'), ('x', 'C'), ('x', 'D'), ('x', 'E'), ('x', 'F'), ('x', 'G'), ('x', 'H'), ('x', 'I'), ('x', 'J'), ('x', 'K'), ('x', 'L'), ('x', 'M'), ('x', 'N'), ('x', 'O'), ('x', 'P'), ('x', 'Q'), ('x', 'R'), ('x', 'S'), ('x', 'T'), ('x', 'U'), ('x', 'V'), ('x', 'W'), ('x', 'X'), ('x', 'Y'), ('x', 'Z'), ('x', '0'), ('x', '1'), ('x', '2'), ('x', '3'), ('x', '4'), ('x', '5'), ('x', '6'), ('x', '7'), ('x', '8'), ('x', '9'), ('x', '!'), ('x', '"'), ('x', '#'), ('x', '$'), ('x', '%'), ('x', '&'), ('x', "'"), ('x', '('), ('x', ')'), ('x', '*'), ('x', '+'), ('x', ','), ('x', '-'), ('x', '.'), ('x', '/'), ('x', ':'), ('x', ';'), ('x', '<'), ('x', '='), ('x', '>'), ('x', '?'), ('x', '@'), ('x', '['), ('x', '\\'), ('x', ']'), ('x', '^'), ('x', '_'), ('x', '`'), ('x', '{'), ('x', '|'), ('x', '}'), ('x', '~'), ('y', 'a'), ('y', 'b'), ('y', 'c'), ('y', 'd'), ('y', 'e'), ('y', 'f'), ('y', 'g'), ('y', 'h'), ('y', 'i'), ('y', 'j'), ('y', 'k'), ('y', 'l'), ('y', 'm'), ('y', 'n'), ('y', 'o'), ('y', 'p'), ('y', 'q'), ('y', 'r'), ('y', 's'), ('y', 't'), ('y', 'u'), ('y', 'v'), ('y', 'w'), ('y', 'x'), ('y', 'y'), ('y', 'z'), ('y', 'A'), ('y', 'B'), ('y', 'C'), ('y', 'D'), ('y', 'E'), ('y', 'F'), ('y', 'G'), ('y', 'H'), ('y', 'I'), ('y', 'J'), ('y', 'K'), ('y', 'L'), ('y', 'M'), ('y', 'N'), ('y', 'O'), ('y', 'P'), ('y', 'Q'), ('y', 'R'), ('y', 'S'), ('y', 'T'), ('y', 'U'), ('y', 'V'), ('y', 'W'), ('y', 'X'), ('y', 'Y'), ('y', 'Z'), ('y', '0'), ('y', '1'), ('y', '2'), ('y', '3'), ('y', '4'), ('y', '5'), ('y', '6'), ('y', '7'), ('y', '8'), ('y', '9'), ('y', '!'), ('y', '"'), ('y', '#'), ('y', '$'), ('y', '%'), ('y', '&'), ('y', "'"), ('y', '('), ('y', ')'), ('y', '*'), ('y', '+'), ('y', ','), ('y', '-'), ('y', '.'), ('y', '/'), ('y', ':'), ('y', ';'), ('y', '<'), ('y', '='), ('y', '>'), ('y', '?'), ('y', '@'), ('y', '['), ('y', '\\'), ('y', ']'), ('y', '^'), ('y', '_'), ('y', '`'), ('y', '{'), ('y', '|'), ('y', '}'), ('y', '~'), ('z', 'a'), ('z', 'b'), ('z', 'c'), ('z', 'd'), ('z', 'e'), ('z', 'f'), ('z', 'g'), ('z', 'h'), ('z', 'i'), ('z', 'j'), ('z', 'k'), ('z', 'l'), ('z', 'm'), ('z', 'n'), ('z', 'o'), ('z', 'p'), ('z', 'q'), ('z', 'r'), ('z', 's'), ('z', 't'), ('z', 'u'), ('z', 'v'), ('z', 'w'), ('z', 'x'), ('z', 'y'), ('z', 'z'), ('z', 'A'), ('z', 'B'), ('z', 'C'), ('z', 'D'), ('z', 'E'), ('z', 'F'), ('z', 'G'), ('z', 'H'), ('z', 'I'), ('z', 'J'), ('z', 'K'), ('z', 'L'), ('z', 'M'), ('z', 'N'), ('z', 'O'), ('z', 'P'), ('z', 'Q'), ('z', 'R'), ('z', 'S'), ('z', 'T'), ('z', 'U'), ('z', 'V'), ('z', 'W'), ('z', 'X'), ('z', 'Y'), ('z', 'Z'), ('z', '0'), ('z', '1'), ('z', '2'), ('z', '3'), ('z', '4'), ('z', '5'), ('z', '6'), ('z', '7'), ('z', '8'), ('z', '9'), ('z', '!'), ('z', '"'), ('z', '#'), ('z', '$'), ('z', '%'), ('z', '&'), ('z', "'"), ('z', '('), ('z', ')'), ('z', '*'), ('z', '+'), ('z', ','), ('z', '-'), ('z', '.'), ('z', '/'), ('z', ':'), ('z', ';'), ('z', '<'), ('z', '='), ('z', '>'), ('z', '?'), ('z', '@'), ('z', '['), ('z', '\\'), ('z', ']'), ('z', '^'), ('z', '_'), ('z', '`'), ('z', '{'), ('z', '|'), ('z', '}'), ('z', '~'), ('A', 'a'), ('A', 'b'), ('A', 'c'), ('A', 'd'), ('A', 'e'), ('A', 'f'), ('A', 'g'), ('A', 'h'), ('A', 'i'), ('A', 'j'), ('A', 'k'), ('A', 'l'), ('A', 'm'), ('A', 'n'), ('A', 'o'), ('A', 'p'), ('A', 'q'), ('A', 'r'), ('A', 's'), ('A', 't'), ('A', 'u'), ('A', 'v'), ('A', 'w'), ('A', 'x'), ('A', 'y'), ('A', 'z'), ('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('A', 'F'), ('A', 'G'), ('A', 'H'), ('A', 'I'), ('A', 'J'), ('A', 'K'), ('A', 'L'), ('A', 'M'), ('A', 'N'), ('A', 'O'), ('A', 'P'), ('A', 'Q'), ('A', 'R'), ('A', 'S'), ('A', 'T'), ('A', 'U'), ('A', 'V'), ('A', 'W'), ('A', 'X'), ('A', 'Y'), ('A', 'Z'), ('A', '0'), ('A', '1'), ('A', '2'), ('A', '3'), ('A', '4'), ('A', '5'), ('A', '6'), ('A', '7'), ('A', '8'), ('A', '9'), ('A', '!'), ('A', '"'), ('A', '#'), ('A', '$'), ('A', '%'), ('A', '&'), ('A', "'"), ('A', '('), ('A', ')'), ('A', '*'), ('A', '+'), ('A', ','), ('A', '-'), ('A', '.'), ('A', '/'), ('A', ':'), ('A', ';'), ('A', '<'), ('A', '='), ('A', '>'), ('A', '?'), ('A', '@'), ('A', '['), ('A', '\\'), ('A', ']'), ('A', '^'), ('A', '_'), ('A', '`'), ('A', '{'), ('A', '|'), ('A', '}'), ('A', '~'), ('B', 'a'), ('B', 'b'), ('B', 'c'), ('B', 'd'), ('B', 'e'), ('B', 'f'), ('B', 'g'), ('B', 'h'), ('B', 'i'), ('B', 'j'), ('B', 'k'), ('B', 'l'), ('B', 'm'), ('B', 'n'), ('B', 'o'), ('B', 'p'), ('B', 'q'), ('B', 'r'), ('B', 's'), ('B', 't'), ('B', 'u'), ('B', 'v'), ('B', 'w'), ('B', 'x'), ('B', 'y'), ('B', 'z'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('B', 'F'), ('B', 'G'), ('B', 'H'), ('B', 'I'), ('B', 'J'), ('B', 'K'), ('B', 'L'), ('B', 'M'), ('B', 'N'), ('B', 'O'), ('B', 'P'), ('B', 'Q'), ('B', 'R'), ('B', 'S'), ('B', 'T'), ('B', 'U'), ('B', 'V'), ('B', 'W'), ('B', 'X'), ('B', 'Y'), ('B', 'Z'), ('B', '0'), ('B', '1'), ('B', '2'), ('B', '3'), ('B', '4'), ('B', '5'), ('B', '6'), ('B', '7'), ('B', '8'), ('B', '9'), ('B', '!'), ('B', '"'), ('B', '#'), ('B', '$'), ('B', '%'), ('B', '&'), ('B', "'"), ('B', '('), ('B', ')'), ('B', '*'), ('B', '+'), ('B', ','), ('B', '-'), ('B', '.'), ('B', '/'), ('B', ':'), ('B', ';'), ('B', '<'), ('B', '='), ('B', '>'), ('B', '?'), ('B', '@'), ('B', '['), ('B', '\\'), ('B', ']'), ('B', '^'), ('B', '_'), ('B', '`'), ('B', '{'), ('B', '|'), ('B', '}'), ('B', '~'), ('C', 'a'), ('C', 'b'), ('C', 'c'), ('C', 'd'), ('C', 'e'), ('C', 'f'), ('C', 'g'), ('C', 'h'), ('C', 'i'), ('C', 'j'), ('C', 'k'), ('C', 'l'), ('C', 'm'), ('C', 'n'), ('C', 'o'), ('C', 'p'), ('C', 'q'), ('C', 'r'), ('C', 's'), ('C', 't'), ('C', 'u'), ('C', 'v'), ('C', 'w'), ('C', 'x'), ('C', 'y'), ('C', 'z'), ('C', 'A'), ('C', 'B'), ('C', 'C'), ('C', 'D'), ('C', 'E'), ('C', 'F'), ('C', 'G'), ('C', 'H'), ('C', 'I'), ('C', 'J'), ('C', 'K'), ('C', 'L'), ('C', 'M'), ('C', 'N'), ('C', 'O'), ('C', 'P'), ('C', 'Q'), ('C', 'R'), ('C', 'S'), ('C', 'T'), ('C', 'U'), ('C', 'V'), ('C', 'W'), ('C', 'X'), ('C', 'Y'), ('C', 'Z'), ('C', '0'), ('C', '1'), ('C', '2'), ('C', '3'), ('C', '4'), ('C', '5'), ('C', '6'), ('C', '7'), ('C', '8'), ('C', '9'), ('C', '!'), ('C', '"'), ('C', '#'), ('C', '$'), ('C', '%'), ('C', '&'), ('C', "'"), ('C', '('), ('C', ')'), ('C', '*'), ('C', '+'), ('C', ','), ('C', '-'), ('C', '.'), ('C', '/'), ('C', ':'), ('C', ';'), ('C', '<'), ('C', '='), ('C', '>'), ('C', '?'), ('C', '@'), ('C', '['), ('C', '\\'), ('C', ']'), ('C', '^'), ('C', '_'), ('C', '`'), ('C', '{'), ('C', '|'), ('C', '}'), ('C', '~'), ('D', 'a'), ('D', 'b'), ('D', 'c'), ('D', 'd'), ('D', 'e'), ('D', 'f'), ('D', 'g'), ('D', 'h'), ('D', 'i'), ('D', 'j'), ('D', 'k'), ('D', 'l'), ('D', 'm'), ('D', 'n'), ('D', 'o'), ('D', 'p'), ('D', 'q'), ('D', 'r'), ('D', 's'), ('D', 't'), ('D', 'u'), ('D', 'v'), ('D', 'w'), ('D', 'x'), ('D', 'y'), ('D', 'z'), ('D', 'A'), ('D', 'B'), ('D', 'C'), ('D', 'D'), ('D', 'E'), ('D', 'F'), ('D', 'G'), ('D', 'H'), ('D', 'I'), ('D', 'J'), ('D', 'K'), ('D', 'L'), ('D', 'M'), ('D', 'N'), ('D', 'O'), ('D', 'P'), ('D', 'Q'), ('D', 'R'), ('D', 'S'), ('D', 'T'), ('D', 'U'), ('D', 'V'), ('D', 'W'), ('D', 'X'), ('D', 'Y'), ('D', 'Z'), ('D', '0'), ('D', '1'), ('D', '2'), ('D', '3'), ('D', '4'), ('D', '5'), ('D', '6'), ('D', '7'), ('D', '8'), ('D', '9'), ('D', '!'), ('D', '"'), ('D', '#'), ('D', '$'), ('D', '%'), ('D', '&'), ('D', "'"), ('D', '('), ('D', ')'), ('D', '*'), ('D', '+'), ('D', ','), ('D', '-'), ('D', '.'), ('D', '/'), ('D', ':'), ('D', ';'), ('D', '<'), ('D', '='), ('D', '>'), ('D', '?'), ('D', '@'), ('D', '['), ('D', '\\'), ('D', ']'), ('D', '^'), ('D', '_'), ('D', '`'), ('D', '{'), ('D', '|'), ('D', '}'), ('D', '~'), ('E', 'a'), ('E', 'b'), ('E', 'c'), ('E', 'd'), ('E', 'e'), ('E', 'f'), ('E', 'g'), ('E', 'h'), ('E', 'i'), ('E', 'j'), ('E', 'k'), ('E', 'l'), ('E', 'm'), ('E', 'n'), ('E', 'o'), ('E', 'p'), ('E', 'q'), ('E', 'r'), ('E', 's'), ('E', 't'), ('E', 'u'), ('E', 'v'), ('E', 'w'), ('E', 'x'), ('E', 'y'), ('E', 'z'), ('E', 'A'), ('E', 'B'), ('E', 'C'), ('E', 'D'), ('E', 'E'), ('E', 'F'), ('E', 'G'), ('E', 'H'), ('E', 'I'), ('E', 'J'), ('E', 'K'), ('E', 'L'), ('E', 'M'), ('E', 'N'), ('E', 'O'), ('E', 'P'), ('E', 'Q'), ('E', 'R'), ('E', 'S'), ('E', 'T'), ('E', 'U'), ('E', 'V'), ('E', 'W'), ('E', 'X'), ('E', 'Y'), ('E', 'Z'), ('E', '0'), ('E', '1'), ('E', '2'), ('E', '3'), ('E', '4'), ('E', '5'), ('E', '6'), ('E', '7'), ('E', '8'), ('E', '9'), ('E', '!'), ('E', '"'), ('E', '#'), ('E', '$'), ('E', '%'), ('E', '&'), ('E', "'"), ('E', '('), ('E', ')'), ('E', '*'), ('E', '+'), ('E', ','), ('E', '-'), ('E', '.'), ('E', '/'), ('E', ':'), ('E', ';'), ('E', '<'), ('E', '='), ('E', '>'), ('E', '?'), ('E', '@'), ('E', '['), ('E', '\\'), ('E', ']'), ('E', '^'), ('E', '_'), ('E', '`'), ('E', '{'), ('E', '|'), ('E', '}'), ('E', '~'), ('F', 'a'), ('F', 'b'), ('F', 'c'), ('F', 'd'), ('F', 'e'), ('F', 'f'), ('F', 'g'), ('F', 'h'), ('F', 'i'), ('F', 'j'), ('F', 'k'), ('F', 'l'), ('F', 'm'), ('F', 'n'), ('F', 'o'), ('F', 'p'), ('F', 'q'), ('F', 'r'), ('F', 's'), ('F', 't'), ('F', 'u'), ('F', 'v'), ('F', 'w'), ('F', 'x'), ('F', 'y'), ('F', 'z'), ('F', 'A'), ('F', 'B'), ('F', 'C'), ('F', 'D'), ('F', 'E'), ('F', 'F'), ('F', 'G'), ('F', 'H'), ('F', 'I'), ('F', 'J'), ('F', 'K'), ('F', 'L'), ('F', 'M'), ('F', 'N'), ('F', 'O'), ('F', 'P'), ('F', 'Q'), ('F', 'R'), ('F', 'S'), ('F', 'T'), ('F', 'U'), ('F', 'V'), ('F', 'W'), ('F', 'X'), ('F', 'Y'), ('F', 'Z'), ('F', '0'), ('F', '1'), ('F', '2'), ('F', '3'), ('F', '4'), ('F', '5'), ('F', '6'), ('F', '7'), ('F', '8'), ('F', '9'), ('F', '!'), ('F', '"'), ('F', '#'), ('F', '$'), ('F', '%'), ('F', '&'), ('F', "'"), ('F', '('), ('F', ')'), ('F', '*'), ('F', '+'), ('F', ','), ('F', '-'), ('F', '.'), ('F', '/'), ('F', ':'), ('F', ';'), ('F', '<'), ('F', '='), ('F', '>'), ('F', '?'), ('F', '@'), ('F', '['), ('F', '\\'), ('F', ']'), ('F', '^'), ('F', '_'), ('F', '`'), ('F', '{'), ('F', '|'), ('F', '}'), ('F', '~'), ('G', 'a'), ('G', 'b'), ('G', 'c'), ('G', 'd'), ('G', 'e'), ('G', 'f'), ('G', 'g'), ('G', 'h'), ('G', 'i'), ('G', 'j'), ('G', 'k'), ('G', 'l'), ('G', 'm'), ('G', 'n'), ('G', 'o'), ('G', 'p'), ('G', 'q'), ('G', 'r'), ('G', 's'), ('G', 't'), ('G', 'u'), ('G', 'v'), ('G', 'w'), ('G', 'x'), ('G', 'y'), ('G', 'z'), ('G', 'A'), ('G', 'B'), ('G', 'C'), ('G', 'D'), ('G', 'E'), ('G', 'F'), ('G', 'G'), ('G', 'H'), ('G', 'I'), ('G', 'J'), ('G', 'K'), ('G', 'L'), ('G', 'M'), ('G', 'N'), ('G', 'O'), ('G', 'P'), ('G', 'Q'), ('G', 'R'), ('G', 'S'), ('G', 'T'), ('G', 'U'), ('G', 'V'), ('G', 'W'), ('G', 'X'), ('G', 'Y'), ('G', 'Z'), ('G', '0'), ('G', '1'), ('G', '2'), ('G', '3'), ('G', '4'), ('G', '5'), ('G', '6'), ('G', '7'), ('G', '8'), ('G', '9'), ('G', '!'), ('G', '"'), ('G', '#'), ('G', '$'), ('G', '%'), ('G', '&'), ('G', "'"), ('G', '('), ('G', ')'), ('G', '*'), ('G', '+'), ('G', ','), ('G', '-'), ('G', '.'), ('G', '/'), ('G', ':'), ('G', ';'), ('G', '<'), ('G', '='), ('G', '>'), ('G', '?'), ('G', '@'), ('G', '['), ('G', '\\'), ('G', ']'), ('G', '^'), ('G', '_'), ('G', '`'), ('G', '{'), ('G', '|'), ('G', '}'), ('G', '~'), ('H', 'a'), ('H', 'b'), ('H', 'c'), ('H', 'd'), ('H', 'e'), ('H', 'f'), ('H', 'g'), ('H', 'h'), ('H', 'i'), ('H', 'j'), ('H', 'k'), ('H', 'l'), ('H', 'm'), ('H', 'n'), ('H', 'o'), ('H', 'p'), ('H', 'q'), ('H', 'r'), ('H', 's'), ('H', 't'), ('H', 'u'), ('H', 'v'), ('H', 'w'), ('H', 'x'), ('H', 'y'), ('H', 'z'), ('H', 'A'), ('H', 'B'), ('H', 'C'), ('H', 'D'), ('H', 'E'), ('H', 'F'), ('H', 'G'), ('H', 'H'), ('H', 'I'), ('H', 'J'), ('H', 'K'), ('H', 'L'), ('H', 'M'), ('H', 'N'), ('H', 'O'), ('H', 'P'), ('H', 'Q'), ('H', 'R'), ('H', 'S'), ('H', 'T'), ('H', 'U'), ('H', 'V'), ('H', 'W'), ('H', 'X'), ('H', 'Y'), ('H', 'Z'), ('H', '0'), ('H', '1'), ('H', '2'), ('H', '3'), ('H', '4'), ('H', '5'), ('H', '6'), ('H', '7'), ('H', '8'), ('H', '9'), ('H', '!'), ('H', '"'), ('H', '#'), ('H', '$'), ('H', '%'), ('H', '&'), ('H', "'"), ('H', '('), ('H', ')'), ('H', '*'), ('H', '+'), ('H', ','), ('H', '-'), ('H', '.'), ('H', '/'), ('H', ':'), ('H', ';'), ('H', '<'), ('H', '='), ('H', '>'), ('H', '?'), ('H', '@'), ('H', '['), ('H', '\\'), ('H', ']'), ('H', '^'), ('H', '_'), ('H', '`'), ('H', '{'), ('H', '|'), ('H', '}'), ('H', '~'), ('I', 'a'), ('I', 'b'), ('I', 'c'), ('I', 'd'), ('I', 'e'), ('I', 'f'), ('I', 'g'), ('I', 'h'), ('I', 'i'), ('I', 'j'), ('I', 'k'), ('I', 'l'), ('I', 'm'), ('I', 'n'), ('I', 'o'), ('I', 'p'), ('I', 'q'), ('I', 'r'), ('I', 's'), ('I', 't'), ('I', 'u'), ('I', 'v'), ('I', 'w'), ('I', 'x'), ('I', 'y'), ('I', 'z'), ('I', 'A'), ('I', 'B'), ('I', 'C'), ('I', 'D'), ('I', 'E'), ('I', 'F'), ('I', 'G'), ('I', 'H'), ('I', 'I'), ('I', 'J'), ('I', 'K'), ('I', 'L'), ('I', 'M'), ('I', 'N'), ('I', 'O'), ('I', 'P'), ('I', 'Q'), ('I', 'R'), ('I', 'S'), ('I', 'T'), ('I', 'U'), ('I', 'V'), ('I', 'W'), ('I', 'X'), ('I', 'Y'), ('I', 'Z'), ('I', '0'), ('I', '1'), ('I', '2'), ('I', '3'), ('I', '4'), ('I', '5'), ('I', '6'), ('I', '7'), ('I', '8'), ('I', '9'), ('I', '!'), ('I', '"'), ('I', '#'), ('I', '$'), ('I', '%'), ('I', '&'), ('I', "'"), ('I', '('), ('I', ')'), ('I', '*'), ('I', '+'), ('I', ','), ('I', '-'), ('I', '.'), ('I', '/'), ('I', ':'), ('I', ';'), ('I', '<'), ('I', '='), ('I', '>'), ('I', '?'), ('I', '@'), ('I', '['), ('I', '\\'), ('I', ']'), ('I', '^'), ('I', '_'), ('I', '`'), ('I', '{'), ('I', '|'), ('I', '}'), ('I', '~'), ('J', 'a'), ('J', 'b'), ('J', 'c'), ('J', 'd'), ('J', 'e'), ('J', 'f'), ('J', 'g'), ('J', 'h'), ('J', 'i'), ('J', 'j'), ('J', 'k'), ('J', 'l'), ('J', 'm'), ('J', 'n'), ('J', 'o'), ('J', 'p'), ('J', 'q'), ('J', 'r'), ('J', 's'), ('J', 't'), ('J', 'u'), ('J', 'v'), ('J', 'w'), ('J', 'x'), ('J', 'y'), ('J', 'z'), ('J', 'A'), ('J', 'B'), ('J', 'C'), ('J', 'D'), ('J', 'E'), ('J', 'F'), ('J', 'G'), ('J', 'H'), ('J', 'I'), ('J', 'J'), ('J', 'K'), ('J', 'L'), ('J', 'M'), ('J', 'N'), ('J', 'O'), ('J', 'P'), ('J', 'Q'), ('J', 'R'), ('J', 'S'), ('J', 'T'), ('J', 'U'), ('J', 'V'), ('J', 'W'), ('J', 'X'), ('J', 'Y'), ('J', 'Z'), ('J', '0'), ('J', '1'), ('J', '2'), ('J', '3'), ('J', '4'), ('J', '5'), ('J', '6'), ('J', '7'), ('J', '8'), ('J', '9'), ('J', '!'), ('J', '"'), ('J', '#'), ('J', '$'), ('J', '%'), ('J', '&'), ('J', "'"), ('J', '('), ('J', ')'), ('J', '*'), ('J', '+'), ('J', ','), ('J', '-'), ('J', '.'), ('J', '/'), ('J', ':'), ('J', ';'), ('J', '<'), ('J', '='), ('J', '>'), ('J', '?'), ('J', '@'), ('J', '['), ('J', '\\'), ('J', ']'), ('J', '^'), ('J', '_'), ('J', '`'), ('J', '{'), ('J', '|'), ('J', '}'), ('J', '~'), ('K', 'a'), ('K', 'b'), ('K', 'c'), ('K', 'd'), ('K', 'e'), ('K', 'f'), ('K', 'g'), ('K', 'h'), ('K', 'i'), ('K', 'j'), ('K', 'k'), ('K', 'l'), ('K', 'm'), ('K', 'n'), ('K', 'o'), ('K', 'p'), ('K', 'q'), ('K', 'r'), ('K', 's'), ('K', 't'), ('K', 'u'), ('K', 'v'), ('K', 'w'), ('K', 'x'), ('K', 'y'), ('K', 'z'), ('K', 'A'), ('K', 'B'), ('K', 'C'), ('K', 'D'), ('K', 'E'), ('K', 'F'), ('K', 'G'), ('K', 'H'), ('K', 'I'), ('K', 'J'), ('K', 'K'), ('K', 'L'), ('K', 'M'), ('K', 'N'), ('K', 'O'), ('K', 'P'), ('K', 'Q'), ('K', 'R'), ('K', 'S'), ('K', 'T'), ('K', 'U'), ('K', 'V'), ('K', 'W'), ('K', 'X'), ('K', 'Y'), ('K', 'Z'), ('K', '0'), ('K', '1'), ('K', '2'), ('K', '3'), ('K', '4'), ('K', '5'), ('K', '6'), ('K', '7'), ('K', '8'), ('K', '9'), ('K', '!'), ('K', '"'), ('K', '#'), ('K', '$'), ('K', '%'), ('K', '&'), ('K', "'"), ('K', '('), ('K', ')'), ('K', '*'), ('K', '+'), ('K', ','), ('K', '-'), ('K', '.'), ('K', '/'), ('K', ':'), ('K', ';'), ('K', '<'), ('K', '='), ('K', '>'), ('K', '?'), ('K', '@'), ('K', '['), ('K', '\\'), ('K', ']'), ('K', '^'), ('K', '_'), ('K', '`'), ('K', '{'), ('K', '|'), ('K', '}'), ('K', '~'), ('L', 'a'), ('L', 'b'), ('L', 'c'), ('L', 'd'), ('L', 'e'), ('L', 'f'), ('L', 'g'), ('L', 'h'), ('L', 'i'), ('L', 'j'), ('L', 'k'), ('L', 'l'), ('L', 'm'), ('L', 'n'), ('L', 'o'), ('L', 'p'), ('L', 'q'), ('L', 'r'), ('L', 's'), ('L', 't'), ('L', 'u'), ('L', 'v'), ('L', 'w'), ('L', 'x'), ('L', 'y'), ('L', 'z'), ('L', 'A'), ('L', 'B'), ('L', 'C'), ('L', 'D'), ('L', 'E'), ('L', 'F'), ('L', 'G'), ('L', 'H'), ('L', 'I'), ('L', 'J'), ('L', 'K'), ('L', 'L'), ('L', 'M'), ('L', 'N'), ('L', 'O'), ('L', 'P'), ('L', 'Q'), ('L', 'R'), ('L', 'S'), ('L', 'T'), ('L', 'U'), ('L', 'V'), ('L', 'W'), ('L', 'X'), ('L', 'Y'), ('L', 'Z'), ('L', '0'), ('L', '1'), ('L', '2'), ('L', '3'), ('L', '4'), ('L', '5'), ('L', '6'), ('L', '7'), ('L', '8'), ('L', '9'), ('L', '!'), ('L', '"'), ('L', '#'), ('L', '$'), ('L', '%'), ('L', '&'), ('L', "'"), ('L', '('), ('L', ')'), ('L', '*'), ('L', '+'), ('L', ','), ('L', '-'), ('L', '.'), ('L', '/'), ('L', ':'), ('L', ';'), ('L', '<'), ('L', '='), ('L', '>'), ('L', '?'), ('L', '@'), ('L', '['), ('L', '\\'), ('L', ']'), ('L', '^'), ('L', '_'), ('L', '`'), ('L', '{'), ('L', '|'), ('L', '}'), ('L', '~'), ('M', 'a'), ('M', 'b'), ('M', 'c'), ('M', 'd'), ('M', 'e'), ('M', 'f'), ('M', 'g'), ('M', 'h'), ('M', 'i'), ('M', 'j'), ('M', 'k'), ('M', 'l'), ('M', 'm'), ('M', 'n'), ('M', 'o'), ('M', 'p'), ('M', 'q'), ('M', 'r'), ('M', 's'), ('M', 't'), ('M', 'u'), ('M', 'v'), ('M', 'w'), ('M', 'x'), ('M', 'y'), ('M', 'z'), ('M', 'A'), ('M', 'B'), ('M', 'C'), ('M', 'D'), ('M', 'E'), ('M', 'F'), ('M', 'G'), ('M', 'H'), ('M', 'I'), ('M', 'J'), ('M', 'K'), ('M', 'L'), ('M', 'M'), ('M', 'N'), ('M', 'O'), ('M', 'P'), ('M', 'Q'), ('M', 'R'), ('M', 'S'), ('M', 'T'), ('M', 'U'), ('M', 'V'), ('M', 'W'), ('M', 'X'), ('M', 'Y'), ('M', 'Z'), ('M', '0'), ('M', '1'), ('M', '2'), ('M', '3'), ('M', '4'), ('M', '5'), ('M', '6'), ('M', '7'), ('M', '8'), ('M', '9'), ('M', '!'), ('M', '"'), ('M', '#'), ('M', '$'), ('M', '%'), ('M', '&'), ('M', "'"), ('M', '('), ('M', ')'), ('M', '*'), ('M', '+'), ('M', ','), ('M', '-'), ('M', '.'), ('M', '/'), ('M', ':'), ('M', ';'), ('M', '<'), ('M', '='), ('M', '>'), ('M', '?'), ('M', '@'), ('M', '['), ('M', '\\'), ('M', ']'), ('M', '^'), ('M', '_'), ('M', '`'), ('M', '{'), ('M', '|'), ('M', '}'), ('M', '~'), ('N', 'a'), ('N', 'b'), ('N', 'c'), ('N', 'd'), ('N', 'e'), ('N', 'f'), ('N', 'g'), ('N', 'h'), ('N', 'i'), ('N', 'j'), ('N', 'k'), ('N', 'l'), ('N', 'm'), ('N', 'n'), ('N', 'o'), ('N', 'p'), ('N', 'q'), ('N', 'r'), ('N', 's'), ('N', 't'), ('N', 'u'), ('N', 'v'), ('N', 'w'), ('N', 'x'), ('N', 'y'), ('N', 'z'), ('N', 'A'), ('N', 'B'), ('N', 'C'), ('N', 'D'), ('N', 'E'), ('N', 'F'), ('N', 'G'), ('N', 'H'), ('N', 'I'), ('N', 'J'), ('N', 'K'), ('N', 'L'), ('N', 'M'), ('N', 'N'), ('N', 'O'), ('N', 'P'), ('N', 'Q'), ('N', 'R'), ('N', 'S'), ('N', 'T'), ('N', 'U'), ('N', 'V'), ('N', 'W'), ('N', 'X'), ('N', 'Y'), ('N', 'Z'), ('N', '0'), ('N', '1'), ('N', '2'), ('N', '3'), ('N', '4'), ('N', '5'), ('N', '6'), ('N', '7'), ('N', '8'), ('N', '9'), ('N', '!'), ('N', '"'), ('N', '#'), ('N', '$'), ('N', '%'), ('N', '&'), ('N', "'"), ('N', '('), ('N', ')'), ('N', '*'), ('N', '+'), ('N', ','), ('N', '-'), ('N', '.'), ('N', '/'), ('N', ':'), ('N', ';'), ('N', '<'), ('N', '='), ('N', '>'), ('N', '?'), ('N', '@'), ('N', '['), ('N', '\\'), ('N', ']'), ('N', '^'), ('N', '_'), ('N', '`'), ('N', '{'), ('N', '|'), ('N', '}'), ('N', '~'), ('O', 'a'), ('O', 'b'), ('O', 'c'), ('O', 'd'), ('O', 'e'), ('O', 'f'), ('O', 'g'), ('O', 'h'), ('O', 'i'), ('O', 'j'), ('O', 'k'), ('O', 'l'), ('O', 'm'), ('O', 'n'), ('O', 'o'), ('O', 'p'), ('O', 'q'), ('O', 'r'), ('O', 's'), ('O', 't'), ('O', 'u'), ('O', 'v'), ('O', 'w'), ('O', 'x'), ('O', 'y'), ('O', 'z'), ('O', 'A'), ('O', 'B'), ('O', 'C'), ('O', 'D'), ('O', 'E'), ('O', 'F'), ('O', 'G'), ('O', 'H'), ('O', 'I'), ('O', 'J'), ('O', 'K'), ('O', 'L'), ('O', 'M'), ('O', 'N'), ('O', 'O'), ('O', 'P'), ('O', 'Q'), ('O', 'R'), ('O', 'S'), ('O', 'T'), ('O', 'U'), ('O', 'V'), ('O', 'W'), ('O', 'X'), ('O', 'Y'), ('O', 'Z'), ('O', '0'), ('O', '1'), ('O', '2'), ('O', '3'), ('O', '4'), ('O', '5'), ('O', '6'), ('O', '7'), ('O', '8'), ('O', '9'), ('O', '!'), ('O', '"'), ('O', '#'), ('O', '$'), ('O', '%'), ('O', '&'), ('O', "'"), ('O', '('), ('O', ')'), ('O', '*'), ('O', '+'), ('O', ','), ('O', '-'), ('O', '.'), ('O', '/'), ('O', ':'), ('O', ';'), ('O', '<'), ('O', '='), ('O', '>'), ('O', '?'), ('O', '@'), ('O', '['), ('O', '\\'), ('O', ']'), ('O', '^'), ('O', '_'), ('O', '`'), ('O', '{'), ('O', '|'), ('O', '}'), ('O', '~'), ('P', 'a'), ('P', 'b'), ('P', 'c'), ('P', 'd'), ('P', 'e'), ('P', 'f'), ('P', 'g'), ('P', 'h'), ('P', 'i'), ('P', 'j'), ('P', 'k'), ('P', 'l'), ('P', 'm'), ('P', 'n'), ('P', 'o'), ('P', 'p'), ('P', 'q'), ('P', 'r'), ('P', 's'), ('P', 't'), ('P', 'u'), ('P', 'v'), ('P', 'w'), ('P', 'x'), ('P', 'y'), ('P', 'z'), ('P', 'A'), ('P', 'B'), ('P', 'C'), ('P', 'D'), ('P', 'E'), ('P', 'F'), ('P', 'G'), ('P', 'H'), ('P', 'I'), ('P', 'J'), ('P', 'K'), ('P', 'L'), ('P', 'M'), ('P', 'N'), ('P', 'O'), ('P', 'P'), ('P', 'Q'), ('P', 'R'), ('P', 'S'), ('P', 'T'), ('P', 'U'), ('P', 'V'), ('P', 'W'), ('P', 'X'), ('P', 'Y'), ('P', 'Z'), ('P', '0'), ('P', '1'), ('P', '2'), ('P', '3'), ('P', '4'), ('P', '5'), ('P', '6'), ('P', '7'), ('P', '8'), ('P', '9'), ('P', '!'), ('P', '"'), ('P', '#'), ('P', '$'), ('P', '%'), ('P', '&'), ('P', "'"), ('P', '('), ('P', ')'), ('P', '*'), ('P', '+'), ('P', ','), ('P', '-'), ('P', '.'), ('P', '/'), ('P', ':'), ('P', ';'), ('P', '<'), ('P', '='), ('P', '>'), ('P', '?'), ('P', '@'), ('P', '['), ('P', '\\'), ('P', ']'), ('P', '^'), ('P', '_'), ('P', '`'), ('P', '{'), ('P', '|'), ('P', '}'), ('P', '~'), ('Q', 'a'), ('Q', 'b'), ('Q', 'c'), ('Q', 'd'), ('Q', 'e'), ('Q', 'f'), ('Q', 'g'), ('Q', 'h'), ('Q', 'i'), ('Q', 'j'), ('Q', 'k'), ('Q', 'l'), ('Q', 'm'), ('Q', 'n'), ('Q', 'o'), ('Q', 'p'), ('Q', 'q'), ('Q', 'r'), ('Q', 's'), ('Q', 't'), ('Q', 'u'), ('Q', 'v'), ('Q', 'w'), ('Q', 'x'), ('Q', 'y'), ('Q', 'z'), ('Q', 'A'), ('Q', 'B'), ('Q', 'C'), ('Q', 'D'), ('Q', 'E'), ('Q', 'F'), ('Q', 'G'), ('Q', 'H'), ('Q', 'I'), ('Q', 'J'), ('Q', 'K'), ('Q', 'L'), ('Q', 'M'), ('Q', 'N'), ('Q', 'O'), ('Q', 'P'), ('Q', 'Q'), ('Q', 'R'), ('Q', 'S'), ('Q', 'T'), ('Q', 'U'), ('Q', 'V'), ('Q', 'W'), ('Q', 'X'), ('Q', 'Y'), ('Q', 'Z'), ('Q', '0'), ('Q', '1'), ('Q', '2'), ('Q', '3'), ('Q', '4'), ('Q', '5'), ('Q', '6'), ('Q', '7'), ('Q', '8'), ('Q', '9'), ('Q', '!'), ('Q', '"'), ('Q', '#'), ('Q', '$'), ('Q', '%'), ('Q', '&'), ('Q', "'"), ('Q', '('), ('Q', ')'), ('Q', '*'), ('Q', '+'), ('Q', ','), ('Q', '-'), ('Q', '.'), ('Q', '/'), ('Q', ':'), ('Q', ';'), ('Q', '<'), ('Q', '='), ('Q', '>'), ('Q', '?'), ('Q', '@'), ('Q', '['), ('Q', '\\'), ('Q', ']'), ('Q', '^'), ('Q', '_'), ('Q', '`'), ('Q', '{'), ('Q', '|'), ('Q', '}'), ('Q', '~'), ('R', 'a'), ('R', 'b'), ('R', 'c'), ('R', 'd'), ('R', 'e'), ('R', 'f'), ('R', 'g'), ('R', 'h'), ('R', 'i'), ('R', 'j'), ('R', 'k'), ('R', 'l'), ('R', 'm'), ('R', 'n'), ('R', 'o'), ('R', 'p'), ('R', 'q'), ('R', 'r'), ('R', 's'), ('R', 't'), ('R', 'u'), ('R', 'v'), ('R', 'w'), ('R', 'x'), ('R', 'y'), ('R', 'z'), ('R', 'A'), ('R', 'B'), ('R', 'C'), ('R', 'D'), ('R', 'E'), ('R', 'F'), ('R', 'G'), ('R', 'H'), ('R', 'I'), ('R', 'J'), ('R', 'K'), ('R', 'L'), ('R', 'M'), ('R', 'N'), ('R', 'O'), ('R', 'P'), ('R', 'Q'), ('R', 'R'), ('R', 'S'), ('R', 'T'), ('R', 'U'), ('R', 'V'), ('R', 'W'), ('R', 'X'), ('R', 'Y'), ('R', 'Z'), ('R', '0'), ('R', '1'), ('R', '2'), ('R', '3'), ('R', '4'), ('R', '5'), ('R', '6'), ('R', '7'), ('R', '8'), ('R', '9'), ('R', '!'), ('R', '"'), ('R', '#'), ('R', '$'), ('R', '%'), ('R', '&'), ('R', "'"), ('R', '('), ('R', ')'), ('R', '*'), ('R', '+'), ('R', ','), ('R', '-'), ('R', '.'), ('R', '/'), ('R', ':'), ('R', ';'), ('R', '<'), ('R', '='), ('R', '>'), ('R', '?'), ('R', '@'), ('R', '['), ('R', '\\'), ('R', ']'), ('R', '^'), ('R', '_'), ('R', '`'), ('R', '{'), ('R', '|'), ('R', '}'), ('R', '~'), ('S', 'a'), ('S', 'b'), ('S', 'c'), ('S', 'd'), ('S', 'e'), ('S', 'f'), ('S', 'g'), ('S', 'h'), ('S', 'i'), ('S', 'j'), ('S', 'k'), ('S', 'l'), ('S', 'm'), ('S', 'n'), ('S', 'o'), ('S', 'p'), ('S', 'q'), ('S', 'r'), ('S', 's'), ('S', 't'), ('S', 'u'), ('S', 'v'), ('S', 'w'), ('S', 'x'), ('S', 'y'), ('S', 'z'), ('S', 'A'), ('S', 'B'), ('S', 'C'), ('S', 'D'), ('S', 'E'), ('S', 'F'), ('S', 'G'), ('S', 'H'), ('S', 'I'), ('S', 'J'), ('S', 'K'), ('S', 'L'), ('S', 'M'), ('S', 'N'), ('S', 'O'), ('S', 'P'), ('S', 'Q'), ('S', 'R'), ('S', 'S'), ('S', 'T'), ('S', 'U'), ('S', 'V'), ('S', 'W'), ('S', 'X'), ('S', 'Y'), ('S', 'Z'), ('S', '0'), ('S', '1'), ('S', '2'), ('S', '3'), ('S', '4'), ('S', '5'), ('S', '6'), ('S', '7'), ('S', '8'), ('S', '9'), ('S', '!'), ('S', '"'), ('S', '#'), ('S', '$'), ('S', '%'), ('S', '&'), ('S', "'"), ('S', '('), ('S', ')'), ('S', '*'), ('S', '+'), ('S', ','), ('S', '-'), ('S', '.'), ('S', '/'), ('S', ':'), ('S', ';'), ('S', '<'), ('S', '='), ('S', '>'), ('S', '?'), ('S', '@'), ('S', '['), ('S', '\\'), ('S', ']'), ('S', '^'), ('S', '_'), ('S', '`'), ('S', '{'), ('S', '|'), ('S', '}'), ('S', '~'), ('T', 'a'), ('T', 'b'), ('T', 'c'), ('T', 'd'), ('T', 'e'), ('T', 'f'), ('T', 'g'), ('T', 'h'), ('T', 'i'), ('T', 'j'), ('T', 'k'), ('T', 'l'), ('T', 'm'), ('T', 'n'), ('T', 'o'), ('T', 'p'), ('T', 'q'), ('T', 'r'), ('T', 's'), ('T', 't'), ('T', 'u'), ('T', 'v'), ('T', 'w'), ('T', 'x'), ('T', 'y'), ('T', 'z'), ('T', 'A'), ('T', 'B'), ('T', 'C'), ('T', 'D'), ('T', 'E'), ('T', 'F'), ('T', 'G'), ('T', 'H'), ('T', 'I'), ('T', 'J'), ('T', 'K'), ('T', 'L'), ('T', 'M'), ('T', 'N'), ('T', 'O'), ('T', 'P'), ('T', 'Q'), ('T', 'R'), ('T', 'S'), ('T', 'T'), ('T', 'U'), ('T', 'V'), ('T', 'W'), ('T', 'X'), ('T', 'Y'), ('T', 'Z'), ('T', '0'), ('T', '1'), ('T', '2'), ('T', '3'), ('T', '4'), ('T', '5'), ('T', '6'), ('T', '7'), ('T', '8'), ('T', '9'), ('T', '!'), ('T', '"'), ('T', '#'), ('T', '$'), ('T', '%'), ('T', '&'), ('T', "'"), ('T', '('), ('T', ')'), ('T', '*'), ('T', '+'), ('T', ','), ('T', '-'), ('T', '.'), ('T', '/'), ('T', ':'), ('T', ';'), ('T', '<'), ('T', '='), ('T', '>'), ('T', '?'), ('T', '@'), ('T', '['), ('T', '\\'), ('T', ']'), ('T', '^'), ('T', '_'), ('T', '`'), ('T', '{'), ('T', '|'), ('T', '}'), ('T', '~'), ('U', 'a'), ('U', 'b'), ('U', 'c'), ('U', 'd'), ('U', 'e'), ('U', 'f'), ('U', 'g'), ('U', 'h'), ('U', 'i'), ('U', 'j'), ('U', 'k'), ('U', 'l'), ('U', 'm'), ('U', 'n'), ('U', 'o'), ('U', 'p'), ('U', 'q'), ('U', 'r'), ('U', 's'), ('U', 't'), ('U', 'u'), ('U', 'v'), ('U', 'w'), ('U', 'x'), ('U', 'y'), ('U', 'z'), ('U', 'A'), ('U', 'B'), ('U', 'C'), ('U', 'D'), ('U', 'E'), ('U', 'F'), ('U', 'G'), ('U', 'H'), ('U', 'I'), ('U', 'J'), ('U', 'K'), ('U', 'L'), ('U', 'M'), ('U', 'N'), ('U', 'O'), ('U', 'P'), ('U', 'Q'), ('U', 'R'), ('U', 'S'), ('U', 'T'), ('U', 'U'), ('U', 'V'), ('U', 'W'), ('U', 'X'), ('U', 'Y'), ('U', 'Z'), ('U', '0'), ('U', '1'), ('U', '2'), ('U', '3'), ('U', '4'), ('U', '5'), ('U', '6'), ('U', '7'), ('U', '8'), ('U', '9'), ('U', '!'), ('U', '"'), ('U', '#'), ('U', '$'), ('U', '%'), ('U', '&'), ('U', "'"), ('U', '('), ('U', ')'), ('U', '*'), ('U', '+'), ('U', ','), ('U', '-'), ('U', '.'), ('U', '/'), ('U', ':'), ('U', ';'), ('U', '<'), ('U', '='), ('U', '>'), ('U', '?'), ('U', '@'), ('U', '['), ('U', '\\'), ('U', ']'), ('U', '^'), ('U', '_'), ('U', '`'), ('U', '{'), ('U', '|'), ('U', '}'), ('U', '~'), ('V', 'a'), ('V', 'b'), ('V', 'c'), ('V', 'd'), ('V', 'e'), ('V', 'f'), ('V', 'g'), ('V', 'h'), ('V', 'i'), ('V', 'j'), ('V', 'k'), ('V', 'l'), ('V', 'm'), ('V', 'n'), ('V', 'o'), ('V', 'p'), ('V', 'q'), ('V', 'r'), ('V', 's'), ('V', 't'), ('V', 'u'), ('V', 'v'), ('V', 'w'), ('V', 'x'), ('V', 'y'), ('V', 'z'), ('V', 'A'), ('V', 'B'), ('V', 'C'), ('V', 'D'), ('V', 'E'), ('V', 'F'), ('V', 'G'), ('V', 'H'), ('V', 'I'), ('V', 'J'), ('V', 'K'), ('V', 'L'), ('V', 'M'), ('V', 'N'), ('V', 'O'), ('V', 'P'), ('V', 'Q'), ('V', 'R'), ('V', 'S'), ('V', 'T'), ('V', 'U'), ('V', 'V'), ('V', 'W'), ('V', 'X'), ('V', 'Y'), ('V', 'Z'), ('V', '0'), ('V', '1'), ('V', '2'), ('V', '3'), ('V', '4'), ('V', '5'), ('V', '6'), ('V', '7'), ('V', '8'), ('V', '9'), ('V', '!'), ('V', '"'), ('V', '#'), ('V', '$'), ('V', '%'), ('V', '&'), ('V', "'"), ('V', '('), ('V', ')'), ('V', '*'), ('V', '+'), ('V', ','), ('V', '-'), ('V', '.'), ('V', '/'), ('V', ':'), ('V', ';'), ('V', '<'), ('V', '='), ('V', '>'), ('V', '?'), ('V', '@'), ('V', '['), ('V', '\\'), ('V', ']'), ('V', '^'), ('V', '_'), ('V', '`'), ('V', '{'), ('V', '|'), ('V', '}'), ('V', '~'), ('W', 'a'), ('W', 'b'), ('W', 'c'), ('W', 'd'), ('W', 'e'), ('W', 'f'), ('W', 'g'), ('W', 'h'), ('W', 'i'), ('W', 'j'), ('W', 'k'), ('W', 'l'), ('W', 'm'), ('W', 'n'), ('W', 'o'), ('W', 'p'), ('W', 'q'), ('W', 'r'), ('W', 's'), ('W', 't'), ('W', 'u'), ('W', 'v'), ('W', 'w'), ('W', 'x'), ('W', 'y'), ('W', 'z'), ('W', 'A'), ('W', 'B'), ('W', 'C'), ('W', 'D'), ('W', 'E'), ('W', 'F'), ('W', 'G'), ('W', 'H'), ('W', 'I'), ('W', 'J'), ('W', 'K'), ('W', 'L'), ('W', 'M'), ('W', 'N'), ('W', 'O'), ('W', 'P'), ('W', 'Q'), ('W', 'R'), ('W', 'S'), ('W', 'T'), ('W', 'U'), ('W', 'V'), ('W', 'W'), ('W', 'X'), ('W', 'Y'), ('W', 'Z'), ('W', '0'), ('W', '1'), ('W', '2'), ('W', '3'), ('W', '4'), ('W', '5'), ('W', '6'), ('W', '7'), ('W', '8'), ('W', '9'), ('W', '!'), ('W', '"'), ('W', '#'), ('W', '$'), ('W', '%'), ('W', '&'), ('W', "'"), ('W', '('), ('W', ')'), ('W', '*'), ('W', '+'), ('W', ','), ('W', '-'), ('W', '.'), ('W', '/'), ('W', ':'), ('W', ';'), ('W', '<'), ('W', '='), ('W', '>'), ('W', '?'), ('W', '@'), ('W', '['), ('W', '\\'), ('W', ']'), ('W', '^'), ('W', '_'), ('W', '`'), ('W', '{'), ('W', '|'), ('W', '}'), ('W', '~'), ('X', 'a'), ('X', 'b'), ('X', 'c'), ('X', 'd'), ('X', 'e'), ('X', 'f'), ('X', 'g'), ('X', 'h'), ('X', 'i'), ('X', 'j'), ('X', 'k'), ('X', 'l'), ('X', 'm'), ('X', 'n'), ('X', 'o'), ('X', 'p'), ('X', 'q'), ('X', 'r'), ('X', 's'), ('X', 't'), ('X', 'u'), ('X', 'v'), ('X', 'w'), ('X', 'x'), ('X', 'y'), ('X', 'z'), ('X', 'A'), ('X', 'B'), ('X', 'C'), ('X', 'D'), ('X', 'E'), ('X', 'F'), ('X', 'G'), ('X', 'H'), ('X', 'I'), ('X', 'J'), ('X', 'K'), ('X', 'L'), ('X', 'M'), ('X', 'N'), ('X', 'O'), ('X', 'P'), ('X', 'Q'), ('X', 'R'), ('X', 'S'), ('X', 'T'), ('X', 'U'), ('X', 'V'), ('X', 'W'), ('X', 'X'), ('X', 'Y'), ('X', 'Z'), ('X', '0'), ('X', '1'), ('X', '2'), ('X', '3'), ('X', '4'), ('X', '5'), ('X', '6'), ('X', '7'), ('X', '8'), ('X', '9'), ('X', '!'), ('X', '"'), ('X', '#'), ('X', '$'), ('X', '%'), ('X', '&'), ('X', "'"), ('X', '('), ('X', ')'), ('X', '*'), ('X', '+'), ('X', ','), ('X', '-'), ('X', '.'), ('X', '/'), ('X', ':'), ('X', ';'), ('X', '<'), ('X', '='), ('X', '>'), ('X', '?'), ('X', '@'), ('X', '['), ('X', '\\'), ('X', ']'), ('X', '^'), ('X', '_'), ('X', '`'), ('X', '{'), ('X', '|'), ('X', '}'), ('X', '~'), ('Y', 'a'), ('Y', 'b'), ('Y', 'c'), ('Y', 'd'), ('Y', 'e'), ('Y', 'f'), ('Y', 'g'), ('Y', 'h'), ('Y', 'i'), ('Y', 'j'), ('Y', 'k'), ('Y', 'l'), ('Y', 'm'), ('Y', 'n'), ('Y', 'o'), ('Y', 'p'), ('Y', 'q'), ('Y', 'r'), ('Y', 's'), ('Y', 't'), ('Y', 'u'), ('Y', 'v'), ('Y', 'w'), ('Y', 'x'), ('Y', 'y'), ('Y', 'z'), ('Y', 'A'), ('Y', 'B'), ('Y', 'C'), ('Y', 'D'), ('Y', 'E'), ('Y', 'F'), ('Y', 'G'), ('Y', 'H'), ('Y', 'I'), ('Y', 'J'), ('Y', 'K'), ('Y', 'L'), ('Y', 'M'), ('Y', 'N'), ('Y', 'O'), ('Y', 'P'), ('Y', 'Q'), ('Y', 'R'), ('Y', 'S'), ('Y', 'T'), ('Y', 'U'), ('Y', 'V'), ('Y', 'W'), ('Y', 'X'), ('Y', 'Y'), ('Y', 'Z'), ('Y', '0'), ('Y', '1'), ('Y', '2'), ('Y', '3'), ('Y', '4'), ('Y', '5'), ('Y', '6'), ('Y', '7'), ('Y', '8'), ('Y', '9'), ('Y', '!'), ('Y', '"'), ('Y', '#'), ('Y', '$'), ('Y', '%'), ('Y', '&'), ('Y', "'"), ('Y', '('), ('Y', ')'), ('Y', '*'), ('Y', '+'), ('Y', ','), ('Y', '-'), ('Y', '.'), ('Y', '/'), ('Y', ':'), ('Y', ';'), ('Y', '<'), ('Y', '='), ('Y', '>'), ('Y', '?'), ('Y', '@'), ('Y', '['), ('Y', '\\'), ('Y', ']'), ('Y', '^'), ('Y', '_'), ('Y', '`'), ('Y', '{'), ('Y', '|'), ('Y', '}'), ('Y', '~'), ('Z', 'a'), ('Z', 'b'), ('Z', 'c'), ('Z', 'd'), ('Z', 'e'), ('Z', 'f'), ('Z', 'g'), ('Z', 'h'), ('Z', 'i'), ('Z', 'j'), ('Z', 'k'), ('Z', 'l'), ('Z', 'm'), ('Z', 'n'), ('Z', 'o'), ('Z', 'p'), ('Z', 'q'), ('Z', 'r'), ('Z', 's'), ('Z', 't'), ('Z', 'u'), ('Z', 'v'), ('Z', 'w'), ('Z', 'x'), ('Z', 'y'), ('Z', 'z'), ('Z', 'A'), ('Z', 'B'), ('Z', 'C'), ('Z', 'D'), ('Z', 'E'), ('Z', 'F'), ('Z', 'G'), ('Z', 'H'), ('Z', 'I'), ('Z', 'J'), ('Z', 'K'), ('Z', 'L'), ('Z', 'M'), ('Z', 'N'), ('Z', 'O'), ('Z', 'P'), ('Z', 'Q'), ('Z', 'R'), ('Z', 'S'), ('Z', 'T'), ('Z', 'U'), ('Z', 'V'), ('Z', 'W'), ('Z', 'X'), ('Z', 'Y'), ('Z', 'Z'), ('Z', '0'), ('Z', '1'), ('Z', '2'), ('Z', '3'), ('Z', '4'), ('Z', '5'), ('Z', '6'), ('Z', '7'), ('Z', '8'), ('Z', '9'), ('Z', '!'), ('Z', '"'), ('Z', '#'), ('Z', '$'), ('Z', '%'), ('Z', '&'), ('Z', "'"), ('Z', '('), ('Z', ')'), ('Z', '*'), ('Z', '+'), ('Z', ','), ('Z', '-'), ('Z', '.'), ('Z', '/'), ('Z', ':'), ('Z', ';'), ('Z', '<'), ('Z', '='), ('Z', '>'), ('Z', '?'), ('Z', '@'), ('Z', '['), ('Z', '\\'), ('Z', ']'), ('Z', '^'), ('Z', '_'), ('Z', '`'), ('Z', '{'), ('Z', '|'), ('Z', '}'), ('Z', '~'), ('0', 'a'), ('0', 'b'), ('0', 'c'), ('0', 'd'), ('0', 'e'), ('0', 'f'), ('0', 'g'), ('0', 'h'), ('0', 'i'), ('0', 'j'), ('0', 'k'), ('0', 'l'), ('0', 'm'), ('0', 'n'), ('0', 'o'), ('0', 'p'), ('0', 'q'), ('0', 'r'), ('0', 's'), ('0', 't'), ('0', 'u'), ('0', 'v'), ('0', 'w'), ('0', 'x'), ('0', 'y'), ('0', 'z'), ('0', 'A'), ('0', 'B'), ('0', 'C'), ('0', 'D'), ('0', 'E'), ('0', 'F'), ('0', 'G'), ('0', 'H'), ('0', 'I'), ('0', 'J'), ('0', 'K'), ('0', 'L'), ('0', 'M'), ('0', 'N'), ('0', 'O'), ('0', 'P'), ('0', 'Q'), ('0', 'R'), ('0', 'S'), ('0', 'T'), ('0', 'U'), ('0', 'V'), ('0', 'W'), ('0', 'X'), ('0', 'Y'), ('0', 'Z'), ('0', '0'), ('0', '1'), ('0', '2'), ('0', '3'), ('0', '4'), ('0', '5'), ('0', '6'), ('0', '7'), ('0', '8'), ('0', '9'), ('0', '!'), ('0', '"'), ('0', '#'), ('0', '$'), ('0', '%'), ('0', '&'), ('0', "'"), ('0', '('), ('0', ')'), ('0', '*'), ('0', '+'), ('0', ','), ('0', '-'), ('0', '.'), ('0', '/'), ('0', ':'), ('0', ';'), ('0', '<'), ('0', '='), ('0', '>'), ('0', '?'), ('0', '@'), ('0', '['), ('0', '\\'), ('0', ']'), ('0', '^'), ('0', '_'), ('0', '`'), ('0', '{'), ('0', '|'), ('0', '}'), ('0', '~'), ('1', 'a'), ('1', 'b'), ('1', 'c'), ('1', 'd'), ('1', 'e'), ('1', 'f'), ('1', 'g'), ('1', 'h'), ('1', 'i'), ('1', 'j'), ('1', 'k'), ('1', 'l'), ('1', 'm'), ('1', 'n'), ('1', 'o'), ('1', 'p'), ('1', 'q'), ('1', 'r'), ('1', 's'), ('1', 't'), ('1', 'u'), ('1', 'v'), ('1', 'w'), ('1', 'x'), ('1', 'y'), ('1', 'z'), ('1', 'A'), ('1', 'B'), ('1', 'C'), ('1', 'D'), ('1', 'E'), ('1', 'F'), ('1', 'G'), ('1', 'H'), ('1', 'I'), ('1', 'J'), ('1', 'K'), ('1', 'L'), ('1', 'M'), ('1', 'N'), ('1', 'O'), ('1', 'P'), ('1', 'Q'), ('1', 'R'), ('1', 'S'), ('1', 'T'), ('1', 'U'), ('1', 'V'), ('1', 'W'), ('1', 'X'), ('1', 'Y'), ('1', 'Z'), ('1', '0'), ('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('1', '6'), ('1', '7'), ('1', '8'), ('1', '9'), ('1', '!'), ('1', '"'), ('1', '#'), ('1', '$'), ('1', '%'), ('1', '&'), ('1', "'"), ('1', '('), ('1', ')'), ('1', '*'), ('1', '+'), ('1', ','), ('1', '-'), ('1', '.'), ('1', '/'), ('1', ':'), ('1', ';'), ('1', '<'), ('1', '='), ('1', '>'), ('1', '?'), ('1', '@'), ('1', '['), ('1', '\\'), ('1', ']'), ('1', '^'), ('1', '_'), ('1', '`'), ('1', '{'), ('1', '|'), ('1', '}'), ('1', '~'), ('2', 'a'), ('2', 'b'), ('2', 'c'), ('2', 'd'), ('2', 'e'), ('2', 'f'), ('2', 'g'), ('2', 'h'), ('2', 'i'), ('2', 'j'), ('2', 'k'), ('2', 'l'), ('2', 'm'), ('2', 'n'), ('2', 'o'), ('2', 'p'), ('2', 'q'), ('2', 'r'), ('2', 's'), ('2', 't'), ('2', 'u'), ('2', 'v'), ('2', 'w'), ('2', 'x'), ('2', 'y'), ('2', 'z'), ('2', 'A'), ('2', 'B'), ('2', 'C'), ('2', 'D'), ('2', 'E'), ('2', 'F'), ('2', 'G'), ('2', 'H'), ('2', 'I'), ('2', 'J'), ('2', 'K'), ('2', 'L'), ('2', 'M'), ('2', 'N'), ('2', 'O'), ('2', 'P'), ('2', 'Q'), ('2', 'R'), ('2', 'S'), ('2', 'T'), ('2', 'U'), ('2', 'V'), ('2', 'W'), ('2', 'X'), ('2', 'Y'), ('2', 'Z'), ('2', '0'), ('2', '1'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('2', '6'), ('2', '7'), ('2', '8'), ('2', '9'), ('2', '!'), ('2', '"'), ('2', '#'), ('2', '$'), ('2', '%'), ('2', '&'), ('2', "'"), ('2', '('), ('2', ')'), ('2', '*'), ('2', '+'), ('2', ','), ('2', '-'), ('2', '.'), ('2', '/'), ('2', ':'), ('2', ';'), ('2', '<'), ('2', '='), ('2', '>'), ('2', '?'), ('2', '@'), ('2', '['), ('2', '\\'), ('2', ']'), ('2', '^'), ('2', '_'), ('2', '`'), ('2', '{'), ('2', '|'), ('2', '}'), ('2', '~'), ('3', 'a'), ('3', 'b'), ('3', 'c'), ('3', 'd'), ('3', 'e'), ('3', 'f'), ('3', 'g'), ('3', 'h'), ('3', 'i'), ('3', 'j'), ('3', 'k'), ('3', 'l'), ('3', 'm'), ('3', 'n'), ('3', 'o'), ('3', 'p'), ('3', 'q'), ('3', 'r'), ('3', 's'), ('3', 't'), ('3', 'u'), ('3', 'v'), ('3', 'w'), ('3', 'x'), ('3', 'y'), ('3', 'z'), ('3', 'A'), ('3', 'B'), ('3', 'C'), ('3', 'D'), ('3', 'E'), ('3', 'F'), ('3', 'G'), ('3', 'H'), ('3', 'I'), ('3', 'J'), ('3', 'K'), ('3', 'L'), ('3', 'M'), ('3', 'N'), ('3', 'O'), ('3', 'P'), ('3', 'Q'), ('3', 'R'), ('3', 'S'), ('3', 'T'), ('3', 'U'), ('3', 'V'), ('3', 'W'), ('3', 'X'), ('3', 'Y'), ('3', 'Z'), ('3', '0'), ('3', '1'), ('3', '2'), ('3', '3'), ('3', '4'), ('3', '5'), ('3', '6'), ('3', '7'), ('3', '8'), ('3', '9'), ('3', '!'), ('3', '"'), ('3', '#'), ('3', '$'), ('3', '%'), ('3', '&'), ('3', "'"), ('3', '('), ('3', ')'), ('3', '*'), ('3', '+'), ('3', ','), ('3', '-'), ('3', '.'), ('3', '/'), ('3', ':'), ('3', ';'), ('3', '<'), ('3', '='), ('3', '>'), ('3', '?'), ('3', '@'), ('3', '['), ('3', '\\'), ('3', ']'), ('3', '^'), ('3', '_'), ('3', '`'), ('3', '{'), ('3', '|'), ('3', '}'), ('3', '~'), ('4', 'a'), ('4', 'b'), ('4', 'c'), ('4', 'd'), ('4', 'e'), ('4', 'f'), ('4', 'g'), ('4', 'h'), ('4', 'i'), ('4', 'j'), ('4', 'k'), ('4', 'l'), ('4', 'm'), ('4', 'n'), ('4', 'o'), ('4', 'p'), ('4', 'q'), ('4', 'r'), ('4', 's'), ('4', 't'), ('4', 'u'), ('4', 'v'), ('4', 'w'), ('4', 'x'), ('4', 'y'), ('4', 'z'), ('4', 'A'), ('4', 'B'), ('4', 'C'), ('4', 'D'), ('4', 'E'), ('4', 'F'), ('4', 'G'), ('4', 'H'), ('4', 'I'), ('4', 'J'), ('4', 'K'), ('4', 'L'), ('4', 'M'), ('4', 'N'), ('4', 'O'), ('4', 'P'), ('4', 'Q'), ('4', 'R'), ('4', 'S'), ('4', 'T'), ('4', 'U'), ('4', 'V'), ('4', 'W'), ('4', 'X'), ('4', 'Y'), ('4', 'Z'), ('4', '0'), ('4', '1'), ('4', '2'), ('4', '3'), ('4', '4'), ('4', '5'), ('4', '6'), ('4', '7'), ('4', '8'), ('4', '9'), ('4', '!'), ('4', '"'), ('4', '#'), ('4', '$'), ('4', '%'), ('4', '&'), ('4', "'"), ('4', '('), ('4', ')'), ('4', '*'), ('4', '+'), ('4', ','), ('4', '-'), ('4', '.'), ('4', '/'), ('4', ':'), ('4', ';'), ('4', '<'), ('4', '='), ('4', '>'), ('4', '?'), ('4', '@'), ('4', '['), ('4', '\\'), ('4', ']'), ('4', '^'), ('4', '_'), ('4', '`'), ('4', '{'), ('4', '|'), ('4', '}'), ('4', '~'), ('5', 'a'), ('5', 'b'), ('5', 'c'), ('5', 'd'), ('5', 'e'), ('5', 'f'), ('5', 'g'), ('5', 'h'), ('5', 'i'), ('5', 'j'), ('5', 'k'), ('5', 'l'), ('5', 'm'), ('5', 'n'), ('5', 'o'), ('5', 'p'), ('5', 'q'), ('5', 'r'), ('5', 's'), ('5', 't'), ('5', 'u'), ('5', 'v'), ('5', 'w'), ('5', 'x'), ('5', 'y'), ('5', 'z'), ('5', 'A'), ('5', 'B'), ('5', 'C'), ('5', 'D'), ('5', 'E'), ('5', 'F'), ('5', 'G'), ('5', 'H'), ('5', 'I'), ('5', 'J'), ('5', 'K'), ('5', 'L'), ('5', 'M'), ('5', 'N'), ('5', 'O'), ('5', 'P'), ('5', 'Q'), ('5', 'R'), ('5', 'S'), ('5', 'T'), ('5', 'U'), ('5', 'V'), ('5', 'W'), ('5', 'X'), ('5', 'Y'), ('5', 'Z'), ('5', '0'), ('5', '1'), ('5', '2'), ('5', '3'), ('5', '4'), ('5', '5'), ('5', '6'), ('5', '7'), ('5', '8'), ('5', '9'), ('5', '!'), ('5', '"'), ('5', '#'), ('5', '$'), ('5', '%'), ('5', '&'), ('5', "'"), ('5', '('), ('5', ')'), ('5', '*'), ('5', '+'), ('5', ','), ('5', '-'), ('5', '.'), ('5', '/'), ('5', ':'), ('5', ';'), ('5', '<'), ('5', '='), ('5', '>'), ('5', '?'), ('5', '@'), ('5', '['), ('5', '\\'), ('5', ']'), ('5', '^'), ('5', '_'), ('5', '`'), ('5', '{'), ('5', '|'), ('5', '}'), ('5', '~'), ('6', 'a'), ('6', 'b'), ('6', 'c'), ('6', 'd'), ('6', 'e'), ('6', 'f'), ('6', 'g'), ('6', 'h'), ('6', 'i'), ('6', 'j'), ('6', 'k'), ('6', 'l'), ('6', 'm'), ('6', 'n'), ('6', 'o'), ('6', 'p'), ('6', 'q'), ('6', 'r'), ('6', 's'), ('6', 't'), ('6', 'u'), ('6', 'v'), ('6', 'w'), ('6', 'x'), ('6', 'y'), ('6', 'z'), ('6', 'A'), ('6', 'B'), ('6', 'C'), ('6', 'D'), ('6', 'E'), ('6', 'F'), ('6', 'G'), ('6', 'H'), ('6', 'I'), ('6', 'J'), ('6', 'K'), ('6', 'L'), ('6', 'M'), ('6', 'N'), ('6', 'O'), ('6', 'P'), ('6', 'Q'), ('6', 'R'), ('6', 'S'), ('6', 'T'), ('6', 'U'), ('6', 'V'), ('6', 'W'), ('6', 'X'), ('6', 'Y'), ('6', 'Z'), ('6', '0'), ('6', '1'), ('6', '2'), ('6', '3'), ('6', '4'), ('6', '5'), ('6', '6'), ('6', '7'), ('6', '8'), ('6', '9'), ('6', '!'), ('6', '"'), ('6', '#'), ('6', '$'), ('6', '%'), ('6', '&'), ('6', "'"), ('6', '('), ('6', ')'), ('6', '*'), ('6', '+'), ('6', ','), ('6', '-'), ('6', '.'), ('6', '/'), ('6', ':'), ('6', ';'), ('6', '<'), ('6', '='), ('6', '>'), ('6', '?'), ('6', '@'), ('6', '['), ('6', '\\'), ('6', ']'), ('6', '^'), ('6', '_'), ('6', '`'), ('6', '{'), ('6', '|'), ('6', '}'), ('6', '~'), ('7', 'a'), ('7', 'b'), ('7', 'c'), ('7', 'd'), ('7', 'e'), ('7', 'f'), ('7', 'g'), ('7', 'h'), ('7', 'i'), ('7', 'j'), ('7', 'k'), ('7', 'l'), ('7', 'm'), ('7', 'n'), ('7', 'o'), ('7', 'p'), ('7', 'q'), ('7', 'r'), ('7', 's'), ('7', 't'), ('7', 'u'), ('7', 'v'), ('7', 'w'), ('7', 'x'), ('7', 'y'), ('7', 'z'), ('7', 'A'), ('7', 'B'), ('7', 'C'), ('7', 'D'), ('7', 'E'), ('7', 'F'), ('7', 'G'), ('7', 'H'), ('7', 'I'), ('7', 'J'), ('7', 'K'), ('7', 'L'), ('7', 'M'), ('7', 'N'), ('7', 'O'), ('7', 'P'), ('7', 'Q'), ('7', 'R'), ('7', 'S'), ('7', 'T'), ('7', 'U'), ('7', 'V'), ('7', 'W'), ('7', 'X'), ('7', 'Y'), ('7', 'Z'), ('7', '0'), ('7', '1'), ('7', '2'), ('7', '3'), ('7', '4'), ('7', '5'), ('7', '6'), ('7', '7'), ('7', '8'), ('7', '9'), ('7', '!'), ('7', '"'), ('7', '#'), ('7', '$'), ('7', '%'), ('7', '&'), ('7', "'"), ('7', '('), ('7', ')'), ('7', '*'), ('7', '+'), ('7', ','), ('7', '-'), ('7', '.'), ('7', '/'), ('7', ':'), ('7', ';'), ('7', '<'), ('7', '='), ('7', '>'), ('7', '?'), ('7', '@'), ('7', '['), ('7', '\\'), ('7', ']'), ('7', '^'), ('7', '_'), ('7', '`'), ('7', '{'), ('7', '|'), ('7', '}'), ('7', '~'), ('8', 'a'), ('8', 'b'), ('8', 'c'), ('8', 'd'), ('8', 'e'), ('8', 'f'), ('8', 'g'), ('8', 'h'), ('8', 'i'), ('8', 'j'), ('8', 'k'), ('8', 'l'), ('8', 'm'), ('8', 'n'), ('8', 'o'), ('8', 'p'), ('8', 'q'), ('8', 'r'), ('8', 's'), ('8', 't'), ('8', 'u'), ('8', 'v'), ('8', 'w'), ('8', 'x'), ('8', 'y'), ('8', 'z'), ('8', 'A'), ('8', 'B'), ('8', 'C'), ('8', 'D'), ('8', 'E'), ('8', 'F'), ('8', 'G'), ('8', 'H'), ('8', 'I'), ('8', 'J'), ('8', 'K'), ('8', 'L'), ('8', 'M'), ('8', 'N'), ('8', 'O'), ('8', 'P'), ('8', 'Q'), ('8', 'R'), ('8', 'S'), ('8', 'T'), ('8', 'U'), ('8', 'V'), ('8', 'W'), ('8', 'X'), ('8', 'Y'), ('8', 'Z'), ('8', '0'), ('8', '1'), ('8', '2'), ('8', '3'), ('8', '4'), ('8', '5'), ('8', '6'), ('8', '7'), ('8', '8'), ('8', '9'), ('8', '!'), ('8', '"'), ('8', '#'), ('8', '$'), ('8', '%'), ('8', '&'), ('8', "'"), ('8', '('), ('8', ')'), ('8', '*'), ('8', '+'), ('8', ','), ('8', '-'), ('8', '.'), ('8', '/'), ('8', ':'), ('8', ';'), ('8', '<'), ('8', '='), ('8', '>'), ('8', '?'), ('8', '@'), ('8', '['), ('8', '\\'), ('8', ']'), ('8', '^'), ('8', '_'), ('8', '`'), ('8', '{'), ('8', '|'), ('8', '}'), ('8', '~'), ('9', 'a'), ('9', 'b'), ('9', 'c'), ('9', 'd'), ('9', 'e'), ('9', 'f'), ('9', 'g'), ('9', 'h'), ('9', 'i'), ('9', 'j'), ('9', 'k'), ('9', 'l'), ('9', 'm'), ('9', 'n'), ('9', 'o'), ('9', 'p'), ('9', 'q'), ('9', 'r'), ('9', 's'), ('9', 't'), ('9', 'u'), ('9', 'v'), ('9', 'w'), ('9', 'x'), ('9', 'y'), ('9', 'z'), ('9', 'A'), ('9', 'B'), ('9', 'C'), ('9', 'D'), ('9', 'E'), ('9', 'F'), ('9', 'G'), ('9', 'H'), ('9', 'I'), ('9', 'J'), ('9', 'K'), ('9', 'L'), ('9', 'M'), ('9', 'N'), ('9', 'O'), ('9', 'P'), ('9', 'Q'), ('9', 'R'), ('9', 'S'), ('9', 'T'), ('9', 'U'), ('9', 'V'), ('9', 'W'), ('9', 'X'), ('9', 'Y'), ('9', 'Z'), ('9', '0'), ('9', '1'), ('9', '2'), ('9', '3'), ('9', '4'), ('9', '5'), ('9', '6'), ('9', '7'), ('9', '8'), ('9', '9'), ('9', '!'), ('9', '"'), ('9', '#'), ('9', '$'), ('9', '%'), ('9', '&'), ('9', "'"), ('9', '('), ('9', ')'), ('9', '*'), ('9', '+'), ('9', ','), ('9', '-'), ('9', '.'), ('9', '/'), ('9', ':'), ('9', ';'), ('9', '<'), ('9', '='), ('9', '>'), ('9', '?'), ('9', '@'), ('9', '['), ('9', '\\'), ('9', ']'), ('9', '^'), ('9', '_'), ('9', '`'), ('9', '{'), ('9', '|'), ('9', '}'), ('9', '~'), ('!', 'a'), ('!', 'b'), ('!', 'c'), ('!', 'd'), ('!', 'e'), ('!', 'f'), ('!', 'g'), ('!', 'h'), ('!', 'i'), ('!', 'j'), ('!', 'k'), ('!', 'l'), ('!', 'm'), ('!', 'n'), ('!', 'o'), ('!', 'p'), ('!', 'q'), ('!', 'r'), ('!', 's'), ('!', 't'), ('!', 'u'), ('!', 'v'), ('!', 'w'), ('!', 'x'), ('!', 'y'), ('!', 'z'), ('!', 'A'), ('!', 'B'), ('!', 'C'), ('!', 'D'), ('!', 'E'), ('!', 'F'), ('!', 'G'), ('!', 'H'), ('!', 'I'), ('!', 'J'), ('!', 'K'), ('!', 'L'), ('!', 'M'), ('!', 'N'), ('!', 'O'), ('!', 'P'), ('!', 'Q'), ('!', 'R'), ('!', 'S'), ('!', 'T'), ('!', 'U'), ('!', 'V'), ('!', 'W'), ('!', 'X'), ('!', 'Y'), ('!', 'Z'), ('!', '0'), ('!', '1'), ('!', '2'), ('!', '3'), ('!', '4'), ('!', '5'), ('!', '6'), ('!', '7'), ('!', '8'), ('!', '9'), ('!', '!'), ('!', '"'), ('!', '#'), ('!', '$'), ('!', '%'), ('!', '&'), ('!', "'"), ('!', '('), ('!', ')'), ('!', '*'), ('!', '+'), ('!', ','), ('!', '-'), ('!', '.'), ('!', '/'), ('!', ':'), ('!', ';'), ('!', '<'), ('!', '='), ('!', '>'), ('!', '?'), ('!', '@'), ('!', '['), ('!', '\\'), ('!', ']'), ('!', '^'), ('!', '_'), ('!', '`'), ('!', '{'), ('!', '|'), ('!', '}'), ('!', '~'), ('"', 'a'), ('"', 'b'), ('"', 'c'), ('"', 'd'), ('"', 'e'), ('"', 'f'), ('"', 'g'), ('"', 'h'), ('"', 'i'), ('"', 'j'), ('"', 'k'), ('"', 'l'), ('"', 'm'), ('"', 'n'), ('"', 'o'), ('"', 'p'), ('"', 'q'), ('"', 'r'), ('"', 's'), ('"', 't'), ('"', 'u'), ('"', 'v'), ('"', 'w'), ('"', 'x'), ('"', 'y'), ('"', 'z'), ('"', 'A'), ('"', 'B'), ('"', 'C'), ('"', 'D'), ('"', 'E'), ('"', 'F'), ('"', 'G'), ('"', 'H'), ('"', 'I'), ('"', 'J'), ('"', 'K'), ('"', 'L'), ('"', 'M'), ('"', 'N'), ('"', 'O'), ('"', 'P'), ('"', 'Q'), ('"', 'R'), ('"', 'S'), ('"', 'T'), ('"', 'U'), ('"', 'V'), ('"', 'W'), ('"', 'X'), ('"', 'Y'), ('"', 'Z'), ('"', '0'), ('"', '1'), ('"', '2'), ('"', '3'), ('"', '4'), ('"', '5'), ('"', '6'), ('"', '7'), ('"', '8'), ('"', '9'), ('"', '!'), ('"', '"'), ('"', '#'), ('"', '$'), ('"', '%'), ('"', '&'), ('"', "'"), ('"', '('), ('"', ')'), ('"', '*'), ('"', '+'), ('"', ','), ('"', '-'), ('"', '.'), ('"', '/'), ('"', ':'), ('"', ';'), ('"', '<'), ('"', '='), ('"', '>'), ('"', '?'), ('"', '@'), ('"', '['), ('"', '\\'), ('"', ']'), ('"', '^'), ('"', '_'), ('"', '`'), ('"', '{'), ('"', '|'), ('"', '}'), ('"', '~'), ('#', 'a'), ('#', 'b'), ('#', 'c'), ('#', 'd'), ('#', 'e'), ('#', 'f'), ('#', 'g'), ('#', 'h'), ('#', 'i'), ('#', 'j'), ('#', 'k'), ('#', 'l'), ('#', 'm'), ('#', 'n'), ('#', 'o'), ('#', 'p'), ('#', 'q'), ('#', 'r'), ('#', 's'), ('#', 't'), ('#', 'u'), ('#', 'v'), ('#', 'w'), ('#', 'x'), ('#', 'y'), ('#', 'z'), ('#', 'A'), ('#', 'B'), ('#', 'C'), ('#', 'D'), ('#', 'E'), ('#', 'F'), ('#', 'G'), ('#', 'H'), ('#', 'I'), ('#', 'J'), ('#', 'K'), ('#', 'L'), ('#', 'M'), ('#', 'N'), ('#', 'O'), ('#', 'P'), ('#', 'Q'), ('#', 'R'), ('#', 'S'), ('#', 'T'), ('#', 'U'), ('#', 'V'), ('#', 'W'), ('#', 'X'), ('#', 'Y'), ('#', 'Z'), ('#', '0'), ('#', '1'), ('#', '2'), ('#', '3'), ('#', '4'), ('#', '5'), ('#', '6'), ('#', '7'), ('#', '8'), ('#', '9'), ('#', '!'), ('#', '"'), ('#', '#'), ('#', '$'), ('#', '%'), ('#', '&'), ('#', "'"), ('#', '('), ('#', ')'), ('#', '*'), ('#', '+'), ('#', ','), ('#', '-'), ('#', '.'), ('#', '/'), ('#', ':'), ('#', ';'), ('#', '<'), ('#', '='), ('#', '>'), ('#', '?'), ('#', '@'), ('#', '['), ('#', '\\'), ('#', ']'), ('#', '^'), ('#', '_'), ('#', '`'), ('#', '{'), ('#', '|'), ('#', '}'), ('#', '~'), ('$', 'a'), ('$', 'b'), ('$', 'c'), ('$', 'd'), ('$', 'e'), ('$', 'f'), ('$', 'g'), ('$', 'h'), ('$', 'i'), ('$', 'j'), ('$', 'k'), ('$', 'l'), ('$', 'm'), ('$', 'n'), ('$', 'o'), ('$', 'p'), ('$', 'q'), ('$', 'r'), ('$', 's'), ('$', 't'), ('$', 'u'), ('$', 'v'), ('$', 'w'), ('$', 'x'), ('$', 'y'), ('$', 'z'), ('$', 'A'), ('$', 'B'), ('$', 'C'), ('$', 'D'), ('$', 'E'), ('$', 'F'), ('$', 'G'), ('$', 'H'), ('$', 'I'), ('$', 'J'), ('$', 'K'), ('$', 'L'), ('$', 'M'), ('$', 'N'), ('$', 'O'), ('$', 'P'), ('$', 'Q'), ('$', 'R'), ('$', 'S'), ('$', 'T'), ('$', 'U'), ('$', 'V'), ('$', 'W'), ('$', 'X'), ('$', 'Y'), ('$', 'Z'), ('$', '0'), ('$', '1'), ('$', '2'), ('$', '3'), ('$', '4'), ('$', '5'), ('$', '6'), ('$', '7'), ('$', '8'), ('$', '9'), ('$', '!'), ('$', '"'), ('$', '#'), ('$', '$'), ('$', '%'), ('$', '&'), ('$', "'"), ('$', '('), ('$', ')'), ('$', '*'), ('$', '+'), ('$', ','), ('$', '-'), ('$', '.'), ('$', '/'), ('$', ':'), ('$', ';'), ('$', '<'), ('$', '='), ('$', '>'), ('$', '?'), ('$', '@'), ('$', '['), ('$', '\\'), ('$', ']'), ('$', '^'), ('$', '_'), ('$', '`'), ('$', '{'), ('$', '|'), ('$', '}'), ('$', '~'), ('%', 'a'), ('%', 'b'), ('%', 'c'), ('%', 'd'), ('%', 'e'), ('%', 'f'), ('%', 'g'), ('%', 'h'), ('%', 'i'), ('%', 'j'), ('%', 'k'), ('%', 'l'), ('%', 'm'), ('%', 'n'), ('%', 'o'), ('%', 'p'), ('%', 'q'), ('%', 'r'), ('%', 's'), ('%', 't'), ('%', 'u'), ('%', 'v'), ('%', 'w'), ('%', 'x'), ('%', 'y'), ('%', 'z'), ('%', 'A'), ('%', 'B'), ('%', 'C'), ('%', 'D'), ('%', 'E'), ('%', 'F'), ('%', 'G'), ('%', 'H'), ('%', 'I'), ('%', 'J'), ('%', 'K'), ('%', 'L'), ('%', 'M'), ('%', 'N'), ('%', 'O'), ('%', 'P'), ('%', 'Q'), ('%', 'R'), ('%', 'S'), ('%', 'T'), ('%', 'U'), ('%', 'V'), ('%', 'W'), ('%', 'X'), ('%', 'Y'), ('%', 'Z'), ('%', '0'), ('%', '1'), ('%', '2'), ('%', '3'), ('%', '4'), ('%', '5'), ('%', '6'), ('%', '7'), ('%', '8'), ('%', '9'), ('%', '!'), ('%', '"'), ('%', '#'), ('%', '$'), ('%', '%'), ('%', '&'), ('%', "'"), ('%', '('), ('%', ')'), ('%', '*'), ('%', '+'), ('%', ','), ('%', '-'), ('%', '.'), ('%', '/'), ('%', ':'), ('%', ';'), ('%', '<'), ('%', '='), ('%', '>'), ('%', '?'), ('%', '@'), ('%', '['), ('%', '\\'), ('%', ']'), ('%', '^'), ('%', '_'), ('%', '`'), ('%', '{'), ('%', '|'), ('%', '}'), ('%', '~'), ('&', 'a'), ('&', 'b'), ('&', 'c'), ('&', 'd'), ('&', 'e'), ('&', 'f'), ('&', 'g'), ('&', 'h'), ('&', 'i'), ('&', 'j'), ('&', 'k'), ('&', 'l'), ('&', 'm'), ('&', 'n'), ('&', 'o'), ('&', 'p'), ('&', 'q'), ('&', 'r'), ('&', 's'), ('&', 't'), ('&', 'u'), ('&', 'v'), ('&', 'w'), ('&', 'x'), ('&', 'y'), ('&', 'z'), ('&', 'A'), ('&', 'B'), ('&', 'C'), ('&', 'D'), ('&', 'E'), ('&', 'F'), ('&', 'G'), ('&', 'H'), ('&', 'I'), ('&', 'J'), ('&', 'K'), ('&', 'L'), ('&', 'M'), ('&', 'N'), ('&', 'O'), ('&', 'P'), ('&', 'Q'), ('&', 'R'), ('&', 'S'), ('&', 'T'), ('&', 'U'), ('&', 'V'), ('&', 'W'), ('&', 'X'), ('&', 'Y'), ('&', 'Z'), ('&', '0'), ('&', '1'), ('&', '2'), ('&', '3'), ('&', '4'), ('&', '5'), ('&', '6'), ('&', '7'), ('&', '8'), ('&', '9'), ('&', '!'), ('&', '"'), ('&', '#'), ('&', '$'), ('&', '%'), ('&', '&'), ('&', "'"), ('&', '('), ('&', ')'), ('&', '*'), ('&', '+'), ('&', ','), ('&', '-'), ('&', '.'), ('&', '/'), ('&', ':'), ('&', ';'), ('&', '<'), ('&', '='), ('&', '>'), ('&', '?'), ('&', '@'), ('&', '['), ('&', '\\'), ('&', ']'), ('&', '^'), ('&', '_'), ('&', '`'), ('&', '{'), ('&', '|'), ('&', '}'), ('&', '~'), ("'", 'a'), ("'", 'b'), ("'", 'c'), ("'", 'd'), ("'", 'e'), ("'", 'f'), ("'", 'g'), ("'", 'h'), ("'", 'i'), ("'", 'j'), ("'", 'k'), ("'", 'l'), ("'", 'm'), ("'", 'n'), ("'", 'o'), ("'", 'p'), ("'", 'q'), ("'", 'r'), ("'", 's'), ("'", 't'), ("'", 'u'), ("'", 'v'), ("'", 'w'), ("'", 'x'), ("'", 'y'), ("'", 'z'), ("'", 'A'), ("'", 'B'), ("'", 'C'), ("'", 'D'), ("'", 'E'), ("'", 'F'), ("'", 'G'), ("'", 'H'), ("'", 'I'), ("'", 'J'), ("'", 'K'), ("'", 'L'), ("'", 'M'), ("'", 'N'), ("'", 'O'), ("'", 'P'), ("'", 'Q'), ("'", 'R'), ("'", 'S'), ("'", 'T'), ("'", 'U'), ("'", 'V'), ("'", 'W'), ("'", 'X'), ("'", 'Y'), ("'", 'Z'), ("'", '0'), ("'", '1'), ("'", '2'), ("'", '3'), ("'", '4'), ("'", '5'), ("'", '6'), ("'", '7'), ("'", '8'), ("'", '9'), ("'", '!'), ("'", '"'), ("'", '#'), ("'", '$'), ("'", '%'), ("'", '&'), ("'", "'"), ("'", '('), ("'", ')'), ("'", '*'), ("'", '+'), ("'", ','), ("'", '-'), ("'", '.'), ("'", '/'), ("'", ':'), ("'", ';'), ("'", '<'), ("'", '='), ("'", '>'), ("'", '?'), ("'", '@'), ("'", '['), ("'", '\\'), ("'", ']'), ("'", '^'), ("'", '_'), ("'", '`'), ("'", '{'), ("'", '|'), ("'", '}'), ("'", '~'), ('(', 'a'), ('(', 'b'), ('(', 'c'), ('(', 'd'), ('(', 'e'), ('(', 'f'), ('(', 'g'), ('(', 'h'), ('(', 'i'), ('(', 'j'), ('(', 'k'), ('(', 'l'), ('(', 'm'), ('(', 'n'), ('(', 'o'), ('(', 'p'), ('(', 'q'), ('(', 'r'), ('(', 's'), ('(', 't'), ('(', 'u'), ('(', 'v'), ('(', 'w'), ('(', 'x'), ('(', 'y'), ('(', 'z'), ('(', 'A'), ('(', 'B'), ('(', 'C'), ('(', 'D'), ('(', 'E'), ('(', 'F'), ('(', 'G'), ('(', 'H'), ('(', 'I'), ('(', 'J'), ('(', 'K'), ('(', 'L'), ('(', 'M'), ('(', 'N'), ('(', 'O'), ('(', 'P'), ('(', 'Q'), ('(', 'R'), ('(', 'S'), ('(', 'T'), ('(', 'U'), ('(', 'V'), ('(', 'W'), ('(', 'X'), ('(', 'Y'), ('(', 'Z'), ('(', '0'), ('(', '1'), ('(', '2'), ('(', '3'), ('(', '4'), ('(', '5'), ('(', '6'), ('(', '7'), ('(', '8'), ('(', '9'), ('(', '!'), ('(', '"'), ('(', '#'), ('(', '$'), ('(', '%'), ('(', '&'), ('(', "'"), ('(', '('), ('(', ')'), ('(', '*'), ('(', '+'), ('(', ','), ('(', '-'), ('(', '.'), ('(', '/'), ('(', ':'), ('(', ';'), ('(', '<'), ('(', '='), ('(', '>'), ('(', '?'), ('(', '@'), ('(', '['), ('(', '\\'), ('(', ']'), ('(', '^'), ('(', '_'), ('(', '`'), ('(', '{'), ('(', '|'), ('(', '}'), ('(', '~'), (')', 'a'), (')', 'b'), (')', 'c'), (')', 'd'), (')', 'e'), (')', 'f'), (')', 'g'), (')', 'h'), (')', 'i'), (')', 'j'), (')', 'k'), (')', 'l'), (')', 'm'), (')', 'n'), (')', 'o'), (')', 'p'), (')', 'q'), (')', 'r'), (')', 's'), (')', 't'), (')', 'u'), (')', 'v'), (')', 'w'), (')', 'x'), (')', 'y'), (')', 'z'), (')', 'A'), (')', 'B'), (')', 'C'), (')', 'D'), (')', 'E'), (')', 'F'), (')', 'G'), (')', 'H'), (')', 'I'), (')', 'J'), (')', 'K'), (')', 'L'), (')', 'M'), (')', 'N'), (')', 'O'), (')', 'P'), (')', 'Q'), (')', 'R'), (')', 'S'), (')', 'T'), (')', 'U'), (')', 'V'), (')', 'W'), (')', 'X'), (')', 'Y'), (')', 'Z'), (')', '0'), (')', '1'), (')', '2'), (')', '3'), (')', '4'), (')', '5'), (')', '6'), (')', '7'), (')', '8'), (')', '9'), (')', '!'), (')', '"'), (')', '#'), (')', '$'), (')', '%'), (')', '&'), (')', "'"), (')', '('), (')', ')'), (')', '*'), (')', '+'), (')', ','), (')', '-'), (')', '.'), (')', '/'), (')', ':'), (')', ';'), (')', '<'), (')', '='), (')', '>'), (')', '?'), (')', '@'), (')', '['), (')', '\\'), (')', ']'), (')', '^'), (')', '_'), (')', '`'), (')', '{'), (')', '|'), (')', '}'), (')', '~'), ('*', 'a'), ('*', 'b'), ('*', 'c'), ('*', 'd'), ('*', 'e'), ('*', 'f'), ('*', 'g'), ('*', 'h'), ('*', 'i'), ('*', 'j'), ('*', 'k'), ('*', 'l'), ('*', 'm'), ('*', 'n'), ('*', 'o'), ('*', 'p'), ('*', 'q'), ('*', 'r'), ('*', 's'), ('*', 't'), ('*', 'u'), ('*', 'v'), ('*', 'w'), ('*', 'x'), ('*', 'y'), ('*', 'z'), ('*', 'A'), ('*', 'B'), ('*', 'C'), ('*', 'D'), ('*', 'E'), ('*', 'F'), ('*', 'G'), ('*', 'H'), ('*', 'I'), ('*', 'J'), ('*', 'K'), ('*', 'L'), ('*', 'M'), ('*', 'N'), ('*', 'O'), ('*', 'P'), ('*', 'Q'), ('*', 'R'), ('*', 'S'), ('*', 'T'), ('*', 'U'), ('*', 'V'), ('*', 'W'), ('*', 'X'), ('*', 'Y'), ('*', 'Z'), ('*', '0'), ('*', '1'), ('*', '2'), ('*', '3'), ('*', '4'), ('*', '5'), ('*', '6'), ('*', '7'), ('*', '8'), ('*', '9'), ('*', '!'), ('*', '"'), ('*', '#'), ('*', '$'), ('*', '%'), ('*', '&'), ('*', "'"), ('*', '('), ('*', ')'), ('*', '*'), ('*', '+'), ('*', ','), ('*', '-'), ('*', '.'), ('*', '/'), ('*', ':'), ('*', ';'), ('*', '<'), ('*', '='), ('*', '>'), ('*', '?'), ('*', '@'), ('*', '['), ('*', '\\'), ('*', ']'), ('*', '^'), ('*', '_'), ('*', '`'), ('*', '{'), ('*', '|'), ('*', '}'), ('*', '~'), ('+', 'a'), ('+', 'b'), ('+', 'c'), ('+', 'd'), ('+', 'e'), ('+', 'f'), ('+', 'g'), ('+', 'h'), ('+', 'i'), ('+', 'j'), ('+', 'k'), ('+', 'l'), ('+', 'm'), ('+', 'n'), ('+', 'o'), ('+', 'p'), ('+', 'q'), ('+', 'r'), ('+', 's'), ('+', 't'), ('+', 'u'), ('+', 'v'), ('+', 'w'), ('+', 'x'), ('+', 'y'), ('+', 'z'), ('+', 'A'), ('+', 'B'), ('+', 'C'), ('+', 'D'), ('+', 'E'), ('+', 'F'), ('+', 'G'), ('+', 'H'), ('+', 'I'), ('+', 'J'), ('+', 'K'), ('+', 'L'), ('+', 'M'), ('+', 'N'), ('+', 'O'), ('+', 'P'), ('+', 'Q'), ('+', 'R'), ('+', 'S'), ('+', 'T'), ('+', 'U'), ('+', 'V'), ('+', 'W'), ('+', 'X'), ('+', 'Y'), ('+', 'Z'), ('+', '0'), ('+', '1'), ('+', '2'), ('+', '3'), ('+', '4'), ('+', '5'), ('+', '6'), ('+', '7'), ('+', '8'), ('+', '9'), ('+', '!'), ('+', '"'), ('+', '#'), ('+', '$'), ('+', '%'), ('+', '&'), ('+', "'"), ('+', '('), ('+', ')'), ('+', '*'), ('+', '+'), ('+', ','), ('+', '-'), ('+', '.'), ('+', '/'), ('+', ':'), ('+', ';'), ('+', '<'), ('+', '='), ('+', '>'), ('+', '?'), ('+', '@'), ('+', '['), ('+', '\\'), ('+', ']'), ('+', '^'), ('+', '_'), ('+', '`'), ('+', '{'), ('+', '|'), ('+', '}'), ('+', '~'), (',', 'a'), (',', 'b'), (',', 'c'), (',', 'd'), (',', 'e'), (',', 'f'), (',', 'g'), (',', 'h'), (',', 'i'), (',', 'j'), (',', 'k'), (',', 'l'), (',', 'm'), (',', 'n'), (',', 'o'), (',', 'p'), (',', 'q'), (',', 'r'), (',', 's'), (',', 't'), (',', 'u'), (',', 'v'), (',', 'w'), (',', 'x'), (',', 'y'), (',', 'z'), (',', 'A'), (',', 'B'), (',', 'C'), (',', 'D'), (',', 'E'), (',', 'F'), (',', 'G'), (',', 'H'), (',', 'I'), (',', 'J'), (',', 'K'), (',', 'L'), (',', 'M'), (',', 'N'), (',', 'O'), (',', 'P'), (',', 'Q'), (',', 'R'), (',', 'S'), (',', 'T'), (',', 'U'), (',', 'V'), (',', 'W'), (',', 'X'), (',', 'Y'), (',', 'Z'), (',', '0'), (',', '1'), (',', '2'), (',', '3'), (',', '4'), (',', '5'), (',', '6'), (',', '7'), (',', '8'), (',', '9'), (',', '!'), (',', '"'), (',', '#'), (',', '$'), (',', '%'), (',', '&'), (',', "'"), (',', '('), (',', ')'), (',', '*'), (',', '+'), (',', ','), (',', '-'), (',', '.'), (',', '/'), (',', ':'), (',', ';'), (',', '<'), (',', '='), (',', '>'), (',', '?'), (',', '@'), (',', '['), (',', '\\'), (',', ']'), (',', '^'), (',', '_'), (',', '`'), (',', '{'), (',', '|'), (',', '}'), (',', '~'), ('-', 'a'), ('-', 'b'), ('-', 'c'), ('-', 'd'), ('-', 'e'), ('-', 'f'), ('-', 'g'), ('-', 'h'), ('-', 'i'), ('-', 'j'), ('-', 'k'), ('-', 'l'), ('-', 'm'), ('-', 'n'), ('-', 'o'), ('-', 'p'), ('-', 'q'), ('-', 'r'), ('-', 's'), ('-', 't'), ('-', 'u'), ('-', 'v'), ('-', 'w'), ('-', 'x'), ('-', 'y'), ('-', 'z'), ('-', 'A'), ('-', 'B'), ('-', 'C'), ('-', 'D'), ('-', 'E'), ('-', 'F'), ('-', 'G'), ('-', 'H'), ('-', 'I'), ('-', 'J'), ('-', 'K'), ('-', 'L'), ('-', 'M'), ('-', 'N'), ('-', 'O'), ('-', 'P'), ('-', 'Q'), ('-', 'R'), ('-', 'S'), ('-', 'T'), ('-', 'U'), ('-', 'V'), ('-', 'W'), ('-', 'X'), ('-', 'Y'), ('-', 'Z'), ('-', '0'), ('-', '1'), ('-', '2'), ('-', '3'), ('-', '4'), ('-', '5'), ('-', '6'), ('-', '7'), ('-', '8'), ('-', '9'), ('-', '!'), ('-', '"'), ('-', '#'), ('-', '$'), ('-', '%'), ('-', '&'), ('-', "'"), ('-', '('), ('-', ')'), ('-', '*'), ('-', '+'), ('-', ','), ('-', '-'), ('-', '.'), ('-', '/'), ('-', ':'), ('-', ';'), ('-', '<'), ('-', '='), ('-', '>'), ('-', '?'), ('-', '@'), ('-', '['), ('-', '\\'), ('-', ']'), ('-', '^'), ('-', '_'), ('-', '`'), ('-', '{'), ('-', '|'), ('-', '}'), ('-', '~'), ('.', 'a'), ('.', 'b'), ('.', 'c'), ('.', 'd'), ('.', 'e'), ('.', 'f'), ('.', 'g'), ('.', 'h'), ('.', 'i'), ('.', 'j'), ('.', 'k'), ('.', 'l'), ('.', 'm'), ('.', 'n'), ('.', 'o'), ('.', 'p'), ('.', 'q'), ('.', 'r'), ('.', 's'), ('.', 't'), ('.', 'u'), ('.', 'v'), ('.', 'w'), ('.', 'x'), ('.', 'y'), ('.', 'z'), ('.', 'A'), ('.', 'B'), ('.', 'C'), ('.', 'D'), ('.', 'E'), ('.', 'F'), ('.', 'G'), ('.', 'H'), ('.', 'I'), ('.', 'J'), ('.', 'K'), ('.', 'L'), ('.', 'M'), ('.', 'N'), ('.', 'O'), ('.', 'P'), ('.', 'Q'), ('.', 'R'), ('.', 'S'), ('.', 'T'), ('.', 'U'), ('.', 'V'), ('.', 'W'), ('.', 'X'), ('.', 'Y'), ('.', 'Z'), ('.', '0'), ('.', '1'), ('.', '2'), ('.', '3'), ('.', '4'), ('.', '5'), ('.', '6'), ('.', '7'), ('.', '8'), ('.', '9'), ('.', '!'), ('.', '"'), ('.', '#'), ('.', '$'), ('.', '%'), ('.', '&'), ('.', "'"), ('.', '('), ('.', ')'), ('.', '*'), ('.', '+'), ('.', ','), ('.', '-'), ('.', '.'), ('.', '/'), ('.', ':'), ('.', ';'), ('.', '<'), ('.', '='), ('.', '>'), ('.', '?'), ('.', '@'), ('.', '['), ('.', '\\'), ('.', ']'), ('.', '^'), ('.', '_'), ('.', '`'), ('.', '{'), ('.', '|'), ('.', '}'), ('.', '~'), ('/', 'a'), ('/', 'b'), ('/', 'c'), ('/', 'd'), ('/', 'e'), ('/', 'f'), ('/', 'g'), ('/', 'h'), ('/', 'i'), ('/', 'j'), ('/', 'k'), ('/', 'l'), ('/', 'm'), ('/', 'n'), ('/', 'o'), ('/', 'p'), ('/', 'q'), ('/', 'r'), ('/', 's'), ('/', 't'), ('/', 'u'), ('/', 'v'), ('/', 'w'), ('/', 'x'), ('/', 'y'), ('/', 'z'), ('/', 'A'), ('/', 'B'), ('/', 'C'), ('/', 'D'), ('/', 'E'), ('/', 'F'), ('/', 'G'), ('/', 'H'), ('/', 'I'), ('/', 'J'), ('/', 'K'), ('/', 'L'), ('/', 'M'), ('/', 'N'), ('/', 'O'), ('/', 'P'), ('/', 'Q'), ('/', 'R'), ('/', 'S'), ('/', 'T'), ('/', 'U'), ('/', 'V'), ('/', 'W'), ('/', 'X'), ('/', 'Y'), ('/', 'Z'), ('/', '0'), ('/', '1'), ('/', '2'), ('/', '3'), ('/', '4'), ('/', '5'), ('/', '6'), ('/', '7'), ('/', '8'), ('/', '9'), ('/', '!'), ('/', '"'), ('/', '#'), ('/', '$'), ('/', '%'), ('/', '&'), ('/', "'"), ('/', '('), ('/', ')'), ('/', '*'), ('/', '+'), ('/', ','), ('/', '-'), ('/', '.'), ('/', '/'), ('/', ':'), ('/', ';'), ('/', '<'), ('/', '='), ('/', '>'), ('/', '?'), ('/', '@'), ('/', '['), ('/', '\\'), ('/', ']'), ('/', '^'), ('/', '_'), ('/', '`'), ('/', '{'), ('/', '|'), ('/', '}'), ('/', '~'), (':', 'a'), (':', 'b'), (':', 'c'), (':', 'd'), (':', 'e'), (':', 'f'), (':', 'g'), (':', 'h'), (':', 'i'), (':', 'j'), (':', 'k'), (':', 'l'), (':', 'm'), (':', 'n'), (':', 'o'), (':', 'p'), (':', 'q'), (':', 'r'), (':', 's'), (':', 't'), (':', 'u'), (':', 'v'), (':', 'w'), (':', 'x'), (':', 'y'), (':', 'z'), (':', 'A'), (':', 'B'), (':', 'C'), (':', 'D'), (':', 'E'), (':', 'F'), (':', 'G'), (':', 'H'), (':', 'I'), (':', 'J'), (':', 'K'), (':', 'L'), (':', 'M'), (':', 'N'), (':', 'O'), (':', 'P'), (':', 'Q'), (':', 'R'), (':', 'S'), (':', 'T'), (':', 'U'), (':', 'V'), (':', 'W'), (':', 'X'), (':', 'Y'), (':', 'Z'), (':', '0'), (':', '1'), (':', '2'), (':', '3'), (':', '4'), (':', '5'), (':', '6'), (':', '7'), (':', '8'), (':', '9'), (':', '!'), (':', '"'), (':', '#'), (':', '$'), (':', '%'), (':', '&'), (':', "'"), (':', '('), (':', ')'), (':', '*'), (':', '+'), (':', ','), (':', '-'), (':', '.'), (':', '/'), (':', ':'), (':', ';'), (':', '<'), (':', '='), (':', '>'), (':', '?'), (':', '@'), (':', '['), (':', '\\'), (':', ']'), (':', '^'), (':', '_'), (':', '`'), (':', '{'), (':', '|'), (':', '}'), (':', '~'), (';', 'a'), (';', 'b'), (';', 'c'), (';', 'd'), (';', 'e'), (';', 'f'), (';', 'g'), (';', 'h'), (';', 'i'), (';', 'j'), (';', 'k'), (';', 'l'), (';', 'm'), (';', 'n'), (';', 'o'), (';', 'p'), (';', 'q'), (';', 'r'), (';', 's'), (';', 't'), (';', 'u'), (';', 'v'), (';', 'w'), (';', 'x'), (';', 'y'), (';', 'z'), (';', 'A'), (';', 'B'), (';', 'C'), (';', 'D'), (';', 'E'), (';', 'F'), (';', 'G'), (';', 'H'), (';', 'I'), (';', 'J'), (';', 'K'), (';', 'L'), (';', 'M'), (';', 'N'), (';', 'O'), (';', 'P'), (';', 'Q'), (';', 'R'), (';', 'S'), (';', 'T'), (';', 'U'), (';', 'V'), (';', 'W'), (';', 'X'), (';', 'Y'), (';', 'Z'), (';', '0'), (';', '1'), (';', '2'), (';', '3'), (';', '4'), (';', '5'), (';', '6'), (';', '7'), (';', '8'), (';', '9'), (';', '!'), (';', '"'), (';', '#'), (';', '$'), (';', '%'), (';', '&'), (';', "'"), (';', '('), (';', ')'), (';', '*'), (';', '+'), (';', ','), (';', '-'), (';', '.'), (';', '/'), (';', ':'), (';', ';'), (';', '<'), (';', '='), (';', '>'), (';', '?'), (';', '@'), (';', '['), (';', '\\'), (';', ']'), (';', '^'), (';', '_'), (';', '`'), (';', '{'), (';', '|'), (';', '}'), (';', '~'), ('<', 'a'), ('<', 'b'), ('<', 'c'), ('<', 'd'), ('<', 'e'), ('<', 'f'), ('<', 'g'), ('<', 'h'), ('<', 'i'), ('<', 'j'), ('<', 'k'), ('<', 'l'), ('<', 'm'), ('<', 'n'), ('<', 'o'), ('<', 'p'), ('<', 'q'), ('<', 'r'), ('<', 's'), ('<', 't'), ('<', 'u'), ('<', 'v'), ('<', 'w'), ('<', 'x'), ('<', 'y'), ('<', 'z'), ('<', 'A'), ('<', 'B'), ('<', 'C'), ('<', 'D'), ('<', 'E'), ('<', 'F'), ('<', 'G'), ('<', 'H'), ('<', 'I'), ('<', 'J'), ('<', 'K'), ('<', 'L'), ('<', 'M'), ('<', 'N'), ('<', 'O'), ('<', 'P'), ('<', 'Q'), ('<', 'R'), ('<', 'S'), ('<', 'T'), ('<', 'U'), ('<', 'V'), ('<', 'W'), ('<', 'X'), ('<', 'Y'), ('<', 'Z'), ('<', '0'), ('<', '1'), ('<', '2'), ('<', '3'), ('<', '4'), ('<', '5'), ('<', '6'), ('<', '7'), ('<', '8'), ('<', '9'), ('<', '!'), ('<', '"'), ('<', '#'), ('<', '$'), ('<', '%'), ('<', '&'), ('<', "'"), ('<', '('), ('<', ')'), ('<', '*'), ('<', '+'), ('<', ','), ('<', '-'), ('<', '.'), ('<', '/'), ('<', ':'), ('<', ';'), ('<', '<'), ('<', '='), ('<', '>'), ('<', '?'), ('<', '@'), ('<', '['), ('<', '\\'), ('<', ']'), ('<', '^'), ('<', '_'), ('<', '`'), ('<', '{'), ('<', '|'), ('<', '}'), ('<', '~'), ('=', 'a'), ('=', 'b'), ('=', 'c'), ('=', 'd'), ('=', 'e'), ('=', 'f'), ('=', 'g'), ('=', 'h'), ('=', 'i'), ('=', 'j'), ('=', 'k'), ('=', 'l'), ('=', 'm'), ('=', 'n'), ('=', 'o'), ('=', 'p'), ('=', 'q'), ('=', 'r'), ('=', 's'), ('=', 't'), ('=', 'u'), ('=', 'v'), ('=', 'w'), ('=', 'x'), ('=', 'y'), ('=', 'z'), ('=', 'A'), ('=', 'B'), ('=', 'C'), ('=', 'D'), ('=', 'E'), ('=', 'F'), ('=', 'G'), ('=', 'H'), ('=', 'I'), ('=', 'J'), ('=', 'K'), ('=', 'L'), ('=', 'M'), ('=', 'N'), ('=', 'O'), ('=', 'P'), ('=', 'Q'), ('=', 'R'), ('=', 'S'), ('=', 'T'), ('=', 'U'), ('=', 'V'), ('=', 'W'), ('=', 'X'), ('=', 'Y'), ('=', 'Z'), ('=', '0'), ('=', '1'), ('=', '2'), ('=', '3'), ('=', '4'), ('=', '5'), ('=', '6'), ('=', '7'), ('=', '8'), ('=', '9'), ('=', '!'), ('=', '"'), ('=', '#'), ('=', '$'), ('=', '%'), ('=', '&'), ('=', "'"), ('=', '('), ('=', ')'), ('=', '*'), ('=', '+'), ('=', ','), ('=', '-'), ('=', '.'), ('=', '/'), ('=', ':'), ('=', ';'), ('=', '<'), ('=', '='), ('=', '>'), ('=', '?'), ('=', '@'), ('=', '['), ('=', '\\'), ('=', ']'), ('=', '^'), ('=', '_'), ('=', '`'), ('=', '{'), ('=', '|'), ('=', '}'), ('=', '~'), ('>', 'a'), ('>', 'b'), ('>', 'c'), ('>', 'd'), ('>', 'e'), ('>', 'f'), ('>', 'g'), ('>', 'h'), ('>', 'i'), ('>', 'j'), ('>', 'k'), ('>', 'l'), ('>', 'm'), ('>', 'n'), ('>', 'o'), ('>', 'p'), ('>', 'q'), ('>', 'r'), ('>', 's'), ('>', 't'), ('>', 'u'), ('>', 'v'), ('>', 'w'), ('>', 'x'), ('>', 'y'), ('>', 'z'), ('>', 'A'), ('>', 'B'), ('>', 'C'), ('>', 'D'), ('>', 'E'), ('>', 'F'), ('>', 'G'), ('>', 'H'), ('>', 'I'), ('>', 'J'), ('>', 'K'), ('>', 'L'), ('>', 'M'), ('>', 'N'), ('>', 'O'), ('>', 'P'), ('>', 'Q'), ('>', 'R'), ('>', 'S'), ('>', 'T'), ('>', 'U'), ('>', 'V'), ('>', 'W'), ('>', 'X'), ('>', 'Y'), ('>', 'Z'), ('>', '0'), ('>', '1'), ('>', '2'), ('>', '3'), ('>', '4'), ('>', '5'), ('>', '6'), ('>', '7'), ('>', '8'), ('>', '9'), ('>', '!'), ('>', '"'), ('>', '#'), ('>', '$'), ('>', '%'), ('>', '&'), ('>', "'"), ('>', '('), ('>', ')'), ('>', '*'), ('>', '+'), ('>', ','), ('>', '-'), ('>', '.'), ('>', '/'), ('>', ':'), ('>', ';'), ('>', '<'), ('>', '='), ('>', '>'), ('>', '?'), ('>', '@'), ('>', '['), ('>', '\\'), ('>', ']'), ('>', '^'), ('>', '_'), ('>', '`'), ('>', '{'), ('>', '|'), ('>', '}'), ('>', '~'), ('?', 'a'), ('?', 'b'), ('?', 'c'), ('?', 'd'), ('?', 'e'), ('?', 'f'), ('?', 'g'), ('?', 'h'), ('?', 'i'), ('?', 'j'), ('?', 'k'), ('?', 'l'), ('?', 'm'), ('?', 'n'), ('?', 'o'), ('?', 'p'), ('?', 'q'), ('?', 'r'), ('?', 's'), ('?', 't'), ('?', 'u'), ('?', 'v'), ('?', 'w'), ('?', 'x'), ('?', 'y'), ('?', 'z'), ('?', 'A'), ('?', 'B'), ('?', 'C'), ('?', 'D'), ('?', 'E'), ('?', 'F'), ('?', 'G'), ('?', 'H'), ('?', 'I'), ('?', 'J'), ('?', 'K'), ('?', 'L'), ('?', 'M'), ('?', 'N'), ('?', 'O'), ('?', 'P'), ('?', 'Q'), ('?', 'R'), ('?', 'S'), ('?', 'T'), ('?', 'U'), ('?', 'V'), ('?', 'W'), ('?', 'X'), ('?', 'Y'), ('?', 'Z'), ('?', '0'), ('?', '1'), ('?', '2'), ('?', '3'), ('?', '4'), ('?', '5'), ('?', '6'), ('?', '7'), ('?', '8'), ('?', '9'), ('?', '!'), ('?', '"'), ('?', '#'), ('?', '$'), ('?', '%'), ('?', '&'), ('?', "'"), ('?', '('), ('?', ')'), ('?', '*'), ('?', '+'), ('?', ','), ('?', '-'), ('?', '.'), ('?', '/'), ('?', ':'), ('?', ';'), ('?', '<'), ('?', '='), ('?', '>'), ('?', '?'), ('?', '@'), ('?', '['), ('?', '\\'), ('?', ']'), ('?', '^'), ('?', '_'), ('?', '`'), ('?', '{'), ('?', '|'), ('?', '}'), ('?', '~'), ('@', 'a'), ('@', 'b'), ('@', 'c'), ('@', 'd'), ('@', 'e'), ('@', 'f'), ('@', 'g'), ('@', 'h'), ('@', 'i'), ('@', 'j'), ('@', 'k'), ('@', 'l'), ('@', 'm'), ('@', 'n'), ('@', 'o'), ('@', 'p'), ('@', 'q'), ('@', 'r'), ('@', 's'), ('@', 't'), ('@', 'u'), ('@', 'v'), ('@', 'w'), ('@', 'x'), ('@', 'y'), ('@', 'z'), ('@', 'A'), ('@', 'B'), ('@', 'C'), ('@', 'D'), ('@', 'E'), ('@', 'F'), ('@', 'G'), ('@', 'H'), ('@', 'I'), ('@', 'J'), ('@', 'K'), ('@', 'L'), ('@', 'M'), ('@', 'N'), ('@', 'O'), ('@', 'P'), ('@', 'Q'), ('@', 'R'), ('@', 'S'), ('@', 'T'), ('@', 'U'), ('@', 'V'), ('@', 'W'), ('@', 'X'), ('@', 'Y'), ('@', 'Z'), ('@', '0'), ('@', '1'), ('@', '2'), ('@', '3'), ('@', '4'), ('@', '5'), ('@', '6'), ('@', '7'), ('@', '8'), ('@', '9'), ('@', '!'), ('@', '"'), ('@', '#'), ('@', '$'), ('@', '%'), ('@', '&'), ('@', "'"), ('@', '('), ('@', ')'), ('@', '*'), ('@', '+'), ('@', ','), ('@', '-'), ('@', '.'), ('@', '/'), ('@', ':'), ('@', ';'), ('@', '<'), ('@', '='), ('@', '>'), ('@', '?'), ('@', '@'), ('@', '['), ('@', '\\'), ('@', ']'), ('@', '^'), ('@', '_'), ('@', '`'), ('@', '{'), ('@', '|'), ('@', '}'), ('@', '~'), ('[', 'a'), ('[', 'b'), ('[', 'c'), ('[', 'd'), ('[', 'e'), ('[', 'f'), ('[', 'g'), ('[', 'h'), ('[', 'i'), ('[', 'j'), ('[', 'k'), ('[', 'l'), ('[', 'm'), ('[', 'n'), ('[', 'o'), ('[', 'p'), ('[', 'q'), ('[', 'r'), ('[', 's'), ('[', 't'), ('[', 'u'), ('[', 'v'), ('[', 'w'), ('[', 'x'), ('[', 'y'), ('[', 'z'), ('[', 'A'), ('[', 'B'), ('[', 'C'), ('[', 'D'), ('[', 'E'), ('[', 'F'), ('[', 'G'), ('[', 'H'), ('[', 'I'), ('[', 'J'), ('[', 'K'), ('[', 'L'), ('[', 'M'), ('[', 'N'), ('[', 'O'), ('[', 'P'), ('[', 'Q'), ('[', 'R'), ('[', 'S'), ('[', 'T'), ('[', 'U'), ('[', 'V'), ('[', 'W'), ('[', 'X'), ('[', 'Y'), ('[', 'Z'), ('[', '0'), ('[', '1'), ('[', '2'), ('[', '3'), ('[', '4'), ('[', '5'), ('[', '6'), ('[', '7'), ('[', '8'), ('[', '9'), ('[', '!'), ('[', '"'), ('[', '#'), ('[', '$'), ('[', '%'), ('[', '&'), ('[', "'"), ('[', '('), ('[', ')'), ('[', '*'), ('[', '+'), ('[', ','), ('[', '-'), ('[', '.'), ('[', '/'), ('[', ':'), ('[', ';'), ('[', '<'), ('[', '='), ('[', '>'), ('[', '?'), ('[', '@'), ('[', '['), ('[', '\\'), ('[', ']'), ('[', '^'), ('[', '_'), ('[', '`'), ('[', '{'), ('[', '|'), ('[', '}'), ('[', '~'), ('\\', 'a'), ('\\', 'b'), ('\\', 'c'), ('\\', 'd'), ('\\', 'e'), ('\\', 'f'), ('\\', 'g'), ('\\', 'h'), ('\\', 'i'), ('\\', 'j'), ('\\', 'k'), ('\\', 'l'), ('\\', 'm'), ('\\', 'n'), ('\\', 'o'), ('\\', 'p'), ('\\', 'q'), ('\\', 'r'), ('\\', 's'), ('\\', 't'), ('\\', 'u'), ('\\', 'v'), ('\\', 'w'), ('\\', 'x'), ('\\', 'y'), ('\\', 'z'), ('\\', 'A'), ('\\', 'B'), ('\\', 'C'), ('\\', 'D'), ('\\', 'E'), ('\\', 'F'), ('\\', 'G'), ('\\', 'H'), ('\\', 'I'), ('\\', 'J'), ('\\', 'K'), ('\\', 'L'), ('\\', 'M'), ('\\', 'N'), ('\\', 'O'), ('\\', 'P'), ('\\', 'Q'), ('\\', 'R'), ('\\', 'S'), ('\\', 'T'), ('\\', 'U'), ('\\', 'V'), ('\\', 'W'), ('\\', 'X'), ('\\', 'Y'), ('\\', 'Z'), ('\\', '0'), ('\\', '1'), ('\\', '2'), ('\\', '3'), ('\\', '4'), ('\\', '5'), ('\\', '6'), ('\\', '7'), ('\\', '8'), ('\\', '9'), ('\\', '!'), ('\\', '"'), ('\\', '#'), ('\\', '$'), ('\\', '%'), ('\\', '&'), ('\\', "'"), ('\\', '('), ('\\', ')'), ('\\', '*'), ('\\', '+'), ('\\', ','), ('\\', '-'), ('\\', '.'), ('\\', '/'), ('\\', ':'), ('\\', ';'), ('\\', '<'), ('\\', '='), ('\\', '>'), ('\\', '?'), ('\\', '@'), ('\\', '['), ('\\', '\\'), ('\\', ']'), ('\\', '^'), ('\\', '_'), ('\\', '`'), ('\\', '{'), ('\\', '|'), ('\\', '}'), ('\\', '~'), (']', 'a'), (']', 'b'), (']', 'c'), (']', 'd'), (']', 'e'), (']', 'f'), (']', 'g'), (']', 'h'), (']', 'i'), (']', 'j'), (']', 'k'), (']', 'l'), (']', 'm'), (']', 'n'), (']', 'o'), (']', 'p'), (']', 'q'), (']', 'r'), (']', 's'), (']', 't'), (']', 'u'), (']', 'v'), (']', 'w'), (']', 'x'), (']', 'y'), (']', 'z'), (']', 'A'), (']', 'B'), (']', 'C'), (']', 'D'), (']', 'E'), (']', 'F'), (']', 'G'), (']', 'H'), (']', 'I'), (']', 'J'), (']', 'K'), (']', 'L'), (']', 'M'), (']', 'N'), (']', 'O'), (']', 'P'), (']', 'Q'), (']', 'R'), (']', 'S'), (']', 'T'), (']', 'U'), (']', 'V'), (']', 'W'), (']', 'X'), (']', 'Y'), (']', 'Z'), (']', '0'), (']', '1'), (']', '2'), (']', '3'), (']', '4'), (']', '5'), (']', '6'), (']', '7'), (']', '8'), (']', '9'), (']', '!'), (']', '"'), (']', '#'), (']', '$'), (']', '%'), (']', '&'), (']', "'"), (']', '('), (']', ')'), (']', '*'), (']', '+'), (']', ','), (']', '-'), (']', '.'), (']', '/'), (']', ':'), (']', ';'), (']', '<'), (']', '='), (']', '>'), (']', '?'), (']', '@'), (']', '['), (']', '\\'), (']', ']'), (']', '^'), (']', '_'), (']', '`'), (']', '{'), (']', '|'), (']', '}'), (']', '~'), ('^', 'a'), ('^', 'b'), ('^', 'c'), ('^', 'd'), ('^', 'e'), ('^', 'f'), ('^', 'g'), ('^', 'h'), ('^', 'i'), ('^', 'j'), ('^', 'k'), ('^', 'l'), ('^', 'm'), ('^', 'n'), ('^', 'o'), ('^', 'p'), ('^', 'q'), ('^', 'r'), ('^', 's'), ('^', 't'), ('^', 'u'), ('^', 'v'), ('^', 'w'), ('^', 'x'), ('^', 'y'), ('^', 'z'), ('^', 'A'), ('^', 'B'), ('^', 'C'), ('^', 'D'), ('^', 'E'), ('^', 'F'), ('^', 'G'), ('^', 'H'), ('^', 'I'), ('^', 'J'), ('^', 'K'), ('^', 'L'), ('^', 'M'), ('^', 'N'), ('^', 'O'), ('^', 'P'), ('^', 'Q'), ('^', 'R'), ('^', 'S'), ('^', 'T'), ('^', 'U'), ('^', 'V'), ('^', 'W'), ('^', 'X'), ('^', 'Y'), ('^', 'Z'), ('^', '0'), ('^', '1'), ('^', '2'), ('^', '3'), ('^', '4'), ('^', '5'), ('^', '6'), ('^', '7'), ('^', '8'), ('^', '9'), ('^', '!'), ('^', '"'), ('^', '#'), ('^', '$'), ('^', '%'), ('^', '&'), ('^', "'"), ('^', '('), ('^', ')'), ('^', '*'), ('^', '+'), ('^', ','), ('^', '-'), ('^', '.'), ('^', '/'), ('^', ':'), ('^', ';'), ('^', '<'), ('^', '='), ('^', '>'), ('^', '?'), ('^', '@'), ('^', '['), ('^', '\\'), ('^', ']'), ('^', '^'), ('^', '_'), ('^', '`'), ('^', '{'), ('^', '|'), ('^', '}'), ('^', '~'), ('_', 'a'), ('_', 'b'), ('_', 'c'), ('_', 'd'), ('_', 'e'), ('_', 'f'), ('_', 'g'), ('_', 'h'), ('_', 'i'), ('_', 'j'), ('_', 'k'), ('_', 'l'), ('_', 'm'), ('_', 'n'), ('_', 'o'), ('_', 'p'), ('_', 'q'), ('_', 'r'), ('_', 's'), ('_', 't'), ('_', 'u'), ('_', 'v'), ('_', 'w'), ('_', 'x'), ('_', 'y'), ('_', 'z'), ('_', 'A'), ('_', 'B'), ('_', 'C'), ('_', 'D'), ('_', 'E'), ('_', 'F'), ('_', 'G'), ('_', 'H'), ('_', 'I'), ('_', 'J'), ('_', 'K'), ('_', 'L'), ('_', 'M'), ('_', 'N'), ('_', 'O'), ('_', 'P'), ('_', 'Q'), ('_', 'R'), ('_', 'S'), ('_', 'T'), ('_', 'U'), ('_', 'V'), ('_', 'W'), ('_', 'X'), ('_', 'Y'), ('_', 'Z'), ('_', '0'), ('_', '1'), ('_', '2'), ('_', '3'), ('_', '4'), ('_', '5'), ('_', '6'), ('_', '7'), ('_', '8'), ('_', '9'), ('_', '!'), ('_', '"'), ('_', '#'), ('_', '$'), ('_', '%'), ('_', '&'), ('_', "'"), ('_', '('), ('_', ')'), ('_', '*'), ('_', '+'), ('_', ','), ('_', '-'), ('_', '.'), ('_', '/'), ('_', ':'), ('_', ';'), ('_', '<'), ('_', '='), ('_', '>'), ('_', '?'), ('_', '@'), ('_', '['), ('_', '\\'), ('_', ']'), ('_', '^'), ('_', '_'), ('_', '`'), ('_', '{'), ('_', '|'), ('_', '}'), ('_', '~'), ('`', 'a'), ('`', 'b'), ('`', 'c'), ('`', 'd'), ('`', 'e'), ('`', 'f'), ('`', 'g'), ('`', 'h'), ('`', 'i'), ('`', 'j'), ('`', 'k'), ('`', 'l'), ('`', 'm'), ('`', 'n'), ('`', 'o'), ('`', 'p'), ('`', 'q'), ('`', 'r'), ('`', 's'), ('`', 't'), ('`', 'u'), ('`', 'v'), ('`', 'w'), ('`', 'x'), ('`', 'y'), ('`', 'z'), ('`', 'A'), ('`', 'B'), ('`', 'C'), ('`', 'D'), ('`', 'E'), ('`', 'F'), ('`', 'G'), ('`', 'H'), ('`', 'I'), ('`', 'J'), ('`', 'K'), ('`', 'L'), ('`', 'M'), ('`', 'N'), ('`', 'O'), ('`', 'P'), ('`', 'Q'), ('`', 'R'), ('`', 'S'), ('`', 'T'), ('`', 'U'), ('`', 'V'), ('`', 'W'), ('`', 'X'), ('`', 'Y'), ('`', 'Z'), ('`', '0'), ('`', '1'), ('`', '2'), ('`', '3'), ('`', '4'), ('`', '5'), ('`', '6'), ('`', '7'), ('`', '8'), ('`', '9'), ('`', '!'), ('`', '"'), ('`', '#'), ('`', '$'), ('`', '%'), ('`', '&'), ('`', "'"), ('`', '('), ('`', ')'), ('`', '*'), ('`', '+'), ('`', ','), ('`', '-'), ('`', '.'), ('`', '/'), ('`', ':'), ('`', ';'), ('`', '<'), ('`', '='), ('`', '>'), ('`', '?'), ('`', '@'), ('`', '['), ('`', '\\'), ('`', ']'), ('`', '^'), ('`', '_'), ('`', '`'), ('`', '{'), ('`', '|'), ('`', '}'), ('`', '~'), ('{', 'a'), ('{', 'b'), ('{', 'c'), ('{', 'd'), ('{', 'e'), ('{', 'f'), ('{', 'g'), ('{', 'h'), ('{', 'i'), ('{', 'j'), ('{', 'k'), ('{', 'l'), ('{', 'm'), ('{', 'n'), ('{', 'o'), ('{', 'p'), ('{', 'q'), ('{', 'r'), ('{', 's'), ('{', 't'), ('{', 'u'), ('{', 'v'), ('{', 'w'), ('{', 'x'), ('{', 'y'), ('{', 'z'), ('{', 'A'), ('{', 'B'), ('{', 'C'), ('{', 'D'), ('{', 'E'), ('{', 'F'), ('{', 'G'), ('{', 'H'), ('{', 'I'), ('{', 'J'), ('{', 'K'), ('{', 'L'), ('{', 'M'), ('{', 'N'), ('{', 'O'), ('{', 'P'), ('{', 'Q'), ('{', 'R'), ('{', 'S'), ('{', 'T'), ('{', 'U'), ('{', 'V'), ('{', 'W'), ('{', 'X'), ('{', 'Y'), ('{', 'Z'), ('{', '0'), ('{', '1'), ('{', '2'), ('{', '3'), ('{', '4'), ('{', '5'), ('{', '6'), ('{', '7'), ('{', '8'), ('{', '9'), ('{', '!'), ('{', '"'), ('{', '#'), ('{', '$'), ('{', '%'), ('{', '&'), ('{', "'"), ('{', '('), ('{', ')'), ('{', '*'), ('{', '+'), ('{', ','), ('{', '-'), ('{', '.'), ('{', '/'), ('{', ':'), ('{', ';'), ('{', '<'), ('{', '='), ('{', '>'), ('{', '?'), ('{', '@'), ('{', '['), ('{', '\\'), ('{', ']'), ('{', '^'), ('{', '_'), ('{', '`'), ('{', '{'), ('{', '|'), ('{', '}'), ('{', '~'), ('|', 'a'), ('|', 'b'), ('|', 'c'), ('|', 'd'), ('|', 'e'), ('|', 'f'), ('|', 'g'), ('|', 'h'), ('|', 'i'), ('|', 'j'), ('|', 'k'), ('|', 'l'), ('|', 'm'), ('|', 'n'), ('|', 'o'), ('|', 'p'), ('|', 'q'), ('|', 'r'), ('|', 's'), ('|', 't'), ('|', 'u'), ('|', 'v'), ('|', 'w'), ('|', 'x'), ('|', 'y'), ('|', 'z'), ('|', 'A'), ('|', 'B'), ('|', 'C'), ('|', 'D'), ('|', 'E'), ('|', 'F'), ('|', 'G'), ('|', 'H'), ('|', 'I'), ('|', 'J'), ('|', 'K'), ('|', 'L'), ('|', 'M'), ('|', 'N'), ('|', 'O'), ('|', 'P'), ('|', 'Q'), ('|', 'R'), ('|', 'S'), ('|', 'T'), ('|', 'U'), ('|', 'V'), ('|', 'W'), ('|', 'X'), ('|', 'Y'), ('|', 'Z'), ('|', '0'), ('|', '1'), ('|', '2'), ('|', '3'), ('|', '4'), ('|', '5'), ('|', '6'), ('|', '7'), ('|', '8'), ('|', '9'), ('|', '!'), ('|', '"'), ('|', '#'), ('|', '$'), ('|', '%'), ('|', '&'), ('|', "'"), ('|', '('), ('|', ')'), ('|', '*'), ('|', '+'), ('|', ','), ('|', '-'), ('|', '.'), ('|', '/'), ('|', ':'), ('|', ';'), ('|', '<'), ('|', '='), ('|', '>'), ('|', '?'), ('|', '@'), ('|', '['), ('|', '\\'), ('|', ']'), ('|', '^'), ('|', '_'), ('|', '`'), ('|', '{'), ('|', '|'), ('|', '}'), ('|', '~'), ('}', 'a'), ('}', 'b'), ('}', 'c'), ('}', 'd'), ('}', 'e'), ('}', 'f'), ('}', 'g'), ('}', 'h'), ('}', 'i'), ('}', 'j'), ('}', 'k'), ('}', 'l'), ('}', 'm'), ('}', 'n'), ('}', 'o'), ('}', 'p'), ('}', 'q'), ('}', 'r'), ('}', 's'), ('}', 't'), ('}', 'u'), ('}', 'v'), ('}', 'w'), ('}', 'x'), ('}', 'y'), ('}', 'z'), ('}', 'A'), ('}', 'B'), ('}', 'C'), ('}', 'D'), ('}', 'E'), ('}', 'F'), ('}', 'G'), ('}', 'H'), ('}', 'I'), ('}', 'J'), ('}', 'K'), ('}', 'L'), ('}', 'M'), ('}', 'N'), ('}', 'O'), ('}', 'P'), ('}', 'Q'), ('}', 'R'), ('}', 'S'), ('}', 'T'), ('}', 'U'), ('}', 'V'), ('}', 'W'), ('}', 'X'), ('}', 'Y'), ('}', 'Z'), ('}', '0'), ('}', '1'), ('}', '2'), ('}', '3'), ('}', '4'), ('}', '5'), ('}', '6'), ('}', '7'), ('}', '8'), ('}', '9'), ('}', '!'), ('}', '"'), ('}', '#'), ('}', '$'), ('}', '%'), ('}', '&'), ('}', "'"), ('}', '('), ('}', ')'), ('}', '*'), ('}', '+'), ('}', ','), ('}', '-'), ('}', '.'), ('}', '/'), ('}', ':'), ('}', ';'), ('}', '<'), ('}', '='), ('}', '>'), ('}', '?'), ('}', '@'), ('}', '['), ('}', '\\'), ('}', ']'), ('}', '^'), ('}', '_'), ('}', '`'), ('}', '{'), ('}', '|'), ('}', '}'), ('}', '~'), ('~', 'a'), ('~', 'b'), ('~', 'c'), ('~', 'd'), ('~', 'e'), ('~', 'f'), ('~', 'g'), ('~', 'h'), ('~', 'i'), ('~', 'j'), ('~', 'k'), ('~', 'l'), ('~', 'm'), ('~', 'n'), ('~', 'o'), ('~', 'p'), ('~', 'q'), ('~', 'r'), ('~', 's'), ('~', 't'), ('~', 'u'), ('~', 'v'), ('~', 'w'), ('~', 'x'), ('~', 'y'), ('~', 'z'), ('~', 'A'), ('~', 'B'), ('~', 'C'), ('~', 'D'), ('~', 'E'), ('~', 'F'), ('~', 'G'), ('~', 'H'), ('~', 'I'), ('~', 'J'), ('~', 'K'), ('~', 'L'), ('~', 'M'), ('~', 'N'), ('~', 'O'), ('~', 'P'), ('~', 'Q'), ('~', 'R'), ('~', 'S'), ('~', 'T'), ('~', 'U'), ('~', 'V'), ('~', 'W'), ('~', 'X'), ('~', 'Y'), ('~', 'Z'), ('~', '0'), ('~', '1'), ('~', '2'), ('~', '3'), ('~', '4'), ('~', '5'), ('~', '6'), ('~', '7'), ('~', '8'), ('~', '9'), ('~', '!'), ('~', '"'), ('~', '#'), ('~', '$'), ('~', '%'), ('~', '&'), ('~', "'"), ('~', '('), ('~', ')'), ('~', '*'), ('~', '+'), ('~', ','), ('~', '-'), ('~', '.'), ('~', '/'), ('~', ':'), ('~', ';'), ('~', '<'), ('~', '='), ('~', '>'), ('~', '?'), ('~', '@'), ('~', '['), ('~', '\\'), ('~', ']'), ('~', '^'), ('~', '_'), ('~', '`'), ('~', '{'), ('~', '|'), ('~', '}'), ('~', '~')]

```python
print("7.2 PERMUTATIONS")
# Permutations is a function which returns all possible permutations of the given iterable

from itertools import permutations
g7=[1,2,3]

g8=permutations(g7)
g9=permutations(g7,2) # r keyword argument, returns permutations of length r
g12=list(g9)

print(list(g8)) # output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print(g12) # output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print(len(g12)) # nPr = n!/(n-r)! = 3!/(3-2)! = 6
```

    7.2 PERMUTATIONS
    [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
    6

```python
print("7.3 COMBINATIONS")
# Combinations is a function which returns all possible combinations of the given iterable

from itertools import combinations , combinations_with_replacement
g10=[1,2,3,4]

g11=list(combinations(g10,2)) # r keyword argument, returns combinations of length r
g13=list(combinations(g10,3))

print(g11)
print(len(g11)) # output: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)] nCr = n!/(r!*(n-r)!) = 4!/(2!*(4-2)!) = 6

print(g13)      # nCr = n!/(r!*(n-r)!) = 4!/(3!*(4-3)!) = 4
print(len(g13)) # output: [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

g14=list(combinations_with_replacement(g10,2)) # combinations_with_replacement() function, returns combinations with replacement
print(g14)      # output: [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
print(len(g14)) # nHr = n+r-1Cr = 4+2-1C2 = 5C2 = 10
```

    7.3 COMBINATIONS
    [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    6
    [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
    4
    [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
    10

```python
print("7.4 ACCUMULATE")
# Accumulate is a function which returns the accumulated sum of the given iterable

import itertools
import operator

g15=[1,2,5,3,4]
g16=list(itertools.accumulate(g15))
print(g16) # output: [1, 3, 8, 11, 15]

g17=list(itertools.accumulate(g15,operator.mul)) # operator.mul is the function which is applied to the accumulated multiplied
print(g17) # output: [1, 2, 10, 30, 120]

g18=list(itertools.accumulate(g15,operator.sub)) # operator.sub is the function which is applied to the accumulated subtracted
print(g18) # output: [1, -1, -6, -9, -13]

g19=list(itertools.accumulate(g15,max)) # gives max
print(g19) # output: [1, 2, 5, 5, 5]
```

    7.4 ACCUMULATE
    [1, 3, 8, 11, 15]
    [1, 2, 10, 30, 120]
    [1, -1, -6, -9, -13]
    [1, 2, 5, 5, 5]

```python
print("7.5 GROUPBY")
# groupby is a function which returns an iterator object, with consecutive keys and groups
# groupby is used when we want to group the elements of the iterable based on a key function

from itertools import groupby
g20=[1,2,3,4,5,6,7,8,9,10]

def smaller_than5(x):
    return x<5

g21=groupby(g20,key=smaller_than5) # groupby() function, returns an iterator object

for key,value in g21:
    print("1 ",key,value)

#########################################
for k,v in groupby(g20,key=lambda x:x<5):   # this works
    print("2 ",k,list(v))

#########################################
for k,v in groupby(g20,key=lambda x:x%2==0):    # does not work
    print("3 ",k,list(v))

#########################################
g22=[{'name':'janav','age':21},{'name':'makkar','age':21},{'name':'janav','age':24},{'name':'makkar','age':24}] # list of dictionaries

for k, v in groupby(g22, lambda x:x['age']):    # this works
    print("4 ",k,list(v))

for k, v in groupby(g22, lambda x:x['name']):   # does not work
    print("5 ",k,list(v))
```

    7.5 GROUPBY
    1  True <itertools._grouper object at 0x000002B12EE5DB50>
    1  False <itertools._grouper object at 0x000002B12EE45130>
    2  True [1, 2, 3, 4]
    2  False [5, 6, 7, 8, 9, 10]
    3  False [1]
    3  True [2]
    3  False [3]
    3  True [4]
    3  False [5]
    3  True [6]
    3  False [7]
    3  True [8]
    3  False [9]
    3  True [10]
    4  21 [{'name': 'janav', 'age': 21}, {'name': 'makkar', 'age': 21}]
    4  24 [{'name': 'janav', 'age': 24}, {'name': 'makkar', 'age': 24}]
    5  janav [{'name': 'janav', 'age': 21}]
    5  makkar [{'name': 'makkar', 'age': 21}]
    5  janav [{'name': 'janav', 'age': 24}]
    5  makkar [{'name': 'makkar', 'age': 24}]

```python
print("7.6 INFINITE ITERATORS") # count, cycle, repeat

from itertools import count, cycle, repeat

for i in count(10): # count() function, returns an iterator object, which counts from the given value
    print(i)
    if i==15:
        print("\n")   # infinite loop, break to stop
        break

#########################################
for i in repeat(69,8): # repeat() function, returns an iterator object, which repeats the given value n times
    print(i)

print("\n")   # infinite loop, break to stop

#########################################
g23=[1,2,3,4,5]
for i in cycle(g23): # cycle() function, returns an iterator object, which cycles through the given iterable
    print(i)
    if i==5:    # infinite loop, break to stop
        break


```

    7.6 INFINITE ITERATORS
    10
    11
    12
    13
    14
    15


    69
    69
    69
    69
    69
    69
    69
    69
    1
    2
    3
    4
    5

## 8. Lambda Functions

map, filter, reduce

```python
# lambda functions are anonymous functions, which are defined without a name, which is used only once
# a function which is passed as an argument to another function

# lambda arguments: expression
add10 = lambda x: x+10
print(add10(15))

expo = lambda x,y: x**y # lambda function with multiple arguments
print(expo(4,3))
```

    25
    64

```python
print("8.1 Map \n")
# map(func, seq)
# map() function, returns an iterator object, which applies the given function to each element of the given iterable

h1=[1,2,3,4,5,6]
h2=map(lambda x: x*2, h1)
print(list(h2)) # output: [2, 4, 6, 8, 10, 12]

h3=[x*2 for x in h1] # list comprehension used to do the same thing
print(h3)
```

    8.1 Map

    [2, 4, 6, 8, 10, 12]
    [2, 4, 6, 8, 10, 12]

```python
print("8.2 Filter \n")
# filter(func, seq)
# filter() function, returns an iterator object, which filters the given iterable based on the given function
# returns only those elements for which the function returns true

h3=filter(lambda x: x%2==0,h1)
print(list(h3))

h4=[x for x in h1 if x%2==0] # list comprehension used to do the same thing
print(list(h4))
```

    8.2 Filter

    [2, 4, 6]
    [2, 4, 6]

```python
print("8.3 Reduce \n")
# reduce(func, seq)
# reduce() function, returns a single value, which is the result of applying the given function to the given iterable
# it is not a built-in function, it is in the functools module
# it is used to apply a function to all the elements of the given iterable, and reduce it to a single value

from functools import reduce

h5=reduce(lambda prevResult, currElement: prevResult*currElement, h1)
print(h5)
```

    8.3 Reduce

    720

## 9. Exceptions And Errors

```python
# Types of Errors
# 1. Syntax Error - when the syntax is wrong
# 2. Runtime Error - when the code is syntactically correct, but the code fails to execute
# 3. Logical Error - when the code is syntactically correct, but the code does not do what it is supposed to do

# Types of runtime errors
# 1. ZeroDivisionError - when we divide by zero
# 2. NameError - when we use a variable which is not defined
# 3. TypeError - when we use an object of the wrong type
# 4. IndexError - when we use an index which is out of range
# 5. ValueError - when we use an object of the right type, but with an inappropriate value
# 6. KeyError - when we use a key which is not in the dictionary
# 7. ImportError - when we import a module which does not exist
# 8. AttributeError - when we use an attribute which does not exist
# 9. KeyboardInterrupt - when we press ctrl+c to interrupt the program
# 10. RuntimeError - when we use an object of the right type, but with an inappropriate value
# 11. NotImplementedError - when we use a function which is not implemented
# 12. StopIteration - when we use next() on an iterator which has no more values
# 13. IndentationError - when the indentation is wrong
# 14. TabError - when the indentation is wrong
# 15. SystemError - when the interpreter detects an internal error
# 16. MemoryError - when the program runs out of memory
# 17. FloatingPointError - when we use a floating point number which is not defined
# 18. OverflowError - when we use a number which is too large
# 19. IOError - when we use a file which does not exist
# 20. OSError - when we use a file which does not exist
# 21. EOFError - when we use input() and the user presses ctrl+d
# 22. Warning - when something unexpected happens, but the program can still continue
# 23. DeprecationWarning - when a deprecated feature is used
# 24. SyntaxWarning - when a syntax error is detected
# 25. RuntimeWarning - when a runtime error is detected
# 26. FileNotFoundError - when a file is not found
# 27. ModuleNotFoundError - when a module is not found
# 28. UnicodeError - when a unicode error occurs
# 29. ValueError - when a value error occurs
```

```python
# Exception Handling

# Raise an exception
# raise Exception("Error Message")
i1=-5
if i1<0:                                        # raise an exception
    raise Exception("i1 cannot be negative")

```

    <>:11: SyntaxWarning: assertion is always true, perhaps remove parentheses?
    <>:11: SyntaxWarning: assertion is always true, perhaps remove parentheses?



    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    c:\Users\ASUS\Desktop\Intermediate python.ipynb Cell 39 in <cell line: 6>()
          <a href='vscode-notebook-cell:/c%3A/Users/ASUS/Desktop/Intermediate%20python.ipynb#Y222sZmlsZQ%3D%3D?line=4'>5</a> i1=-5
          <a href='vscode-notebook-cell:/c%3A/Users/ASUS/Desktop/Intermediate%20python.ipynb#Y222sZmlsZQ%3D%3D?line=5'>6</a> if i1<0:                                        #
    ----> <a href='vscode-notebook-cell:/c%3A/Users/ASUS/Desktop/Intermediate%20python.ipynb#Y222sZmlsZQ%3D%3D?line=6'>7</a>     raise Exception("i1 cannot be negative")
          <a href='vscode-notebook-cell:/c%3A/Users/ASUS/Desktop/Intermediate%20python.ipynb#Y222sZmlsZQ%3D%3D?line=8'>9</a> # Assert statement
         <a href='vscode-notebook-cell:/c%3A/Users/ASUS/Desktop/Intermediate%20python.ipynb#Y222sZmlsZQ%3D%3D?line=9'>10</a> # assert condition, "Error Message", if condition is false, then AssertionError is raised
         <a href='vscode-notebook-cell:/c%3A/Users/ASUS/Desktop/Intermediate%20python.ipynb#Y222sZmlsZQ%3D%3D?line=10'>11</a> assert(i1>0, "i1 cannot be negative")


    Exception: i1 cannot be negative

```python
# Assert statement
# assert condition, "Error Message"
# if condition is false, then AssertionError is raised
assert i1>0, "i1 cannot be negative"            # assert statement
```

    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    c:\Users\ASUS\Desktop\Intermediate python.ipynb Cell 40 in <cell line: 4>()
          <a href='vscode-notebook-cell:/c%3A/Users/ASUS/Desktop/Intermediate%20python.ipynb#Y223sZmlsZQ%3D%3D?line=0'>1</a> # Assert statement
          <a href='vscode-notebook-cell:/c%3A/Users/ASUS/Desktop/Intermediate%20python.ipynb#Y223sZmlsZQ%3D%3D?line=1'>2</a> # assert condition, "Error Message"
          <a href='vscode-notebook-cell:/c%3A/Users/ASUS/Desktop/Intermediate%20python.ipynb#Y223sZmlsZQ%3D%3D?line=2'>3</a> # if condition is false, then AssertionError is raised
    ----> <a href='vscode-notebook-cell:/c%3A/Users/ASUS/Desktop/Intermediate%20python.ipynb#Y223sZmlsZQ%3D%3D?line=3'>4</a> assert i1>0, "i1 cannot be negative"


    AssertionError: i1 cannot be negative

```python
# try-except-finally-else statement
# code in try block is executed, if an exception occurs, then the code in except block is executed
# if no exception occurs, then the code in else block is executed
# code in finally block is always executed, whether an exception occurs or not

print("\n 1. try-except")
try:
    i2=5/0
except:
    print("Error")

print("\n 2. try-except as e")
try:
    i2=5/0
except Exception as e: # Exception is the base class of all exceptions
    print(e)

print("\n 3. try except multiple exceptions")
try:
    i2=5/1
    i3=i2+"10"
except ZeroDivisionError as e: # ZeroDivisionError is a subclass of Exception
    print(e)
except TypeError as e: # TypeError is a subclass of Exception
    print(e)

print("\n 4. try except multiple exceptions-2")
try:
    i2=5/0
    i3=i2+"10"
except ZeroDivisionError as e: # ZeroDivisionError
    print(e)
except TypeError as e: # TypeError
    print(e)

print("\n 5. try-except-else")
try:
    i2=5/1
    i3=i2+10
except ZeroDivisionError as e: # ZeroDivisionError
    print(e)
except TypeError as e: # TypeError
    print(e)
else:
    print("No Error")

print("\n 6. try-except-finally with exception")
try:
    i2=5/1
    i3=i2+"10"
except ZeroDivisionError as e: # ZeroDivisionError
    print(e)
except TypeError as e: # TypeError
    print(e)
else:
    print("No Error")
finally:
    print("Finally, cleanup code")

print("\n 7. try-except-finally-2 with else running")
try:
    i2=5/1
    i3=i2+10
except ZeroDivisionError as e: # ZeroDivisionError
    print(e)
except TypeError as e: # TypeError
    print(e)
else:
    print("No Error")
finally:
    print("Finally, cleanup code")
```

     1. try-except
    Error

     2. try-except as e
    division by zero

     3. try except multiple exceptions
    unsupported operand type(s) for +: 'float' and 'str'

     4. try except multiple exceptions-2
    division by zero

     5. try-except-else
    No Error

     6. try-except-finally with exception
    unsupported operand type(s) for +: 'float' and 'str'
    Finally, cleanup code

     7. try-except-finally-2 with else running
    No Error
    Finally, cleanup code

```python
# Create a custom exception

class ValueToHighError(Exception):                      # custom exception
    pass

class ValueToSmall(Exception):                          # custom exception2
    def __init__(self, message, value):
        self.message=message
        self.value=value

def test_value(x):                                      # function to test the value
    if x>100:
        raise ValueToHighError("Value is too high")
    if x<5:
        raise ValueToSmall("Value is too small",x)


try:                                                    # try-except block
    test_value(200)
except ValueToHighError as e:
    print(e)
except ValueToSmall as e:
    print(e.message,e.value)


try:                                                    # try-except block2
    test_value(2)
except ValueToHighError as e:
    print(e)
except ValueToSmall as e:
    print(e.message,e.value)
```

    Value is too high
    Value is too small 2

## 10. Logging

```python

```

## 11. Json

```python
# PYTHON        ->    JSON
# dict          ->    object
# list, tuple   ->    array
# str           ->    string
# int, float    ->    number
# True, False   ->    true, false
# None          ->    null

# Serialization/ Encoding - converting a python object/dictionary to a json string
import json

k1_person={"name":"Janav","age":21,"married":False,"address":{"street":"abc","city":"xyz","state":"pqr"}}

k1_personJSON=json.dumps(k1_person) # dumps() function, converts a python object/dictionary to a json string
print("1. ",k1_personJSON,"\n",type(k1_personJSON),"\n")

k2_personJSON=json.dumps(k1_person,indent=4) # indent keyword argument, adds indentation to the json string
print("2.",k2_personJSON,"\n")

k3_personJSON=json.dumps(k1_person, indent=4, separators=(";","=")) # separators keyword argument, changes the separators, not recommended to use
print("3.",k3_personJSON,"\n")

k4_personJSON=json.dumps(k1_person, indent=4, sort_keys=True) # sort_keys keyword argument, sorts the keys alphabetically
print("4.",k4_personJSON,"\n")


# Dumping to a file
with open('persons.json', 'w') as file: # w - write mode
    json.dump(k1_person, file, indent=4)          # dump() function, converts a python object/dictionary to a json string and writes it to a file


```

    1.  {"name": "Janav", "age": 21, "married": false, "address": {"street": "abc", "city": "xyz", "state": "pqr"}}
     <class 'str'>

    2. {
        "name": "Janav",
        "age": 21,
        "married": false,
        "address": {
            "street": "abc",
            "city": "xyz",
            "state": "pqr"
        }
    }

    3. {
        "name"="Janav";
        "age"=21;
        "married"=false;
        "address"={
            "street"="abc";
            "city"="xyz";
            "state"="pqr"
        }
    }

    4. {
        "address": {
            "city": "xyz",
            "state": "pqr",
            "street": "abc"
        },
        "age": 21,
        "married": false,
        "name": "Janav"
    }

```python
# Deserialization/ Decoding - converting a json string to a python object/dictionary
k2_person=json.loads(k1_personJSON) # loads() function, converts a json string to a python object/dictionary
print("5.",k2_person,"\n",type(k2_person),"\n")

# Loading from a file
with open('persons.json','r') as file:               # r - read mode
    k3_person=json.load(file)                        # load() function, converts a json string to a python object/dictionary
    print("6.",k3_person,"\n",type(k3_person),"\n")
```

    5. {'name': 'Janav', 'age': 21, 'married': False, 'address': {'street': 'abc', 'city': 'xyz', 'state': 'pqr'}}
     <class 'dict'>

    6. {'name': 'Janav', 'age': 21, 'married': False, 'address': {'street': 'abc', 'city': 'xyz', 'state': 'pqr'}}
     <class 'dict'>

```python
# Class objects are not serializable, so we need to use default keyword argument
# Need to create a function which converts the class object to a dictionary

class User:                               # class
    def __init__(self, name, age):
        self.name=name
        self.age=age

k5 = User("Janav",21)                      # class object

try:                                       # this will give an error
    k5JSON=json.dumps(k5)
except Exception as e:
    print(e)

def encodeUser(obj):                       # function to convert the class object to a dictionary
    if isinstance(obj, User):
        return {"name":obj.name, "age":obj.age, obj.__class__.__name__:True}
    else:
        raise TypeError("Object of type User is not JSON serializable")

k5JSON=json.dumps(k5, default=encodeUser)   # default keyword argument, converts the class object to a dictionary
print("7.",k5JSON,"\n")
```

    Object of type User is not JSON serializable
    7. {"name": "Janav", "age": 21, "User": true}

```python
# Second way to encode the class object to a dictionary

from json import JSONEncoder

class UserEncoder(JSONEncoder):                 # UserEncoder class, inherits from the JSONEncoder class
    def default(self, obj):                     # default method of the JSONEncoder class is overridden
        if isinstance(obj, User):               # isinstance() function, returns true if the object is an instance of the class
            return {'name':obj.name,
                    'age':obj.age,
                    obj.__class__.__name__:True
                    }                           # return a dictionary
        return JSONEncoder.default(self, obj)   # return the default method of the JSONEncoder class}

k6JSON=json.dumps(k5, cls=UserEncoder)          # cls keyword argument, converts the class object to a dictionary
print("8.",k6JSON,"\n")

k7JSON=UserEncoder().encode(k5)                # encode() method, converts the class object to a dictionary
print("9.",k7JSON,"\n")




```

    8. {"name": "Janav", "age": 21, "User": true}

    9. {"name": "Janav", "age": 21, "User": true}

## 12. Random Numbers

```python

```

## 13. Decorators

```python

```

## 14. Generators

```python

```

## 15. Threading vs Multiprocessing

```python

```

## 16. Multithreading

```python

```

## 17. Multiprocessing

```python

```

## 18. Function Arguments

```python

```

## 19. Shallow vs Deep Copying

```python

```

## 20. Asterisk Operator \*

```python

```

## 21. Context Managers

```python

```
