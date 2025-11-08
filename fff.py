# Method 1: Using update() method
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
# dict1 now contains merged result

# Method 2: Using | operator (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dict1 | dict2

# Method 3: Using dict() constructor and two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dict(**dict1, **dict2)

# Example usage:
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

sample={"a":45, "b":67, "c":76, "d":98, "e":21}

max_key = max(sample, key=sample.get)
print(f"Key with maximum value: {max_key}")  # Will print 'd'

# Creating sets in different ways
empty_set = set()  # Empty set
numbers = {1, 2, 3, 4, 5}  # Set from literals
from_list = set([1, 2, 3, 4])  # Set from list
from_string = set("hello")  # Set from string

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1.union(set2)  # or set1 | set2

# Intersection
intersection_set = set1.intersection(set2)  # or set1 & set2

# Difference
difference_set = set1.difference(set2)  # or set1 - set2

# Symmetric Difference
symmetric_diff = set1.symmetric_difference(set2)  # or set1 ^ set2

# Add and remove elements
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)  # raises error if not found
my_set.discard(5)  # doesn't raise error if not found

# Check membership
print(1 in my_set)  # True

list2=[i*10 for i in range(1,11) if i%2==0]
print(list2)


# Method 1: Using update() method
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
# dict1 now contains merged result

# Method 2: Using | operator (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dict1 | dict2

# Method 3: Using dict() constructor and two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dict(**dict1, **dict2)

# Example usage:
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

sample={"a":45, "b":67, "c":76, "d":98, "e":21}

max_key = max(sample, key=sample.get)
print(f"Key with maximum value: {max_key}")  # Will print 'd'

# Creating sets in different ways
empty_set = set()  # Empty set
numbers = {1, 2, 3, 4, 5}  # Set from literals
from_list = set([1, 2, 3, 4])  # Set from list
from_string = set("hello")  # Set from string

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1.union(set2)  # or set1 | set2

# Intersection
intersection_set = set1.intersection(set2)  # or set1 & set2

# Difference
difference_set = set1.difference(set2)  # or set1 - set2

# Symmetric Difference
symmetric_diff = set1.symmetric_difference(set2)  # or set1 ^ set2

# Add and remove elements
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)  # raises error if not found
my_set.discard(5)  # doesn't raise error if not found

# Check membership
print(1 in my_set)  # True

list2=[i*10 for i in range(1,11) if i%2==0]
print(list2)


# Method 1: Using update() method
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
# dict1 now contains merged result

# Method 2: Using | operator (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dict1 | dict2

# Method 3: Using dict() constructor and two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dict(**dict1, **dict2)

# Example usage:
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

sample={"a":45, "b":67, "c":76, "d":98, "e":21}

max_key = max(sample, key=sample.get)
print(f"Key with maximum value: {max_key}")  # Will print 'd'

# Creating sets in different ways
empty_set = set()  # Empty set
numbers = {1, 2, 3, 4, 5}  # Set from literals
from_list = set([1, 2, 3, 4])  # Set from list
from_string = set("hello")  # Set from string

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1.union(set2)  # or set1 | set2

# Intersection
intersection_set = set1.intersection(set2)  # or set1 & set2

# Difference
difference_set = set1.difference(set2)  # or set1 - set2

# Symmetric Difference
symmetric_diff = set1.symmetric_difference(set2)  # or set1 ^ set2

# Add and remove elements
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)  # raises error if not found
my_set.discard(5)  # doesn't raise error if not found

# Check membership
print(1 in my_set)  # True

list2=[i*10 for i in range(1,11) if i%2==0]
print(list2)


# Method 1: Using update() method
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
# dict1 now contains merged result

# Method 2: Using | operator (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dict1 | dict2

# Method 3: Using dict() constructor and two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dict(**dict1, **dict2)

# Example usage:
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

sample={"a":45, "b":67, "c":76, "d":98, "e":21}

max_key = max(sample, key=sample.get)
print(f"Key with maximum value: {max_key}")  # Will print 'd'

# Creating sets in different ways
empty_set = set()  # Empty set
numbers = {1, 2, 3, 4, 5}  # Set from literals
from_list = set([1, 2, 3, 4])  # Set from list
from_string = set("hello")  # Set from string

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1.union(set2)  # or set1 | set2

# Intersection
intersection_set = set1.intersection(set2)  # or set1 & set2

# Difference
difference_set = set1.difference(set2)  # or set1 - set2

# Symmetric Difference
symmetric_diff = set1.symmetric_difference(set2)  # or set1 ^ set2

# Add and remove elements
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)  # raises error if not found
my_set.discard(5)  # doesn't raise error if not found

# Check membership
print(1 in my_set)  # True

list2=[i*10 for i in range(1,11) if i%2==0]
print(list2)

