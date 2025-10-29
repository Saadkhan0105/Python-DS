# PYTHON

## Syntax and Semantics in Python:
1. Syntax:
- Syntax refers to the set of rules that defines the combinations of symbols that are considerable to be correctly structured programs in a language.
- In simple terms, syntax is about the correct arrangement of words and symbols in a code.
- Python is case sensitive.

#### Basic Syntax rules in Python

```
name = "Saad"
Name = "Khan"

print(name)  # Output: Saad
print(Name)  # Output: Khan
```

2. Semantics:
- Semantics refers to the meanings or interpreatation of the symbols, characters, and commands in a language.
- It is about what the code is supposed to do when it runs.

3. Indentation:
- Indentation in Python is used to define the structure and hierarchy of the code.
- Unlike many other programming languages that uses braces {} to delimit the blocks of code, Python uses indentation to determine the grouping of statements.
- This means that all statements within a block must be indented at the same level.
- Python uses indentation to define block of code. Consistent use of spaces (commonly 4) or a tab is required

```
age = 32
if age > 30:
    print("You are old")
else:
    print("You are not old")

print(age)
```
## Variables:
- Variables are fundamental elements in programming used to store data that can be referenced and manipulated in a program.
- In python, variables are created when you assign a value to them, and they do not need explicit declaration to reserve memory space.
- The declaration to reserve memoruy space. The declaration happens automatically when you assign a value to variable.
- Valid variable names examples:
```
## valid variable names:
first_name = "Saad"
last_name = "Khan"
full_name = first_name + " " + last_name
print(full_name)
```
- Invalid variable names examples:
```
1. 2names = "Saad"
2. 2 names = "Saad"
3. @names = "Saad"
```

### Understanding variable types:
- Python is dynamically typed, type of a variable is determined at runtime
```
age = 29 #int
height = 5.2 #float
name = "Saad" #string
is_student = True #boolean
print(type(age), type(height), type(name), type(is_student))

# Output:
<class 'int'> <class 'float'> <class 'str'> <class 'bool'>
```

## Datatypes:
1. Definition:
- Datatypes are a classification of data which tell the compiler or interpreter how the program intends to use the data.
- They determine the type of operations that can be performed on the data, the values that can be stored, and the amount of memory needed to store the data.

2. Importance of Data Types in Programming:
- Datatypes ensure that the data is stored in an efficiet way.
- They help in performing correct operations on data.
- Proper use of datatypes can prevent errors and bugs in the program.

3. Python DataTypes:
![Python Data Types](./assets/python-data-types.png)

# Operators in Python:
![Operators](./assets/operators.png)
- Example:
1. Arithmetic Operators:
```
a = 10
b = 5

add_result = a + b
print(add_result)
# Output
15

sub_result = a - b
print(sub_result)
# Output
5

mul_result = a * b
print(mul_result)
# Output
50

div_result = a / b
print(div_result)
# Output
2.0

mod_result = a % b
print(mod_result)
# Output
0

exp_result = a ** b
print(exp_result)
# Output
100000
```
2. Comparison Operators:

```
a = 10
b = 5
print(a == b)
# Output
False

print(a != b)
# Output
True

print(a > b)
# Output
True

print(a < b)
# Output
False

print(a >= b)
# Output
True

print(a <= b)
# Output
False
```
3. Logical Operators:
```
a = True
b = False

print(a and b)
# Output
False

print(a or b)
# Output
True

print(not a)
# Output
False
```

## Conditional Statements:
1. if-statement:
- The if condition is considered the simplest of the three and makes a decision based on whether the condition is true or not. 
- If the condition is true, it prints out the indented expression. If the condition is false, it skips printing the indented expression.
```
age = 23
if age>= 18:
    print("You are old enough to vote!")
```
2. else-statement:
- The else statement executes a block of code if the condition in the if statement is False.
```
age = 16

if age>=18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote!")
```
3. elif-statement:
- The elif statement allows you to check multiple conditions. It stands for "else if"
```
age = 17

if age < 13:
    print("Ypou are a child")
elif age < 18:
    print("You are a teenager")
else:
    print("You are an adult")
```

## Loops:
- Loops are used to execute a block of code repeatedly until a certain condition is met.
- There are two types of loops in Python:
1. for-loop:
- The for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects.
```
for i in range(5):
    print(i)
```
2. while-loop:
- The While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. 
- The condition is checked before each iteration of the loop. When the condition becomes false, the line immediately after the loop in the program is executed.
```
count = 0
while count < 3:
    count = count + 1
    print("Hello Geek")
```

