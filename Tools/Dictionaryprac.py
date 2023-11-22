# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing values
print("Name:", my_dict['name'])

# Adding or updating elements
my_dict['email'] = 'alice@example.com'  # Adding a new key-value pair
my_dict['age'] = 26                     # Updating an existing value

# Removing elements
del my_dict['city']             # Using del
email = my_dict.pop('email')    # Using pop
print("Removed email:", email)

# Iterating through a dictionary
print("\nIterating through keys and values:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking if a key exists
if 'name' in my_dict:
    print("\nName is present in the dictionary.")

# Dictionary length
print("\nNumber of key-value pairs:", len(my_dict))

# Nested dictionary
nested_dict = {
    'person': {'name': 'Alice', 'age': 26},
    'location': 'New York'
}

print("\nNested Dictionary:")
for key, value in nested_dict.items():
    print(f"{key}: {value}")

# Working with nested dictionary
print("\nAccessing nested dictionary elements:")
print("Name:", nested_dict['person']['name'])

# Dictionary comprehensions
print("\nDictionary Comprehension:")
squares = {x: x*x for x in range(6)}
print(squares)

# Merging two dictionaries (Python 3.5+)
print("\nMerging two dictionaries:")
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

# Using get() method to access values
print("\nUsing get() method:")
print("Age:", my_dict.get('age', 'Unknown'))
# Default value if key not found
print("Birthday:", my_dict.get('birthday', 'Unknown'))

# Sorting a dictionary by keys
print("\nSorting by keys:")
for key in sorted(my_dict):
    print(f"{key}: {my_dict[key]}")

# Sorting by values
# Sorting by values, handling different types (e.g., int and str)
print("\nSorting by values with type handling:")
for key in sorted(my_dict, key=lambda k: str(my_dict[k])):
    print(f"{key}: {my_dict[key]}")