## Data Structures:
- Data structures are used to organize and manage data in a program.
- Python has four built-in data structures:
#### 1. Lists:
- Lists are ordered, mutable collections of items.
- They can contain elements of different data types, including numbers, strings, and even other lists
- Lists are defined using square brackets [] and elements are separated by commas.
- Lists are mutable, meaning you can change, add, or remove elements after the list is created.
- Example:
```
marks = [54, 23, 64, 93, 32]
mixed = [45, "Saad", 23.5, True]
print(marks) # Output: [54, 23, 64, 93, 32]
print(mixed) # Output: [45, 'Saad', 23.5, True]
print(type(marks)) # Output: <class 'list'>
print(type(mixed)) # Output: <class 'list'>
```
#### List Methods:
- Python provides several built-in methods to manipulate lists:
1. append(item): Adds an item to the end of the list.
2. insert(index, item): Inserts an item at a specified index.
3. remove(item): Removes the first occurrence of an item from the list.
4. pop(index): Removes and returns the item at the specified index (default is the last item).
5. sort(): Sorts the list in ascending order.
6. reverse(): Reverses the order of the list.
7. index(item): Returns the index of the first occurrence of an item.
8. count(item): Returns the number of occurrences of an item in the list.
- Example:
```
marks = [5, 2, 21, 5, 7]
extra_marks = [45, 67, 89]
print(marks)

marks.append(63)  # adds 63 to the end of the list
marks.pop()     # removes the last element from the list
marks.sort()    # sorts the list in ascending order
marks.reverse() # reverses the list
marks.insert(2, 23) # inserts 23 at index 2
marks.remove(23) # removes the first occurrence of 23
marks.count(5) # counts the number of occurrences of 5
marks.index(5) # returns the index of the first occurrence of 5
marks.extend(extra_marks) # extends the list by adding elements from another list
marks.clear() # clears the list
marks.copy() # returns a shallow copy of the list

print(marks)
```

#### List Comprehension:
- List comprehension is a concise way to create lists in Python.
- It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list or range) and optionally filtering items based on a condition.
- The syntax for list comprehension is:
```
table_comp = [5 * i for i in range(1, 11)]
print(table_comp)
```

#### 2. Tuples:
- Tuples are ordered, immutable collections of items.
- They are similar to lists but cannot be modified after creation.
- Tuples are defined using parentheses () and elements are separated by commas.
- Example:
```
a = (3, 2, 22, 13)
print(a)
print(type(a))
print(a[2])  # Output: 22

Single Element Tuple:
b = (5,)  
print(b)
```

#### Tuple Unpacking:
- Tuple unpacking allows you to assign the elements of a tuple to individual variables in a single statement.
- Example:
```
tu = (3, 2, 45)
a, b, c = tu
print(a, b, c)  # Output: 3 2 45
```

#### Tuple Methods:
- Tuples have a limited number of built-in methods due to their immutability:
1. count(item): Returns the number of occurrences of an item in the tuple.
2. index(item): Returns the index of the first occurrence of an item.
- Example:
```
t = (3, 12, 1, 54, 23, 12)
print(t.count(12))  # Output: 2
print(t.index(54))  # Output: 3
```

#### Why Use Tuples?
- Tuples are used when you want to create a collection of items that should not be modified.
- They are more memory efficient than lists and can be used as keys in dictionaries.

#### 3. Sets:
- Sets are built-in data type in Python that are used to store collections of unique elements.
- They are unordered meaning that the elements do not follow a specific order, and they do not allow duplicate elements.
- Sets are useful for membership testing, removing duplicates, and performing mathematical operations like union, intersection,difference and symmetric difference.
- Sets are defined using curly braces {} and elements are separated by commas.
- Example:
```
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
print(type(my_set))  # Output: <class 'set'>
```

## Sets Methods:
- Python provides several built-in methods to manipulate sets:
1. add(item): Adds an item to the set.
2. remove(item): Removes an item from the set. Raises a KeyError if the item is not found.
3. discard(item): Removes an item from the set if it exists. Does not raise an error if the item is not found.
4. pop(): Removes and returns an arbitrary item from the set.
5. clear(): Removes all items from the set.
- Example:
```
s = {34, 23, 1, 3}
s.add(45)  # adds 45 to the set
s.remove(3) # removes 3 from the set
s.discard(10) # tries to remove 10 from the set, but does not
s.pop() # removes and returns an arbitrary item from the set
s.clear() # clears the set
print(s)
```

## Set Operations:
- Sets support various mathematical operations:
1. Union (|): Combines two sets, including all unique elements from both sets.
2. Intersection (&): Returns only the elements that are present in both sets.
3. Difference (-): Returns elements that are in the first set but not in the second set
4. Symmetric Difference (^): Returns elements that are in either set but not in both.
5. issubset(): Checks if one set is a subset of another.
6. issuperset(): Checks if one set is a superset of another.
7. isdisjoint(): Checks if two sets have no elements in common.
8. copy(): Returns a shallow copy of the set.
- Example:
```
a = {3, 23, 1}
b = {23, 4, 2, 55, 1}

c = a.union(b) # Union of two sets
print("Union:", c)
d = a.intersection(b) # Intersection of two sets
print("Intersection:", d)
e = a.difference(b) # Elements in a but not in b
print("Difference (a-b):", e)
f = b.difference(a) # Elements in b but not in a
print("Difference (b-a):", f)
g = a.symmetric_difference(b) # Elements in either a or b but not in both
print("Symmetric Difference:", g)
h = a.issubset(b) # Check if a is subset of b
print("Is a subset of b:", h)
i = a.issuperset(b) # Check if a is superset of b
print("Is a superset of b:", i)
j = a.isdisjoint(b) # Check if a and b have no elements in common
print("Are a and b disjoint:", j)
k = a.copy() # Shallow copy of set a
print("Copy of a:", k)
l = a.clear() # Clear all elements from set a
print("Cleared a:", a)
```

### Important Point 🧠:
- when we call add(), Python:
	1.	Calculates the hash of the element.
	2.	Puts it in a bucket in the hash table.
	3.	Prints the set in whatever order it currently has internally — not “first added, first shown.”

#### 4. Dictionaries:
- Dictionaries are unordered collections of key-value pairs.
- They are defined using curly braces {} with key-value pairs separated by commas.
- Keys must be unique and immutable, while values can be of any data type.
- Example:
```
my_dict = {"name": "Saad", "age": 29, "city": "Mumbai"}
print(my_dict)  # Output: {'name': 'Saad', 'age': 29, 'city': 'Mumbai'}
print(my_dict["name"])  # Output: Saad
print(type(my_dict))  # Output: <class 'dict'>
```

#### Dictionary Methods:
- Python provides several built-in methods to manipulate dictionaries:
1. keys(): Returns a view object containing the keys of the dictionary.
2. values(): Returns a view object containing the values of the dictionary.
3. items(): Returns a view object containing the key-value pairs of the dictionary.
4. get(key, default): Returns the value for the specified key. If the key is not found, returns the default value (None if not specified).
5. update(other_dict): Updates the dictionary with key-value pairs from another dictionary.
6. pop(key, default): Removes the specified key and returns its value. If the key is not found, returns the default value (raises KeyError if not specified).
7. popitem(): Removes and returns an arbitrary key-value pair from the dictionary.
8. clear(): Removes all items from the dictionary.
- Example:
```
marks = {"Saad": 54, "Abuzar": 45, "Umaima": 93}

print(marks.keys())  # Prints all the keys in the dictionary
print(marks.values())  # Prints all the values in the dictionary
print(marks.items())  # Prints all the key-value pairs in the dictionary
marks.update({"Saad": 100, "Ali": 67})  # Updates the dictionary with new key-value pairs
print(marks)
marks.pop("Ali")  # Removes the key-value pair with the specified key
print(marks)
marks.popitem()  # Removes the last key-value pair from the dictionary
print(marks)
marks.clear()  # Clears the dictionary
print(marks)
```

#### Dictionary Comprehension:
- Dictionary comprehension is a concise way to create dictionaries in Python.
- It allows you to generate a new dictionary by applying an expression to each item in an existing
- iterable (like a list or range) and optionally filtering items based on a condition.
- The syntax for dictionary comprehension is:
```
table_comp = {i: 5*i for i in range(1, 11)}
print(table_comp)
```



## Important Notice:
- It is always advisable and good practice that we should create a separate environment(venv) for any project we work on , so that we can segregate the packages and libraries in a very easy way and if in future there are any new updates in those packages.